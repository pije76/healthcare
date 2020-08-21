from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.db.models import F, Func, Value, CharField
from django.db.models import Value, CharField
from django.db.models.functions import Cast, Concat, ExtractYear, ExtractMonth, ExtractDay, ExtractHour, ExtractMinute
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.utils.translation import ugettext as _

from patient.models import *
from patient.Forms.appointment import *
from accounts.models import *
from customers.models import *

from bootstrap_modal_forms.generic import *

startdate = datetime.date.today()
enddate = startdate + datetime.timedelta(days=1)

start_time_day = datetime.datetime.strptime('00:00', '%H:%M').time()
end_time_day = datetime.datetime.strptime('12:00', '%H:%M').time()
start_time_night = datetime.datetime.strptime('12:01', '%H:%M').time()
end_time_night = datetime.datetime.strptime('23:59', '%H:%M').time()


@login_required
def appointment_list(request, username):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Appointment Data')
	patientid = UserProfile.objects.get(username=username).id
	patients = Appointment.objects.filter(patient=patientid)
	profiles = UserProfile.objects.filter(pk=patientid)
#	starttime = datetime.datetime.now()
	starttime = timezone.now()
#	endtime = starttime + datetime.timedelta(hours=1)
	endtime = starttime + timezone.timedelta(hours=1)
	to_remind = Appointment.objects.filter(date_time__range=(starttime, endtime)).values('date_time')
	remind = Appointment.objects.filter(date_time__range=(starttime, endtime))

	try:
		datetimeyear = remind.annotate(year=Cast(ExtractYear('date_time'), CharField()), str_datetime=Concat(Value(''), 'year', output_field=CharField())).values('str_datetime').first()
		datetimemonth = remind.annotate(month=Cast(ExtractMonth('date_time'), CharField()), str_datetime=Concat(Value(''), 'month', output_field=CharField())).values('str_datetime').first()
		datetimeday = remind.annotate(day=Cast(ExtractDay('date_time'), CharField()), str_datetime=Concat(Value(''), 'day', output_field=CharField())).values('str_datetime').first()
		datetimehour = remind.annotate(hour=Cast(ExtractHour('date_time'), CharField()), str_datetime=Concat(Value(''), 'hour', output_field=CharField())).values('str_datetime').first()
		datetimeminute = remind.annotate(minute=Cast(ExtractMinute('date_time'), CharField()), str_datetime=Concat(Value(''), 'minute', output_field=CharField())).values('str_datetime').order_by('str_datetime').first()
	except remind.DoesNotExist:
		datetimeyear = None
		datetimemonth = None
		datetimeday = None
		datetimehour = None
		datetimeminute = None

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
		'remind': remind,
		'datetimeyear': datetimeyear,
		'datetimemonth': datetimemonth,
		'datetimeday': datetimeday,
		'datetimehour': datetimehour,
		'datetimeminute': datetimeminute,
	}

	return render(request, 'patient/appointment/appointment_data.html', context)


@login_required
def appointment_create(request, username):
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
			profile = Appointment()
			profile.patient = patients
			profile.date_time = form.cleaned_data['date_time']
			profile.hospital_clinic_center = form.cleaned_data['hospital_clinic_center']
			profile.department = form.cleaned_data['department']
			profile.planning_investigation = form.cleaned_data['planning_investigation']
			profile.treatment_order = form.cleaned_data['treatment_order']
			profile.save()

			messages.success(request, _(page_title + ' form was created.'))
			return redirect('patient:patientdata_detail', username=patients.username)
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

	return render(request, 'patient/appointment/appointment_form.html', context)



class AppointmentUpdateView(BSModalUpdateView):
	model = Appointment
	template_name = 'patient/appointment/partial_edit.html'
	form_class = AppointmentForm
	page_title = _('Appointment Form')
	success_message = _(page_title + ' form has been save successfully.')

	def get_success_url(self):
		username = self.kwargs['username']
		return reverse_lazy('patient:appointment_list', kwargs={'username': username})


appointment_edit = AppointmentUpdateView.as_view()


class AppointmentDeleteView(BSModalDeleteView):
	model = Appointment
	template_name = 'patient/appointment/partial_delete.html'
	page_title = _('Appointment Form')
	success_message = _(page_title + ' form was deleted.')

	def get_success_url(self):
		username = self.kwargs['username']
		return reverse_lazy('patient:appointment_list', kwargs={'username': username})


appointment_delete = AppointmentDeleteView.as_view()
