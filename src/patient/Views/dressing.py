from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.db.models import F, Func, Value, CharField
from django.db.models import Value, CharField
from django.db.models.functions import Cast, Concat, ExtractYear, ExtractMonth, ExtractDay, ExtractHour, ExtractMinute
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.utils.translation import ugettext as _

from patient.models import *
from patient.Forms.dressing import *
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
def dressing_list(request, username):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Dressing Chart')
	patientid = UserProfile.objects.get(username=username).id
	patients = Dressing.objects.filter(patient=patientid)
	profiles = UserProfile.objects.filter(pk=patientid)

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
	}

	return render(request, 'patient/dressing/dressing_data.html', context)


@login_required
def dressing_create(request, username):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Dressing Chart')
	patients = get_object_or_404(UserProfile, username=username)
	profiles = UserProfile.objects.filter(username=username)
	icnumbers = UserProfile.objects.filter(username=username).values_list('ic_number', flat=True).first()

	initial = [{
		'patient': item.full_name,
		'done_by': request.user,
	}
	for item in profiles]

	if request.method == 'POST':
		formset = Dressing_FormSet(request.POST or None, request.FILES or None)

		if formset.is_valid():
			for item in formset:
				profile = Dressing()
				profile.patient = patients
				profile.date = item.cleaned_data['date']
				profile.time = item.cleaned_data['time']
				profile.frequency_dressing = item.cleaned_data['frequency_dressing']
				profile.type_dressing = item.cleaned_data['type_dressing']
				profile.wound_location = item.cleaned_data['wound_location']
				profile.wound_condition = item.cleaned_data['wound_condition']
				profile.photos = item.cleaned_data['photos']
				profile.note = item.cleaned_data['note']
				profile.done_by = item.cleaned_data['done_by']
				profile.save()

			messages.success(request, _(page_title + ' form was created.'))
			return redirect('patient:patientdata_detail', username=patients.username)
		else:
			messages.warning(request, formset.errors)
	else:
		formset = Dressing_FormSet(initial=initial)

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
		'icnumbers': icnumbers,
		'formset': formset,
	}

	return render(request, 'patient/dressing/dressing_form.html', context)


class DressingUpdateView(BSModalUpdateView):
	model = Dressing
	template_name = 'patient/dressing/partial_edit.html'
	form_class = Dressing_ModelForm
	page_title = _('Dressing Form')
	success_message = _(page_title + ' form has been save successfully.')

	def get_success_url(self):
		username = self.kwargs['username']
		return reverse_lazy('patient:dressing_list', kwargs={'username': username})


dressing_edit = DressingUpdateView.as_view()


class DressingDeleteView(BSModalDeleteView):
	model = Dressing
	template_name = 'patient/dressing/partial_delete.html'
	page_title = _('Dressing Form')
	success_message = _(page_title + ' form was deleted.')

	def get_success_url(self):
		username = self.kwargs['username']
		return reverse_lazy('patient:dressing_list', kwargs={'username': username})


dressing_delete = DressingDeleteView.as_view()
