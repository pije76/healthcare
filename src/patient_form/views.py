from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.db import connection, transaction, IntegrityError
from django.db.models import F, Sum, Q, signals
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.utils import timezone
from django.utils.translation import ugettext as _
from django.views.generic import ListView, CreateView, UpdateView

#from jsignature.utils import draw_signature
from crispy_forms.helper import *
from dal import autocomplete

from .models import *
from .forms import *
#from accounts.models import *
from customers.models import *

import datetime
now = timezone.now()

# Create your views here.
def index(request):
	schema_name = connection.schema_name
	patients = UserProfile.objects.filter(username=request.user.username)
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Home')

	context = {
		'patients': patients,
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
	}
	return render(request, 'index.html', context)


@login_required
def admission(request, username):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Admission Form')
	patients = get_object_or_404(UserProfile, username=username)
	patientusername = UserProfile.objects.get(username=username)
	profiles = UserProfile.objects.filter(username=username)
	icnumbers = UserProfile.objects.filter(username=username).values_list('ic_number', flat=True).first()

	initial_form = {
		'patient': patients,
		'ic_number': icnumbers,
	}

	initial_formset_factory = [{
		'patient': patients,
		'medication_date': get_today,
		'medication_time': get_time,
		'medicationstat_date_time': get_datetime,
		},
	]

	
	if request.method == 'POST':
		formset = AdmissionFormSet(request.POST or None)

		if formset.is_valid():
			for item in formset:
				patient = patients
				date = item.cleaned_data['date']
				time = item.cleaned_data['time']
				admitted = item.cleaned_data['admitted']
				admitted_others = item.cleaned_data['admitted_others']
				mode = item.cleaned_data['mode']
				birth_date = item.cleaned_data['birth_date']
				today = datetime.date.today()
				delta_day = int((datetime.datetime.now().date() - birth_date).days / 365.24219)
				age = delta_day
