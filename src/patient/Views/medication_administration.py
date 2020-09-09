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

from bootstrap_modal_forms.generic import *

startdate = datetime.date.today()
enddate = startdate + datetime.timedelta(days=1)

start_time_day = datetime.datetime.strptime('00:00', '%H:%M').time()
end_time_day = datetime.datetime.strptime('12:00', '%H:%M').time()
start_time_night = datetime.datetime.strptime('12:01', '%H:%M').time()
end_time_night = datetime.datetime.strptime('23:59', '%H:%M').time()




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
	fulll_name_profiles = UserProfile.objects.filter(username=username).values_list('full_name', flat=True).first()
	profiles = UserProfile.objects.filter(pk=patientid)
	allergies = MedicationAdministrationRecord.objects.filter(patient=patientid).values_list('allergy', flat=True).first()
	medicine_date = MedicationAdministrationRecord.objects.filter(patient=patientid).values_list('medication_date', flat=True).first()
	medicine_data = MedicationAdministrationRecord.objects.filter(patient=patientid)
	medicine_stat = MedicationAdministrationRecord.objects.filter(patient=patientid)
	allergy_drug_data = Allergy.objects.filter(patient=patientid).values_list('allergy_drug', flat=True).first()
	allergy_food_data = Allergy.objects.filter(patient=patientid).values_list('allergy_food', flat=True).first()
	allergy_others_data = Allergy.objects.filter(patient=patientid).values_list('allergy_others', flat=True).first()

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
		'allergies': allergies,
		'icnumbers': icnumbers,
		'fulll_name_profiles': fulll_name_profiles,
		'medicine_date': medicine_date,
		'allergy_drug_data': allergy_drug_data,
		'allergy_food_data': allergy_food_data,
		'allergy_others_data': allergy_others_data,
		'medicine_data': medicine_data,
		'medicine_stat': medicine_stat,
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
	patientusername = UserProfile.objects.get(username=username)
	profiles = UserProfile.objects.filter(username=username)
	patients = get_object_or_404(UserProfile, username=username)
#	patients_allergies = get_object_or_404(UserProfile, username=username)
	patients_allergies = UserProfile.objects.filter(username=username).values_list('full_name', flat=True).first()

	allergies = Allergy.objects.filter(patient=patientid)
#	allergies = Allergy.objects.get(patient=patientid)
#	allergies = Allergy.objects.filter(patient=patientid).values_list('allergy', flat=True).first()
#	allergies = Allergy.objects.select_related('patient').filter(patient=patientid)
#	allergies = Allergy.objects.filter(patient=patientid).values()

	stat = MedicationAdministrationRecord.objects.filter(patient=patientid).values_list('stat', flat=True).first()
	medicationstat_date_time = MedicationAdministrationRecord.objects.filter(patient=patientid).values_list('medicationstat_date_time', flat=True).first()
	given_by = MedicationAdministrationRecord.objects.filter(patient=patientid).values_list('given_by', flat=True).first()

	allergy_drug = Allergy.objects.filter(patient=patientid).values_list('allergy_drug', flat=True).first()
	allergy_food = Allergy.objects.filter(patient=patientid).values_list('allergy_food', flat=True).first()
	allergy_others = Allergy.objects.filter(patient=patientid).values_list('allergy_others', flat=True).first()

	initial_form = {
		'patient': patients,
		'ic_number': icnumbers,
#		'allergy': allergies,
		'stat': stat,
		'medicationstat_date_time': medicationstat_date_time,
		'given_by': request.user,
	}

	initial_allergy = {
		'patient': patients,
#		'allergy': allergies,
		'allergy_drug': allergy_drug,
		'allergy_food': allergy_food,
		'allergy_others': allergy_others,
	}

	initial_formset_factory = [
	{
		'patient': patients,
		'medication_date': get_today,
		'medication_time': get_time,
		'medicationstat_date_time': get_datetime,
		'given_by': request.user,
	}]

	initial_modelform_factory = {
		'patient': patients,
		'medication_date': get_today,
		'medication_time': get_time,
		'medicationstat_date_time': get_datetime,
		'given_by': request.user,
	}
	initial_modelformset_factory = [
	{
		'patient': patients,
		'medication_date': get_today,
		'medication_time': get_time,
		'medicationstat_date_time': get_datetime,
	}]

	initial_inlineformset_factory = [
	{
				#       'patient': patients,
		'medication_date': get_today,
		'medication_time': get_time,
		'medicationstat_date_time': get_datetime,
	}]

	initial_list = [
		{'medication_time': '00:00'},
		{'medication_time': '01:00'},
		{'medication_time': '02:00'},
		{'medication_time': '03:00'},
		{'medication_time': '04:00'},
		{'medication_time': '05:00'},
		{'medication_time': '06:00'},
		{'medication_time': '07:00'},
		{'medication_time': '08:00'},
		{'medication_time': '09:00'},
		{'medication_time': '10:00'},
		{'medication_time': '11:00'},
		{'medication_time': '12:00'},
		{'medication_time': '13:00'},
		{'medication_time': '14:00'},
		{'medication_time': '15:00'},
		{'medication_time': '16:00'},
		{'medication_time': '17:00'},
		{'medication_time': '18:00'},
		{'medication_time': '19:00'},
		{'medication_time': '20:00'},
		{'medication_time': '21:00'},
		{'medication_time': '22:00'},
		{'medication_time': '23:00'},
	]

	GROUP_SIZE = 4

	if request.method == 'POST':

		form = MedicationAdministrationRecord_Form(request.POST or None)
		formset = MedicationAdministrationRecord_FormSet(request.POST or None)
		allergy_form = Allergy_ModelForm(request.POST or None)

		if form.is_valid() and formset.is_valid() and allergy_form.is_valid():

			profile_form = MedicationAdministrationRecord()
			profile_form.patient = patients
			profile_form.medication_date = form.cleaned_data['medication_date']
			profile_form.save()

			if allergy_form.has_changed():
				allergy_profile = allergy_form.save(commit=False)
