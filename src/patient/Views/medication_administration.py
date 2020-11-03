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
#	patients = UserProfile.objects.filter(username=username)
	patients = MedicationAdministrationRecord.objects.filter(patient=patientid)
	icnumbers = UserProfile.objects.filter(username=username).values_list('ic_number', flat=True).first()
#	profiles = UserProfile.objects.filter(pk=patientid)
	full_name_profiles = UserProfile.objects.filter(username=username).values_list('full_name', flat=True).first()
	profiles = UserProfile.objects.filter(pk=patientid)
#	allergies = MedicationAdministrationRecord.objects.filter(patient=patientid).values_list('allergy', flat=True).first()
	medicine_date = MedicationAdministrationRecord.objects.filter(patient=patientid).values_list('medication_date', flat=True).first()
#	medicine_data = MedicationAdministrationRecord.objects.filter(patient=patientid)
	medicine_data = MedicationAdministrationRecord.objects.filter(patient=patientid).exclude(medication_time__isnull=True)
	medicine_stat = MedicationAdministrationRecord.objects.filter(patient=patientid).exclude(medication_time__isnull=True)
	allergy_drug_data = Allergy.objects.filter(patient=patientid).values_list('allergy_drug', flat=True).first()
	allergy_food_data = Allergy.objects.filter(patient=patientid).values_list('allergy_food', flat=True).first()
	allergy_others_data = Allergy.objects.filter(patient=patientid).values_list('allergy_others', flat=True).first()

#	if request.method == 'GET':
	form = MedicationAdministrationRecord_Form()

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
#		'allergies': allergies,
		'icnumbers': icnumbers,
		'full_name_profiles': full_name_profiles,
		'medicine_date': medicine_date,
		'allergy_drug_data': allergy_drug_data,
		'allergy_food_data': allergy_food_data,
		'allergy_others_data': allergy_others_data,
		'medicine_data': medicine_data,
		'medicine_stat': medicine_stat,
		'form': form,
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
	allergy_drug = Allergy.objects.filter(patient=patientid).values_list('allergy_drug', flat=True).first()
	allergy_food = Allergy.objects.filter(patient=patientid).values_list('allergy_food', flat=True).first()
	allergy_others = Allergy.objects.filter(patient=patientid).values_list('allergy_others', flat=True).first()

	patients_templates = MedicationAdministrationRecord.objects.filter(patient=patientid).filter(medication_time__in=['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00']).order_by("medication_time")

	initial_form = {
		'patient': patients,
		'ic_number': icnumbers,
	}

	initial_allergy = {
		'patient': patients,
		'allergy_drug': allergy_drug,
		'allergy_food': allergy_food,
		'allergy_others': allergy_others,
	}

	if request.method == 'POST':

		form = MedicationAdministrationRecord_Model_Form(request.POST or None)
		formset = MedicationAdministrationRecord_ModelForm_Set(request.POST or None)
		allergy_form = Allergy_Model_Form(request.POST or None)

		if form.is_valid():
#			profile_form = MedicationAdministrationRecord()
			profile_form = form.save(commit=False)
			profile_form.patient = patients
			profile_form.medication_date = form.cleaned_data['medication_date']
			profile_form.save()

		if allergy_form.is_valid():
#			allergy_data = Allergy()
			allergy_data = allergy_form.save(commit=False)
#			allergy_data.patient = patients
			allergy_data.patient = allergy_form.cleaned_data['patient']
#			allergy_data.allergy = allergy_form.cleaned_data['allergy']
			allergy_data.allergy_drug = allergy_form.cleaned_data['allergy_drug']
			allergy_data.allergy_food = allergy_form.cleaned_data['allergy_food']
			allergy_data.allergy_others = allergy_form.cleaned_data['allergy_others']
			allergy_data.save()

		if formset.is_valid():
			for item in formset:
#				mar_save = MedicationAdministrationRecord()
				mar_save = item.save(commit=False)
				mar_save.patient = patients
#				mar_save.patient = item.cleaned_data['patient']
#				mar_save.allergy = item.cleaned_data['allergy']
				mar_save.allergy_drug = item.cleaned_data['allergy_drug']
				mar_save.allergy_food = item.cleaned_data['allergy_food']
				mar_save.allergy_others = item.cleaned_data['allergy_others']
#				mar_save.medication = item.cleaned_data['medication']
				mar_save.medication_date = item.cleaned_data['medication_date']
				mar_save.medication_time = item.cleaned_data['medication_time']
				mar_save.medication_drug_name = item.cleaned_data['medication_drug_name']
				mar_save.medication_dosage = item.cleaned_data['medication_dosage']
				mar_save.medication_unit = item.cleaned_data['medication_unit']
				mar_save.medication_tablet_capsule = item.cleaned_data['medication_tablet_capsule']
				mar_save.medication_frequency = item.cleaned_data['medication_frequency']

				mar_save.medication_route = item.cleaned_data['medication_route']
				mar_save.medication_source = item.cleaned_data['medication_source']
				mar_save.medication_status = item.cleaned_data['medication_status']
				mar_save.medication_done = item.cleaned_data['medication_done']
				mar_save.save()

			messages.success(request, _(page_title + ' form was created.'))
			return redirect('patient:patientdata_detail', username=patients.username)
		else:
			messages.warning(request, form.errors)
			messages.warning(request, formset.errors)
			messages.warning(request, allergy_form.errors)
	else:
		form = MedicationAdministrationRecord_Model_Form(initial=initial_form)
#		form = MedicationAdministrationRecord_ModelForm_Set(initial=[{'medication_date': get_today} for medication_date in queryset])
		formset = MedicationAdministrationRecord_ModelForm_Set(initial=[{'patient': x} for x in profiles], queryset=patients_templates)
		allergy_form = Allergy_Model_Form(initial=initial_allergy)

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
		'icnumbers': icnumbers,
		'form': form,
		'formset': formset,
		'allergy_form': allergy_form,
	}

	return render(request, 'patient/medication_administration/medication_administration_form.html', context)


class MedicationAdministrationRecordUpdateView(BSModalUpdateView):
	model = MedicationAdministrationRecord
	template_name = 'patient/medication_administration/partial_edit.html'
	form_class = MedicationAdministrationRecord_ModelForm
	page_title = _('Medication Administration Record Form')
	success_message = _(page_title + ' form has been save successfully.')

	def get_form(self, form_class=None):
		form = super().get_form(form_class=None)
		form.fields['allergy_drug'].label = _("Allergy Drug")
		form.fields['allergy_food'].label = _("Allergy Dood")
		form.fields['allergy_others'].label = _("Allergy Others")
		form.fields['medication_date'].label = _("Date")
		form.fields['medication_time'].label = _("Time")
		form.fields['medication_drug_name'].label = _("Drug Name")
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


medication_administration_edit = MedicationAdministrationRecordUpdateView.as_view()


class MedicationAdministrationRecordDeleteView(BSModalDeleteView):
	model = MedicationAdministrationRecord
	template_name = 'patient/medication_administration/partial_delete.html'
	page_title = _('Medication Administration Record Form')
	success_message = _(page_title + ' form was deleted.')

	def get_success_url(self):
		username = self.kwargs['username']
		return reverse_lazy('patient:medication_administration_list', kwargs={'username': username})


medication_administration_delete = MedicationAdministrationRecordDeleteView.as_view()
