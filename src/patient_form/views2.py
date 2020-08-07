from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.db import connection, transaction, IntegrityError
from django.db.models import F, Sum
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils.timezone import now
from django.utils.translation import ugettext as _
from django.views.generic import ListView, CreateView, UpdateView
from django.db.models import Q

#from jsignature.utils import draw_signature
from crispy_forms.helper import *

from .models import *
from .forms import *
#from accounts.models import *
from customers.models import *

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
		form = AdmissionForm(request.POST or None)
		formset = AdmissionFormSet(request.POST or None)

		if form.is_valid():
			patient = form.save(commit=False)
			patient.patient = form.cleaned_data.get('patient')
			patient.date = form.cleaned_data.get('date')
			patient.time = form.cleaned_data.get('time')
			patient.admitted = form.cleaned_data.get('admitted')
			patient.admitted_others = form.cleaned_data.get('admitted_others')
			patient.save()

		if formset.is_valid():
			for item in formset:
				getpatient = Admission.objects.filter(patient=request.POST.get('patient')).exists()
				if getpatient:
					pass
				else:
					patient = patients
				get_ec_ic_number = Admission.objects.filter(patient=request.POST.get('ec_ic_number')).exists()
				if get_ec_ic_number:
					pass
				else:
					ec_ic_number = item.cleaned_data['ec_ic_number']
				ec_name = item.cleaned_data['ec_name']
				ec_relationship = item.cleaned_data['ec_relationship']
				ec_phone = item.cleaned_data['ec_phone']
				ec_address = item.cleaned_data['ec_address']
				date_diagnosis = item.cleaned_data['date_diagnosis']
				diagnosis = item.cleaned_data['diagnosis']
				date_operation = item.cleaned_data['date_operation']
				operation = item.cleaned_data['operation']
				own_medication = item.cleaned_data['own_medication']
				own_medication_drug_name = item.cleaned_data['own_medication_drug_name']
				own_medication_dosage = item.cleaned_data['own_medication_dosage']
				own_medication_tablet_capsule = item.cleaned_data['own_medication_tablet_capsule']
				own_medication_frequency = item.cleaned_data['own_medication_frequency']

				patientdata = Admission(
#					patient=patient,
					ec_name=ec_name,
					ec_ic_number=ec_ic_number,
					ec_relationship=ec_relationship,
					ec_phone=ec_phone,
					ec_address=ec_address,
					date_diagnosis=date_diagnosis,
					diagnosis=diagnosis,
					date_operation=date_operation,
					operation=operation,
					own_medication=own_medication,
					own_medication_drug_name=own_medication_drug_name,
					own_medication_dosage=own_medication_dosage,
					own_medication_tablet_capsule=own_medication_tablet_capsule,
					own_medication_frequency=own_medication_frequency,
				)
				patientdata.save()


			messages.success(request, _(page_title + ' form has been save successfully.'))
			return redirect('patient_data:patientdata_detail', username=patients.username)
		else:
			messages.warning(request, form.errors)
			messages.warning(request, formset.errors)
	else:
		form = AdmissionForm(initial=initial_form, instance=patientusername)
		formset = AdmissionFormSet(initial=initial_formset_factory)

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
		'icnumbers': icnumbers,
		'form': form,
		'formset': formset,
	}

	return render(request, 'patient_form/admission_form.html', context)


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
		'patient': patients,
		'ic_number': icnumbers,
	}

	if request.method == 'POST':
		form = ApplicationForHomeLeaveForm(request.POST or None, instance=request.user)
		if form.is_valid():
			profile = form.save(commit=False)
			profile.patient = form.cleaned_data['patient']
			profile.patient_family_name = form.cleaned_data['patient_family_name']
			profile.nric_number = form.cleaned_data['nric_number']
			profile.patient_family_relationship = form.cleaned_data['patient_family_relationship']
			profile.patient_family_phone = form.cleaned_data['patient_family_phone']
			profile.designation = form.cleaned_data['designation']
			profile.signature = form.cleaned_data['signature']
			profile.date = form.cleaned_data['date']
			profile.save()

			messages.success(request, _(page_title + ' form has been save successfully.'))
			return redirect('patient_data:patientdata_detail', username=patients.username)
		else:
			messages.warning(request, form.errors)
	else:
		#		form = ApplicationForHomeLeaveForm(initial=initial)
		#		form = ApplicationForHomeLeaveForm(instance=request.user)
		form = ApplicationForHomeLeaveForm(initial=initial, instance=request.user)

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
	query = request.GET.get('full_name')
	results = Admission.objects.filter(full_name=query)
	context = {
		'results': results,
	}
	return render(request, 'patient_form/dropdown_list.html', context)


