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
	allergy_data = Allergy.objects.filter(patient=patientid)

	initial = {
		'patient': patients,
		'patient_name': patients,
		'username': username,
		'is_active': True,
		'is_patient': True,
		'password': password,
		'first_name': first_name,
		'admission_by': request.user,
		'birth_date': get_today,
	}

	initial_emergency = [{
		'patient': item.full_name,
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
		ec_formset = Family_FormSet(request.POST or None, prefix="ec_formset")
		admision_form = Admission_Form(request.POST or None, prefix="admision_form")
		admision_formset = AdmissionFormSet(request.POST or None, prefix="admision_formset")
		allergy_form = Allergy_Form(request.POST or None, prefix="allergy_form")
		medication_formset = Medication_FormSet(request.POST or None, prefix="medication_formset")

		if patient_form.is_valid() and ec_formset.is_valid() and admision_form.is_valid() and admision_formset.is_valid() and allergy_form.is_valid() and medication_formset.is_valid():

			profile = patient_form.save(commit=False)
			profile.full_name = patient_form.cleaned_data['full_name']
			profile.username = patient_form.cleaned_data['username']
			profile.email = patient_form.cleaned_data['email']
			profile.password = patient_form.cleaned_data['password']
			profile.date_joined = patient_form.cleaned_data['date_joined']
			profile.is_patient = patient_form.cleaned_data['is_patient']
			profile.is_active = patient_form.cleaned_data['is_active']
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

			profile.save()

			form_profile = Admission()
			form_profile.patient = patients
			form_profile.date_admission = admision_form.cleaned_data['date_admission']
			form_profile.time_admission = admision_form.cleaned_data['time_admission']
			form_profile.admitted = admision_form.cleaned_data['admitted']
			form_profile.mode = admision_form.cleaned_data['mode']

			form_profile.general_condition = admision_form.cleaned_data['general_condition']
			form_profile.vital_sign_temperature = admision_form.cleaned_data['vital_sign_temperature']
			form_profile.vital_sign_pulse = admision_form.cleaned_data['vital_sign_pulse']
			form_profile.vital_sign_bp = admision_form.cleaned_data['vital_sign_bp']
			form_profile.vital_sign_resp = admision_form.cleaned_data['vital_sign_resp']
			form_profile.vital_sign_spo2 = admision_form.cleaned_data['vital_sign_spo2']
			form_profile.vital_sign_on_oxygen_therapy = admision_form.cleaned_data['vital_sign_on_oxygen_therapy']
			form_profile.vital_sign_on_oxygen_therapy_flow_rate = admision_form.cleaned_data['vital_sign_on_oxygen_therapy_flow_rate']
			form_profile.vital_sign_hgt = admision_form.cleaned_data['vital_sign_hgt']

			form_profile.biohazard_infectious_disease = admision_form.cleaned_data['biohazard_infectious_disease']
			form_profile.invasive_line_insitu = admision_form.cleaned_data['invasive_line_insitu']
			form_profile.medical_history = admision_form.cleaned_data['medical_history']
			form_profile.surgical_history_none = admision_form.cleaned_data['surgical_history_none']
			form_profile.surgical_history = admision_form.cleaned_data['surgical_history']

			form_profile.adaptive_aids_with_patient = admision_form.cleaned_data['adaptive_aids_with_patient']
			form_profile.adaptive_aids_with_patient_others = admision_form.cleaned_data['adaptive_aids_with_patient_others']
			form_profile.orientation = admision_form.cleaned_data['orientation']
			form_profile.special_information = admision_form.cleaned_data['special_information']
			form_profile.admission_by = admision_form.cleaned_data['admission_by']

			form_profile.save()

			allergy_profile = Allergy()
			allergy_profile.patient = patients
			allergy_profile.allergy_drug = allergy_form.cleaned_data['allergy_drug']
			allergy_profile.allergy_food = allergy_form.cleaned_data['allergy_food']
			allergy_profile.allergy_others = allergy_form.cleaned_data['allergy_others']

			allergy_profile.save()

			for item in ec_formset:
				ec_profile = Family()
				ec_profile.patient = patients
				ec_profile.ec_name = item.cleaned_data['ec_name']
				ec_profile.ec_ic_number = item.cleaned_data['ec_ic_number']
				ec_profile.ec_ic_upload = item.cleaned_data['ec_ic_upload']
				ec_profile.ec_relationship = item.cleaned_data['ec_relationship']
				ec_profile.ec_phone = item.cleaned_data['ec_phone']
				ec_profile.ec_address = item.cleaned_data['ec_address']
				ec_profile.save()

			for item in admision_formset:
				admision_formset_profile = Admission()
				admision_formset_profile.patient = patients
				admision_formset_profile.date_diagnosis = item.cleaned_data['date_diagnosis']
				admision_formset_profile.diagnosis = item.cleaned_data['diagnosis']
				admision_formset_profile.date_operation = item.cleaned_data['date_operation']
				admision_formset_profile.operation = item.cleaned_data['operation']
				admision_formset_profile.save()

			for item in medication_formset:
				medication_formset_profile = Medication()
				medication_formset_profile.patient = patients
				medication_formset_profile.medication = item.cleaned_data['medication']
				medication_formset_profile.medication_drug_name = item.cleaned_data['medication_drug_name']
				medication_formset_profile.medication_dosage = item.cleaned_data['medication_dosage']
				medication_formset_profile.medication_tablet_capsule = item.cleaned_data['medication_tablet_capsule']
				medication_formset_profile.medication_frequency = item.cleaned_data['medication_frequency']
				medication_formset_profile.save()

			messages.success(request, _(page_title + ' form was created.'))
			return redirect('patient:patientdata_detail', username=patientusername)

		else:
			messages.warning(request, patient_form.errors)
			messages.warning(request, ec_formset.errors)
			messages.warning(request, admision_form.errors)
			messages.warning(request, admision_formset.errors)
			messages.warning(request, allergy_form.errors)
			messages.warning(request, medication_formset.errors)

	else:
		patient_form = UserProfile_ModelForm(initial=initial, instance=patients, prefix="patient_form")
		ec_formset = Family_FormSet(initial=initial_formset, prefix="ec_formset")
		admision_form = Admission_Form(initial=initial, prefix="admision_form")
		admision_formset = AdmissionFormSet(initial=initial_formset, prefix="admision_formset")
		allergy_form = Allergy_Form(initial=initial, prefix="allergy_form")
		medication_formset = Medication_FormSet(initial=initial_formset, prefix="medication_formset")

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
		'icnumbers': icnumbers,
		'patient_form': patient_form,
		'ec_formset': ec_formset,
		'admision_form': admision_form,
		'admision_formset': admision_formset,
		'allergy_form': allergy_form,
		'medication_formset': medication_formset,
	}

	return render(request, 'patient/admission/admission_form.html', context)


class AdmissionUpdateView(BSModalUpdateView):
	model = Admission
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
