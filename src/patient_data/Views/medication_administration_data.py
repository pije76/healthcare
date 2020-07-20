from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.db import connection
from django.db.models import Count, Sum, F, Q
from django.db.models.functions import Trunc
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.translation import ugettext as _
from django.views.generic import ListView

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
def save_medication_administration_data_form(request, form, template_name):
    data = dict()

    if request.method == 'POST':
        if form.is_valid():
            patients = MedicationAdministrationRecord()
            patients = form.save(commit=False)
            patients.patient = request.user
            patients.save()
            data['form_is_valid'] = True
            patients = MedicationAdministrationRecord.objects.all()
            data['html_candidat_list'] = render_to_string('patient_data/patient_list.html', {'patients': patients})
        else:
            data['form_is_valid'] = False

    context = {
        'form': form,
    }
    data['html_form'] = render_to_string(template_name, context, request=request)

    return JsonResponse(data)


@login_required
def medication_administration_data(request, username):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
    page_title = _('Medication Administration Record')
    patientid = PatientProfile.objects.get(username=username).id
    patients = MedicationAdministrationRecord.objects.filter(patient=patientid)
    profiles = PatientProfile.objects.filter(pk=patientid)
    allergies = MedicationAdministrationRecord.objects.filter(patient=patientid).values_list('allergy', flat=True).first()

    context = {
        'logos': logos,
        'titles': titles,
        'page_title': page_title,
        'patients': patients,
        'profiles': profiles,
        'allergies': allergies,
    }

    return render(request, 'patient_data/medication_administration_data/medication_administration_data.html', context)

@login_required
def medication_administration_data_edit(request, id):
    medication_administration_datas = get_object_or_404(MedicationAdministrationRecord, pk=id)
    if request.method == 'POST':
        form = MedicationAdministrationRecordForm(request.POST or None, instance=medication_administration_datas)
    else:
        form = MedicationAdministrationRecordForm(instance=medication_administration_datas)
    return save_medication_administration_data_form(request, form, 'patient_data/medication_administration_data/partial_edit.html')


@login_required
def medication_administration_data_delete(request, id):
    medication_administration_datas = get_object_or_404(MedicationAdministrationRecord, pk=id)
    data = dict()

    if request.method == 'POST':
        medication_administration_datas.delete()
        data['form_is_valid'] = True
        patients = MedicationAdministrationRecord.objects.all()
        data['html_candidat_list'] = render_to_string('patient_data/patient_list.html', {'patients': patients})
        return JsonResponse(data)
    else:
        context = {'medication_administration_datas': medication_administration_datas}
        data['html_form'] = render_to_string('patient_data/medication_administration_data/partial_delete.html', context, request=request)
        return JsonResponse(data)

    return JsonResponse(data)