@login_required
def appointment(request, username):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Appointment Records')
	patients = get_object_or_404(UserProfile, username=username)
	profiles = UserProfile.objects.filter(username=username)
	icnumbers = UserProfile.objects.filter(username=username).values_list('ic_number', flat=True).first()

	initial = {
		'patient': patients,
		'ic_number': icnumbers,
	}

	if request.method == 'POST':
		form = AppointmentForm(request.POST or None)

		if form.is_valid():
			form.save()

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
	if request.method == 'POST':
		form = IntakeOutputChartForm(request.POST or None)
		formset = IntakeOutputChartFormSet(request.POST or None, queryset=IntakeOutputChart.objects.filter(patient=patientid))

		if form.is_valid():
			form.save()

			messages.success(request, _(page_title + ' form has been save successfully.'))
			return redirect('patient_data:patientdata_detail', username=patients.username)
		else:
			messages.warning(request, form.errors)
	else:
		form = IntakeOutputChartForm(initial=initial)
		formset = IntakeOutputChartFormSet(queryset=IntakeOutputChart.objects.filter(patient=patientid))

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
		'icnumbers': icnumbers,
		'form': form,
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
		'patient': patients,
		'medication_date': get_today,
		'medication_time': get_time,
		'medicationstat_date_time': get_datetime,
		},
	]

#	getpatient = MedicationAdministrationRecord.objects.filter(patient=patients, allergy=request['allergy']).exists()
#	getpatient = MedicationAdministrationRecord.objects.filter(patient=patients & allergy=request['allergy']).exists()
#	getpatient = MedicationAdministrationRecord.objects.filter(patient=patients, allergy=request['allergy']).exists()	

#	try:
#		form = MedicationAdministrationRecord_ModelForm(initial=initial_form, instance=patients)
#		formset_factory = MedicationAdministrationRecord_FormSet_Factory(initial=initial_formset_factory, instance=patients)
#	except:
#		form = MedicationAdministrationRecord_ModelForm(request.POST or None, initial=initial_form)
#		formset_factory = MedicationAdministrationRecord_FormSet_Factory(request.POST or None, initial=initial_formset_factory)


	if request.method == 'POST':
#		try:
		form = MedicationAdministrationRecord_ModelForm(request.POST or None)
		formset_factory = MedicationAdministrationRecord_FormSet_Factory(request.POST or None)
#		modelform_factory = MedicationAdministrationRecord_FormFactory1(request.POST or None)
#		modelformset_factory = MedicationAdministrationRecord_FormSet_Factory(request.POST or None, queryset=MedicationAdministrationRecord.objects.filter(patient__id=patientusername.id))
#		modelformset_factory = MedicationAdministrationRecord_FormSet_Factory(request.POST or None, queryset=MedicationAdministrationRecord.objects.none(), prefix='patient_medicationadministrationrecord')
#		inlineformset_factory = MedicationAdministrationRecordInlineFormsetFactory(request.POST or None, instance=patientusername)
#		helper = MedicationAdministrationRecordFormSetHelper()

		if form.is_valid():
			patient = form.save(commit=False)
			patient.patient = form.cleaned_data.get('patient')

