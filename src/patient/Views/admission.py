from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.utils.translation import ugettext as _
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.forms.models import model_to_dict
from django.db.models import F, Func, Value, CharField

from patient.models import *
from patient.Forms.admission import *
from accounts.models import *
from accounts.forms import *
from customers.models import *
from data.forms import *

from bootstrap_modal_forms.generic import *

import datetime
from collections import defaultdict
import pytz


@login_required
def admission_list(request, username):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
    page_title = _('Admission Form')
    patientid = UserProfile.objects.get(username=username).id
    patients = Admission.objects.filter(patient=patientid)
    patientform = UserProfile.objects.filter(username=username)
    ecform = Family.objects.filter(patient=patientid)
    admissionform = Admission.objects.filter(patient=patientid).exclude(admitted_admission__isnull=True)
#    admissionform = [item for item in admissionform]
#    admissionform = list(admissionform)
#    admissionform = str(admissionform)
#    print(len(admissionform))

    profiles = UserProfile.objects.filter(pk=patientid)
    allergyform = Allergy.objects.filter(patient=patientid)

    context = {
        'logos': logos,
        'titles': titles,
        'page_title': page_title,
        'patients': patients,
        'patientform': patientform,
        'ecform': ecform,
        'admissionform': admissionform,
        'allergyform': allergyform,
        'profiles': profiles,
    }

    return render(request, 'patient/admission/admission_data.html', context)


@login_required
def admission_create(request, username):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
    page_title = _('Admission Form')
    patients = get_object_or_404(UserProfile, username=username)
    patientid = get_object_or_404(UserProfile, username=username).id
    patientusername = get_object_or_404(UserProfile, username=username).username
    username = get_object_or_404(UserProfile, username=username).username
    password = get_object_or_404(UserProfile, username=username).password
    first_name = get_object_or_404(UserProfile, username=username).first_name
    profiles = UserProfile.objects.filter(username=username)
    icnumbers = UserProfile.objects.filter(username=username).values_list('ic_number', flat=True).first()
    allergy_drug = Allergy.objects.filter(patient=patientid).values_list('allergy_drug', flat=True).first()
    allergy_food = Allergy.objects.filter(patient=patientid).values_list('allergy_food', flat=True).first()
    allergy_others = Allergy.objects.filter(patient=patientid).values_list('allergy_others', flat=True).first()

    initial = {
        'patient': patients,
        'patient_name': patients,
        'username': username,
        'is_active': True,
        'is_patient': True,
        'password': password,
        'first_name': first_name,
        'admission_by': request.user,
    }

    initial_admision_formset = [{
        'patient': patients,
        'medication_date': get_today,
        'medication_time': '00:00',
        'date_admission': get_datetime,
        'admission_by': request.user,
    }
    for item in profiles]

    initial_martformset_medication = [{
        'patient': item.id,
        'own_medication': 'Yes',
    }
    for item in profiles]

    initial_own_medication = {
        'patient': patients,
        'own_medication': 'No',
    }

    initial_allergy = {
        'patient': patients,
        'medication_date': get_today,
        'allergy_drug': allergy_drug,
        'allergy_food': allergy_food,
        'allergy_others': allergy_others,

    }

    if request.method == 'POST':
        patientprofile_form = PatientProfile_ModelForm(request.POST or None, request.FILES or None, instance=patients, prefix="patientprofile_form")
        family_formset = Family_ModelFormSet(request.POST or None, request.FILES or None, prefix="family_formset")
        admision_form = Admission_ModelForm(request.POST or None, request.FILES or None, prefix="admision_form")
        admision_formset = Admission_FormSet(request.POST or None, prefix="admision_formset")
        allergy_form = Allergy_Model_Form(request.POST or None, prefix="allergy_form")
        martformset_medication = MedicationAdministrationRecordTemplate_FormSet(request.POST or None, prefix="martformset_medication")
        martform_own_medication = MedicationAdministrationRecordTemplate_OwnForm(request.POST or None, prefix="martform_own_medication")

        if patientprofile_form.is_valid():
            profile = patientprofile_form.save(commit=False)
            profile.full_name = patientprofile_form.cleaned_data['full_name']
            profile.username = patientprofile_form.cleaned_data['username']
            profile.email = patientprofile_form.cleaned_data['email']
            profile.password = patientprofile_form.cleaned_data['password']
            profile.date_joined = patientprofile_form.cleaned_data['date_joined']
            profile.is_patient = patientprofile_form.cleaned_data['is_patient']
            profile.is_active = patientprofile_form.cleaned_data['is_active']
            profile.ic_number = patientprofile_form.cleaned_data['ic_number']
            profile.ic_upload = patientprofile_form.cleaned_data['ic_upload']
            profile.birth_date = patientprofile_form.cleaned_data['birth_date']
            if profile.birth_date is None:
                pass
            if profile.birth_date is not None:
                delta_day = int((datetime.datetime.now().date() - profile.birth_date).days / 365.24219)
                profile.age = delta_day
            profile.gender = patientprofile_form.cleaned_data['gender']
            profile.marital_status = patientprofile_form.cleaned_data['marital_status']
            profile.religion = patientprofile_form.cleaned_data['religion']
            profile.occupation = patientprofile_form.cleaned_data['occupation']
            profile.communication_sight = patientprofile_form.cleaned_data['communication_sight']
            profile.communication_hearing = patientprofile_form.cleaned_data['communication_hearing']
            profile.address = patientprofile_form.cleaned_data['address']
            profile.save()

        if admision_form.is_valid():

            get_ic_number = UserProfile.objects.filter(full_name=patients).values_list("ic_number", flat=True).first()
            get_ic_upload = UserProfile.objects.filter(full_name=patients).values_list("ic_upload", flat=True).first()
            get_ic_birth_date = UserProfile.objects.filter(full_name=patients).values_list("birth_date", flat=True).first()
            get_ic_age = UserProfile.objects.filter(full_name=patients).values_list("age", flat=True).first()
            get_gender = UserProfile.objects.filter(full_name=patients).values_list("gender", flat=True).first()
            get_marital_status = UserProfile.objects.filter(full_name=patients).values_list("marital_status", flat=True).first()
            get_religion = UserProfile.objects.filter(full_name=patients).values_list("religion", flat=True).first()
            get_occupation = UserProfile.objects.filter(full_name=patients).values_list("occupation", flat=True).first()
            get_communication_sight = UserProfile.objects.filter(full_name=patients).values_list("communication_sight", flat=True).first()
            get_communication_hearing = UserProfile.objects.filter(full_name=patients).values_list("communication_hearing", flat=True).first()
            get_address = UserProfile.objects.filter(full_name=patients).values_list("address", flat=True).first()

            admision = Admission()
