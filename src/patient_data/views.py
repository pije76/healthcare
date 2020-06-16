from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.db import connection
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.urls import reverse_lazy
from django.utils.translation import ugettext as _
from django.views.generic import ListView
from django.db.models import Sum

from patient_form.models import *
from accounts.models import *
from customers.models import *


# Create your views here.
@login_required
def patientdata_list(request):
	schema_name = connection.schema_name
	patients = PatientProfile.objects.filter(username=request.user.username)
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = 'Patient Data'
#	patient_data = Appointment.objects.all()
#	table = PatientProfileTable(PatientProfile.objects.all())
	tables = PatientProfile.objects.all()

	context = {
		'patients': patients,
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
#		'patient_data': patient_data,
		"tables": tables,
	}
	return render(request, 'patient_data/patient_list.html', context)


@login_required
def patientdata_detail(request, pk):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	patients = PatientProfile.objects.filter(username=request.user.username)
#	patients = PatientProfile.objects.all()
	page_title = patients
	icnumbers = Admission.objects.filter(full_name=request.user)

	context = {
		'titles': titles,
		'logos': logos,
		'page_title': patients,
		"patients": patients,
		"icnumbers": icnumbers,
	}

	return render(request, 'patient_data/patient_detail.html', context)


@login_required
def admission(request):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = 'Admission Form'
	patient_data = Admission.objects.all()

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patient_data': patient_data,
	}

	return render(request, 'patient_data/admission.html', context)


@login_required
def homeleave(request):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = 'Application For Home Leave'
	patient_data = ApplicationForHomeLeave.objects.all()

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patient_data': patient_data,
	}

	return render(request, 'patient_data/homeleave.html', context)


@login_required
def appointment(request):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = 'Appointment Form'
	patient_data = Appointment.objects.all()

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patient_data': patient_data,
	}

	return render(request, 'patient_data/appointment.html', context)


@login_required
def cannulation(request):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = 'Cannulation Chart'
	patient_data = Cannulation.objects.all()

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patient_data': patient_data,
	}

	return render(request, 'patient_data/cannulation.html', context)


@login_required
def charges_sheet(request):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = 'Charges Sheet'
	patient_data = Charges.objects.all()

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patient_data': patient_data,
	}

	return render(request, 'patient_data/charges_sheet.html', context)


@login_required
def dressing(request):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = 'Dressing Chart'
	patient_data = Dressing.objects.all()

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patient_data': patient_data,
	}

	return render(request, 'patient_data/dressing.html', context)


@login_required
def enteral_feeding_regime(request):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = 'Enteral Feeding Regime'
	patient_data = EnteralFeedingRegime.objects.all()
	total = EnteralFeedingRegime.objects.aggregate(Sum('amount'))

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patient_data': patient_data,
		'total': total,
	}

	return render(request, 'patient_data/enteral_feeding_regime.html', context)


@login_required
def hgt_chart(request):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = 'HGT Chart'
	patient_data = Appointment.objects.all()

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patient_data': patient_data,
	}

	return render(request, 'patient_data/hgt_chart.html', context)


@login_required
def intake_output(request):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = 'Intake Output Chart'
	patient_data = Appointment.objects.all()

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patient_data': patient_data,
	}

	return render(request, 'patient_data/intake_output.html', context)


@login_required
def maintainance(request):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = 'Maintainance Form'
	patient_data = Appointment.objects.all()

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patient_data': patient_data,
	}

	return render(request, 'patient_data/maintainance.html', context)


@login_required
def medication(request):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = 'Medication Records'
	patient_data = Appointment.objects.all()

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patient_data': patient_data,
	}

	return render(request, 'patient_data/medication.html', context)


@login_required
def medication_administration(request):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = 'Medication Administration Record'
	patient_data = Appointment.objects.all()

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patient_data': patient_data,
	}

	return render(request, 'patient_data/medication_administration.html', context)


@login_required
def nursing(request):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = 'Nursing Report'
	patient_data = Appointment.objects.all()

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patient_data': patient_data,
	}

	return render(request, 'patient_data/nursing.html', context)


@login_required
def physio_progress_note(request):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = 'Physiotherapy Progress Note'
	patient_data = Appointment.objects.all()

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patient_data': patient_data,
	}

	return render(request, 'patient_data/physio_progress_note.html', context)


@login_required
def physiotherapy_general_assessment(request):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = 'Physiotherapy General Assessment Form'
	patient_data = Appointment.objects.all()

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patient_data': patient_data,
	}

	return render(request, 'patient_data/physiotherapy_general_assessment.html', context)


@login_required
def stool(request):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = 'Stool Chart'
	patient_data = Appointment.objects.all()

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patient_data': patient_data,
	}

	return render(request, 'patient_data/stool.html', context)


@login_required
def vital_sign_flow(request):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = 'Vital Sign Flow Sheet'
	patient_data = Appointment.objects.all()

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patient_data': patient_data,
	}

	return render(request, 'patient_data/vital_sign_flow.html', context)