#			allergy, created = get_or_create(MedicationAdministrationRecord, allergy=allergy)
#			allergy, created = get_or_create(MedicationAdministrationRecord, allergy=request['allergy'])
#			allergy.value = request.POST.get(allergy)
#			allergy.save()
#			if MedicationAdministrationRecord.objects.filter(allergy=request.POST['allergy']).exists()			
#			if MedicationAdministrationRecord.objects.filter(allergy=request.POST['allergy'] is None:
#			getpatient = MedicationAdministrationRecord.objects.filter(allergy=request.POST['allergy']).exists()
			getpatient = MedicationAdministrationRecord.objects.filter(allergy=request.POST.get('allergy')).exists()
			if getpatient:
				pass
			else:
				patient.allergy = form.cleaned_data.get('allergy')
				patient.stat = form.cleaned_data.get('stat')
				patient.medicationstat_date_time = form.cleaned_data.get('medicationstat_date_time')
				patient.given_by = form.cleaned_data.get('given_by')
				patient.save()

		if formset_factory.is_valid():
#			pass
#			formset_factory.save()

#			instances = formset_factory.save(commit=False)
#			patientdata = MedicationAdministrationRecord.objects.all()
			for item in formset_factory:
				patient = patients
#				allergy = item.cleaned_data['allergy']
				medication_name = item.cleaned_data['medication_name']
				medication_dosage = item.cleaned_data['medication_dosage']
				medication_tab = item.cleaned_data['medication_tab']
				medication_frequency = item.cleaned_data['medication_frequency']
				medication_route = item.cleaned_data['medication_route']
				medication_date = item.cleaned_data['medication_date']
				medication_time = item.cleaned_data['medication_time']
				signature_nurse = item.cleaned_data['signature_nurse']
				patientdata = MedicationAdministrationRecord(
					patient=patient,
#					allergy=allergy,
					medication_name=medication_name,
					medication_dosage=medication_dosage,
					medication_tab=medication_tab,
					medication_frequency=medication_frequency,
					medication_route=medication_route,
					medication_date=medication_date,
					medication_time=medication_time,
					signature_nurse=signature_nurse,
				)
				patientdata.save()

#			for instances in formset_factory:
#				instances.patient = patients
#				instances.save()

			#for obj in formset:
				#obj.save()

#		if modelformset_factory.is_valid():
			#for obj in modelformset_factory:
#			for obj in modelformset_factory.cleaned_data:
#				profile = obj.save(commit=False)
#				profile.patient = obj.cleaned_data.get('patient')
#				profile.stat = obj.cleaned_data.get('stat')
#				profile.medicationstat_date_time = obj.cleaned_data.get('medicationstat_date_time')
#				profile.given_by = obj.cleaned_data.get('given_by')
#				profile.save()

#		if modelformset_factory.is_valid():
#			instances = modelformset_factory.save(commit=False)
#			for obj in instances:
#				obj.patient = patientusername.patient
#				obj.stat = patientusername.stat
#				obj.medicationstat_date_time = patientusername.medicationstat_date_time
#				obj.given_by = patientusername.given_by
#				obj.save()

		# for inlineformset_factory
#		if inlineformset_factory.is_valid():
#			inlineformset_factory.save()

#			instances = formset.save(commit=False)
#			for obj in instances:
#				obj.patient = patientinstance.patient
#				obj.medication_name = patientinstance.medication_name
#				obj.save()
#			instances.patient = obj.cleaned_data.get('patient')
#			instances.allergy = obj.cleaned_data.get('allergy')
#			instances.medication_name = obj.cleaned_data.get('medication_name')
#			instances.medication_dosage = obj.cleaned_data.get('medication_dosage')
#			instances.medication_tab = obj.cleaned_data.get('medication_tab')
#			instances.medication_frequency = obj.cleaned_data.get('medication_frequency')
#			instances.medication_route = obj.cleaned_data.get('medication_route')
#			instances.medication_date = obj.cleaned_data.get('medication_date')
#			instances.medication_time = obj.cleaned_data.get('medication_time')
#			instances.signature_nurse = obj.cleaned_data.get('signature_nurse')
#			instances.stat = obj.cleaned_data.get('stat')
#			instances.medicationstat_date_time = obj.cleaned_data.get('medicationstat_date_time')
#			instances.given_by = obj.cleaned_data.get('given_by')
#			instances.save()