#            admision = admision_form.save(commit=False)
            admision.patient = admision_form.cleaned_data['patient']
            admision.date_admission = admision_form.cleaned_data['date_admission']
            admision.time_admission = admision_form.cleaned_data['time_admission']
            admision.admitted_admission = admision_form.cleaned_data['admitted_admission']
            admision.mode_admission = admision_form.cleaned_data['mode_admission']

            admision.ic_number = get_ic_number
            admision.ic_upload = get_ic_upload
            admision.birth_date = get_ic_birth_date
            admision.age = get_ic_age
            admision.gender = get_gender
            admision.marital_status = get_marital_status
            admision.religion = get_religion
            admision.occupation = get_occupation
            admision.communication_sight = get_communication_sight
            admision.communication_hearing = get_communication_hearing
            admision.address = get_address

            admision.general_condition = ', '.join(admision_form.cleaned_data['general_condition'])
            admision.vital_sign_temperature = admision_form.cleaned_data['vital_sign_temperature']
            admision.vital_sign_pulse = admision_form.cleaned_data['vital_sign_pulse']
            admision.vital_sign_bp_upper = admision_form.cleaned_data['vital_sign_bp_upper']
            admision.vital_sign_bp_lower = admision_form.cleaned_data['vital_sign_bp_lower']
            admision.vital_sign_resp = admision_form.cleaned_data['vital_sign_resp']
            admision.vital_sign_spo2 = admision_form.cleaned_data['vital_sign_spo2']
            admision.vital_sign_on_oxygen_therapy = admision_form.cleaned_data['vital_sign_on_oxygen_therapy']
            admision.vital_sign_on_oxygen_therapy_flow_rate = admision_form.cleaned_data['vital_sign_on_oxygen_therapy_flow_rate']
            admision.vital_sign_hgt = admision_form.cleaned_data['vital_sign_hgt']

            admision.biohazard_infectious_disease = admision_form.cleaned_data['biohazard_infectious_disease']
            admision.invasive_line_insitu = ', '.join(admision_form.cleaned_data['invasive_line_insitu'])
            admision.medical_history = ', '.join(admision_form.cleaned_data['medical_history'])
            admision.surgical_history_none = ''.join(admision_form.cleaned_data['surgical_history_none'])
            admision.surgical_history = ''.join(admision_form.cleaned_data['surgical_history'])

            admision.adaptive_aids_with_patient = ', '.join(admision_form.cleaned_data['adaptive_aids_with_patient'])
            admision.adaptive_aids_with_patient_others = admision_form.cleaned_data['adaptive_aids_with_patient_others']
            admision.orientation = ', '.join(admision_form.cleaned_data['orientation'])
            admision.special_information = admision_form.cleaned_data['special_information']
            admision.admission_by = admision_form.cleaned_data['admission_by']
            admision.save()

        if admision_formset.is_valid():
            get_admission_date_admission = Admission.objects.filter(patient=patients).values_list("date_admission", flat=True).first()
            get_admission_time_admission = Admission.objects.filter(patient=patients).values_list("time_admission", flat=True).first()
            get_admission_admitted_admission = Admission.objects.filter(patient=patients).values_list("admitted_admission", flat=True).first()
            get_admission_mode_admission = Admission.objects.filter(patient=patients).values_list("mode_admission", flat=True).first()
            get_admission_ic_number = Admission.objects.filter(patient=patients).values_list("ic_number", flat=True).first()
            get_admission_ic_upload = Admission.objects.filter(patient=patients).values_list("ic_upload", flat=True).first()
            get_admission_birth_date = Admission.objects.filter(patient=patients).values_list("birth_date", flat=True).first()
            get_admission_age = Admission.objects.filter(patient=patients).values_list("age", flat=True).first()
            get_admission_gender = Admission.objects.filter(patient=patients).values_list("gender", flat=True).first()
            get_admission_marital_status = Admission.objects.filter(patient=patients).values_list("marital_status", flat=True).first()
            get_admission_religion = Admission.objects.filter(patient=patients).values_list("religion", flat=True).first()
            get_admission_occupation = Admission.objects.filter(patient=patients).values_list("occupation", flat=True).first()
            get_admission_communication_sight = Admission.objects.filter(patient=patients).values_list("communication_sight", flat=True).first()
            get_admission_communication_hearing = Admission.objects.filter(patient=patients).values_list("communication_hearing", flat=True).first()
            get_admission_address = Admission.objects.filter(patient=patients).values_list("address", flat=True).first()
            get_admission_general_condition = Admission.objects.filter(patient=patients).values_list("general_condition", flat=True).first()
            get_admission_vital_sign_temperature = Admission.objects.filter(patient=patients).values_list("vital_sign_temperature", flat=True).first()
            get_admission_vital_sign_pulse = Admission.objects.filter(patient=patients).values_list("vital_sign_pulse", flat=True).first()
            get_admission_vital_sign_bp_upper = Admission.objects.filter(patient=patients).values_list("vital_sign_bp_upper", flat=True).first()
            get_admission_vital_sign_bp_lower = Admission.objects.filter(patient=patients).values_list("vital_sign_bp_lower", flat=True).first()
            get_admission_vital_sign_resp = Admission.objects.filter(patient=patients).values_list("vital_sign_resp", flat=True).first()
            get_admission_vital_sign_spo2 = Admission.objects.filter(patient=patients).values_list("vital_sign_spo2", flat=True).first()
            get_admission_vital_sign_on_oxygen_therapy = Admission.objects.filter(patient=patients).values_list("vital_sign_on_oxygen_therapy", flat=True).first()
            get_admission_vital_sign_on_oxygen_therapy_flow_rate = Admission.objects.filter(patient=patients).values_list("vital_sign_on_oxygen_therapy_flow_rate", flat=True).first()
            get_admission_vital_sign_hgt = Admission.objects.filter(patient=patients).values_list("vital_sign_hgt", flat=True).first()
            get_admission_biohazard_infectious_disease = Admission.objects.filter(patient=patients).values_list("biohazard_infectious_disease", flat=True).first()
            get_admission_invasive_line_insitu = Admission.objects.filter(patient=patients).values_list("invasive_line_insitu", flat=True).first()
            get_admission_medical_history = Admission.objects.filter(patient=patients).values_list("medical_history", flat=True).first()
            get_admission_surgical_history_none = Admission.objects.filter(patient=patients).values_list("surgical_history_none", flat=True).first()
            get_admission_surgical_history = Admission.objects.filter(patient=patients).values_list("surgical_history", flat=True).first()
            get_admission_adaptive_aids_with_patient = Admission.objects.filter(patient=patients).values_list("adaptive_aids_with_patient", flat=True).first()
            get_admission_adaptive_aids_with_patient_others = Admission.objects.filter(patient=patients).values_list("adaptive_aids_with_patient_others", flat=True).first()
            get_admission_orientation = Admission.objects.filter(patient=patients).values_list("orientation", flat=True).first()
            get_admission_special_information = Admission.objects.filter(patient=patients).values_list("special_information", flat=True).first()
            get_admission_admission_by = Admission.objects.filter(patient=patients).values_list("admission_by", flat=True).first()

            get_admission_date_admission = datetime.datetime.strftime(get_admission_date_admission, '%Y-%m-%d')
            get_admission_time_admission = datetime.time.strftime(get_admission_time_admission, '%H:%M')
            get_admission_birth_date = datetime.datetime.strftime(get_admission_birth_date, '%Y-%m-%d')

            for item in admision_formset:
                admision_formset_profile = Admission()
                admision_formset_profile.patient = patients
                admision_formset_profile.date_admission = get_admission_date_admission
                admision_formset_profile.time_admission = get_admission_time_admission
                admision_formset_profile.admitted_admission = str(get_admission_admitted_admission)
                admision_formset_profile.mode_admission = str(get_admission_mode_admission)
