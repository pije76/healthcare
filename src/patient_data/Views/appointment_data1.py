from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder
from django.db import connection
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.utils import timezone
from django.utils.timezone import is_aware
from django.utils.translation import ugettext as _
from django.db.models import Value, CharField
from django.db.models.functions import Cast, Concat, ExtractYear, ExtractMonth, ExtractDay, ExtractHour, ExtractMinute
from django.db.models import F, Func, Value, CharField

import json
import decimal

from patient_form.models import *
from patient_form.forms import *
from accounts.models import *
from customers.models import *

import datetime
#from datetime import *

startdate = datetime.date.today()
enddate = startdate + datetime.timedelta(days=1)

start_time_day = datetime.datetime.strptime('00:00', '%H:%M').time()
end_time_day = datetime.datetime.strptime('12:00', '%H:%M').time()
start_time_night = datetime.datetime.strptime('12:01', '%H:%M').time()
end_time_night = datetime.datetime.strptime('23:59', '%H:%M').time()

@login_required
def save_appointment_data_form(request, form, template_name):
	data = dict()

	if request.method == 'POST':
		if form.is_valid():
			patients = Appointment()
			patients = form.save(commit=False)
			patients.patient = request.user
			patients.save()
			data['form_is_valid'] = True
			patients = Appointment.objects.all()
			data['html_appointment_list'] = render_to_string('patient_data/appointment_data/partial_list.html', {'patients': patients})
		else:
			data['form_is_valid'] = False

	context = {
		'form': form,
	}
	data['html_form'] = render_to_string(template_name, context, request=request)

	return JsonResponse(data)


class DjangoOverRideJSONEncoder(DjangoJSONEncoder):
	def default(self, o):
		if isinstance(o, datetime.datetime):
			r = o.strftime(' ')
			if o.microsecond:
				r = r[:23] + r[26:]
			if r.endswith('+00:00'):
				r = r[:-6] + 'Z'
			return r
		elif isinstance(o, datetime.date):
			return o.strftime(' ')
		elif isinstance(o, datetime.time):
			if is_aware(o):
				raise ValueError("JSON can't represent timezone-aware times.")
			r = o.strftime(' ')
			if o.microsecond:
				r = r[:12]
			return r
		elif isinstance(o, decimal.Decimal):
			return str(o)
		else:
			return super(DjangoOverRideJSONEncoder, self).default(o)


class MyEncoder(DjangoJSONEncoder):
	def default(self, obj):
		if isinstance(obj, date):
			return obj.strftime('%d.%m.%Y')
		return super(MyEncoder, self).default(obj)


@login_required
def appointment_data(request, username):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Appointment Data')
	patientid = UserProfile.objects.get(username=username).id
	patients = Appointment.objects.filter(patient=patientid)
	profiles = UserProfile.objects.filter(pk=patientid)
#	to_remind = Appointment.objects.exclude(remind_date__isnull=False).filter(date_time__lte=now)
#	to_remind = Appointment.objects.filter(date_time__lte=now)
#	to_remind = Appointment.objects.all()
#	today_date = datetime.datetime.now().date()
#	today_time = datetime.datetime.now()
#	earlier = datetime.timedelta(hours=5)
#	time_threshold = today_time + earlier
	starttime = datetime.datetime.now()
#	starttime = timezone.now()
	endtime = starttime + datetime.timedelta(hours=1)
#	endtime = starttime + timezone.timedelta(hours=5)
#	five_h_ago = timezone.now()-timezone.timedelta(hours=5)
#	from_date = datetime.datetime.strptime(input_date, '%H:%M').time()
#	to_remind = Appointment.objects.filter(date_time__lt=time_threshold).values_list('date_time', flat=True)
#	to_remind = Appointment.objects.filter(date_time__date=datetime.date.today()).values('date_time', flat=True)
#	to_remind = Appointment.objects.filter(date_time__range=(starttime, endtime)).values('date_time', flat=True).first()
#	to_remind = Appointment.objects.filter(date_time__range=(starttime, endtime)).values('date_time', flat=True)
	to_remind = Appointment.objects.filter(date_time__range=(starttime, endtime)).values('date_time')
	remind = Appointment.objects.filter(date_time__range=(starttime, endtime))
	remindall = Appointment.objects.all().values("date_time")