#				age = item.cleaned_data['age']
				gender = item.cleaned_data['gender']
				marital_status = item.cleaned_data['marital_status']
				marital_status_others = item.cleaned_data['marital_status_others']
				religion = item.cleaned_data['religion']
				religion_others = item.cleaned_data['religion_others']
				occupation = item.cleaned_data['occupation']
				occupation_others = item.cleaned_data['occupation_others']
				communication_sight = item.cleaned_data['communication_sight']
				communication_hearing = item.cleaned_data['communication_hearing']
				communication_hearing_others = item.cleaned_data['communication_hearing_others']
				address = item.cleaned_data['address']

				ec_name = item.cleaned_data['ec_name']
				ec_ic_number = item.cleaned_data['ec_ic_number']
				ec_relationship = item.cleaned_data['ec_relationship']
				ec_phone = item.cleaned_data['ec_phone']
				ec_address = item.cleaned_data['ec_address']

				general_condition = item.cleaned_data['general_condition']
				vital_sign_temperature = item.cleaned_data['vital_sign_temperature']
				vital_sign_pulse = item.cleaned_data['vital_sign_pulse']
				vital_sign_bp = item.cleaned_data['vital_sign_bp']
				vital_sign_resp = item.cleaned_data['vital_sign_resp']
				vital_sign_spo2 = item.cleaned_data['vital_sign_spo2']
				vital_sign_on_oxygen_therapy = item.cleaned_data['vital_sign_on_oxygen_therapy']
				vital_sign_on_oxygen_therapy_flow_rate = item.cleaned_data['vital_sign_on_oxygen_therapy_flow_rate']
				vital_sign_hgt = item.cleaned_data['vital_sign_hgt']
				allergy_drug = item.cleaned_data['allergy_drug']
				allergy_food = item.cleaned_data['allergy_food']
				allergy_others = item.cleaned_data['allergy_others']
				biohazard_infectious_disease = item.cleaned_data['biohazard_infectious_disease']
				biohazard_infectious_disease_others = item.cleaned_data['biohazard_infectious_disease_others']
				invasive_line_insitu = item.cleaned_data['invasive_line_insitu']
				invasive_line_insitu_others = item.cleaned_data['invasive_line_insitu_others']
				medical_history = item.cleaned_data['medical_history']
				medical_history_others = item.cleaned_data['medical_history_others']
				surgical_history_none = item.cleaned_data['surgical_history_none']
				surgical_history = item.cleaned_data['surgical_history']

				date_diagnosis = item.cleaned_data['date_diagnosis']
				diagnosis = item.cleaned_data['diagnosis']
				date_operation = item.cleaned_data['date_operation']
				operation = item.cleaned_data['operation']
				own_medication = item.cleaned_data['own_medication']
				own_medication_drug_name = item.cleaned_data['own_medication_drug_name']
				own_medication_dosage = item.cleaned_data['own_medication_dosage']
				own_medication_tablet_capsule = item.cleaned_data['own_medication_tablet_capsule']
				own_medication_frequency = item.cleaned_data['own_medication_frequency']

				adaptive_aids_with_patient = item.cleaned_data['adaptive_aids_with_patient']
				adaptive_aids_with_patient_others = item.cleaned_data['adaptive_aids_with_patient_others']
				orientation = item.cleaned_data['orientation']
				special_information = item.cleaned_data['special_information']
				admission_by = item.cleaned_data['admission_by']

				patientdata = Admission(
					patient = patient,
					date = date,
					time = time,
					admitted = admitted,
					admitted_others = admitted_others,
					mode = mode,

					birth_date = birth_date,
					age = age,
					gender = gender,
					marital_status = marital_status,
					marital_status_others = marital_status_others,
					religion = religion,
					religion_others = religion_others,
					occupation = occupation,
					occupation_others = occupation_others,
					communication_sight = communication_sight,
					communication_hearing = communication_hearing,
					communication_hearing_others = communication_hearing_others,
					address = address,

					ec_name = ec_name,
					ec_ic_number = ec_ic_number,
					ec_relationship = ec_relationship,
					ec_phone = ec_phone,
					ec_address = ec_address,

					general_condition = general_condition,
					vital_sign_temperature = vital_sign_temperature,
					vital_sign_pulse = vital_sign_pulse,
					vital_sign_bp = vital_sign_bp,
					vital_sign_resp = vital_sign_resp,
					vital_sign_spo2 = vital_sign_spo2,
					vital_sign_on_oxygen_therapy = vital_sign_on_oxygen_therapy,
					vital_sign_on_oxygen_therapy_flow_rate = vital_sign_on_oxygen_therapy_flow_rate,
					vital_sign_hgt = vital_sign_hgt,
					allergy_drug = allergy_drug,
					allergy_food = allergy_food,
					allergy_others = allergy_others,
					biohazard_infectious_disease = biohazard_infectious_disease,
					biohazard_infectious_disease_others = biohazard_infectious_disease_others,
					invasive_line_insitu = invasive_line_insitu,
					invasive_line_insitu_others = invasive_line_insitu_others,
					medical_history = medical_history,
					medical_history_others = medical_history_others,
					surgical_history_none = surgical_history_none,
					surgical_history = surgical_history,

					date_diagnosis = date_diagnosis,
					diagnosis = diagnosis,
					date_operation = date_operation,
					operation = operation,
					own_medication = own_medication,
					own_medication_drug_name = own_medication_drug_name,
					own_medication_dosage = own_medication_dosage,
					own_medication_tablet_capsule = own_medication_tablet_capsule,
					own_medication_frequency = own_medication_frequency,

					adaptive_aids_with_patient = adaptive_aids_with_patient,
					adaptive_aids_with_patient_others = adaptive_aids_with_patient_others,
					orientation = orientation,
					special_information = special_information,
					admission_by = admission_by,
				)
				patientdata.save()


			messages.success(request, _(page_title + ' form has been save successfully.'))
			return redirect('patient_data:patientdata_detail', username=patients.username)
		else:
			messages.warning(request, formset.errors)
	else:
		formset = AdmissionFormSet(initial=initial_formset_factory)

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
		'icnumbers': icnumbers,
		'formset': formset,
	}

	return render(request, 'patient_form/admission_form.html', context)


#class Select2QuerySetView(autocomplete.Select2QuerySetView):
#	def get_queryset(self):
#		if not self.request.user.is_authenticated:
#			return ApplicationForHomeLeave.objects.none()
#		qs = ApplicationForHomeLeave.objects.all()

#		if self.q:
#			qs = qs.filter(ec_name__istartswith=self.q)
#		return qs

