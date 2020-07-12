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

#from jsignature.utils import draw_signature

from .models import *
from .forms import *
#from accounts.models import *
from customers.models import *

#from datetime import timedelta
import datetime

#nowtime = datetime.time(datetime.now())
now = datetime.date.today

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
def admission(request, id):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Admission Form')
	patients = get_object_or_404(PatientProfile, pk=id)
	profiles = PatientProfile.objects.filter(pk=id)
	icnumbers = PatientProfile.objects.filter(pk=id).values_list('ic_number', flat=True).first()

	initial = {
		'patient': patients,
		'ic_number': icnumbers,
	}

	if request.method == 'POST':
		form = AdmissionForm(request.POST or None)
		
		if form.is_valid():
			form.save()

			messages.success(request, _('Your form has been save successfully.'))
			return redirect('patient_data:patientdata_detail', id=patients.id)
		else:
			messages.warning(request, form.errors)
	else:
		form = AdmissionForm(initial=initial)

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
		'icnumbers': icnumbers,
		'form': form,
	}

	return render(request, 'patient_form/admission_form.html', context)


@login_required
def application_homeleave(request, id):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Application For Home Leave')
	patients = get_object_or_404(PatientProfile, pk=id)
	profiles = PatientProfile.objects.filter(pk=id)
	icnumbers = PatientProfile.objects.filter(pk=id).values_list('ic_number', flat=True).first()

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

			messages.success(request, _('Your form has been save successfully.'))
			return redirect('patient_data:patientdata_detail', id=patients.id)
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
def appointment(request, id):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Appointment Records')
	patients = get_object_or_404(PatientProfile, pk=id)
	profiles = PatientProfile.objects.filter(pk=id)
	icnumbers = PatientProfile.objects.filter(pk=id).values_list('ic_number', flat=True).first()

	initial = {
		'patient': patients,
		'ic_number': icnumbers,
	}

	if request.method == 'POST':
		form = AppointmentForm(request.POST or None)

		if form.is_valid():
			form.save()

			messages.success(request, _('Your form has been save successfully.'))
			return redirect('patient_data:patientdata_detail', id=patients.id)
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
def catheterization_cannulation(request, id):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Catheterization and Cannulation Chart')
	patients = get_object_or_404(PatientProfile, pk=id)
	profiles = PatientProfile.objects.filter(pk=id)
	icnumbers = PatientProfile.objects.filter(pk=id).values_list('ic_number', flat=True).first()

	initial = {
		'patient': patients,
		'ic_number': icnumbers,
	}


	if request.method == 'POST':
		form = CannulationForm(request.POST or None)
		if form.is_valid():
			form.save()

			messages.success(request, _('Your form has been save successfully.'))
			return redirect('patient_data:patientdata_detail', id=patients.id)
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
def charges_sheet(request, id):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Charges Sheet')
	patients = get_object_or_404(PatientProfile, pk=id)
	profiles = PatientProfile.objects.filter(pk=id)
	icnumbers = PatientProfile.objects.filter(pk=id).values_list('ic_number', flat=True).first()

	initial = {
		'patient': patients,
		'ic_number': icnumbers,
	}


	if request.method == 'POST':
		form = ChargesForm(request.POST or None)
		if form.is_valid():
			form.save()

			messages.success(request, _('Your form has been save successfully.'))
			return redirect('patient_data:patientdata_detail', id=patients.id)
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
def dressing(request, id):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Dressing Chart')
	patients = get_object_or_404(PatientProfile, pk=id)
	profiles = PatientProfile.objects.filter(pk=id)
	icnumbers = PatientProfile.objects.filter(pk=id).values_list('ic_number', flat=True).first()

	initial = {
		'patient': patients,
		'ic_number': icnumbers,
	}


	if request.method == 'POST':
		form = DressingForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()

			messages.success(request, _('Your form has been save successfully.'))
			return redirect('patient_data:patientdata_detail', id=patients.id)
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
def enteral_feeding_regime(request, id):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Enteral Feeding Regime')
#	total_flush = EnteralFeedingRegime.objects.all().annotate(total_food=F('warm_water_before ') + F('warm_water_after'))
#    total = EnteralFeedingRegime.objects.aggregate(total_population=Sum('amount'))
	patients = get_object_or_404(PatientProfile, pk=id)
	profiles = PatientProfile.objects.filter(pk=id)
	icnumbers = PatientProfile.objects.filter(pk=id).values_list('ic_number', flat=True).first()

	initial = {
		'patient': patients,
		'ic_number': icnumbers,
	}


	if request.method == 'POST':
		form = EnteralFeedingRegimeForm(request.POST or None)
		if form.is_valid():
			form.save()

			messages.success(request, _('Your form has been save successfully.'))
			return redirect('patient_data:patientdata_detail', id=patients.id)
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
def hgt_chart(request, id):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('HGT Chart')
	patients = get_object_or_404(PatientProfile, pk=id)
	profiles = PatientProfile.objects.filter(pk=id)
	icnumbers = PatientProfile.objects.filter(pk=id).values_list('ic_number', flat=True).first()

	initial = {
		'patient': patients,
		'ic_number': icnumbers,
	}


	if request.method == 'POST':
		form = HGTChartForm(request.POST or None)
		if form.is_valid():
			form.save()

			messages.success(request, _('Your form has been save successfully.'))
			return redirect('patient_data:patientdata_detail', id=patients.id)
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
def intake_output(request, id):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Intake Output Chart')
	profiles = PatientProfile.objects.filter(pk=id)
	patients = get_object_or_404(PatientProfile, pk=id)
	icnumbers = PatientProfile.objects.filter(pk=id).values_list('ic_number', flat=True).first()

	initial = {
		'patient': patients,
		'ic_number': icnumbers,
	}
	if request.method == 'POST':
		form = IntakeOutputChartForm(request.POST or None)
		if form.is_valid():
			form.save()

			messages.success(request, _('Your form has been save successfully.'))
			return redirect('patient_data:patientdata_detail', id=patients.id)
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
def maintainance(request, id):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Maintainance Form')
	patients = get_object_or_404(PatientProfile, pk=id)
	profiles = PatientProfile.objects.filter(pk=id)
	icnumbers = PatientProfile.objects.filter(pk=id).values_list('ic_number', flat=True).first()

	initial = {
		'patient': patients,
		'ic_number': icnumbers,
	}


	if request.method == 'POST':
		form = MaintainanceForm(request.POST or None)
		if form.is_valid():
			form.save()

			messages.success(request, _('Your form has been save successfully.'))
			return redirect('patient_data:patientdata_detail', id=patients.id)
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
def medication_record(request, id):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Medication Records')
	patients = get_object_or_404(PatientProfile, pk=id)
	profiles = PatientProfile.objects.filter(pk=id)
	icnumbers = PatientProfile.objects.filter(pk=id).values_list('ic_number', flat=True).first()

	initial = {
		'patient': patients,
		'ic_number': icnumbers,
	}


	if request.method == 'POST':
		form = MedicationRecordForm(request.POST or None)
		if form.is_valid():
			form.save()

			messages.success(request, _('Your form has been save successfully.'))
			return redirect('patient_data:patientdata_detail', id=patients.id)
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
def medication_administration(request, id):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Medication Administration Record')
	patients = get_object_or_404(PatientProfile, pk=id)
	profiles = PatientProfile.objects.filter(pk=id)
	icnumbers = PatientProfile.objects.filter(pk=id).values_list('ic_number', flat=True).first()
	allergies = MedicationAdministrationRecord.objects.filter(pk=id).values_list('allergy', flat=True).first()

	initial = {
		'patient': patients,
		'ic_number': icnumbers,
		'allergy': allergies,
	}


	if request.method == 'POST':
		form = MedicationAdministrationRecordForm(request.POST or None)
		if form.is_valid():
			form.save()

			messages.success(request, _('Your form has been save successfully.'))
			return redirect('patient_data:patientdata_detail', id=patients.id)
		else:
			messages.warning(request, form.errors)
	else:
		form = MedicationAdministrationRecordForm(initial=initial)

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
		'icnumbers': icnumbers,
		'form': form,
	}

	return render(request, 'patient_form/medication_administration_form.html', context)


