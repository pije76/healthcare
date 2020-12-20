from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.db import connection
from django.db.models import Count, Sum, F, Q
from django.db.models.functions import Trunc
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.translation import ugettext as _
from django.views.generic import ListView

from patient.models import *
from patient.Forms.medication_administration import *
from accounts.models import *
from customers.models import *
from data.forms import *
from bootstrap_modal_forms.generic import *


@login_required
def medication_administration_list(request, username):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
    page_title = _('Medication Administration Record')
    patientid = UserProfile.objects.get(username=username).id
#   patients = UserProfile.objects.filter(username=username)
    patients = MedicationAdministrationRecord.objects.filter(patient=patientid)
    icnumbers = UserProfile.objects.filter(username=username).values_list('ic_number', flat=True).first()
#   profiles = UserProfile.objects.filter(pk=patientid)
    full_name_profiles = UserProfile.objects.filter(username=username).values_list('full_name', flat=True).first()
    profiles = UserProfile.objects.filter(pk=patientid)
#   allergies = MedicationAdministrationRecord.objects.filter(patient=patientid).values_list('allergy', flat=True).first()
    medicine_date = MedicationAdministrationRecord.objects.filter(patient=patientid).values_list('medication_date', flat=True).first()
#   medicine_data = MedicationAdministrationRecord.objects.filter(patient=patientid)
    get_lastdate = MedicationAdministrationRecord.objects.filter(patient=patientid).order_by('-medication_date').exclude(medication_time__isnull=True).values_list('medication_date', flat=True).first()
    medicine_data = MedicationAdministrationRecord.objects.filter(patient=patientid).filter(medication_date=get_lastdate).exclude(medication_time__isnull=True)
    medicine_stat = MedicationAdministrationRecord.objects.filter(patient=patientid).exclude(medication_time__isnull=False)
#    medicine_stat = MedicationAdministrationRecord.objects.filter(patient=patientid).values_list('medication_stat_date', flat=True).first()
    allergy_drug_data = Allergy.objects.filter(patient=patientid).values_list('allergy_drug', flat=True).first()
    allergy_food_data = Allergy.objects.filter(patient=patientid).values_list('allergy_food', flat=True).first()
    allergy_others_data = Allergy.objects.filter(patient=patientid).values_list('allergy_others', flat=True).first()
    themes = request.session.get('theme')

#   if request.method == 'GET':
#   form = MedicationAdministrationRecord_Form()

    initial_list = {
        'medication_date': get_lastdate,
    }

    if request.method == 'POST':
        form = MedicationAdministrationRecordTemplate_ModelForm_Set(request.POST or None)

        if form.is_valid():
            #       profile = IntakeOutput()
            #       profile.patient = patients
            #       profile.date = form.cleaned_data['date']
            #       profile.save()

            messages.success(request, _(page_title + ' form was created.'))
            return redirect('patient:patientdata_detail', username=patients.username)
        else:
            messages.warning(request, form.errors)
    else:
        form = MedicationAdministrationRecordTemplate_ModelForm_Set(initial=initial_list)

    context = {
        'logos': logos,
        'titles': titles,
        'page_title': page_title,
        'patients': patients,
        'profiles': profiles,
        #       'allergies': allergies,
        'icnumbers': icnumbers,
        'full_name_profiles': full_name_profiles,
        'medicine_date': medicine_date,
        'allergy_drug_data': allergy_drug_data,
        'allergy_food_data': allergy_food_data,
        'allergy_others_data': allergy_others_data,
        'medicine_data': medicine_data,
        'medicine_stat': medicine_stat,
        'form': form,
        "themes": themes,
    }

    return render(request, 'patient/medication_administration/medication_administration_data.html', context)


