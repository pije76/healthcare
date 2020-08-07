from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.shortcuts import render, get_object_or_404
from django.utils.translation import ugettext as _
from django.http import JsonResponse

from patient_form.models import *
from patient_form.forms import *
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


@login_required
def admission_data(request, username):
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

	return render(request, 'patient_data/admission_data/admission_data.html', context)


@login_required
def admission_data_edit(request, id, username):
	data = dict()

	patientid = get_object_or_404(UserProfile, username=username)
	patientname = get_object_or_404(UserProfile, username=username).full_name
	patients = Appointment.objects.filter(patient=patientid)
	admissions = get_object_or_404(Admission, pk=id)

	if request.method == "POST":
		form = AdmissionForm(request.POST or None, instance=admissions)
		if form.is_valid():
			patients = Admission()
			patients = form.save(commit=False)
			patients.patient = request.user
			patients.save()
			data['form_is_valid'] = True
			patients = Admission.objects.all()
			data['html_admission_list'] = render_to_string('patient_data/admission_data/partial_edit.html', {'patients': patients})

		else:
			data['form_is_valid'] = False

		data['html_form'] = render_to_string('patient_data/admission_data/partial_edit.html', {'form': form,}, request=request)
	return JsonResponse(data)

#	else:
	if request.method == "GET":
		form = AdmissionForm(instance=admissions)

	context = {
		'patients': patients,
		'patientname': patientname,
		'patientid': patientid,
		'form': form,
	}
#	return save_admission_data_form(request, context, 'patient_data/admission_data/partial_edit.html')
	return render(request, 'patient_data/admission_data/admission_data.html', context)


@login_required
def admission_data_delete(request, id):
	admissions = get_object_or_404(Admission, pk=id)
	data = dict()

	if request.method == 'POST':
		admissions.delete()
		data['form_is_valid'] = True
		patients = Admission.objects.all()
		data['html_admission_list'] = render_to_string('patient_data/admission_data/admission_data.html', {'patients': patients})
		return JsonResponse(data)
	else:
		context = {'admissions': admissions}
		data['html_form'] = render_to_string('patient_data/admission_data/partial_delete.html', context, request=request)
		return JsonResponse(data)

	return JsonResponse(data)