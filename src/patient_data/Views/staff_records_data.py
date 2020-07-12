from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.db.models import Sum, Count
from django.shortcuts import render, get_object_or_404
from django.utils.translation import ugettext as _
from django.http import JsonResponse

from patient_form.models import *
from patient_form.forms import *
from accounts.models import *
from customers.models import *

#import datetime
from datetime import *

startdate = date.today()
enddate = startdate + timedelta(days=1)

start_time_day = datetime.strptime('00:00', '%H:%M').time()
end_time_day = datetime.strptime('12:00', '%H:%M').time()
start_time_night = datetime.strptime('12:01', '%H:%M').time()
end_time_night = datetime.strptime('23:59', '%H:%M').time()


@login_required
def save_staff_records_data_form(request, form, template_name):
    data = dict()

    if request.method == 'POST':
        if form.is_valid():
            patients = Appointment()
            patients = form.save(commit=False)
            patients.patient = request.user
            patients.save()
            data['form_is_valid'] = True
            patients = Appointment.objects.all()
            data['html_staff_records_list'] = render_to_string('patient_data/staff_records_data/staff_records_data.html', {'patients': patients})
        else:
            data['form_is_valid'] = False

    context = {
        'form': form,
    }
    data['html_form'] = render_to_string(template_name, context, request=request)

    return JsonResponse(data)


@login_required
def staff_records(request, id):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
    page_title = _('Staff Records')
    patients = StaffRecords.objects.filter(patient=id)
    profiles = PatientProfile.objects.filter(pk=id)
    total_annual = StaffRecords.objects.filter(patient=id).aggregate(Sum('annual_leave_days'))
    total_public = StaffRecords.objects.filter(patient=id,).aggregate(Sum('public_holiday_days'))

    context = {
        'logos': logos,
        'titles': titles,
        'page_title': page_title,
        'patients': patients,
        'profiles': profiles,
        'total_annual': total_annual,
        'total_public': total_public,
    }

    return render(request, 'patient_data/staff_records_data/staff_records_data.html', context)

@login_required
def staff_records_data_edit(request, id):
    staff_recordss = get_object_or_404(Appointment, pk=id)
    if request.method == 'POST':
        form = AppointmentForm(request.POST or None, instance=staff_recordss)
    else:
        form = AppointmentForm(instance=staff_recordss)
    return save_staff_records_data_form(request, form, 'patient_data/staff_records_data/partial_edit.html')


@login_required
def staff_records_data_delete(request, id):
    staff_recordss = get_object_or_404(Appointment, pk=id)
    data = dict()

    if request.method == 'POST':
        staff_recordss.delete()
        data['form_is_valid'] = True
        patients = Appointment.objects.all()
        data['html_staff_records_list'] = render_to_string('patient_data/staff_records_data/staff_records_data.html', {'patients': patients})
        return JsonResponse(data)
    else:
        context = {'staff_recordss': staff_recordss}
        data['html_form'] = render_to_string('patient_data/staff_records_data/partial_delete.html', context, request=request)
        return JsonResponse(data)

    return JsonResponse(data)