@login_required
def medication_administration_create(request, username):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
    page_title = _('Medication Administration Record')

    patientid = UserProfile.objects.get(username=username).id
    icnumbers = UserProfile.objects.get(username=username).ic_number
    profiles = UserProfile.objects.filter(username=username)
    patients = get_object_or_404(UserProfile, username=username)
    allergies = get_object_or_404(Allergy, patient=patientid)
    themes = request.session.get('theme')

    allergy_profiles = get_object_or_404(Allergy, patient=patientid)
    patients_templates = MedicationAdministrationRecord.objects.filter(patient=patientid).filter(medication_time__in=['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00']).order_by("medication_time")

    initial_form = {
        'patient': patients,
        'ic_number': icnumbers,
    }

    initial_mart_formset = [{
        'patient': item.patient,
        'medication_date': item.medication_date,
        'medication_time': item.medication_time,
        'medication_medicine': item.medication_medicine,
        'medication_dosage': item.medication_dosage,
        'medication_unit': item.medication_unit,
        'medication_tablet_capsule': item.medication_tablet_capsule,
    }
        for item in patients_templates]

    initial_martstat_formset = [{
        'patient': item.full_name,
        # 'medication_time': get_time,
        'given_by': request.user,
    }
        for item in profiles]

    if request.method == 'POST':

        form = MedicationAdministrationRecordTemplate_ModelForm_Set(request.POST or None)
        formset = MedicationAdministrationRecordTemplate_ModelFormSet(request.POST or None, prefix='formset')
        stat_formset = MedicationAdministrationRecordTemplateStat_FormSet(request.POST or None, prefix='stat_formset')
        allergy_form = Allergy_Model_Form(request.POST or None)

        if allergy_form.is_valid():
            allergies = get_object_or_404(Allergy, patient=patientid)
            allergies.patient = allergy_form.cleaned_data['patient']
            allergies.allergy_drug = allergy_form.cleaned_data['allergy_drug']
            allergies.allergy_food = allergy_form.cleaned_data['allergy_food']
            allergies.allergy_others = allergy_form.cleaned_data['allergy_others']
            allergies.save()

#        if formset.is_valid() and stat_formset.is_valid():
        if formset.is_valid():
            for item in formset:
                mar_save = MedicationAdministrationRecord()
                mar_save.patient = patients
                mar_save.medication_date = item.cleaned_data['medication_date']
                mar_save.medication_time = item.cleaned_data['medication_time']
                mar_save.medication_medicine = item.cleaned_data['medication_medicine']
                mar_save.medication_dosage = item.cleaned_data['medication_dosage']
                mar_save.medication_unit = item.cleaned_data['medication_unit']
                mar_save.medication_tablet_capsule = item.cleaned_data['medication_tablet_capsule']
                mar_save.medication_frequency = item.cleaned_data['medication_frequency']

                mar_save.medication_route = item.cleaned_data['medication_route']
                mar_save.medication_source = item.cleaned_data['medication_source']
                mar_save.medication_status = item.cleaned_data['medication_status']
                mar_save.medication_done = item.cleaned_data['medication_done']
                mar_save.given_by = request.user
                mar_save.save()

        if stat_formset.is_valid():
            for itemstat in stat_formset:
                marstat_save = MedicationAdministrationRecord()
                marstat_save.patient = patients
                marstat_save.medication_stat_date = itemstat.cleaned_data['medication_stat_date']
                marstat_save.medication_stat_time = itemstat.cleaned_data['medication_stat_time']
                marstat_save.medication_medicine = itemstat.cleaned_data['medication_medicine']
                marstat_save.given_by = request.user
                marstat_save.save()

            messages.success(request, _(page_title + ' form was created.'))
            return redirect('patient:patientdata_detail', username=patients.username)
        else:
            messages.warning(request, form.errors)
            messages.warning(request, formset.errors)
            messages.warning(request, stat_formset.errors)
            messages.warning(request, allergy_form.errors)
    else:
        form = MedicationAdministrationRecordTemplate_ModelForm_Set(initial=initial_form)
        formset = MedicationAdministrationRecordTemplate_ModelFormSet(initial=initial_mart_formset, prefix='formset')
        stat_formset = MedicationAdministrationRecordTemplateStat_FormSet(initial=initial_martstat_formset, prefix='stat_formset')
        allergy_form = Allergy_Model_Form(instance=allergy_profiles)

    context = {
        'logos': logos,
        'titles': titles,
        'page_title': page_title,
        'patients': patients,
        'profiles': profiles,
        'icnumbers': icnumbers,
        'form': form,
        'formset': formset,
        'stat_formset': stat_formset,
        'allergy_form': allergy_form,
        "themes": themes,
    }

    return render(request, 'patient/medication_administration/medication_administration_form.html', context)


