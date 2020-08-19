from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.utils.translation import ugettext as _

from .models import *
from accounts.models import *
from customers.models import *

# Create your views here.

@login_required
def patientdata_list(request):
	schema_name = connection.schema_name
	patients = UserProfile.objects.filter(username=request.user.username)
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Patient List')

	if request.user.is_superuser or request.user.is_staff:
		datastaff = UserProfile.objects.filter(is_patient=True).order_by("id")
		print("datastaff1: ", datastaff)
#		q = Q()
#		for item in city_list:
#			q = q | Q(address__city__icontains=city)
#		fullname_data = datastaff.values_list('id', flat=True)
#		datapatients = Admission.objects.filter(patient__in=fullname_data).order_by('patient')
#		datapatients = UserProfile.objects.filter(username=request.user.username)
#		datapatients = Admission.objects.all()
#		results = chain(datapatients, datastaff)

	if request.user.is_patient:
		datastaff = UserProfile.objects.filter(full_name=request.user).order_by("id")
#		datapatients = Admission.objects.filter(patient__in=datastaff)
		print("datastaff2: ", datastaff)

	context = {
		'patients': patients,
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		"datastaff": datastaff,
	}

	return render(request, 'patient/patient_list.html', context)


@login_required
def patientdata_detail(request, username):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	patients = UserProfile.objects.filter(username=username)
#	patients = UserProfile.objects.filter(patient=id)
#	patients = UserProfile.objects.filter(pk=id).values_list('patient', flat=True).first()
	page_title = _('Patient Detail')
	icnumbers = Admission.objects.filter(patient=request.user)

	context = {
		'titles': titles,
		'logos': logos,
		'page_title': page_title,
		"patients": patients,
		"icnumbers": icnumbers,
	}

	return render(request, 'patient/patient_detail.html', context)


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
	return render(request, 'patient/dropdown_list.html', context)

