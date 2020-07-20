from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.db import connection
from django.db.models import F, Sum
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils.translation import ugettext as _
from django.views.generic import ListView, CreateView, UpdateView
from django.forms import modelformset_factory
from django.forms.models import inlineformset_factory

#from jsignature.utils import draw_signature
from crispy_forms.helper import *

from .models import *
from .forms import *
#from accounts.models import *
from customers.models import *

from datetime import *
#import datetime

#nowtime = datetime.time(datetime.now())
#now = datetime.date.today
#now = datetime.now()
now = date.today

# Create your views here.


def index(request):
	schema_name = connection.schema_name
	patients = PatientProfile.objects.filter(username=request.user.username)
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
	patients = get_object_or_404(PatientProfile, username=username)
	profiles = PatientProfile.objects.filter(username=username)
	icnumbers = PatientProfile.objects.filter(username=username).values_list('ic_number', flat=True).first()

	initial = {
		'patient': patients,
		'ic_number': icnumbers,
	}

	if request.method == 'GET':
		form = AdmissionForm(request.GET or None)
		formset = AdmissionFormSet(queryset=Admission.objects.none())
		helper = MyFormSetHelper()

#	if request.method == 'POST':
	elif request.method == 'POST':
#		form = AdmissionForm(request.POST)
#		form = AdmissionForm(request.POST or None, prefix='forma')
		formset = AdmissionFormSet(request.POST)
#		formset = AdmissionFormSet(request.POST or None, prefix='formb')
#		formset = AdmissionFormSet(request.POST or None, queryset=None)
		formset = AdmissionFormSet(request.POST)
		helper = MyFormSetHelper()

#		if form.is_valid():
		if form.is_valid() and formset.is_valid():
#			profile = form.save(commit=False)
#			profile.patient = form.cleaned_data['patient']
#			profile.birth_date = form.cleaned_data['birth_date']
#			delta = datetime.now().date() - profile.birth_date
#			int((datetime.now().date() - self.birth_date).days / 365.25)
#			profile.age = delta
#			print(delta.days)
#			profile.save()
			admissionform = form.save()

			for form in formset:
				profile = form.save(commit=False)
				profile.ec_name = admissionform
				profile.ec_ic_number = admissionform
				profile.ec_relationship = admissionform
				profile.ec_phone = admissionform
				profile.ec_address = admissionform
				profile.save()

			messages.success(request, _(page_title + ' form has been save successfully.'))
			return redirect('patient_data:patientdata_detail', username=patients.username)
		else:
			messages.warning(request, form.errors)
			messages.warning(request, formset.errors)
	else:
		form = AdmissionForm(initial=initial)
#		form = AdmissionForm(initial=initial, prefix='forma')
#		formset = AdmissionFormSet(queryset=None)
		formset = AdmissionFormSet()
#		formset = AdmissionFormSet(initial=initial, prefix='formb')
		helper = MyFormSetHelper()

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
		'icnumbers': icnumbers,
		'form': form,
		'formset': formset,
#		'helper': helper,
	}

	return render(request, 'patient_form/admission_form.html', context)


@login_required
def application_homeleave(request, username):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Application For Home Leave')
	patients = get_object_or_404(PatientProfile, username=username)
	profiles = PatientProfile.objects.filter(username=username)
	icnumbers = PatientProfile.objects.filter(username=username).values_list('ic_number', flat=True).first()

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
#			form.save()

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
	patients = get_object_or_404(PatientProfile, username=username)
	profiles = PatientProfile.objects.filter(username=username)
	icnumbers = PatientProfile.objects.filter(username=username).values_list('ic_number', flat=True).first()

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
	patients = get_object_or_404(PatientProfile, username=username)
	profiles = PatientProfile.objects.filter(username=username)
	icnumbers = PatientProfile.objects.filter(username=username).values_list('ic_number', flat=True).first()

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
	patients = get_object_or_404(PatientProfile, username=username)
	profiles = PatientProfile.objects.filter(username=username)
	icnumbers = PatientProfile.objects.filter(username=username).values_list('ic_number', flat=True).first()

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
	patients = get_object_or_404(PatientProfile, username=username)
	profiles = PatientProfile.objects.filter(username=username)
	icnumbers = PatientProfile.objects.filter(username=username).values_list('ic_number', flat=True).first()

	initial = {
		'patient': patients,
		'ic_number': icnumbers,
	}

	if request.method == 'POST':
		form = DressingForm(request.POST, request.FILES)
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
	patients = get_object_or_404(PatientProfile, username=username)
	profiles = PatientProfile.objects.filter(username=username)
	icnumbers = PatientProfile.objects.filter(username=username).values_list('ic_number', flat=True).first()

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
	patients = get_object_or_404(PatientProfile, username=username)
	profiles = PatientProfile.objects.filter(username=username)
	icnumbers = PatientProfile.objects.filter(username=username).values_list('ic_number', flat=True).first()

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
	profiles = PatientProfile.objects.filter(username=username)
	patients = get_object_or_404(PatientProfile, username=username)
	icnumbers = PatientProfile.objects.filter(username=username).values_list('ic_number', flat=True).first()

	initial = {
		'patient': patients,
		'ic_number': icnumbers,
	}
	if request.method == 'POST':
		form = IntakeOutputChartForm(request.POST or None)
		if form.is_valid():
			form.save()

			messages.success(request, _(page_title + ' form has been save successfully.'))
			return redirect('patient_data:patientdata_detail', username=patients.username)
		else:
			messages.warning(request, form.errors)
	else:
		form = IntakeOutputChartForm(initial=initial)

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
		'icnumbers': icnumbers,
		'form': form,
	}

	return render(request, 'patient_form/intake_output_form.html', context)


