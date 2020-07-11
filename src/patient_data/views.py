from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.db import connection
from django.db.models import Count, Sum, F, Q
from django.db.models.functions import Trunc
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.translation import ugettext as _
from django.views.generic import ListView

from patient_form.models import *
from accounts.models import *
from customers.models import *

#import datetime
from datetime import *

startdate = date.today()
enddate = startdate + timedelta(days=1)

start_time_day = datetime.strptime('00:00', '%H:%M').time()
end_time_day = datetime.strptime('12:00', '%H:%M').time()
start_time_night = datetime.strptime('12:01', '%H:%M').time()
end_time_night = datetime.strptime('23:59', '%H:%M').time()


# Create your views here.
@login_required
def patientdata_list(request):
	schema_name = connection.schema_name
	patients = PatientProfile.objects.filter(username=request.user.username)
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Patient List')
#	patient_data = Appointment.objects.filter(patient=id)
#	table = PatientProfileTable(PatientProfile.objects.all())
	if request.user.is_superuser:
		tables = PatientProfile.objects.all()
	else:
		tables = PatientProfile.objects.filter(full_name=request.user)

	context = {
		'patients': patients,
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
#		'patients': patients,
		"tables": tables,
	}

	return render(request, 'patient_data/patient_list.html', context)


@login_required
def patientdata_detail(request, id):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	patients = PatientProfile.objects.filter(pk=id)
#	patients = PatientProfile.objects.filter(patient=id)
#	patients = PatientProfile.objects.filter(pk=id).values_list('patient', flat=True).first()
	page_title = _('Patient Detail')
	icnumbers = Admission.objects.filter(patient=request.user)

	context = {
		'titles': titles,
		'logos': logos,
		'page_title': page_title,
		"patients": patients,
		"icnumbers": icnumbers,
	}

	return render(request, 'patient_data/patient_detail.html', context)


@login_required
def admission_data(request, id):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Admission Form')
	patients = Admission.objects.filter(patient=id)
	profiles = PatientProfile.objects.filter(pk=id)

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
	}

	return render(request, 'patient_data/admission_data.html', context)


@login_required
def homeleave_data(request, id):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Application For Home Leave')
	patients = ApplicationForHomeLeave.objects.filter(patient=id)
	profiles = PatientProfile.objects.filter(pk=id)

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
	}

	return render(request, 'patient_data/homeleave_data.html', context)


@login_required
def appointment_data(request, id):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Appointment Data')
	patients = Appointment.objects.filter(patient=id)
	profiles = PatientProfile.objects.filter(pk=id)
	event_date = Appointment.objects.filter(patient=id).values_list('date', flat=True)
#	event_time = Appointment.objects.filter(patient=id).values_list('time', flat=True)
	timenow = datetime.time(datetime.now())
	event_time = Appointment.objects.filter(patient=id, time='12:59')

	print("event_date: ", event_date)
	print("event_time: ", event_time)

	today = date.today()
#	difference = today - event_date
#	event_date_new = event_date + difference


	if event_date == today:
		messages.warning(request, form.errors)

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
	}

	return render(request, 'patient_data/appointment_data.html', context)


@login_required
def cannulation_data(request, id):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Catheterization and Cannulation Chart')
	patients = CatheterizationCannulation.objects.filter(patient=id)
	profiles = PatientProfile.objects.filter(pk=id)

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
	}

	return render(request, 'patient_data/cannulation_data.html', context)


@login_required
def charges_sheet_data(request, id):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Charges Sheet')
	patients = Charges.objects.filter(patient=id)
	profiles = PatientProfile.objects.filter(pk=id)

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
	}

	return render(request, 'patient_data/charges_sheet_data.html', context)


@login_required
def dressing_data(request, id):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Dressing Chart')
	patients = Dressing.objects.filter(patient=id)
	profiles = PatientProfile.objects.filter(pk=id)

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
	}

	return render(request, 'patient_data/dressing_data.html', context)


@login_required
def enteral_feeding_regime_data(request, id):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Enteral Feeding Regime')
	patients = EnteralFeedingRegime.objects.filter(patient=id)
	total = EnteralFeedingRegime.objects.aggregate(Sum('amount'))
	profiles = PatientProfile.objects.filter(pk=id)
	total_feeding = EnteralFeedingRegime.objects.aggregate(Sum('amount'))
	total_fluids = EnteralFeedingRegime.objects.filter(patient=id).values_list('total_fluids', flat=True).first()
	all_total_fluids = EnteralFeedingRegime.objects.aggregate(Sum('total_fluids'))

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
		'total': total,
		'total_feeding': total_feeding,
		'total_fluids': total_fluids,
		'all_total_fluids': all_total_fluids,
	}

	return render(request, 'patient_data/enteral_feeding_regime_data.html', context)