@login_required
def application_homeleave(request, username):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Application For Home Leave')
	patients = get_object_or_404(UserProfile, username=username)
	profiles = UserProfile.objects.filter(username=username)
	icnumbers = UserProfile.objects.filter(username=username).values_list('ic_number', flat=True).first()

	initial = {
#		'patient': patients,
#		'ic_number': icnumbers,
	}

	if request.method == 'POST':
		form = ApplicationForHomeLeaveForm(request.POST or None, instance=request.user)
		if form.is_valid():
			profile = form.save(commit=False)
			profile.patient = form.cleaned_data['patient']
			profile.family_name = form.cleaned_data['family_name']
			profile.family_ic_number = form.cleaned_data['family_ic_number']
			profile.family_relationship = form.cleaned_data['family_relationship']
			profile.family_phone = form.cleaned_data['family_phone']
			profile.designation = form.cleaned_data['designation']
			profile.signature = form.cleaned_data['signature']
			profile.date = form.cleaned_data['date']
			profile.save()

			messages.success(request, _(page_title + ' form has been save successfully.'))
			return redirect('patient_data:patientdata_detail', username=patients.username)
		else:
			messages.warning(request, form.errors)
	else:
		form = ApplicationForHomeLeaveForm(initial=initial)
#		form = ApplicationForHomeLeaveForm(instance=request.user)
#		form = ApplicationForHomeLeaveForm(initial=initial, instance=request.user)
#		form = ApplicationForHomeLeaveForm()

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
		'icnumbers': icnumbers,
		'form': form,
	}

	return render(request, 'patient_form/application_homeleave_form.html', context)


def load_ic_number(request):
	fullname_data = request.GET.get('full_name')
	patient_data = request.GET.get('patient')
	family_data = request.GET.get('ec_name')
	fullname_results = UserProfile.objects.filter(full_name=fullname_data).order_by('full_name')
#	fullname_results = UserProfile.objects.filter(full_name=request.user)
	patient_results = Admission.objects.filter(patient=patient_data)
	context = {
		'fullname_results': fullname_results,
		'patient_results': patient_results,
	}
	return render(request, 'patient_form/dropdown_list.html', context)


def load_family_name(request):
	

	query_data = request.GET.get('family_name')

	data = model.objects.filter(email__startswith=query_data).values_list('email',flat=True)
	data = M.objects.filter(title__istartswith=query_data)
	results = [ x.title for x in data ]

	json = list(data)
	json = simplejson.dumps(results)

	return JsonResponse(json, safe=False)
#	return HttpResponse(json, mimetype="application/json")


@login_required
def appointment(request, username):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Appointment Records')
	patients = get_object_or_404(UserProfile, username=username)
	profiles = UserProfile.objects.filter(username=username)
	user_profile = UserProfile.objects.filter(username=username).values_list('full_name', flat=True)
	icnumbers = UserProfile.objects.filter(username=username).values_list('ic_number', flat=True).first()
	appointments = Appointment.objects.all()
	query = request.GET.get('q')
#	appointments = appointments.filter(date__lte=now).filter(Q(title__icontains=query) | Q(content__icontains=query)).distinct()

	initial = {
		'patient': patients,
		'ic_number': icnumbers,
	}

	if request.method == 'POST':
		form = AppointmentForm(request.POST or None)

		if form.is_valid():
			profile = form.save(commit=False)
			profile.patient = form.cleaned_data['patient']
			profile.date_time = form.cleaned_data['date_time']
			profile.hospital_clinic_center = form.cleaned_data['hospital_clinic_center']
			profile.department = form.cleaned_data['department']
			profile.planning_investigation = form.cleaned_data['planning_investigation']
			profile.treatment_order = form.cleaned_data['treatment_order']
			profile.save()

			messages.success(request, _(page_title + ' form has been save successfully.'))
			return redirect('patient_data:patientdata_detail', username=patients.username)
		else:
			messages.warning(request, form.errors)

	else:
		form = AppointmentForm(initial=initial)

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
		'icnumbers': icnumbers,
		'form': form,
	}

	return render(request, 'patient_form/appointment_form.html', context)

@login_required
def catheterization_cannulation(request, username):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Catheterization and Cannulation Chart')
	patients = get_object_or_404(UserProfile, username=username)
	profiles = UserProfile.objects.filter(username=username)
	icnumbers = UserProfile.objects.filter(username=username).values_list('ic_number', flat=True).first()

	initial = {
		'patient': patients,
		'ic_number': icnumbers,
	}

	if request.method == 'POST':
		form = CannulationForm(request.POST or None)
		if form.is_valid():
			form.save()

			messages.success(request, _(page_title + ' form has been save successfully.'))
			return redirect('patient_data:patientdata_detail', username=patients.username)
		else:
			messages.warning(request, form.errors)

	else:
		form = CannulationForm(initial=initial)

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
		'icnumbers': icnumbers,
		'form': form,
	}

	return render(request, 'patient_form/cannulation_form.html', context)