@login_required
def miscellaneous_charges_slip(request, id):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Miscellaneous Charges Slip')
	patients = get_object_or_404(PatientProfile, pk=id)
	profiles = PatientProfile.objects.filter(pk=id)
	icnumbers = PatientProfile.objects.filter(pk=id).values_list('ic_number', flat=True).first()

	initial = {
		'patient': patients,
		'ic_number': icnumbers,
	}


	if request.method == 'POST':
		form = MiscellaneousChargesSlipForm(request.POST or None)
		if form.is_valid():
			form.save()

			messages.success(request, _('Your form has been save successfully.'))
			return redirect('patient_data:patientdata_detail', id=patients.id)
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

	return render(request, 'patient_form/miscellaneouschargesslip_form.html', context)


@login_required
def nursing(request, id):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Nursing Report')
	patients = get_object_or_404(PatientProfile, pk=id)
	profiles = PatientProfile.objects.filter(pk=id)
	icnumbers = PatientProfile.objects.filter(pk=id).values_list('ic_number', flat=True).first()

	initial = {
		'patient': patients,
		'ic_number': icnumbers,
	}


	if request.method == 'POST':
		form = NursingForm(request.POST or None)
		if form.is_valid():
			form.save()

			messages.success(request, _('Your form has been save successfully.'))
			return redirect('patient_data:patientdata_detail', id=patients.id)
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
def overtime_claim(request, id):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Overtime Claim Form')
	patients = get_object_or_404(PatientProfile, pk=id)
	profiles = PatientProfile.objects.filter(pk=id)
	icnumbers = PatientProfile.objects.filter(pk=id).values_list('ic_number', flat=True).first()

	initial = {
		'patient': patients,
		'ic_number': icnumbers,
	}


	if request.method == 'POST':
		form = OvertimeClaimForm(request.POST or None)
		if form.is_valid():
			form.save()

			messages.success(request, _('Your form has been save successfully.'))
			return redirect('patient_data:patientdata_detail', id=patients.id)
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
def physio_progress_note(request, id):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Physiotherapy Progress Note')
	patients = get_object_or_404(PatientProfile, pk=id)
	profiles = PatientProfile.objects.filter(pk=id)
	icnumbers = PatientProfile.objects.filter(pk=id).values_list('ic_number', flat=True).first()

	initial = {
		'patient': patients,
		'ic_number': icnumbers,
	}


	if request.method == 'POST':
		form = PhysioProgressNoteForm(request.POST or None)
		if form.is_valid():
			form.save()

			messages.success(request, _('Your form has been save successfully.'))
			return redirect('patient_data:patientdata_detail', id=patients.id)
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
def physiotherapy_general_assessment(request, id):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Physiotherapy General Assessment Form')
	patients = get_object_or_404(PatientProfile, pk=id)
	profiles = PatientProfile.objects.filter(pk=id)
	icnumbers = PatientProfile.objects.filter(pk=id).values_list('ic_number', flat=True).first()

	initial = {
		'patient': patients,
		'ic_number': icnumbers,
	}


	if request.method == 'POST':
		form = PhysiotherapyGeneralAssessmentForm(request.POST or None)
		if form.is_valid():
			form.save()

			messages.success(request, _('Your form has been save successfully.'))
			return redirect('patient_data:patientdata_detail', id=patients.id)
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
def staff_records(request, id):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Staff Records')
	patients = get_object_or_404(PatientProfile, pk=id)
	profiles = PatientProfile.objects.filter(pk=id)
	icnumbers = PatientProfile.objects.filter(pk=id).values_list('ic_number', flat=True).first()

	initial = {
		'patient': patients,
		'ic_number': icnumbers,
	}


	if request.method == 'POST':
		form = StaffRecordsForm(request.POST or None)
		if form.is_valid():
			form.save()

			messages.success(request, _('Your form has been save successfully.'))
			return redirect('patient_data:patientdata_detail', id=patients.id)
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
def stool(request, id):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Stool Chart')
	patients = get_object_or_404(PatientProfile, pk=id)
	profiles = PatientProfile.objects.filter(pk=id)
	icnumbers = PatientProfile.objects.filter(pk=id).values_list('ic_number', flat=True).first()

	initial = {
		'patient': patients,
		'ic_number': icnumbers,
	}


	if request.method == 'POST':
		form = StoolForm(request.POST or None)
		if form.is_valid():
			form.save()

			messages.success(request, _('Your form has been save successfully.'))
			return redirect('patient_data:patientdata_detail', id=patients.id)
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
def visiting_consultant_records(request, id):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Visiting Consultant Records')
	patients = get_object_or_404(PatientProfile, pk=id)
	profiles = PatientProfile.objects.filter(pk=id)
	icnumbers = PatientProfile.objects.filter(pk=id).values_list('ic_number', flat=True).first()

	initial = {
		'patient': patients,
		'ic_number': icnumbers,
	}


	if request.method == 'POST':
		form = VisitingConsultantForm(request.POST or None)
		if form.is_valid():
			form.save()

			messages.success(request, _('Your form has been save successfully.'))
			return redirect('patient_data:patientdata_detail', id=patients.id)
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
def vital_sign_flow(request, id):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Vital Sign Flow Sheet')
	patients = get_object_or_404(PatientProfile, pk=id)
	profiles = PatientProfile.objects.filter(pk=id)
	icnumbers = PatientProfile.objects.filter(pk=id).values_list('ic_number', flat=True).first()

	initial = {
		'patient': patients,
		'ic_number': icnumbers,
	}


	if request.method == 'POST':
		form = VitalSignFlowForm(request.POST or None)
		if form.is_valid():
			form.save()

			messages.success(request, _('Your form has been save successfully.'))
			return redirect('patient_data:patientdata_detail', id=patients.id)
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