#		if formset1.is_valid():
#			for obj in formset1.cleaned_data:
#				MedicationAdministrationRecord.objects.create(patient=obj['patient'])
#				MedicationAdministrationRecord.objects.create(medication_name=obj['medication_name'])
#				MedicationAdministrationRecord.objects.create(medication_dosage=obj['medication_dosage'])
#				MedicationAdministrationRecord.objects.create(medication_tab=obj['medication_tab'])
#				MedicationAdministrationRecord.objects.create(medication_frequency=obj['medication_frequency'])
#				MedicationAdministrationRecord.objects.create(medication_date=obj['medication_date'])
#				MedicationAdministrationRecord.objects.create(medication_date=obj['medication_date'])
#				MedicationAdministrationRecord.objects.create(medication_time=obj['medication_time'])
#				MedicationAdministrationRecord.objects.create(signature_nurse=obj['signature_nurse'])

#		if formset2.is_valid():
#			for obj in formset2:
#			for obj in formset2.cleaned_data:
#				profile = obj.save(commit=False)
#				profile.patient = obj.cleaned_data.get('patient')
#				profile.stat = obj.cleaned_data.get('stat')
#				profile.medicationstat_date_time = obj.cleaned_data.get('medicationstat_date_time')
#				profile.given_by = obj.cleaned_data.get('given_by')
#				profile.save()

#		if form.is_valid() and modelformset_factory.is_valid():
#			try:
#				with transaction.atomic():
#					patient = form.save(commit=False)
#					patient.patient = form.cleaned_data.get('patient')
#					patient.save()

#					for obj in modelformset_factory:
#						item = obj.save(commit=False)
#						item.patient = patients
#						item.save()

#			except IntegrityError:
#				print("Error Encountered")

			messages.success(request, _(page_title + ' form has been save successfully.'))
			return redirect('patient_data:patientdata_detail', username=patients.username)
		else:
#			messages.warning(request, form.errors)
			messages.warning(request, formset_factory.errors)
#			messages.warning(request, formset1.errors)
#			messages.warning(request, formset2.errors)
	else:
		form = MedicationAdministrationRecord_ModelForm(initial=initial_form, instance=patientusername)
		formset_factory = MedicationAdministrationRecord_FormSet_Factory(initial=initial_formset_factory)
#		modelform_factory = MedicationAdministrationRecord_FormFactory2(initial=initial_modelform_factory)
#		modelformset_factory = MedicationAdministrationRecord_FormSet_Factory(initial=initial_modelformset_factory, queryset=MedicationAdministrationRecord.objects.filter(patient__id=patientusername.id))
#		modelformset_factory = MedicationAdministrationRecord_FormSet_Factory(initial=initial_modelformset_factory, queryset=MedicationAdministrationRecord.objects.none(), prefix='patient_medicationadministrationrecord')
#		inlineformset_factory = MedicationAdministrationRecordInlineFormsetFactory(instance=patientusername, initial=initial_inlineformset_factory)
#		formset1 = MedicationAdministrationRecordFormSet1(initial=initial_formset, prefix='formSet1')
#		formset2 = MedicationAdministrationRecordFormSet2(initial=initial_formset, prefix='formSet2')
#		helper = MedicationAdministrationRecordFormSetHelper()

#	print("getpatient: ", getpatient)
	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
		'icnumbers': icnumbers,
		'form': form,
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
#			profile = OvertimeClaim()
#			profile = form.save(commit=False)
#			profile.patient = form.cleaned_data['patient']
#			profile.date = form.cleaned_data['date']
#			profile.duration_time = form.cleaned_data['duration_time']
#			profile.hours = form.cleaned_data['hours']
#			profile.hours = profile.hours.strptime(profile.hours.strftime("%H:%M"), "%H:%M")
#			profile.hours = datetime.datetime.strptime(duration_time, '%H:%M').time()
#			profile.total_hours = form.cleaned_data['total_hours']
#			start_time = OvertimeClaim.objects.get(pk=id)
#			start = start_time.hours
#			delta = start.replace(hour=(start.hour + profile.duration_time) % 24)
#			delta = profile.duration_time
#			profile.total_hours = datetime.time(delta)
#			profile.total_hours = datetime.datetime.strptime(profile.duration_time, '%H:%M').time()
#			profile.total_hours = t
#			profile.checked_sign_by = form.cleaned_data['checked_sign_by']
#			profile.verify_by = form.cleaned_data['verify_by']
#			profile.save()
			form.save()

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