@login_required
def charges_sheet(request, username):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Charges Sheet')
	patients = get_object_or_404(UserProfile, username=username)
	profiles = UserProfile.objects.filter(username=username)
	icnumbers = UserProfile.objects.filter(username=username).values_list('ic_number', flat=True).first()

	initial = {
		'patient': patients,
		'ic_number': icnumbers,
	}

	if request.method == 'POST':
		form = ChargesForm(request.POST or None)
		if form.is_valid():
			form.save()

			messages.success(request, _(page_title + ' form has been save successfully.'))
			return redirect('patient_data:patientdata_detail', username=patients.username)
		else:
			messages.warning(request, form.errors)
	else:
		form = ChargesForm(initial=initial)

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
		'icnumbers': icnumbers,
		'form': form,
	}

	return render(request, 'patient_form/charges_sheet_form.html', context)


@login_required
def dressing(request, username):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Dressing Chart')
	patients = get_object_or_404(UserProfile, username=username)
	profiles = UserProfile.objects.filter(username=username)
	icnumbers = UserProfile.objects.filter(username=username).values_list('ic_number', flat=True).first()

	initial = {
		'patient': patients,
		'ic_number': icnumbers,
	}

	if request.method == 'POST':
		form = DressingForm(request.POST or None, request.FILES)
		if form.is_valid():
			form.save()

			messages.success(request, _(page_title + ' form has been save successfully.'))
			return redirect('patient_data:patientdata_detail', username=patients.username)
		else:
			messages.warning(request, form.errors)
	else:
		form = DressingForm(initial=initial)

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
		'icnumbers': icnumbers,
		'form': form,
	}

	return render(request, 'patient_form/dressing_form.html', context)


@login_required
def enteral_feeding_regime(request, username):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Enteral Feeding Regime')
#	total_flush = EnteralFeedingRegime.objects.all().annotate(total_food=F('warm_water_before ') + F('warm_water_after'))
#    total = EnteralFeedingRegime.objects.aggregate(total_population=Sum('amount'))
	patients = get_object_or_404(UserProfile, username=username)
	profiles = UserProfile.objects.filter(username=username)
	icnumbers = UserProfile.objects.filter(username=username).values_list('ic_number', flat=True).first()

	initial = {
		'patient': patients,
		'ic_number': icnumbers,
	}

	if request.method == 'POST':
		form = EnteralFeedingRegimeForm(request.POST or None)
		if form.is_valid():
			form.save()

			messages.success(request, _(page_title + ' form has been save successfully.'))
			return redirect('patient_data:patientdata_detail', username=patients.username)
		else:
			messages.warning(request, form.errors)
	else:
		form = EnteralFeedingRegimeForm(initial=initial)

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
		'icnumbers': icnumbers,
		'form': form,
	}

	return render(request, 'patient_form/enteral_feeding_regime_form.html', context)


@login_required
def hgt_chart(request, username):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('HGT Chart')
	patients = get_object_or_404(UserProfile, username=username)
	profiles = UserProfile.objects.filter(username=username)
	icnumbers = UserProfile.objects.filter(username=username).values_list('ic_number', flat=True).first()

	initial = {
		'patient': patients,
		'ic_number': icnumbers,
	}

	if request.method == 'POST':
		form = HGTChartForm(request.POST or None)
		if form.is_valid():
			form.save()

			messages.success(request, _(page_title + ' form has been save successfully.'))
			return redirect('patient_data:patientdata_detail', username=patients.username)
		else:
			messages.warning(request, form.errors)
	else:
		form = HGTChartForm(initial=initial)

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
		'icnumbers': icnumbers,
		'form': form,
	}

	return render(request, 'patient_form/hgt_chart_form.html', context)