#                admision_formset_profile.ic_number = str(get_admission_ic_number)
                admision_formset_profile.ic_upload = get_admission_ic_upload
                admision_formset_profile.birth_date = get_admission_birth_date
                admision_formset_profile.age = str(get_admission_age)
                admision_formset_profile.gender = str(get_admission_gender)
                admision_formset_profile.marital_status = str(get_admission_marital_status)
                admision_formset_profile.religion = str(get_admission_religion)
                admision_formset_profile.occupation = str(get_admission_occupation)
                admision_formset_profile.communication_sight = str(get_admission_communication_sight)
                admision_formset_profile.communication_hearing = str(get_admission_communication_hearing)
                admision_formset_profile.address = str(get_admission_address)
                admision_formset_profile.general_condition = str(get_admission_general_condition)
                admision_formset_profile.vital_sign_temperature = str(get_admission_vital_sign_temperature)
                admision_formset_profile.vital_sign_pulse = str(get_admission_vital_sign_pulse)
                admision_formset_profile.vital_sign_bp_upper = str(get_admission_vital_sign_bp_upper)
                admision_formset_profile.vital_sign_bp_lower = str(get_admission_vital_sign_bp_lower)
                admision_formset_profile.vital_sign_resp = str(get_admission_vital_sign_resp)
                admision_formset_profile.vital_sign_spo2 = str(get_admission_vital_sign_spo2)
                admision_formset_profile.vital_sign_on_oxygen_therapy = str(get_admission_vital_sign_on_oxygen_therapy)
                admision_formset_profile.vital_sign_on_oxygen_therapy_flow_rate = str(get_admission_vital_sign_on_oxygen_therapy_flow_rate)
                admision_formset_profile.vital_sign_hgt = str(get_admission_vital_sign_hgt)
                admision_formset_profile.biohazard_infectious_disease = str(get_admission_biohazard_infectious_disease)
                admision_formset_profile.invasive_line_insitu = str(get_admission_invasive_line_insitu)
                admision_formset_profile.medical_history = str(get_admission_medical_history)
                admision_formset_profile.surgical_history_none = str(get_admission_surgical_history_none)
                admision_formset_profile.surgical_history = str(get_admission_surgical_history)
                admision_formset_profile.adaptive_aids_with_patient = str(get_admission_adaptive_aids_with_patient)
                admision_formset_profile.adaptive_aids_with_patient_others = str(get_admission_adaptive_aids_with_patient_others)
                admision_formset_profile.orientation = str(get_admission_orientation)
                admision_formset_profile.special_information = str(get_admission_special_information)
                admision_formset_profile.admission_by = str(get_admission_admission_by)

                admision_formset_profile.date_diagnosis = item.cleaned_data['date_diagnosis']
                admision_formset_profile.diagnosis = item.cleaned_data['diagnosis']
                admision_formset_profile.date_operation = item.cleaned_data['date_operation']
                admision_formset_profile.operation = item.cleaned_data['operation']

                admision_formset_profile.save()



        if allergy_form.is_valid():
#            allergy_data = Allergy()
            allergy_data = allergy_form.save(commit=False)
#            allergy_data.patient = patients
            allergy_data.patient = allergy_form.cleaned_data['patient']
            allergy_data.allergy_drug = allergy_form.cleaned_data['allergy_drug']
            allergy_data.allergy_food = allergy_form.cleaned_data['allergy_food']
            allergy_data.allergy_others = allergy_form.cleaned_data['allergy_others']
            allergy_data.save()

            medication_allergy_data = MedicationAdministrationRecord()