#	remind = Appointment.objects.all()
#	datetimeyear = to_remind.strftime('%Y')
#	to_remind = Appointment.objects.annotate(str_datetime=Cast(TruncSecond('date_time', DateTimeField()), CharField())).values('str_datetime').first()
#	desired_format = '%d/%m/%YT %H-%M'
#	delta_day = int((datetime.datetime.now().date() - birth_date).days / 365.25)
#	total_age = datetime.strftime(delta_day / 365.25)

#	sec = datetime.datetime(to_remind)).strftime('%s')
#	convert_duration_hour = int((remind / 3600) % 3600)
#	convert_duration_minute = int((remind / 60) % 60)
#	convert_duration_second = int(remind)
#	delta = datetime.timedelta(hours=convert_duration_hour, minutes=convert_duration_minute)
#	datetimeyear = datetime.datetime.strftime(remind, '%Y')

	try:
#		to_remind = datetime.datetime.strftime(to_remind, '%d/%m/%Y %H:%M')
#		remind = datetime.datetime(datetimeyear.timestamp())
#		remind = datetime.datetime.strftime(remind, '%d/%m/%Y %H:%M')
#		to_remind = datetime_to_milliseconds(to_remind)
		datetimeyear = remind.annotate(year=Cast(ExtractYear('date_time'), CharField()), str_datetime=Concat(Value(''), 'year', output_field=CharField())).values('str_datetime').first()
		datetimemonth = remind.annotate(month=Cast(ExtractMonth('date_time'), CharField()), str_datetime=Concat(Value(''), 'month', output_field=CharField())).values('str_datetime').first()
		datetimeday = remind.annotate(day=Cast(ExtractDay('date_time'), CharField()), str_datetime=Concat(Value(''), 'day', output_field=CharField())).values('str_datetime').first()
		datetimehour = remind.annotate(hour=Cast(ExtractHour('date_time'), CharField()), str_datetime=Concat(Value(''), 'hour', output_field=CharField())).values('str_datetime').first()
		datetimeminute = remind.annotate(minute =Cast(ExtractMinute('date_time'), CharField()), str_datetime=Concat(Value(''), 'minute', output_field=CharField())).values('str_datetime').first()


	except:
#		remind = None
#		to_remind = str(to_remind)
#	to_remind = Appointment.objects.filter(date_time__date=datetime.date.today()).only('date_time')
		datetimeyear = None
		datetimemonth = None
		datetimeday = None
		datetimehour = None
		datetimeminute = None

#	time_t = datetime.time.mktime(to_remind.timetuple())
#	js_data = serialize('json', to_remind, fields=['date_time'])
#	js_data = serialize('json', to_remind)
#	js_output = json.dumps(to_remind, cls=DjangoJSONEncoder)
#	js_output = json.dumps(list(to_remind), cls=DjangoJSONEncoder)
#	js_output = json.dumps(to_remind, cls=DjangoOverRideJSONEncoder)
#	js_output = json.dumps(list(to_remind), cls=DjangoOverRideJSONEncoder)

#	to_output = serialize("json", datetimeyear, fields=("date_time",))
#	js_output = [i.get('date_time', i) for i in json.loads(js_data) if i]
#	js_output = serialize("json", to_remind)
#	js_output = json.dumps(to_output, cls=DjangoOverRideJSONEncoder)
	js_output = json.dumps(datetimeyear)
#	js_output = json.dumps([model_to_dict(o) for o in to_remind], cls=MyEncoder)



#	if to_remind == now:
#		to_remind == True
#	else:
#		pass


	
#	if to_remind.date_time is not None:
#		to_remind_date = to_remind.date_time.date()