@login_required
def intake_output(request, username):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Intake Output Chart')
	profiles = UserProfile.objects.filter(username=username)
	patientid = UserProfile.objects.get(username=username).id
	patients = get_object_or_404(UserProfile, username=username)
	icnumbers = UserProfile.objects.filter(username=username).values_list('ic_number', flat=True).first()
	intakeoutput = IntakeOutputChart.objects.filter(patient=patientid)


	initial = {
		'patient': patients,
		'ic_number': icnumbers,
	}

	initial_formset_factory = [{
		'patient': patients,
		'ic_number': icnumbers,
		},
	]

	if request.method == 'POST':
		formset = IntakeOutputChart_FormSet_Factory(request.POST or None)

		if formset.is_valid():
			for item in formset:
				patient = patients
				date = item.cleaned_data['date']
				time_intake = item.cleaned_data['time_intake']
				intake_oral_type = item.cleaned_data['intake_oral_type']
				intake_oral_ml = item.cleaned_data['intake_oral_ml']
				intake_parenteral_type = item.cleaned_data['intake_parenteral_type']
				intake_parenteral_ml = item.cleaned_data['intake_parenteral_ml']
				intake_other_type = item.cleaned_data['intake_other_type']
				intake_other_ml = item.cleaned_data['intake_other_ml']
				time_output = item.cleaned_data['time_output']
				output_urine_ml = item.cleaned_data['output_urine_ml']
				output_urine_cum = item.cleaned_data['output_urine_cum']
				output_gastric_ml = item.cleaned_data['output_gastric_ml']
				output_other_type = item.cleaned_data['output_other_type']
				output_other_ml = item.cleaned_data['output_other_ml']

				patientdata = IntakeOutputChart(
					patient=patient,
					date=date,
					time_intake=time_intake,
					intake_oral_type=intake_oral_type,
					intake_oral_ml=intake_oral_ml,
					intake_parenteral_type=intake_parenteral_type,
					intake_parenteral_ml=intake_parenteral_ml,
					intake_other_type=intake_other_type,
					intake_other_ml=intake_other_ml,
					time_output=time_output,
					output_urine_ml=output_urine_ml,
					output_urine_cum=output_urine_cum,
					output_gastric_ml=output_gastric_ml,
					output_other_type=output_other_type,
					output_other_ml=output_other_ml,
				)
				patientdata.save()


			messages.success(request, _(page_title + ' form has been save successfully.'))
			return redirect('patient_data:patientdata_detail', username=patients.username)
		else:
#			messages.warning(request, form.errors)
			messages.warning(request, formset.errors)
	else:
#		form = IntakeOutputChartForm(initial=initial)
		formset = IntakeOutputChart_FormSet_Factory(initial=initial_formset_factory)

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
		'icnumbers': icnumbers,
#		'form': form,
		'formset': formset,
	}

	return render(request, 'patient_form/intake_output_form.html', context)


@login_required
def maintainance(request, username):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Maintainance Form')
	patients = get_object_or_404(UserProfile, username=username)
	profiles = UserProfile.objects.filter(username=username)
	icnumbers = UserProfile.objects.filter(username=username).values_list('ic_number', flat=True).first()

	initial = {
		'patient': patients,
		'ic_number': icnumbers,
	}

	if request.method == 'POST':
		form = MaintainanceForm(request.POST or None)
		if form.is_valid():
			form.save()

			messages.success(request, _(page_title + ' form has been save successfully.'))
			return redirect('patient_data:patientdata_detail', username=patients.username)
		else:
			messages.warning(request, form.errors)
	else:
		form = MaintainanceForm(initial=initial)

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
		'icnumbers': icnumbers,
		'form': form,
	}

	return render(request, 'patient_form/maintainance_form.html', context)


@login_required
def medication_record(request, username):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Medication Records')
	patients = get_object_or_404(UserProfile, username=username)
	profiles = UserProfile.objects.filter(username=username)
	icnumbers = UserProfile.objects.filter(username=username).values_list('ic_number', flat=True).first()

	initial = {
		'patient': patients,
		'ic_number': icnumbers,
	}

	if request.method == 'POST':
		form = MedicationRecordForm(request.POST or None)
		if form.is_valid():
			form.save()

			messages.success(request, _(page_title + ' form has been save successfully.'))
			return redirect('patient_data:patientdata_detail', username=patients.username)
		else:
			messages.warning(request, form.errors)
	else:
		form = MedicationRecordForm(initial=initial)

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
		'icnumbers': icnumbers,
		'form': form,
	}

	return render(request, 'patient_form/medication_form.html', context)