#            medication_allergy_data = allergy_form.save(commit=False)
            medication_allergy_data.patient = patients
            medication_allergy_data.medication_date = allergy_form.cleaned_data['medication_date']
            medication_allergy_data.allergy_drug = allergy_form.cleaned_data['allergy_drug']
            medication_allergy_data.allergy_food = allergy_form.cleaned_data['allergy_food']
            medication_allergy_data.allergy_others = allergy_form.cleaned_data['allergy_others']
            medication_allergy_data.save()

        if family_formset.is_valid():
            for item in family_formset:
                ec_profile = Family()
                ec_profile.patient = patients
                ec_profile.ec_name = item.cleaned_data['ec_name']
                ec_profile.ec_ic_number = item.cleaned_data['ec_ic_number']
                ec_profile.ec_ic_upload = item.cleaned_data['ec_ic_upload']
                ec_profile.ec_relationship = item.cleaned_data['ec_relationship']
                ec_profile.ec_phone = item.cleaned_data['ec_phone']
                ec_profile.ec_address = item.cleaned_data['ec_address']
                ec_profile.save()

        if martformset_medication.is_valid():
            for item in martformset_medication:
                medication_savemart_formset = MedicationAdministrationRecordTemplate()
                medication_savemart_formset.patient = patients
                medication_savemart_formset.medication_date = item.cleaned_data['medication_date']
                medication_savemart_formset.medication_time = item.cleaned_data['medication_time'].replace(minute=0, second=0)
                medication_savemart_formset.medication_drug_name = item.cleaned_data['medication_drug_name']
                medication_savemart_formset.medication_dosage = item.cleaned_data['medication_dosage']
                medication_savemart_formset.medication_unit = item.cleaned_data['medication_unit']
                medication_savemart_formset.medication_tablet_capsule = item.cleaned_data['medication_tablet_capsule']
                medication_savemart_formset.medication_frequency = item.cleaned_data['medication_frequency']
                medication_savemart_formset.own_medication = 'Yes'
                medication_savemart_formset.save()

