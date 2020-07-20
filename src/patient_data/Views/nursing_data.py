from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import connection
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
def save_nursing_data_form(request, form, template_name):
    data = dict()

    if request.method == 'POST':
        if form.is_valid():
            patients = Nursing()
            patients = form.save(commit=False)
            patients.patient = request.user
            patients.save()
            data['form_is_valid'] = True
            patients = Nursing.objects.all()
            data['html_nursing_list'] = render_to_string('patient_data/nursing_data/nursing_data.html', {'patients': patients})
        else:
            data['form_is_valid'] = False

    context = {
        'form': form,
    }
    data['html_form'] = render_to_string(template_name, context, request=request)

    return JsonResponse(data)

@login_required
def nursing_data(request, username):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
    page_title = _('Nursing Report')
    patientid = PatientProfile.objects.get(username=username).id
    patients = Nursing.objects.filter(patient=patientid)
    profiles = PatientProfile.objects.filter(pk=patientid)

    context = {
        'logos': logos,
        'titles': titles,
        'page_title': page_title,
        'patients': patients,
        'profiles': profiles,
    }

    return render(request, 'patient_data/nursing_data/nursing_data.html', context)


@login_required
def nursing_data_edit(request, id):
    nursings = get_object_or_404(Nursing, pk=id)
    if request.method == 'POST':
        form = NursingForm(request.POST or None, instance=nursings)
    else:
        form = NursingForm(instance=nursings)
    return save_nursing_data_form(request, form, 'patient_data/nursing_data/partial_edit.html')


@login_required
def nursing_data_delete(request, id):
    nursings = get_object_or_404(Nursing, pk=id)
    data = dict()

    if request.method == 'POST':
        nursings.delete()
        data['form_is_valid'] = True
        patients = Nursing.objects.all()
        data['html_nursing_list'] = render_to_string('patient_data/nursing_data/nursing_data.html', {'patients': patients})
        return JsonResponse(data)
    else:
        context = {'nursings': nursings}
        data['html_form'] = render_to_string('patient_data/nursing_data/partial_delete.html', context, request=request)
        return JsonResponse(data)

    return JsonResponse(data)