class MedicationAdministrationRecordUpdateView(BSModalUpdateView):
    model = MedicationAdministrationRecord
    template_name = 'patient/medication_administration/partial_edit.html'
    form_class = MedicationAdministrationRecordTemplate_ModelForm_Set
    page_title = _('Medication Administration Record Form')
    success_message = _(page_title + ' form has been save successfully.')

    def get_form(self, form_class=None):
        form = super().get_form(form_class=None)
        form.fields['allergy_drug'].label = _("Allergy Drug")
        form.fields['allergy_food'].label = _("Allergy Dood")
        form.fields['allergy_others'].label = _("Allergy Others")
        form.fields['medication_date'].label = _("Date")
        form.fields['medication_time'].label = _("Time")
        form.fields['medication_medicine'].label = _("Drug Name")
        form.fields['medication_dosage'].label = _("Dosage")
        form.fields['medication_unit'].label = _("Unit")
        form.fields['medication_tablet_capsule'].label = _("Tablet/Capsule")
        form.fields['medication_frequency'].label = _("Frequency")
        form.fields['medication_route'].label = _("Route")
        form.fields['medication_status'].label = _("Status")
        form.fields['medication_source'].label = _("Source")
        form.fields['medication_done'].label = _("Done")
        return form

    def get_success_url(self):
        username = self.kwargs['username']
        return reverse_lazy('patient:medication_administration_list', kwargs={'username': username})


#medication_administration_edit = MedicationAdministrationRecordUpdateView.as_view()


@login_required
def medication_administration_edit(request, username, pk):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
    page_title = _('Edit Medication Administration Record')
    patients = get_object_or_404(UserProfile, username=username)
    patientid = UserProfile.objects.get(username=username).id
    profiles = UserProfile.objects.filter(username=username)
    icnumbers = UserProfile.objects.filter(username=username).values_list('ic_number', flat=True).first()
    admissions = MedicationAdministrationRecord.objects.get(patient_id=patientid, id=pk)
    themes = request.session.get('theme')

    initial = {
        'id': pk,
        'patient': patients,
        'given_by': request.user,
    }

    initial_formset = [{
        'patient': item,
        #       'patient': item.id,
        #       'patient': item.username,
        #       'patient': patients,
        'given_by': request.user,
    }
        for item in profiles]

    if request.method == 'POST':
        formset = MedicationAdministrationRecord_ModelFormSet(request.POST or None, queryset=MedicationAdministrationRecord.objects.filter(patient_id=patientid).filter(id=pk))

        if formset.is_valid():
            for item in formset:
                #               mart_data = MedicationAdministrationRecord()
                mart_data = item.save(commit=False)
                mart_data.patient = patients
#               mart_data.id = pk
#               mart_data.id = item.cleaned_data['id']
                mart_data.medication_date = item.cleaned_data['medication_date']
                mart_data.medication_time = item.cleaned_data['medication_time']
                mart_data.medication_medicine = item.cleaned_data['medication_medicine']
                mart_data.medication_dosage = item.cleaned_data['medication_dosage']
                mart_data.medication_unit = item.cleaned_data['medication_unit']
                mart_data.medication_tablet_capsule = item.cleaned_data['medication_tablet_capsule']
                mart_data.medication_frequency = item.cleaned_data['medication_frequency']
                mart_data.save()

            messages.success(request, _(page_title + ' form has been save successfully.'))
            return redirect('patient:medication_administration_list', username=patients.username)
        else:
            messages.warning(request, formset.errors)
    else:
        formset = MedicationAdministrationRecord_ModelFormSet(queryset=MedicationAdministrationRecord.objects.filter(patient_id=patientid).filter(id=pk))

    context = {
        'logos': logos,
        'titles': titles,
        'page_title': page_title,
        'patients': patients,
        'profiles': profiles,
        'icnumbers': icnumbers,
        'formset': formset,
        "themes": themes,
    }

    return render(request, 'patient/medication_administration/partial_edit.html', context)


class MedicationAdministrationRecordDeleteView(BSModalDeleteView):
    model = MedicationAdministrationRecord
    template_name = 'patient/medication_administration/partial_delete.html'
    page_title = _('Medication Administration Record Form')
    success_message = _(page_title + ' form was deleted.')

    def get_success_url(self):
        username = self.kwargs['username']
        return reverse_lazy('patient:medication_administration_list', kwargs={'username': username})


medication_administration_delete = MedicationAdministrationRecordDeleteView.as_view()