#                medication_savemart_form = MedicationAdministrationRecord()
#                medication_savemart_form.patient = patients
#                medication_savemart_form.medication_template = item.cleaned_data['medication_template']
#                medication_savemart_form.medication_date = item.cleaned_data['medication_date']
#                medication_savemart_form.medication_time = item.cleaned_data['medication_time'].replace(minute=0, second=0)
#                medication_savemart_form.medication_drug_name = item.cleaned_data['medication_drug_name']
#                medication_savemart_form.medication_dosage = item.cleaned_data['medication_dosage']
#                medication_savemart_form.medication_unit = item.cleaned_data['medication_unit']
#                medication_savemart_form.medication_tablet_capsule = item.cleaned_data['medication_tablet_capsule']
#                medication_savemart_form.medication_frequency = item.cleaned_data['medication_frequency']
#                medication_savemart_form.save()

        if martform_own_medication.is_valid():
            get_medication_mart_date = MedicationAdministrationRecordTemplate.objects.filter(patient=patients).values_list("medication_date", flat=True).first()

            own_medication_data_mart = MedicationAdministrationRecordTemplate()
            own_medication_data_mart.patient = patients
            own_medication_data_mart.medication_date = martform_own_medication.cleaned_data['medication_date']
            own_medication_data_mart.own_medication = martform_own_medication.cleaned_data['own_medication']

            if MedicationAdministrationRecordTemplate.objects.filter(patient=patients).filter(medication_date=get_medication_mart_date, medication_time="00:00").exists():
                pass
            else:
                own_medication_data_mart.medication_time = MedicationAdministrationRecordTemplate.objects.create(patient=patients, own_medication="Yes", medication_date=get_medication_mart_date, medication_time='00:00')
            if MedicationAdministrationRecordTemplate.objects.filter(patient=patients).filter(medication_date=get_medication_mart_date, medication_time="01:00").exists():
                pass
            else:
                own_medication_data_mart.medication_time = MedicationAdministrationRecordTemplate.objects.create(patient=patients, own_medication="Yes", medication_date=get_medication_mart_date, medication_time='01:00')
            if MedicationAdministrationRecordTemplate.objects.filter(patient=patients).filter(medication_date=get_medication_mart_date, medication_time="02:00").exists():
                pass
            else:
                own_medication_data_mart.medication_time = MedicationAdministrationRecordTemplate.objects.create(patient=patients, own_medication="Yes", medication_date=get_medication_mart_date, medication_time='02:00')
            if MedicationAdministrationRecordTemplate.objects.filter(patient=patients).filter(medication_date=get_medication_mart_date, medication_time="03:00").exists():
                pass
            else:
                own_medication_data_mart.medication_time = MedicationAdministrationRecordTemplate.objects.create(patient=patients, own_medication="Yes", medication_date=get_medication_mart_date, medication_time='03:00')
            if MedicationAdministrationRecordTemplate.objects.filter(patient=patients).filter(medication_date=get_medication_mart_date, medication_time="04:00").exists():
                pass
            else:
                own_medication_data_mart.medication_time = MedicationAdministrationRecordTemplate.objects.create(patient=patients, own_medication="Yes", medication_date=get_medication_mart_date, medication_time='04:00')
            if MedicationAdministrationRecordTemplate.objects.filter(patient=patients).filter(medication_date=get_medication_mart_date, medication_time="05:00").exists():
                pass
            else:
                own_medication_data_mart.medication_time = MedicationAdministrationRecordTemplate.objects.create(patient=patients, own_medication="Yes", medication_date=get_medication_mart_date, medication_time='05:00')
            if MedicationAdministrationRecordTemplate.objects.filter(patient=patients).filter(medication_date=get_medication_mart_date, medication_time="06:00").exists():
                pass
            else:
                own_medication_data_mart.medication_time = MedicationAdministrationRecordTemplate.objects.create(patient=patients, own_medication="Yes", medication_date=get_medication_mart_date, medication_time='06:00')
            if MedicationAdministrationRecordTemplate.objects.filter(patient=patients).filter(medication_date=get_medication_mart_date, medication_time="07:00").exists():
                pass
            else:
                own_medication_data_mart.medication_time = MedicationAdministrationRecordTemplate.objects.create(patient=patients, own_medication="Yes", medication_date=get_medication_mart_date, medication_time='07:00')
            if MedicationAdministrationRecordTemplate.objects.filter(patient=patients).filter(medication_date=get_medication_mart_date, medication_time="08:00").exists():
                pass
            else:
                own_medication_data_mart.medication_time = MedicationAdministrationRecordTemplate.objects.create(patient=patients, own_medication="Yes", medication_date=get_medication_mart_date, medication_time='08:00')
            if MedicationAdministrationRecordTemplate.objects.filter(patient=patients).filter(medication_date=get_medication_mart_date, medication_time="09:00").exists():
                pass
            else:
                own_medication_data_mart.medication_time = MedicationAdministrationRecordTemplate.objects.create(patient=patients, own_medication="Yes", medication_date=get_medication_mart_date, medication_time='09:00')
            if MedicationAdministrationRecordTemplate.objects.filter(patient=patients).filter(medication_date=get_medication_mart_date, medication_time="10:00").exists():
                pass
            else:
                own_medication_data_mart.medication_time = MedicationAdministrationRecordTemplate.objects.create(patient=patients, own_medication="Yes", medication_date=get_medication_mart_date, medication_time='10:00')
            if MedicationAdministrationRecordTemplate.objects.filter(patient=patients).filter(medication_date=get_medication_mart_date, medication_time="11:00").exists():
                pass
            else:
                own_medication_data_mart.medication_time = MedicationAdministrationRecordTemplate.objects.create(patient=patients, own_medication="Yes", medication_date=get_medication_mart_date, medication_time='11:00')
            if MedicationAdministrationRecordTemplate.objects.filter(patient=patients).filter(medication_date=get_medication_mart_date, medication_time="12:00").exists():
                pass
            else:
                own_medication_data_mart.medication_time = MedicationAdministrationRecordTemplate.objects.create(patient=patients, own_medication="Yes", medication_date=get_medication_mart_date, medication_time='12:00')
            if MedicationAdministrationRecordTemplate.objects.filter(patient=patients).filter(medication_date=get_medication_mart_date, medication_time="13:00").exists():
                pass
            else:
                own_medication_data_mart.medication_time = MedicationAdministrationRecordTemplate.objects.create(patient=patients, own_medication="Yes", medication_date=get_medication_mart_date, medication_time='13:00')
            if MedicationAdministrationRecordTemplate.objects.filter(patient=patients).filter(medication_date=get_medication_mart_date, medication_time="14:00").exists():
                pass
            else:
                own_medication_data_mart.medication_time = MedicationAdministrationRecordTemplate.objects.create(patient=patients, own_medication="Yes", medication_date=get_medication_mart_date, medication_time='14:00')
            if MedicationAdministrationRecordTemplate.objects.filter(patient=patients).filter(medication_date=get_medication_mart_date, medication_time="15:00").exists():
                pass
            else:
                own_medication_data_mart.medication_time = MedicationAdministrationRecordTemplate.objects.create(patient=patients, own_medication="Yes", medication_date=get_medication_mart_date, medication_time='15:00')
            if MedicationAdministrationRecordTemplate.objects.filter(patient=patients).filter(medication_date=get_medication_mart_date, medication_time="16:00").exists():
                pass
            else:
                own_medication_data_mart.medication_time = MedicationAdministrationRecordTemplate.objects.create(patient=patients, own_medication="Yes", medication_date=get_medication_mart_date, medication_time='16:00')
            if MedicationAdministrationRecordTemplate.objects.filter(patient=patients).filter(medication_date=get_medication_mart_date, medication_time="17:00").exists():
                pass
            else:
                own_medication_data_mart.medication_time = MedicationAdministrationRecordTemplate.objects.create(patient=patients, own_medication="Yes", medication_date=get_medication_mart_date, medication_time='17:00')
            if MedicationAdministrationRecordTemplate.objects.filter(patient=patients).filter(medication_date=get_medication_mart_date, medication_time="18:00").exists():
                pass
            else:
                own_medication_data_mart.medication_time = MedicationAdministrationRecordTemplate.objects.create(patient=patients, own_medication="Yes", medication_date=get_medication_mart_date, medication_time='18:00')
            if MedicationAdministrationRecordTemplate.objects.filter(patient=patients).filter(medication_date=get_medication_mart_date, medication_time="19:00").exists():
                pass
            else:
                own_medication_data_mart.medication_time = MedicationAdministrationRecordTemplate.objects.create(patient=patients, own_medication="Yes", medication_date=get_medication_mart_date, medication_time='19:00')
            if MedicationAdministrationRecordTemplate.objects.filter(patient=patients).filter(medication_date=get_medication_mart_date, medication_time="20:00").exists():
                pass
            else:
                own_medication_data_mart.medication_time = MedicationAdministrationRecordTemplate.objects.create(patient=patients, own_medication="Yes", medication_date=get_medication_mart_date, medication_time='20:00')
            if MedicationAdministrationRecordTemplate.objects.filter(patient=patients).filter(medication_date=get_medication_mart_date, medication_time="21:00").exists():
                pass
            else:
                own_medication_data_mart.medication_time = MedicationAdministrationRecordTemplate.objects.create(patient=patients, own_medication="Yes", medication_date=get_medication_mart_date, medication_time='21:00')
            if MedicationAdministrationRecordTemplate.objects.filter(patient=patients).filter(medication_date=get_medication_mart_date, medication_time="22:00").exists():
                pass
            else:
                own_medication_data_mart.medication_time = MedicationAdministrationRecordTemplate.objects.create(patient=patients, own_medication="Yes", medication_date=get_medication_mart_date, medication_time='22:00')
            if MedicationAdministrationRecordTemplate.objects.filter(patient=patients).filter(medication_date=get_medication_mart_date, medication_time="23:00").exists():
                pass
            else:
                own_medication_data_mart.medication_time = MedicationAdministrationRecordTemplate.objects.create(patient=patients, own_medication="Yes", medication_date=get_medication_mart_date, medication_time='23:00')


            own_medication_mar = MedicationAdministrationRecord()
            own_medication_mar.patient = patients