#	to_remind = Appointment.objects.filter(patient=patientid).values_list('date_time', flat=True).first()
#	to_remind_date = to_remind.date_time



#    event_date = Appointment.objects.filter(patient=id).values_list('date', flat=True)
#   event_time = Appointment.objects.filter(patient=id).values_list('time', flat=True)
#    timenow = datetime.time(datetime.now())
#    event_time = Appointment.objects.filter(patient=id, time='12:59')

#    print("event_date: ", event_date)
#    print("event_time: ", event_time)

#    today = date.today()
#   difference = today - event_date
#   event_date_new = event_date + difference

#    if event_date == today:
#        messages.warning(request, form.errors)

	print("starttime: ", starttime)
	print("endtime: ", endtime)
	print("remind: ", remind)
	print("datetimeyear: ", datetimeyear)
	print("datetimemonth: ", datetimemonth)
	print("datetimeday: ", datetimeday)
	print("datetimehour: ", datetimehour)
	print("datetimeminute: ", datetimeminute)
	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
		'remind': remind,
		'js_output': js_output,
		'datetimeyear': datetimeyear,
		'datetimemonth': datetimemonth,
		'datetimeday': datetimeday,
		'datetimehour': datetimehour,
		'datetimeminute': datetimeminute,
	}

	return render(request, 'patient_data/appointment_data/appointment_data.html', context)


def notification_post_save(instance, *args, **kwargs):
	send_notification.apply_async((instance,), eta=instance.date_time)

#signals.post_save.connect(notification_post_save, sender=Appointment)

@login_required
def appointment_data_edit(request, id, username):
	appointments = get_object_or_404(Appointment, pk=id)
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Appointment Data')
#	patientid = UserProfile.objects.get(username=username).username
	patientid = get_object_or_404(UserProfile, username=username)
	patientname = get_object_or_404(UserProfile, username=username).full_name
#	patientid = UserProfile.objects.get(username=username).id
#	patients = Appointment.objects.filter(patient=patientid)
#	profiles = UserProfile.objects.filter(pk=patientid)
	patients = Appointment.objects.filter(patient=patientid)
#	icnumbers = UserProfile.objects.filter(pk=id).values_list('ic_number', flat=True).first()
	icnumbers = get_object_or_404(UserProfile, username=username).ic_number

	if request.method == 'POST':
		form = AppointmentForm(request.POST or None, instance=appointments)
		if form.is_valid():
			profile = form.save(commit=False)
			profile.patient = form.cleaned_data['patient']
			profile.date_time = form.cleaned_data['date_time']
			profile.hospital_clinic_center = form.cleaned_data['hospital_clinic_center']
			profile.department = form.cleaned_data['department']
			profile.planning_investigation = form.cleaned_data['planning_investigation']
			profile.treatment_order = form.cleaned_data['treatment_order']
			profile.save()
#		return redirect('patient_data:patientdata_detail', username=patients.username)
		return redirect('patient_data:appointment_data', username=patientid.username)
#		return render(request, 'patient_data/appointment_data/appointment_data.html', {'form': form})
	else:
		form = AppointmentForm(instance=appointments)

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
#		'profiles': profiles,
		'patientname': patientname,
		'patientid': patientid,
		'icnumbers': icnumbers,
		'form': form,
	}

#    return save_appointment_data_form(request, form, 'patient_data/appointment_data/partial_edit.html')
	return render(request, 'patient_data/appointment_data/partial_edit.html', context)


@login_required
def appointment_data_delete(request, id):
	appointments = get_object_or_404(Appointment, pk=id)
	data = dict()

	if request.method == 'POST':
		appointments.delete()
		data['form_is_valid'] = True
		patients = Appointment.objects.all()
		data['html_appointment_list'] = render_to_string('patient_data/appointment_data/partial_list.html', {'patients': patients})
		return JsonResponse(data)
	else:
		context = {'appointments': appointments}
		data['html_form'] = render_to_string('patient_data/appointment_data/partial_delete.html', context, request=request)
		return JsonResponse(data)

	return JsonResponse(data)
