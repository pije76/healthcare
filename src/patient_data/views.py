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
from django.views.generic import ListView, TemplateView
from django.http import JsonResponse

from patient_form.models import *
from accounts.models import *
from customers.models import *

#import datetime
from datetime import *
from itertools import chain

startdate = date.today()
enddate = startdate + timedelta(days=1)

start_time_day = datetime.strptime('00:00', '%H:%M').time()
end_time_day = datetime.strptime('12:00', '%H:%M').time()
start_time_night = datetime.strptime('12:01', '%H:%M').time()
end_time_night = datetime.strptime('23:59', '%H:%M').time()


# Create your views here.
class PatientListView(TemplateView):
	template_name = 'patient_data/patient_list.html'

	def get_context_data(self, **kwargs):
		context_data = super().get_context_data(**kwargs)
#		context_data['datapatients'] = UserProfile.objects.all()
		context_data['datapatients'] = Admission.objects.filter(username=request.user.username)
		return context_data

@login_required
def patientdata_list(request):
	schema_name = connection.schema_name
	patients = UserProfile.objects.filter(username=request.user.username)
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Patient List')
	if request.user.is_superuser or request.user.is_staff:
		datastaff = UserProfile.objects.all()
		datapatients = Admission.objects.filter(patient__in=datastaff)

	else:
		datastaff = UserProfile.objects.filter(full_name=request.user, is_patient=True)
		datapatients = Admission.objects.filter(patient__in=datastaff)

	context = {
		'patients': patients,
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		"datapatients": datapatients,
	}

	return render(request, 'patient_data/patient_list.html', context)


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

	return render(request, 'patient_data/patient_detail.html', context)
