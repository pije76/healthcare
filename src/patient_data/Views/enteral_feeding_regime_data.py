from django.contrib.auth.decorators import login_required
from django.db import connection
from django.db.models import Sum
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
def save_enteral_feeding_regime_data_form(request, form, template_name):
    data = dict()

    if request.method == 'POST':
        if form.is_valid():
            patients = Appointment()
            patients = form.save(commit=False)
            patients.patient = request.user
            patients.save()
            data['form_is_valid'] = True
            patients = Appointment.objects.all()
            data['html_enteral_feeding_regime_list'] = render_to_string('patient_data/enteral_feeding_regime_data/enteral_feeding_regime_data.html', {'patients': patients})
        else:
            data['form_is_valid'] = False

    context = {
        'form': form,
    }
    data['html_form'] = render_to_string(template_name, context, request=request)

    return JsonResponse(data)


@login_required
def enteral_feeding_regime_data(request, id):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
    page_title = _('Enteral Feeding Regime')
    patients = EnteralFeedingRegime.objects.filter(patient=id)
    total = EnteralFeedingRegime.objects.aggregate(Sum('amount'))
    profiles = PatientProfile.objects.filter(pk=id)
    total_feeding = EnteralFeedingRegime.objects.aggregate(Sum('amount'))
    total_fluids = EnteralFeedingRegime.objects.filter(patient=id).values_list('total_fluids', flat=True).first()
    all_total_fluids = EnteralFeedingRegime.objects.aggregate(Sum('total_fluids'))

    context = {
        'logos': logos,
        'titles': titles,
        'page_title': page_title,
        'patients': patients,
        'profiles': profiles,
        'total': total,
        'total_feeding': total_feeding,
        'total_fluids': total_fluids,
        'all_total_fluids': all_total_fluids,
    }

    return render(request, 'patient_data/enteral_feeding_regime_data/enteral_feeding_regime_data.html', context)


@login_required
def enteral_feeding_regime_data_edit(request, id):
    enteral_feeding_regimes = get_object_or_404(Appointment, pk=id)
    if request.method == 'POST':
        form = AppointmentForm(request.POST or None, instance=enteral_feeding_regimes)
    else:
        form = AppointmentForm(instance=enteral_feeding_regimes)
    return save_enteral_feeding_regime_data_form(request, form, 'patient_data/enteral_feeding_regime_data/partial_edit.html')


@login_required
def enteral_feeding_regime_data_delete(request, id):
    enteral_feeding_regimes = get_object_or_404(Appointment, pk=id)
    data = dict()

    if request.method == 'POST':
        enteral_feeding_regimes.delete()
        data['form_is_valid'] = True
        patients = Appointment.objects.all()
        data['html_enteral_feeding_regime_list'] = render_to_string('patient_data/enteral_feeding_regime_data/enteral_feeding_regime_data.html', {'patients': patients})
        return JsonResponse(data)
    else:
        context = {'enteral_feeding_regimes': enteral_feeding_regimes}
        data['html_form'] = render_to_string('patient_data/enteral_feeding_regime_data/partial_delete.html', context, request=request)
        return JsonResponse(data)

    return JsonResponse(data)
