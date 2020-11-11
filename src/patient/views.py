from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.utils.translation import ugettext as _

from accounts.models import *
from customers.models import *
from .models import *

import datetime

get_today = datetime.date.today()
enddate = get_today + datetime.timedelta(days=1)

start_time_day = datetime.datetime.strptime('00:00', '%H:%M').time()
end_time_day = datetime.datetime.strptime('12:00', '%H:%M').time()
start_time_night = datetime.datetime.strptime('12:01', '%H:%M').time()
end_time_night = datetime.datetime.strptime('23:59', '%H:%M').time()


# Create your views here.
def load_ic_number(request):
	fullname_data = request.GET.get('full_name')
	familyname_data = request.GET.get('ec_name')
	fullname_results = UserProfile.objects.filter(full_name=fullname_data).order_by('full_name')
	familyname_results = Family.objects.filter(ec_name=familyname_data).order_by('ec_name')

	context = {
		'fullname_results': fullname_results,
		'familyname_results': familyname_results,
	}
	return render(request, 'patient/dropdown_list_icnumber.html', context)


def load_relationship(request):
	fullname_data = request.GET.get('full_name')
	familyname_data = request.GET.get('ec_name')
	fullname_results = UserProfile.objects.filter(full_name=fullname_data).order_by('full_name')
	familyname_results = Family.objects.filter(ec_name=familyname_data).order_by('ec_name')
	familyrelationship_results = Family.objects.filter(ec_name=familyname_data).values_list('ec_relationship', flat=True).first()

	context = {
		'fullname_results': fullname_results,
		'familyname_results': familyname_results,
		'familyrelationship_results': familyrelationship_results,
	}
	return render(request, 'patient/dropdown_list_relationship.html', context)


def load_signature(request):
	fullname_data = request.GET.get('full_name')
	familyname_data = request.GET.get('ec_name')
	fullname_results = UserProfile.objects.filter(full_name=fullname_data).order_by('full_name')
	familyname_results = Family.objects.filter(ec_name=familyname_data).order_by('ec_name')
	signature_results = Family.objects.filter(ec_name=familyname_data).values_list('ec_name', flat=True).first()

	context = {
		'fullname_results': fullname_results,
		'familyname_results': familyname_results,
		'signature_results': signature_results,
	}
	return render(request, 'patient/dropdown_list_signature.html', context)


def load_phone(request):
	fullname_data = request.GET.get('full_name')
	familyname_data = request.GET.get('ec_name')
	fullname_results = UserProfile.objects.filter(full_name=fullname_data).order_by('full_name')
	familyname_results = Family.objects.filter(ec_name=familyname_data).order_by('ec_name')
	family_phone_results = Family.objects.filter(ec_name=familyname_data).values_list('ec_phone', flat=True).first()

	context = {
		'fullname_results': fullname_results,
		'familyname_results': familyname_results,
		'family_phone_results': family_phone_results,
	}
	return render(request, 'patient/dropdown_list_phone.html', context)


@login_required
def patientdata_list(request):
	schema_name = connection.schema_name
	patients = UserProfile.objects.filter(username=request.user.username)
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Patient List')

#	if request.user.is_superuser or request.user.is_staff:
	datastaff = UserProfile.objects.filter(is_patient=True).order_by("id")

#	if request.user.is_patient:
#		datastaff = UserProfile.objects.filter(full_name=request.user).order_by("id")

	context = {
		'patients': patients,
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'datastaff': datastaff,
	}

	return render(request, 'patient/patient_list.html', context)


@login_required
def patientdata_detail(request, username):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	patients = UserProfile.objects.filter(username=username)
	patientid = UserProfile.objects.filter(username=username).values_list('id', flat=True).first()
	page_title = _('Patient Detail')
	icnumbers = Admission.objects.filter(patient=request.user)
	admission = Admission.objects.filter(patient=patientid).exclude(date_admission__isnull=True)
	application_home_leave = ApplicationForHomeLeave.objects.filter(patient=patientid)
	appointment = Appointment.objects.filter(patient=patientid)
	cannula = Cannula.objects.filter(patient=patientid)
	dischargechecklist = DischargeCheckList.objects.filter(patient=patientid).exclude(medication_reconcilation_patient__isnull=True)
	dressing = Dressing.objects.filter(patient=patientid)
	enteralfeedingregime = EnteralFeedingRegime.objects.filter(patient=patientid).exclude(time__isnull=True)
	hgt = HGT.objects.filter(patient=patientid)
	intakeoutput = IntakeOutput.objects.filter(patient=patientid).exclude(time__isnull=True)
	investigation_report = InvestigationReport.objects.filter(patient=patientid)
	maintenance = Maintenance.objects.filter(patient=patientid)
	medicationadministrationrecord = MedicationAdministrationRecord.objects.filter(patient=patientid).exclude(medication_template__medication_time__isnull=True)
	medicationtemplate = MedicationAdministrationRecordTemplate.objects.filter(patient=patientid).exclude(medication_time__isnull=True)
	medicationrecord = MedicationRecord.objects.filter(patient=patientid)
	multipurpose = Multipurpose.objects.filter(patient=patientid)
	miscellaneouschargesslip = MiscellaneousChargesSlip.objects.filter(patient=patientid)
	nasogastric = Nasogastric.objects.filter(patient=patientid)
	nursing = Nursing.objects.filter(patient=patientid)
	physioprogressnotesheet = PhysioProgressNoteSheet.objects.filter(patient=patientid)
	physiotherapygeneralassessment = PhysiotherapyGeneralAssessment.objects.filter(patient=patientid)
	stool = Stool.objects.filter(patient=patientid)
	urinary = Urinary.objects.filter(patient=patientid)
	vitalsignflow = VitalSignFlow.objects.filter(patient=patientid)
	visitingconsultant = VisitingConsultant.objects.filter(patient=patientid)

	context = {
		'titles': titles,
		'logos': logos,
		'page_title': page_title,
		"patients": patients,
		"icnumbers": icnumbers,
		'admission': admission,
		'application_home_leave': application_home_leave,
		'appointment': appointment,
		'cannula': cannula,
		'dressing': dressing,
		'dischargechecklist': dischargechecklist,
		'enteralfeedingregime': enteralfeedingregime,
		'hgt': hgt,
		'intakeoutput': intakeoutput,
		'investigation_report': investigation_report,
		'maintenance': maintenance,
		'medicationadministrationrecord': medicationadministrationrecord,
		'medicationtemplate': medicationtemplate,
		'medicationrecord': medicationrecord,
		'multipurpose': multipurpose,
		'miscellaneouschargesslip': miscellaneouschargesslip,
		'nasogastric': nasogastric,
		'nursing': nursing,
		'physioprogressnotesheet': physioprogressnotesheet,
		'physiotherapygeneralassessment': physiotherapygeneralassessment,
		'stool': stool,
		'urinary': urinary,
		'vitalsignflow': vitalsignflow,
		'visitingconsultant': visitingconsultant,
	}

	return render(request, 'patient/patient_detail.html', context)