@login_required
def maintainance(request, username):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Maintainance Form')
	patients = get_object_or_404(PatientProfile, username=username)
	profiles = PatientProfile.objects.filter(username=username)
	icnumbers = PatientProfile.objects.filter(username=username).values_list('ic_number', flat=True).first()

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
	patients = get_object_or_404(PatientProfile, username=username)
	profiles = PatientProfile.objects.filter(username=username)
	icnumbers = PatientProfile.objects.filter(username=username).values_list('ic_number', flat=True).first()

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
	patientid = PatientProfile.objects.get(username=username).id
	patients = get_object_or_404(PatientProfile, username=username)
	profiles = PatientProfile.objects.filter(username=username)
	icnumbers = PatientProfile.objects.filter(username=username).values_list('ic_number', flat=True).first()
	allergies = MedicationAdministrationRecord.objects.filter(patient=patientid).values_list('allergy', flat=True).first()

	initial = {
		'patient': patients,
		'ic_number': icnumbers,
		'allergy': allergies,
	}

	if request.method == 'GET':
		form = MedicationAdministrationRecordForm(request.GET or None)
		formset = MedicationAdministrationRecordFormSet(queryset=MedicationAdministrationRecord.objects.none())

	elif request.method == 'POST':
		form = MedicationAdministrationRecordForm(request.POST)
		formset = MedicationAdministrationRecordFormSet(request.POST)

		if form.is_valid() and formset.is_valid():
			medicationadministrationform = form.save()

			for form in formset:
				profile = form.save(commit=False)
				profile.medication_name = medicationadministrationform
				profile.medication_dosage = medicationadministrationform
				profile.medication_tab = medicationadministrationform
				profile.medication_frequency = medicationadministrationform
				profile.medication_route = medicationadministrationform
				profile.save()

			messages.success(request, _(page_title + ' form has been save successfully.'))
			return redirect('patient_data:patientdata_detail', username=patients.username)
		else:
			messages.warning(request, form.errors)
	else:
		form = MedicationAdministrationRecordForm(initial=initial)
		formset = MedicationAdministrationRecordFormSet()

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

	return render(request, 'patient_form/medication_administration_form.html', context)


@login_required
def miscellaneous_charges_slip(request, username):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Miscellaneous Charges Slip')
	patients = get_object_or_404(PatientProfile, username=username)
	profiles = PatientProfile.objects.filter(username=username)
	icnumbers = PatientProfile.objects.filter(username=username).values_list('ic_number', flat=True).first()

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
	patients = get_object_or_404(PatientProfile, username=username)
	profiles = PatientProfile.objects.filter(username=username)
	icnumbers = PatientProfile.objects.filter(username=username).values_list('ic_number', flat=True).first()

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
	patients = get_object_or_404(PatientProfile, username=username)
	profiles = PatientProfile.objects.filter(username=username)
	icnumbers = PatientProfile.objects.filter(username=username).values_list('ic_number', flat=True).first()
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
	patients = get_object_or_404(PatientProfile, username=username)
	profiles = PatientProfile.objects.filter(username=username)
	icnumbers = PatientProfile.objects.filter(username=username).values_list('ic_number', flat=True).first()

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
	patients = get_object_or_404(PatientProfile, username=username)
	profiles = PatientProfile.objects.filter(username=username)
	icnumbers = PatientProfile.objects.filter(username=username).values_list('ic_number', flat=True).first()

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
	patients = get_object_or_404(PatientProfile, username=username)
	profiles = PatientProfile.objects.filter(username=username)
	icnumbers = PatientProfile.objects.filter(username=username).values_list('ic_number', flat=True).first()

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
	patients = get_object_or_404(PatientProfile, username=username)
	profiles = PatientProfile.objects.filter(username=username)
	icnumbers = PatientProfile.objects.filter(username=username).values_list('ic_number', flat=True).first()

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
	patients = get_object_or_404(PatientProfile, username=username)
	profiles = PatientProfile.objects.filter(username=username)
	icnumbers = PatientProfile.objects.filter(username=username).values_list('ic_number', flat=True).first()

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
	patients = get_object_or_404(PatientProfile, username=username)
	profiles = PatientProfile.objects.filter(username=username)
	icnumbers = PatientProfile.objects.filter(username=username).values_list('ic_number', flat=True).first()

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