#            own_medication_mar.medication_date = martform_own_medication.cleaned_data['medication_date']

            get_medication_mart_time0 = MedicationAdministrationRecordTemplate.objects.filter(patient=patients).filter(medication_time='00:00').first()
            get_medication_mart_time1 = MedicationAdministrationRecordTemplate.objects.filter(patient=patients).filter(medication_time='01:00').first()
            get_medication_mart_time2 = MedicationAdministrationRecordTemplate.objects.filter(patient=patients).filter(medication_time='02:00').first()
            get_medication_mart_time3 = MedicationAdministrationRecordTemplate.objects.filter(patient=patients).filter(medication_time='03:00').first()
            get_medication_mart_time4 = MedicationAdministrationRecordTemplate.objects.filter(patient=patients).filter(medication_time='04:00').first()
            get_medication_mart_time5 = MedicationAdministrationRecordTemplate.objects.filter(patient=patients).filter(medication_time='05:00').first()
            get_medication_mart_time6 = MedicationAdministrationRecordTemplate.objects.filter(patient=patients).filter(medication_time='06:00').first()
            get_medication_mart_time7 = MedicationAdministrationRecordTemplate.objects.filter(patient=patients).filter(medication_time='07:00').first()
            get_medication_mart_time8 = MedicationAdministrationRecordTemplate.objects.filter(patient=patients).filter(medication_time='08:00').first()
            get_medication_mart_time9 = MedicationAdministrationRecordTemplate.objects.filter(patient=patients).filter(medication_time='09:00').first()
            get_medication_mart_time10 = MedicationAdministrationRecordTemplate.objects.filter(patient=patients).filter(medication_time='10:00').first()
            get_medication_mart_time11 = MedicationAdministrationRecordTemplate.objects.filter(patient=patients).filter(medication_time='11:00').first()
            get_medication_mart_time12 = MedicationAdministrationRecordTemplate.objects.filter(patient=patients).filter(medication_time='12:00').first()
            get_medication_mart_time13 = MedicationAdministrationRecordTemplate.objects.filter(patient=patients).filter(medication_time='13:00').first()
            get_medication_mart_time14 = MedicationAdministrationRecordTemplate.objects.filter(patient=patients).filter(medication_time='14:00').first()
            get_medication_mart_time15 = MedicationAdministrationRecordTemplate.objects.filter(patient=patients).filter(medication_time='15:00').first()
            get_medication_mart_time16 = MedicationAdministrationRecordTemplate.objects.filter(patient=patients).filter(medication_time='16:00').first()
            get_medication_mart_time17 = MedicationAdministrationRecordTemplate.objects.filter(patient=patients).filter(medication_time='17:00').first()
            get_medication_mart_time18 = MedicationAdministrationRecordTemplate.objects.filter(patient=patients).filter(medication_time='18:00').first()
            get_medication_mart_time19 = MedicationAdministrationRecordTemplate.objects.filter(patient=patients).filter(medication_time='19:00').first()
            get_medication_mart_time20 = MedicationAdministrationRecordTemplate.objects.filter(patient=patients).filter(medication_time='20:00').first()
            get_medication_mart_time21 = MedicationAdministrationRecordTemplate.objects.filter(patient=patients).filter(medication_time='21:00').first()
            get_medication_mart_time22 = MedicationAdministrationRecordTemplate.objects.filter(patient=patients).filter(medication_time='22:00').first()
            get_medication_mart_time23 = MedicationAdministrationRecordTemplate.objects.filter(patient=patients).filter(medication_time='23:00').first()

            if MedicationAdministrationRecord.objects.filter(patient=patients).filter(medication_template=get_medication_mart_time0).exists():
                pass
            else:
                own_medication_mar.medication_time = MedicationAdministrationRecord.objects.create(patient=patients, medication_template=get_medication_mart_time0)
            if MedicationAdministrationRecord.objects.filter(patient=patients).filter(medication_template=get_medication_mart_time1).exists():
                pass
            else:
                own_medication_mar.medication_time = MedicationAdministrationRecord.objects.create(patient=patients, medication_template=get_medication_mart_time1)
            if MedicationAdministrationRecord.objects.filter(patient=patients).filter(medication_template=get_medication_mart_time2).exists():
                pass
            else:
                own_medication_mar.medication_time = MedicationAdministrationRecord.objects.create(patient=patients, medication_template=get_medication_mart_time2)
            if MedicationAdministrationRecord.objects.filter(patient=patients).filter(medication_template=get_medication_mart_time3).exists():
                pass
            else:
                own_medication_mar.medication_time = MedicationAdministrationRecord.objects.create(patient=patients, medication_template=get_medication_mart_time3)
            if MedicationAdministrationRecord.objects.filter(patient=patients).filter(medication_template=get_medication_mart_time4).exists():
                pass
            else:
                own_medication_mar.medication_time = MedicationAdministrationRecord.objects.create(patient=patients, medication_template=get_medication_mart_time4)
            if MedicationAdministrationRecord.objects.filter(patient=patients).filter(medication_template=get_medication_mart_time5).exists():
                pass
            else:
                own_medication_mar.medication_time = MedicationAdministrationRecord.objects.create(patient=patients, medication_template=get_medication_mart_time5)
            if MedicationAdministrationRecord.objects.filter(patient=patients).filter(medication_template=get_medication_mart_time6).exists():
                pass
            else:
                own_medication_mar.medication_time = MedicationAdministrationRecord.objects.create(patient=patients, medication_template=get_medication_mart_time6)
            if MedicationAdministrationRecord.objects.filter(patient=patients).filter(medication_template=get_medication_mart_time7).exists():
                pass
            else:
                own_medication_mar.medication_time = MedicationAdministrationRecord.objects.create(patient=patients, medication_template=get_medication_mart_time7)
            if MedicationAdministrationRecord.objects.filter(patient=patients).filter(medication_template=get_medication_mart_time8).exists():
                pass
            else:
                own_medication_mar.medication_time = MedicationAdministrationRecord.objects.create(patient=patients, medication_template=get_medication_mart_time8)
            if MedicationAdministrationRecord.objects.filter(patient=patients).filter(medication_template=get_medication_mart_time9).exists():
                pass
            else:
                own_medication_mar.medication_time = MedicationAdministrationRecord.objects.create(patient=patients, medication_template=get_medication_mart_time9)
            if MedicationAdministrationRecord.objects.filter(patient=patients).filter(medication_template=get_medication_mart_time10).exists():
                pass
            else:
                own_medication_mar.medication_time = MedicationAdministrationRecord.objects.create(patient=patients, medication_template=get_medication_mart_time10)
            if MedicationAdministrationRecord.objects.filter(patient=patients).filter(medication_template=get_medication_mart_time11).exists():
                pass
            else:
                own_medication_mar.medication_time = MedicationAdministrationRecord.objects.create(patient=patients, medication_template=get_medication_mart_time11)
            if MedicationAdministrationRecord.objects.filter(patient=patients).filter(medication_template=get_medication_mart_time12).exists():
                pass
            else:
                own_medication_mar.medication_time = MedicationAdministrationRecord.objects.create(patient=patients, medication_template=get_medication_mart_time12)
            if MedicationAdministrationRecord.objects.filter(patient=patients).filter(medication_template=get_medication_mart_time13).exists():
                pass
            else:
                own_medication_mar.medication_time = MedicationAdministrationRecord.objects.create(patient=patients, medication_template=get_medication_mart_time13)
            if MedicationAdministrationRecord.objects.filter(patient=patients).filter(medication_template=get_medication_mart_time14).exists():
                pass
            else:
                own_medication_mar.medication_time = MedicationAdministrationRecord.objects.create(patient=patients, medication_template=get_medication_mart_time14)
            if MedicationAdministrationRecord.objects.filter(patient=patients).filter(medication_template=get_medication_mart_time15).exists():
                pass
            else:
                own_medication_mar.medication_time = MedicationAdministrationRecord.objects.create(patient=patients, medication_template=get_medication_mart_time15)
            if MedicationAdministrationRecord.objects.filter(patient=patients).filter(medication_template=get_medication_mart_time16).exists():
                pass
            else:
                own_medication_mar.medication_time = MedicationAdministrationRecord.objects.create(patient=patients, medication_template=get_medication_mart_time16)
            if MedicationAdministrationRecord.objects.filter(patient=patients).filter(medication_template=get_medication_mart_time17).exists():
                pass
            else:
                own_medication_mar.medication_time = MedicationAdministrationRecord.objects.create(patient=patients, medication_template=get_medication_mart_time17)
            if MedicationAdministrationRecord.objects.filter(patient=patients).filter(medication_template=get_medication_mart_time18).exists():
                pass
            else:
                own_medication_mar.medication_time = MedicationAdministrationRecord.objects.create(patient=patients, medication_template=get_medication_mart_time18)
            if MedicationAdministrationRecord.objects.filter(patient=patients).filter(medication_template=get_medication_mart_time19).exists():
                pass
            else:
                own_medication_mar.medication_time = MedicationAdministrationRecord.objects.create(patient=patients, medication_template=get_medication_mart_time19)
            if MedicationAdministrationRecord.objects.filter(patient=patients).filter(medication_template=get_medication_mart_time20).exists():
                pass
            else:
                own_medication_mar.medication_time = MedicationAdministrationRecord.objects.create(patient=patients, medication_template=get_medication_mart_time20)
            if MedicationAdministrationRecord.objects.filter(patient=patients).filter(medication_template=get_medication_mart_time21).exists():
                pass
            else:
                own_medication_mar.medication_time = MedicationAdministrationRecord.objects.create(patient=patients, medication_template=get_medication_mart_time21)
            if MedicationAdministrationRecord.objects.filter(patient=patients).filter(medication_template=get_medication_mart_time22).exists():
                pass
            else:
                own_medication_mar.medication_time = MedicationAdministrationRecord.objects.create(patient=patients, medication_template=get_medication_mart_time22)
            if MedicationAdministrationRecord.objects.filter(patient=patients).filter(medication_template=get_medication_mart_time23).exists():
                pass
            else:
                own_medication_mar.medication_time = MedicationAdministrationRecord.objects.create(patient=patients, medication_template=get_medication_mart_time23)