#				allergy_profile = Allergy()
#				allergy_profile.patient = patients
				allergy_profile.patient = allergy_form.cleaned_data['patient']
#				allergy_profile.allergy = allergy_form.cleaned_data['allergy']
				allergy_profile.allergy_drug = allergy_form.cleaned_data['allergy_drug']
				allergy_profile.allergy_food = allergy_form.cleaned_data['allergy_food']
				allergy_profile.allergy_others = allergy_form.cleaned_data['allergy_others']
				allergy_profile.save()

			for item in formset:
				profile = MedicationAdministrationRecord()
				profile.patient = patients
#				profile.allergy = item.cleaned_data['allergy']
				profile.medication = item.cleaned_data['medication']
#				profile.medication_name = item.cleaned_data['medication_name']
#				profile.medication_dosage = item.cleaned_data['medication_dosage']
#				profile.medication_tab_cap_mls = item.cleaned_data['medication_tab_cap_mls']
#				profile.medication_frequency = item.cleaned_data['medication_frequency']
#				profile.medication_route = item.cleaned_data['medication_route']
				profile.medication_date = item.cleaned_data['medication_date']
				profile.medication_time = item.cleaned_data['medication_time']
				profile.status_nurse = item.cleaned_data['status_nurse']
				profile.done = item.cleaned_data['done']
				profile.stat = item.cleaned_data['stat']
				profile.medicationstat_date_time = item.cleaned_data['medicationstat_date_time']
				profile.given_by = item.cleaned_data['given_by']
				profile.save()

			messages.success(request, _(page_title + ' form was created.'))
			return redirect('patient:patientdata_detail', username=patients.username)
		else:
			messages.warning(request, form.errors)
			messages.warning(request, formset.errors)
			messages.warning(request, allergy_form.errors)
	else:
		form = MedicationAdministrationRecord_Form(initial=initial_form)
#       form = MedicationAdministrationRecord_FormSet(initial=[{'medication_date': get_today} for medication_date in queryset])
		formset = MedicationAdministrationRecord_FormSet(initial=initial_list)
		allergy_form = Allergy_ModelForm(initial=initial_allergy)

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
#       'formset1': formset1,
#       'formset2': formset2,
#       'helper': helper,
	}

	print("patients_allergies: ", profiles)

	return render(request, 'patient/medication_administration/medication_administration_form.html', context)
#	return render(request, 'patient/medication_administration/medication_administration_formset_factory.html', context)
#   return render(request, 'patient/medication_administration/medication_administration_modelform_factory.html', context)
#   return render(request, 'patient/medication_administration/medication_administration_modelformset_factory.html', context)
#   return render(request, 'patient/medication_administration/medication_administration_inlineformset_factory.html', context)


class MedicationAdministrationRecordUpdateView(BSModalUpdateView):
	model = MedicationAdministrationRecord
	template_name = 'patient/medication_administration/partial_edit.html'
	form_class = MedicationAdministrationRecord_ModelForm
	page_title = _('Medication Administration Record Form')
	success_message = _(page_title + ' form has been save successfully.')

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