@login_required
def medication_administration(request, username):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Medication Administration Record')

	patientid = UserProfile.objects.get(username=username).id
	icnumbers = UserProfile.objects.get(username=username).ic_number
	patientusername = UserProfile.objects.get(username=username)
	profiles = UserProfile.objects.filter(username=username)
	patients = get_object_or_404(UserProfile, username=username)

	allergies = MedicationAdministrationRecord.objects.filter(patient=patientid).values_list('allergy', flat=True).first()
	stat = MedicationAdministrationRecord.objects.filter(patient=patientid).values_list('stat', flat=True).first()
	medicationstat_date_time = MedicationAdministrationRecord.objects.filter(patient=patientid).values_list('medicationstat_date_time', flat=True).first()
	given_by = MedicationAdministrationRecord.objects.filter(patient=patientid).values_list('given_by', flat=True).first()

	queryset = MedicationAdministrationRecord.objects.filter(patient=patientid).values()

	initial_form = {
		'patient': patients,
		'ic_number': icnumbers,
		'allergy': allergies,
		'stat': stat,
		'medicationstat_date_time': medicationstat_date_time,
		'given_by': given_by,
	}
	initial_formset_factory = [{
		'patient': patients,
		'medication_date': get_today,
		'medication_time': get_time,
		'medicationstat_date_time': get_datetime,
		},
	]
	initial_modelform_factory = {
		'patient': patients,
		'medication_date': get_today,
		'medication_time': get_time,
		'medicationstat_date_time': get_datetime,
	}
	initial_modelformset_factory = [{
		'patient': patients,
		'medication_date': get_today,
		'medication_time': get_time,
		'medicationstat_date_time': get_datetime,
		},
	]
	initial_inlineformset_factory = [{
#		'patient': patients,
		'medication_date': get_today,
		'medication_time': get_time,
		'medicationstat_date_time': get_datetime,
		},
	]

	GROUP_SIZE = 4

	if request.method == 'POST':
		formset_factory = MedicationAdministrationRecord_FormSet_Factory(request.POST or None)

		if formset_factory.is_valid():
			for item in formset_factory:
				patient = patients
				allergy = item.cleaned_data['allergy']
				medication_name = item.cleaned_data['medication_name']
				medication_dosage = item.cleaned_data['medication_dosage']
				medication_tab = item.cleaned_data['medication_tab']
				medication_frequency = item.cleaned_data['medication_frequency']
				medication_route = item.cleaned_data['medication_route']
				medication_date = item.cleaned_data['medication_date']
				medication_time = item.cleaned_data['medication_time']
				signature_nurse = item.cleaned_data['signature_nurse']
				stat = item.cleaned_data['stat']
				medicationstat_date_time = item.cleaned_data['medicationstat_date_time']
				given_by = item.cleaned_data['given_by']
				patientdata = MedicationAdministrationRecord(
					patient=patient,
					allergy=allergy,
					medication_name=medication_name,
					medication_dosage=medication_dosage,
					medication_tab=medication_tab,
					medication_frequency=medication_frequency,
					medication_route=medication_route,
					medication_date=medication_date,
					medication_time=medication_time,
					signature_nurse=signature_nurse,
					stat=stat,
					medicationstat_date_time=medicationstat_date_time,
					given_by=given_by,
				)
				patientdata.save()

			messages.success(request, _(page_title + ' form has been save successfully.'))
			return redirect('patient_data:patientdata_detail', username=patients.username)
		else:
			messages.warning(request, formset_factory.errors)
	else:
		formset_factory = MedicationAdministrationRecord_FormSet_Factory(initial=initial_formset_factory)
#		formset_factory = MedicationAdministrationRecord_FormSet_Factory(initial=[{'medication_date': get_today} for medication_date in queryset])

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
		'icnumbers': icnumbers,
#		'form': form,
		'formset': formset_factory,
#		'formset1': formset1,
#		'formset2': formset2,
#		'helper': helper,
	}

#	return render(request, 'patient_form/medication_administration_form.html', context)
	return render(request, 'patient_form/medication_administration_formset_factory.html', context)
#	return render(request, 'patient_form/medication_administration_modelform_factory.html', context)
#	return render(request, 'patient_form/medication_administration_modelformset_factory.html', context)
#	return render(request, 'patient_form/medication_administration_inlineformset_factory.html', context)

