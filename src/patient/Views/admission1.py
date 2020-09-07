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
	profiles = UserProfile.objects.filter(pk=patientid)

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
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
	patientusername = UserProfile.objects.get(username=username)
	profiles = UserProfile.objects.filter(username=username)
	icnumbers = UserProfile.objects.filter(username=username).values_list('ic_number', flat=True).first()

	initial = {
		'patient': patients,
		'medication_date': get_today,
		'medication_time': get_time,
		'medicationstat_date_time': get_datetime,
		'admission_by': request.user,
	}

	initial_formset = [{
		'patient': item.full_name,
	}
	for item in profiles]


	if request.method == 'POST':
		patient_form = Patient_ModelForm(request.POST or None, prefix="patient_form")
		ec_form = Family_Form(request.POST or None, prefix="ec_form")
		formset = Admission_FormSet(request.POST or None, prefix="formset")

		if patient_form.is_valid():
			profile = UserProfile()
			profile.patient = patients
			profile.ic_number = patient_form.cleaned_data['ic_number']
			profile.ic_upload = patient_form.cleaned_data['ic_upload']
			profile.birth_date = patient_form.cleaned_data['birth_date']
			delta_day = int((datetime.datetime.now().date() - profile.birth_date).days / 365.24219)
			profile.age = delta_day
			profile.gender = patient_form.cleaned_data['gender']
			profile.marital_status = patient_form.cleaned_data['marital_status']
			profile.marital_status_others = patient_form.cleaned_data['marital_status_others']
			profile.religion = patient_form.cleaned_data['religion']
			profile.religion_others = patient_form.cleaned_data['religion_others']
			profile.occupation = patient_form.cleaned_data['occupation']
			profile.occupation_others = patient_form.cleaned_data['occupation_others']
			profile.communication_sight = patient_form.cleaned_data['communication_sight']
			profile.communication_hearing = patient_form.cleaned_data['communication_hearing']
			profile.communication_hearing_others = patient_form.cleaned_data['communication_hearing_others']
			profile.address = patient_form.cleaned_data['address']
			profile.save()

			messages.success(request, _(page_title + ' form was created.'))
			return redirect('patient:patientdata_detail', username=patients.username)
		else:
			messages.warning(request, patient_form.errors)

		if ec_form.is_valid():
			profile = Family()
			profile.patient = patients
			profile.ec_name = ec_form.cleaned_data['ec_name']
			profile.ec_ic_number = ec_form.cleaned_data['ec_ic_number']
			profile.ec_ic_upload = ec_form.cleaned_data['ec_ic_upload']
			profile.ec_relationship = ec_form.cleaned_data['ec_relationship']
			profile.ec_phone = ec_form.cleaned_data['ec_phone']
			profile.ec_address = ec_form.cleaned_data['ec_address']
			profile.save()

			messages.success(request, _(page_title + ' form was created.'))
			return redirect('patient:patientdata_detail', username=patients.username)
		else:
			messages.warning(request, ec_form.errors)

		if formset.is_valid():
			for item in formset:
				profile = Admission()
				profile.patient = patients
				profile.date = item.cleaned_data['date']
				profile.time = item.cleaned_data['time']
				profile.admitted = item.cleaned_data['admitted']
				profile.admitted_others = item.cleaned_data['admitted_others']
				profile.mode = item.cleaned_data['mode']

				profile.general_condition = item.cleaned_data['general_condition']
				profile.vital_sign_temperature = item.cleaned_data['vital_sign_temperature']
				profile.vital_sign_pulse = item.cleaned_data['vital_sign_pulse']
				profile.vital_sign_bp = item.cleaned_data['vital_sign_bp']
				profile.vital_sign_resp = item.cleaned_data['vital_sign_resp']
				profile.vital_sign_spo2 = item.cleaned_data['vital_sign_spo2']
				profile.vital_sign_on_oxygen_therapy = item.cleaned_data['vital_sign_on_oxygen_therapy']
				profile.vital_sign_on_oxygen_therapy_flow_rate = item.cleaned_data['vital_sign_on_oxygen_therapy_flow_rate']
				profile.vital_sign_hgt = item.cleaned_data['vital_sign_hgt']
				profile.allergy_drug = item.cleaned_data['allergy_drug']
				profile.allergy_food = item.cleaned_data['allergy_food']
				profile.allergy_others = item.cleaned_data['allergy_others']
				profile.biohazard_infectious_disease = item.cleaned_data['biohazard_infectious_disease']
				profile.biohazard_infectious_disease_others = item.cleaned_data['biohazard_infectious_disease_others']
				profile.invasive_line_insitu = item.cleaned_data['invasive_line_insitu']
				profile.invasive_line_insitu_others = item.cleaned_data['invasive_line_insitu_others']
				profile.medical_history = item.cleaned_data['medical_history']
				profile.medical_history_others = item.cleaned_data['medical_history_others']
				profile.surgical_history_none = item.cleaned_data['surgical_history_none']
				profile.surgical_history = item.cleaned_data['surgical_history']

				profile.date_diagnosis = item.cleaned_data['date_diagnosis']
				profile.diagnosis = item.cleaned_data['diagnosis']
				profile.date_operation = item.cleaned_data['date_operation']
				profile.operation = item.cleaned_data['operation']
				profile.medication = item.cleaned_data['medication']
				profile.medication_drug_name = item.cleaned_data['medication_drug_name']
				profile.medication_dosage = item.cleaned_data['medication_dosage']
				profile.medication_tablet_capsule = item.cleaned_data['medication_tablet_capsule']
				profile.medication_frequency = item.cleaned_data['medication_frequency']

				profile.adaptive_aids_with_patient = item.cleaned_data['adaptive_aids_with_patient']
				profile.adaptive_aids_with_patient_others = item.cleaned_data['adaptive_aids_with_patient_others']
				profile.orientation = item.cleaned_data['orientation']
				profile.special_information = item.cleaned_data['special_information']
				profile.admission_by = item.cleaned_data['admission_by']

				profile.save()

			messages.success(request, _(page_title + ' form was created.'))
			return redirect('patient:patientdata_detail', username=patients.username)
		else:
			messages.warning(request, formset.errors)
	else:
		patient_form = Patient_ModelForm(initial=initial, prefix="patient_form")
		ec_form = Family_Form(initial=initial, prefix="ec_form")
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