@login_required
def hgt_chart_data(request, id):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('HGT Chart')
	patients = HGTChart.objects.filter(patient=id)
	profiles = PatientProfile.objects.filter(pk=id)

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
	}

	return render(request, 'patient_data/hgt_chart_data.html', context)


@login_required
def intake_output_data(request, id):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Intake Output Chart')
	patients = IntakeOutputChart.objects.filter(patient=id)
	profiles = PatientProfile.objects.filter(pk=id)

	total_oral_day = IntakeOutputChart.objects.filter(patient=id, date__range=[startdate, enddate], time_intake__range=(start_time_day, end_time_day)).aggregate(Sum('intake_oral_ml'))
	total_parental_day = IntakeOutputChart.objects.filter(patient=id, date__range=[startdate, enddate], time_intake__range=(start_time_day, end_time_day)).aggregate(Sum('intake_parenteral_ml'))
	total_other_intake_day = IntakeOutputChart.objects.filter(patient=id, date__range=[startdate, enddate], time_intake__range=(start_time_day, end_time_day)).aggregate(Sum('intake_other_ml'))
	total_cum_day = IntakeOutputChart.objects.filter(patient=id, date__range=[startdate, enddate], time_intake__range=(start_time_day, end_time_day)).aggregate(Sum('output_urine_cum'))
	total_gastric_day = IntakeOutputChart.objects.filter(patient=id, date__range=[startdate, enddate], time_intake__range=(start_time_day, end_time_day)).aggregate(Sum('output_gastric_ml'))
	total_other_output_day = IntakeOutputChart.objects.filter(patient=id, date__range=[startdate, enddate], time_intake__range=(start_time_day, end_time_day)).aggregate(Sum('output_other_ml'))

	total_oral_night = IntakeOutputChart.objects.filter(patient=id, date__range=[startdate, enddate], time_intake__range=(start_time_night, end_time_night)).aggregate(Sum('intake_oral_ml'))
	total_parental_night = IntakeOutputChart.objects.filter(patient=id, date__range=[startdate, enddate], time_intake__range=(start_time_night, end_time_night)).aggregate(Sum('intake_parenteral_ml'))
	total_other_intake_night = IntakeOutputChart.objects.filter(patient=id, date__range=[startdate, enddate], time_intake__range=(start_time_night, end_time_night)).aggregate(Sum('intake_other_ml'))
	total_cum_night = IntakeOutputChart.objects.filter(patient=id, date__range=[startdate, enddate], time_intake__range=(start_time_night, end_time_night)).aggregate(Sum('output_urine_cum'))
	total_gastric_night = IntakeOutputChart.objects.filter(patient=id, date__range=[startdate, enddate], time_intake__range=(start_time_night, end_time_night)).aggregate(Sum('output_gastric_ml'))
	total_other_output_night = IntakeOutputChart.objects.filter(patient=id, date__range=[startdate, enddate], time_intake__range=(start_time_night, end_time_night)).aggregate(Sum('output_other_ml'))

	total_oral = IntakeOutputChart.objects.filter(patient=id).aggregate(Sum('intake_oral_ml'))
	total_parental = IntakeOutputChart.objects.filter(patient=id).aggregate(Sum('intake_parenteral_ml'))
	total_other_intake = IntakeOutputChart.objects.filter(patient=id,).aggregate(Sum('intake_other_ml'))

	agg_data = IntakeOutputChart.objects.aggregate(total_source1=Count('intake_oral_ml'), total_source2=Count('intake_parenteral_ml'), total_source3=Count('intake_other_ml'))
	total_count = sum(agg_data.values())
	res = IntakeOutputChart.objects.all().annotate(total_source1=Count('intake_oral_ml'), total_source2=Count('intake_parenteral_ml'), total_source3=Count('intake_other_ml')).annotate(total_count=F('total_source1') + F('total_source2') + F('total_source3')).order_by('-total_count')

#	total_intake = total_oral+total_parental+total_other_intake

#	total_intake = IntakeOutputChart.objects.all().aggregate(Sum(F('output_urine_cum') + F('output_gastric_ml') + F('output_other_ml'))

	total_intake = IntakeOutputChart.objects.filter(patient=id).annotate(Count('output_urine_cum')).annotate(Count('output_gastric_ml')).annotate(Count('output_other_ml'))
#	total_output = total_cum+total_gastric+total_other_output