#            own_medication_data_mart.save()
#            own_medication_mar.save()

            messages.success(request, _(page_title + ' form was created.'))
            return redirect('patient:patientdata_detail', username=patientusername)

        else:
            messages.warning(request, patientprofile_form.errors)
            messages.warning(request, family_formset.errors)
            messages.warning(request, admision_form.errors)
            messages.warning(request, admision_formset.errors)
            messages.warning(request, allergy_form.errors)
            messages.warning(request, martformset_medication.errors)
            messages.warning(request, martform_own_medication.errors)

    else:
        patientprofile_form = PatientProfile_ModelForm(initial=initial, instance=patients, prefix="patientprofile_form")
        family_formset = Family_ModelFormSet(initial=[{'patient': x} for x in profiles], prefix="family_formset")
        admision_form = Admission_ModelForm(initial=initial, prefix="admision_form")
        admision_formset = Admission_FormSet(initial=initial_admision_formset, prefix="admision_formset")
        allergy_form = Allergy_Model_Form(initial=initial_allergy, instance=patients, prefix="allergy_form")
        martformset_medication = MedicationAdministrationRecordTemplate_FormSet(initial=initial_martformset_medication, prefix="martformset_medication")
        martform_own_medication = MedicationAdministrationRecordTemplate_OwnForm(initial=initial_own_medication, prefix="martform_own_medication")

    context = {
        'logos': logos,
        'titles': titles,
        'page_title': page_title,
        'patients': patients,
        'profiles': profiles,
        'icnumbers': icnumbers,
        'patientprofile_form': patientprofile_form,
        'family_formset': family_formset,
        'admision_form': admision_form,
        'admision_formset': admision_formset,
        'allergy_form': allergy_form,
        'martformset_medication': martformset_medication,
        'martform_own_medication': martform_own_medication,
    }

    return render(request, 'patient/admission/admission_form.html', context)


