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
from patient.Forms.nasogastric import *
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
def nasogastric_list(request, username):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Nasogastric Chart')
	patientid = UserProfile.objects.get(username=username).id
	patients = Nasogastric.objects.filter(patient=patientid)
	profiles = UserProfile.objects.filter(pk=patientid)

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
	}

	return render(request, 'patient/nasogastric/nasogastric_data.html', context)


@login_required
def nasogastric_create(request, username):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Nasogastric Chart')
	patients = get_object_or_404(UserProfile, username=username)
	profiles = UserProfile.objects.filter(username=username)
	icnumbers = UserProfile.objects.filter(username=username).values_list('ic_number', flat=True).first()

	initial = {
		'patient': patients,
		'ic_number': icnumbers,
		'nasogastric_tube_inserted_by': request.user,
		'urinary_catheter_inserted_by': request.user
	}

	if request.method == 'POST':
		form = NasogastricForm(request.POST or None)
		if form.is_valid():
			profile = Nasogastric()
			profile.patient = patients
			profile.nasogastric_tube_date = form.cleaned_data['nasogastric_tube_date']
			profile.nasogastric_tube_size = form.cleaned_data['nasogastric_tube_size']
			profile.nasogastric_tube_type = form.cleaned_data['nasogastric_tube_type']
			profile.nasogastric_tube_location = form.cleaned_data['nasogastric_tube_location']
			profile.nasogastric_tube_due_date = form.cleaned_data['nasogastric_tube_due_date']
			profile.nasogastric_tube_inserted_by = form.cleaned_data['nasogastric_tube_inserted_by']
			profile.save()

			messages.success(request, _(page_title + ' form was created.'))
			return redirect('patient:patientdata_detail', username=patients.username)
		else:
			messages.warning(request, form.errors)

	else:
		form = NasogastricForm(initial=initial)

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
		'icnumbers': icnumbers,
		'form': form,
	}

	return render(request, 'patient/nasogastric/nasogastric_form.html', context)


class NasogastricUpdateView(BSModalUpdateView):
	model = Nasogastric
	template_name = 'patient/nasogastric/partial_edit.html'
	form_class = NasogastricForm
	page_title = _('Nasogastric Form')
	success_message = _(page_title + ' form has been save successfully.')

	def get_success_url(self):
		username = self.kwargs['username']
		return reverse_lazy('patient:nasogastric_data', kwargs={'username': username})


nasogastric_edit = NasogastricUpdateView.as_view()


class NasogastricDeleteView(BSModalDeleteView):
	model = Nasogastric
	template_name = 'patient/nasogastric/partial_delete.html'
	page_title = _('Nasogastric Form')
	success_message = _(page_title + ' form was deleted.')

	def get_success_url(self):
		username = self.kwargs['username']
		return reverse_lazy('patient:nasogastric_data', kwargs={'username': username})


nasogastric_delete = NasogastricDeleteView.as_view()