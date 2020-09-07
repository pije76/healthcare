from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.utils.translation import ugettext as _
from django.urls import reverse, reverse_lazy
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404

from patient.models import *
from patient.Forms.admission import *
from accounts.models import *
from customers.models import *

from bootstrap_modal_forms.generic import *

import datetime

startdate = datetime.date.today()
enddate = startdate + datetime.timedelta(days=1)

start_time_day = datetime.datetime.strptime('00:00', '%H:%M').time()
end_time_day = datetime.datetime.strptime('12:00', '%H:%M').time()
start_time_night = datetime.datetime.strptime('12:01', '%H:%M').time()
end_time_night = datetime.datetime.strptime('23:59', '%H:%M').time()


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
	admissionform = Admission.objects.filter(patient=patientid)
	profiles = UserProfile.objects.filter(pk=patientid)

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'patientform': patientform,
		'ecform': ecform,
		'admissionform': admissionform,
		'profiles': profiles,
	}
	print("admissionform: ", admissionform)

	return render(request, 'patient/admission/admission_data.html', context)


@login_required
def admission_create(request, username):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Admission Form')
	patients = get_object_or_404(UserProfile, username=username)
#	emergencies = get_object_or_404(Family, ec_name=username)
#	emergenciesprofiles = Family.objects.filter(username=username)
	patientusername = get_object_or_404(UserProfile, username=username).username