class AdmissionUpdateView(BSModalUpdateView):
    model = Admission
    template_name = 'patient/admission/partial_edit.html'
    form_class = Admission_ModelForm_Update
    page_title = _('Admission Form')
    success_message = _(page_title + ' form has been save successfully.')

    def get_form(self, form_class=None):
        form = super().get_form(form_class=None)
        form.fields['date_admission'].label = _("Date Admission")
        form.fields['time_admission'].label = _("Time Admission")

        form.fields['full_name'].label = _("Patient Name")
        form.fields['ic_number'].label = _("IC Number")
        form.fields['ic_upload'].label = _("IC Upload")
        form.fields['age'].label = _("Age")
        form.fields['birth_date'].label = _("Birth Date")
        form.fields['gender'].label = _("Gender")
        form.fields['marital_status'].label = _("Marital Status")
        form.fields['marital_status_others'].label = _("Others")
        form.fields['religion'].label = _("Religion")
        form.fields['religion_others'].label = _("Others")
        form.fields['occupation'].label = _("Occupation")
        form.fields['occupation_others'].label = _("Others")
        form.fields['communication_sight'].label = _("Communication Sight")
        form.fields['communication_hearing'].label = _("Communication Hearing")
        form.fields['communication_hearing_others'].label = _("Others")
        form.fields['address'].label = _("Address")

        form.fields['ec_name'].label = _("EC Name")
        form.fields['ec_ic_number'].label = _("EC IC Number")
        form.fields['ec_ic_upload'].label = _("EC IC Upload")
        form.fields['ec_relationship'].label = _("EC Relationship")
        form.fields['ec_phone'].label = _("EC Phone")
        form.fields['ec_address'].label = _("EC Address")

        form.fields['admitted_admission'].label = _("Admitted Through")
        form.fields['admitted_others'].label = _("Others")
        form.fields['mode_admission'].label = _("Mode of Admission")

        form.fields['general_condition'].label = _("General Condition")
        form.fields['vital_sign_temperature'].label = _("Vital Sign-Temperature")
        form.fields['vital_sign_pulse'].label = _("Vital Sign-Pulse")
        form.fields['vital_sign_bp_upper'].label = _("Vital Sign-BP Upper")
        form.fields['vital_sign_bp_lower'].label = _("Vital Sign-BP Lower")
        form.fields['vital_sign_resp'].label = _("Vital Sign-Resp")
        form.fields['vital_sign_spo2'].label = _("Vital Sign-SPO2")
        form.fields['vital_sign_on_oxygen_therapy'].label = _("Vital Sign-On Oxygen Therapy")
        form.fields['vital_sign_on_oxygen_therapy_flow_rate'].label = _("Vital Sign-On Oxygen Therapy Flow Rate")
        form.fields['vital_sign_hgt'].label = _("Vital Sign-HGT")

        form.fields['allergy_drug'].label = _("Allergy Drug")
        form.fields['allergy_food'].label = _("Allergy Food")
        form.fields['allergy_others'].label = _("Allergy Others")

        form.fields['biohazard_infectious_disease'].label = _("Biohazard Infectious Disease")
        form.fields['biohazard_infectious_disease_others'].label = _("Others")
        form.fields['invasive_line_insitu'].label = _("Invasive Line Insitu")
        form.fields['invasive_line_insitu_others'].label = _("Others")
        form.fields['medical_history'].label = _("Medical History")
        form.fields['medical_history_others'].label = _("Others")
        form.fields['surgical_history_none'].label = _("Surgical History None")
        form.fields['surgical_history'].label = _("Surgical History")

        form.fields['date_diagnosis'].label = _("Date Diagnosis")
        form.fields['diagnosis'].label = _("Diagnosis")
        form.fields['date_operation'].label = _("Date Operation")
        form.fields['operation'].label = _("Operation")

        form.fields['own_medication'].label = _("Own Medication")
        form.fields['medication_time'].label = _("Medication Time")
        form.fields['medication_drug_name'].label = _("Medication Drug Name")
        form.fields['medication_dosage'].label = _("Medication Dosage")
        form.fields['medication_unit'].label = _("Medication Unit")
        form.fields['medication_tablet_capsule'].label = _("Medication Tablet Capsule")
        form.fields['medication_frequency'].label = _("Medication Frequency")

        form.fields['adaptive_aids_with_patient'].label = _("Adaptive Aids With Patient")
        form.fields['adaptive_aids_with_patient_others'].label = _("Others")
        form.fields['orientation'].label = _("Orientation")
        form.fields['special_information'].label = _("Special Information")
        form.fields['admission_by'].label = _("Admission by")

        return form

    def get_success_url(self):
        username = self.kwargs['username']
        return reverse_lazy('patient:admission_list', kwargs={'username': username})


admission_edit = AdmissionUpdateView.as_view()


class AdmissionDeleteView(BSModalDeleteView):
    model = Admission
    template_name = 'patient/admission/partial_delete.html'
    page_title = _('Admission Form')
    success_message = _(page_title + ' form was deleted.')

    def get_success_url(self):
        username = self.kwargs['username']
        return reverse_lazy('patient:admission_list', kwargs={'username': username})

admission_delete = AdmissionDeleteView.as_view()
