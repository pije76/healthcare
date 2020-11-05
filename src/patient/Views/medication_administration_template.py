from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import ugettext as _
from django.urls import reverse, reverse_lazy

from patient.models import *
from patient.Forms.medication_administration_template import *
from accounts.models import *
from customers.models import *

from bootstrap_modal_forms.generic import *


@login_required
def medication_administration_template_list(request, username):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Medication Administration Record (Template)')
	patientid = UserProfile.objects.get(username=username).id
	patients = MedicationAdministrationRecordTemplate.objects.filter(patient=patientid)
	profiles = UserProfile.objects.filter(pk=patientid)

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
	}

	return render(request, 'patient/medication_administration_template/medication_administration_template_data.html', context)


@login_required
def medication_administration_template_create(request, username):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Medication Administration Record (Template)')
	patients = get_object_or_404(UserProfile, username=username)
	patientid = get_object_or_404(UserProfile, username=username).id
	icnumbers = UserProfile.objects.filter(username=username).values_list('ic_number', flat=True).first()
	profiles = UserProfile.objects.filter(username=username)
	mart_profiles = MedicationAdministrationRecordTemplate.objects.filter(patient=patientid)
	templates = MedicationAdministrationRecordTemplate.objects.filter(patient=patientid).values_list('medication_time')
	patients_templates = MedicationAdministrationRecordTemplate.objects.filter(patient=patientid).filter(medication_time__in=['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00']).order_by("medication_time")

	initial_mart_formset = [{
		'id': item.id,
		'patient': item.patient,
	}
	for item in mart_profiles]

	if request.method == 'POST':
		formset = MedicationAdministrationRecordTemplate_FormSet(request.POST or None)
		if formset.is_valid():
			for item in formset:
#				mart_save = MedicationAdministrationRecordTemplate()
				mart_save = item.save(commit=False)
				mart_save.patient = patients
#				mart_save.patient = item.cleaned_data['patient']
#				mart_save.own_medication = True
				mart_save.own_medication = 'Yes'
				mart_save.medication_date = item.cleaned_data['medication_date']
				mart_save.medication_time = item.cleaned_data['medication_time']
				mart_save.medication_drug_name = item.cleaned_data['medication_drug_name']
				mart_save.medication_dosage = item.cleaned_data['medication_dosage']
				mart_save.medication_unit = item.cleaned_data['medication_unit']
				mart_save.medication_tablet_capsule = item.cleaned_data['medication_tablet_capsule']
				mart_save.medication_frequency = item.cleaned_data['medication_frequency']
				mart_save.save()

			messages.success(request, _(page_title + ' form was created.'))
			return redirect('patient:patientdata_detail', username=patients.username)
		else:
			messages.warning(request, formset.errors)
	else:
#		formset = MedicationAdministrationRecordTemplate_FormSet(initial=[{'id': x, 'patient': y} for x,y in mart_profiles], queryset=patients_templates)
		formset = MedicationAdministrationRecordTemplate_FormSet(initial=initial_mart_formset, queryset=patients_templates)

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
		'icnumbers': icnumbers,
		'formset': formset,
	}

	return render(request, 'patient/medication_administration_template/medication_administration_template_form.html', context)


class MedicationAdministrationRecordTemplateUpdateView(BSModalUpdateView):
	model = MedicationAdministrationRecordTemplate
	template_name = 'patient/medication_administration_template/partial_edit.html'
	form_class = MedicationAdministrationRecordTemplate_ModelForm
	page_title = _('MedicationAdministrationRecordTemplate Form')
	success_message = _(page_title + ' form has been save successfully.')

	def get_form(self, form_class=None):
		form = super().get_form(form_class=None)
		form.fields['medication_date'].label = _("Date")
		form.fields['medication_time'].label = _("Time")
		form.fields['medication_drug_name'].label = _("Drug Name")
		form.fields['medication_dosage'].label = _("Dosage")
		form.fields['medication_unit'].label = _("Unit")
		form.fields['medication_tablet_capsule'].label = _("Tablet/Capsule")
		form.fields['medication_frequency'].label = _("Frequency")
		return form

	def get_success_url(self):
		username = self.kwargs['username']
		return reverse_lazy('patient:medication_administration_template_list', kwargs={'username': username})


medication_administration_template_edit = MedicationAdministrationRecordTemplateUpdateView.as_view()


class MedicationAdministrationRecordTemplateDeleteView(BSModalDeleteView):
	model = MedicationAdministrationRecordTemplate
	template_name = 'patient/medication_administration_template/partial_delete.html'
	page_title = _('MedicationAdministrationRecordTemplate Form')
	success_message = _(page_title + ' form was deleted.')

	def get_success_url(self):
		username = self.kwargs['username']
		return reverse_lazy('patient:medication_administration_template_list', kwargs={'username': username})


medication_administration_template_delete = MedicationAdministrationRecordTemplateDeleteView.as_view()