@login_required
def miscellaneous_charges_slip(request, username):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Miscellaneous Charges Slip')
	patients = get_object_or_404(UserProfile, username=username)
	profiles = UserProfile.objects.filter(username=username)
	icnumbers = UserProfile.objects.filter(username=username).values_list('ic_number', flat=True).first()

	initial = {
		'patient': patients,
		'ic_number': icnumbers,
	}

	if request.method == 'POST':
		form = MiscellaneousChargesSlipForm(request.POST or None)
		if form.is_valid():
			form.save()

			messages.success(request, _(page_title + ' form has been save successfully.'))
			return redirect('patient_data:patientdata_detail', username=patients.username)
		else:
			messages.warning(request, form.errors)
	else:
		form = MiscellaneousChargesSlipForm(initial=initial)

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
		'icnumbers': icnumbers,
		'form': form,
	}

	return render(request, 'patient_form/miscellaneous_charges_slip_form.html', context)


@login_required
def nursing(request, username):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Nursing Report')
	patients = get_object_or_404(UserProfile, username=username)
	profiles = UserProfile.objects.filter(username=username)
	icnumbers = UserProfile.objects.filter(username=username).values_list('ic_number', flat=True).first()

	initial = {
		'patient': patients,
		'ic_number': icnumbers,
	}

	if request.method == 'POST':
		form = NursingForm(request.POST or None)
		if form.is_valid():
			form.save()

			messages.success(request, _(page_title + ' form has been save successfully.'))
			return redirect('patient_data:patientdata_detail', username=patients.username)
		else:
			messages.warning(request, form.errors)
	else:
		form = NursingForm(initial=initial)

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
		'icnumbers': icnumbers,
		'form': form,
	}

	return render(request, 'patient_form/nursing_form.html', context)


@login_required
def overtime_claim(request, username):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Overtime Claim Form')
	patients = get_object_or_404(UserProfile, username=username)
	profiles = UserProfile.objects.filter(username=username)
	icnumbers = UserProfile.objects.filter(username=username).values_list('ic_number', flat=True).first()
#	durations = OvertimeClaim.objects.filter(patient=id).values_list('duration_time', flat=True).
#	d = dict()
#	d['duration_time'] = a.duration_time
#	total = OvertimeClaim.objects.annotate(duration = Func(F('end_date'), F('start_date'), function='age'))

#	t = datetime.time(convert_duration_hour, convert_duration_minute)

	initial = {
		'patient': patients,
		'ic_number': icnumbers,
	}

	if request.method == 'POST':
		form = OvertimeClaimForm(request.POST or None)
		if form.is_valid():
			patient = form.cleaned_data['patient']
			date = form.cleaned_data['date']
			duration_time = form.cleaned_data['duration_time']
			hours = form.cleaned_data['hours']
			sec = duration_time.total_seconds()
			convert_duration_hour = int((sec / 3600) % 3600)
			convert_duration_minute = int((sec / 60) % 60)
			convert_duration_second = int(sec)
			delta = datetime.timedelta(hours=convert_duration_hour, minutes=convert_duration_minute)
			total_delta = (datetime.datetime.combine(datetime.date(1,1,1), hours) + delta).time()
			total_hours = total_delta
			checked_sign_by = form.cleaned_data['checked_sign_by']
			verify_by = form.cleaned_data['verify_by']

			patientdata = OvertimeClaim(
				patient = patient,
				date = date,
				duration_time = duration_time,
				hours = hours,
				total_hours = total_hours,
				checked_sign_by = checked_sign_by,
				verify_by = verify_by,
			)
			patientdata.save()
			messages.success(request, _(page_title + ' form has been save successfully.'))
			return redirect('patient_data:patientdata_detail', username=patients.username)
		else:
			messages.warning(request, form.errors)
	else:
		form = OvertimeClaimForm(initial=initial)

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
		'icnumbers': icnumbers,
		'form': form,
	}

	return render(request, 'patient_form/overtime_claim_form.html', context)


@login_required
def physio_progress_note(request, username):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Physiotherapy Progress Note')
	patients = get_object_or_404(UserProfile, username=username)
	profiles = UserProfile.objects.filter(username=username)
	icnumbers = UserProfile.objects.filter(username=username).values_list('ic_number', flat=True).first()

	initial = {
		'patient': patients,
		'ic_number': icnumbers,
	}

	if request.method == 'POST':
		form = PhysioProgressNoteForm(request.POST or None)
		if form.is_valid():
			form.save()

			messages.success(request, _(page_title + ' form has been save successfully.'))
			return redirect('patient_data:patientdata_detail', username=patients.username)
		else:
			messages.warning(request, form.errors)
	else:
		form = PhysioProgressNoteForm(initial=initial)

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
		'icnumbers': icnumbers,
		'form': form,
	}

	return render(request, 'patient_form/physio_progress_note_form.html', context)