#	total_balance = total_intake + total_output

	time_range_day = IntakeOutputChart.objects.filter(patient=id, time_intake__range=(start_time_day, end_time_day))
	time_range_night = IntakeOutputChart.objects.filter(patient=id, time_intake__range=(start_time_night, end_time_night))

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,

		'total_oral_day': total_oral_day,
		'total_parental_day': total_parental_day,
		'total_other_intake_day': total_other_intake_day,
		'total_cum_day': total_cum_day,
		'total_gastric_day': total_gastric_day,
		'total_other_output_day': total_other_output_day,

		'total_oral_night': total_oral_night,
		'total_parental_night': total_parental_night,
		'total_other_intake_night': total_other_intake_night,
		'total_cum_night': total_cum_night,
		'total_gastric_night': total_gastric_night,
		'total_other_output_night': total_other_output_night,

		'total_intake': total_intake,
#		'total_parental': total_parental,

#		'total_intake': total_intake,
#		'total_output': total_output,
#		'total_balance': total_balance,

		'time_range_day': time_range_day,
		'time_range_night': time_range_night,
	}

	return render(request, 'patient_data/intake_output_data.html', context)


@login_required
def maintainance_data(request, id):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Maintainance Form')
	patients = Maintainance.objects.filter(patient=id)
	profiles = PatientProfile.objects.filter(pk=id)

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
	}

	return render(request, 'patient_data/maintainance_data.html', context)


@login_required
def medication_data(request, id):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Medication Records')
	patients = MedicationRecord.objects.filter(patient=id)
	profiles = PatientProfile.objects.filter(pk=id)

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
	}

	return render(request, 'patient_data/medication_data.html', context)


@login_required
def medication_administration_data(request, id):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Medication Administration Record')
	patients = MedicationAdministrationRecord.objects.filter(patient=id)
	profiles = PatientProfile.objects.filter(pk=id)
	allergies = MedicationAdministrationRecord.objects.filter(patient=id).values_list('allergy', flat=True).first()

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
		'allergies': allergies,
	}

	return render(request, 'patient_data/medication_administration_data.html', context)


@login_required
def miscellaneous_charges_slip(request, id):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Miscellaneous Charges Slip')
	patients = MiscellaneousChargesSlip.objects.filter(patient=id)
	profiles = PatientProfile.objects.filter(pk=id)

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
	}

	return render(request, 'patient_data/miscellaneouschargesslip_data.html', context)


@login_required
def nursing_data(request, id):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Nursing Report')
	patients = Nursing.objects.filter(patient=id)
	profiles = PatientProfile.objects.filter(pk=id)

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
	}

	return render(request, 'patient_data/nursing_data.html', context)


@login_required
def overtime_claim(request, id):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Overtime Claim Form')
	patients = OvertimeClaim.objects.filter(patient=id)
	profiles = PatientProfile.objects.filter(pk=id)
#	durations = OvertimeClaim.objects.filter(patient=id).order_by('duration_time').values_list('duration_time', flat=True).first()
#	durations = datetime.time(h, m, s)
#	model.time_field = t

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
#		'durations': durations,
	}

	return render(request, 'patient_data/overtime_claim_data.html', context)


@login_required
def physio_progress_note_data(request, id):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Physiotherapy Progress Note')
	patients = PhysioProgressNote.objects.filter(patient=id)
	profiles = PatientProfile.objects.filter(pk=id)

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
	}

	return render(request, 'patient_data/physio_progress_note_data.html', context)


@login_required
def physiotherapy_general_assessment_data(request, id):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Physiotherapy General Assessment Form')
	patients = PhysiotherapyGeneralAssessment.objects.filter(patient=id)
	profiles = PatientProfile.objects.filter(pk=id)

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
	}

	return render(request, 'patient_data/physiotherapy_general_assessment_data.html', context)


@login_required
def staff_records(request, id):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Staff Records')
	patients = StaffRecords.objects.filter(patient=id)
	profiles = PatientProfile.objects.filter(pk=id)
	total_annual = StaffRecords.objects.filter(patient=id).aggregate(Sum('annual_leave_days'))
	total_public = StaffRecords.objects.filter(patient=id,).aggregate(Sum('public_holiday_days'))

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
		'total_annual': total_annual,
		'total_public': total_public,
	}

	return render(request, 'patient_data/staff_records_data.html', context)


@login_required
def stool_data(request, id):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Stool Chart')
	patients = Stool.objects.filter(patient=id)
	profiles = PatientProfile.objects.filter(pk=id)

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
	}

	return render(request, 'patient_data/stool_data.html', context)


@login_required
def visiting_consultant_records(request, id):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Visiting Consultant Records')
	patients = VisitingConsultant.objects.filter(patient=id)
	profiles = PatientProfile.objects.filter(pk=id)

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
	}

	return render(request, 'patient_data/visiting_consultant_records_data.html', context)


@login_required
def vital_sign_flow_data(request, id):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Vital Sign Flow Sheet')
	patients = VitalSignFlow.objects.filter(patient=id)
	profiles = PatientProfile.objects.filter(pk=id)

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
	}

	return render(request, 'patient_data/vital_sign_flow_data.html', context)