#	patientname = get_object_or_404(PatientProfile, username=username)
	username = get_object_or_404(UserProfile, username=username).username
	password = get_object_or_404(UserProfile, username=username).password
	first_name = get_object_or_404(UserProfile, username=username).first_name
	date_joined = get_object_or_404(UserProfile, username=username).date_joined
	profiles = UserProfile.objects.filter(username=username)
	icnumbers = UserProfile.objects.filter(username=username).values_list('ic_number', flat=True).first()

	initial = {
		'patient_name': patients,
#		'patient': patients,
		'username': username,
		'is_active': True,
		'is_patient': True,
		'password': password,
		'first_name': first_name,
#		'date_joined': date_joined,
#		'birth_date': get_today,
#		'medication_date': get_today,
#		'medication_time': get_time,
#		'medicationstat_date_time': get_datetime,
#		'admission_by': request.user,
	}

	initial_emergency = [{
		'patient': item.full_name,
#		'birth_date': get_today,
#		'medication_date': get_today,
#		'medication_time': get_time,
#		'medicationstat_date_time': get_datetime,
#		'admission_by': request.user,
	}
	for item in profiles]


	initial_formset = [{
		'patient': item.full_name,
		'birth_date': get_today,
		'medication_date': get_today,
		'medication_time': get_time,
		'medicationstat_date_time': get_datetime,
		'admission_by': request.user,
	}
	for item in profiles]

	if request.method == 'POST':
		patient_form = UserProfile_ModelForm(request.POST or None, instance=patients, prefix="patient_form")
		ec_form = Family_FormSet(request.POST or None, prefix="ec_form")
		formset = Admission_FormSet(request.POST or None, prefix="formset")

		if patient_form.is_valid() and ec_form.is_valid() and formset.is_valid():
			profile = patient_form.save(commit=False)
			profile.full_name = patient_form.cleaned_data['full_name']
			profile.username = patient_form.cleaned_data['username']
			profile.email = patient_form.cleaned_data['email']
			profile.password = patient_form.cleaned_data['password']
			profile.date_joined = patient_form.cleaned_data['date_joined']
			profile.ic_number = patient_form.cleaned_data['ic_number']
			profile.ic_upload = patient_form.cleaned_data['ic_upload']
			profile.birth_date = patient_form.cleaned_data['birth_date']
			delta_day = int((datetime.datetime.now().date() - profile.birth_date).days / 365.24219)
			profile.age = delta_day
			profile.gender = patient_form.cleaned_data['gender']
			profile.marital_status = patient_form.cleaned_data['marital_status']
			profile.religion = patient_form.cleaned_data['religion']
			profile.occupation = patient_form.cleaned_data['occupation']
			profile.communication_sight = patient_form.cleaned_data['communication_sight']
			profile.communication_hearing = patient_form.cleaned_data['communication_hearing']
			profile.address = patient_form.cleaned_data['address']
			profile.is_patient = patient_form.cleaned_data['is_patient']
			profile.is_active = patient_form.cleaned_data['is_active']

			profile.save()

			for item in ec_form:
				ec_profile = Family()
				ec_profile.patient = patients
				ec_profile.ec_name = item.cleaned_data['ec_name']
				ec_profile.ec_ic_number = item.cleaned_data['ec_ic_number']
				ec_profile.ec_ic_upload = item.cleaned_data['ec_ic_upload']
				ec_profile.ec_relationship = item.cleaned_data['ec_relationship']
				ec_profile.ec_phone = item.cleaned_data['ec_phone']
				ec_profile.ec_address = item.cleaned_data['ec_address']
				ec_profile.save()

			for item in formset:
				formset_profile = Admission()
				formset_profile.patient = patients
				formset_profile.date = item.cleaned_data['date']
				formset_profile.time = item.cleaned_data['time']
				formset_profile.admitted = item.cleaned_data['admitted']
				formset_profile.admitted_others = item.cleaned_data['admitted_others']
				formset_profile.mode = item.cleaned_data['mode']

				formset_profile.general_condition = item.cleaned_data['general_condition']
				formset_profile.vital_sign_temperature = item.cleaned_data['vital_sign_temperature']
				formset_profile.vital_sign_pulse = item.cleaned_data['vital_sign_pulse']
				formset_profile.vital_sign_bp = item.cleaned_data['vital_sign_bp']
				formset_profile.vital_sign_resp = item.cleaned_data['vital_sign_resp']
				formset_profile.vital_sign_spo2 = item.cleaned_data['vital_sign_spo2']
				formset_profile.vital_sign_on_oxygen_therapy = item.cleaned_data['vital_sign_on_oxygen_therapy']
				formset_profile.vital_sign_on_oxygen_therapy_flow_rate = item.cleaned_data['vital_sign_on_oxygen_therapy_flow_rate']
				formset_profile.vital_sign_hgt = item.cleaned_data['vital_sign_hgt']
				formset_profile.allergy_drug = item.cleaned_data['allergy_drug']
				formset_profile.allergy_food = item.cleaned_data['allergy_food']
				formset_profile.allergy_others = item.cleaned_data['allergy_others']
				formset_profile.biohazard_infectious_disease = item.cleaned_data['biohazard_infectious_disease']
				formset_profile.biohazard_infectious_disease_others = item.cleaned_data['biohazard_infectious_disease_others']
				formset_profile.invasive_line_insitu = item.cleaned_data['invasive_line_insitu']
				formset_profile.invasive_line_insitu_others = item.cleaned_data['invasive_line_insitu_others']
				formset_profile.medical_history = item.cleaned_data['medical_history']
				formset_profile.medical_history_others = item.cleaned_data['medical_history_others']
				formset_profile.surgical_history_none = item.cleaned_data['surgical_history_none']
				formset_profile.surgical_history = item.cleaned_data['surgical_history']

				formset_profile.date_diagnosis = item.cleaned_data['date_diagnosis']
				formset_profile.diagnosis = item.cleaned_data['diagnosis']
				formset_profile.date_operation = item.cleaned_data['date_operation']
				formset_profile.operation = item.cleaned_data['operation']
				formset_profile.medication = item.cleaned_data['medication']
				formset_profile.medication_drug_name = item.cleaned_data['medication_drug_name']
				formset_profile.medication_dosage = item.cleaned_data['medication_dosage']
				formset_profile.medication_tablet_capsule = item.cleaned_data['medication_tablet_capsule']
				formset_profile.medication_frequency = item.cleaned_data['medication_frequency']

				formset_profile.adaptive_aids_with_patient = item.cleaned_data['adaptive_aids_with_patient']
				formset_profile.adaptive_aids_with_patient_others = item.cleaned_data['adaptive_aids_with_patient_others']
				formset_profile.orientation = item.cleaned_data['orientation']
				formset_profile.special_information = item.cleaned_data['special_information']
				formset_profile.admission_by = item.cleaned_data['admission_by']

				formset_profile.save()

			messages.success(request, _(page_title + ' form was created.'))
			return redirect('patient:patientdata_detail', username=patientusername)

		else:
			messages.warning(request, patient_form.errors)
			messages.warning(request, ec_form.errors)
			messages.warning(request, formset.errors)

	else:
		patient_form = UserProfile_ModelForm(initial=initial, instance=patients, prefix="patient_form")
		ec_form = Family_FormSet(initial=initial_emergency, prefix="ec_form")
		formset = Admission_FormSet(initial=initial_formset, prefix="formset")

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
		'icnumbers': icnumbers,
		'patient_form': patient_form,
		'ec_form': ec_form,
		'formset': formset,
	}

	return render(request, 'patient/admission/admission_form.html', context)


class AdmissionUpdateView(BSModalUpdateView):
	model = Admission
#	initial = {
#		'patient': 'foo',
#		'value2': 'bar'
#	}
	template_name = 'patient/admission/partial_edit.html'
	form_class = Admission_ModelForm
	page_title = _('Admission Form')
	success_message = _(page_title + ' form has been save successfully.')
#	success_url = reverse_lazy('patient:admission_list')

	def get_success_url(self):
		username = self.kwargs['username']
		return reverse_lazy('patient:admission_list', kwargs={'username': username})

	def get_initial(self):
		return {'patient': 'foo', 'value2': 'bar'}

#	def get_context(self, **kwargs):
#		data = super(AdmissionUpdateView, self).get_context(**kwargs)
#		if self.request.POST:
#			data['patient'] = Admission_Form(self.request.POST, instance=self.object, form_kwargs={'request': self.request})
#		else:
#			data['patient'] = Admission_Form(instance=self.object, form_kwargs={'request': self.request})
#		return data

	def form_valid(self, form):
		form.instance.date_created = timezone.now()
		context = self.get_context()
		objects = context['patient']
		with transaction.atomic():
			self.object = form.save()

			if objects.is_valid():
				objects.instance = self.object
				objects.save()

		return super(AdmissionUpdateView, self).form_valid(form)

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