@login_required
def physiotherapy_general_assessment(request, username):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Physiotherapy General Assessment Form')
	patients = get_object_or_404(UserProfile, username=username)
	profiles = UserProfile.objects.filter(username=username)
	icnumbers = UserProfile.objects.filter(username=username).values_list('ic_number', flat=True).first()

	initial = {
		'patient': patients,
		'ic_number': icnumbers,
	}

	if request.method == 'POST':
		form = PhysiotherapyGeneralAssessmentForm(request.POST or None)
		if form.is_valid():
			form.save()

			messages.success(request, _(page_title + ' form has been save successfully.'))
			return redirect('patient_data:patientdata_detail', username=patients.username)
		else:
			messages.warning(request, form.errors)
	else:
		form = PhysiotherapyGeneralAssessmentForm(initial=initial)

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
		'icnumbers': icnumbers,
		'form': form,
	}

	return render(request, 'patient_form/physiotherapy_general_assessment_form.html', context)


@login_required
def staff_records(request, username):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Staff Records')
	patients = get_object_or_404(UserProfile, username=username)
	profiles = UserProfile.objects.filter(username=username)
	icnumbers = UserProfile.objects.filter(username=username).values_list('ic_number', flat=True).first()

	initial = {
		'patient': patients,
		'ic_number': icnumbers,
	}

	if request.method == 'POST':
		form = StaffRecordsForm(request.POST or None)
		if form.is_valid():
			form.save()

			messages.success(request, _(page_title + ' form has been save successfully.'))
			return redirect('patient_data:patientdata_detail', username=patients.username)
		else:
			messages.warning(request, form.errors)
	else:
		form = StaffRecordsForm(initial=initial)

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
		'icnumbers': icnumbers,
		'form': form,
	}

	return render(request, 'patient_form/staff_records_form.html', context)


@login_required
def stool(request, username):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Stool Chart')
	patients = get_object_or_404(UserProfile, username=username)
	profiles = UserProfile.objects.filter(username=username)
	icnumbers = UserProfile.objects.filter(username=username).values_list('ic_number', flat=True).first()

	initial = {
		'patient': patients,
		'ic_number': icnumbers,
	}

	if request.method == 'POST':
		form = StoolForm(request.POST or None)
		if form.is_valid():
			form.save()

			messages.success(request, _(page_title + ' form has been save successfully.'))
			return redirect('patient_data:patientdata_detail', username=patients.username)
		else:
			messages.warning(request, form.errors)
	else:
		form = StoolForm(initial=initial)

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
		'icnumbers': icnumbers,
		'form': form,
	}

	return render(request, 'patient_form/stool_form.html', context)


@login_required
def visiting_consultant_records(request, username):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Visiting Consultant Records')
	patients = get_object_or_404(UserProfile, username=username)
	profiles = UserProfile.objects.filter(username=username)
	icnumbers = UserProfile.objects.filter(username=username).values_list('ic_number', flat=True).first()

	initial = {
		'patient': patients,
		'ic_number': icnumbers,
	}

	if request.method == 'POST':
		form = VisitingConsultantForm(request.POST or None)
		if form.is_valid():
			form.save()

			messages.success(request, _(page_title + ' form has been save successfully.'))
			return redirect('patient_data:patientdata_detail', username=patients.username)
		else:
			messages.warning(request, form.errors)
	else:
		form = VisitingConsultantForm(initial=initial)

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
		'icnumbers': icnumbers,
		'form': form,
	}

	return render(request, 'patient_form/visiting_consultant_records_form.html', context)


@login_required
def vital_sign_flow(request, username):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Vital Sign Flow Sheet')
	patients = get_object_or_404(UserProfile, username=username)
	profiles = UserProfile.objects.filter(username=username)
	icnumbers = UserProfile.objects.filter(username=username).values_list('ic_number', flat=True).first()

	initial = {
		'patient': patients,
		'ic_number': icnumbers,
	}

	if request.method == 'POST':
		form = VitalSignFlowForm(request.POST or None)
		if form.is_valid():
			form.save()

			messages.success(request, _(page_title + ' form has been save successfully.'))
			return redirect('patient_data:patientdata_detail', username=patients.username)
		else:
			messages.warning(request, form.errors)
	else:
		form = VitalSignFlowForm(initial=initial)

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
		'icnumbers': icnumbers,
		'form': form,
	}

	return render(request, 'patient_form/vital_sign_flow_form.html', context)
