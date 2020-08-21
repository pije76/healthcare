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
from patient.Forms.cannula import *
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
def cannula_list(request, username):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Cannula Chart')
	patientid = UserProfile.objects.get(username=username).id
	patients = Cannula.objects.filter(patient=patientid)
	profiles = UserProfile.objects.filter(pk=patientid)

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
	}

	return render(request, 'patient/cannula/cannula_data.html', context)


@login_required
def cannula_create(request, username):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Cannula Chart')
	patients = get_object_or_404(UserProfile, username=username)
	profiles = UserProfile.objects.filter(username=username)
	icnumbers = UserProfile.objects.filter(username=username).values_list('ic_number', flat=True).first()

	initial = {
		'patient': patients,
		'ic_number': icnumbers,
		'nasogastric_tube_inserted_by': request.user,
		'urinary_catheter_inserted_by': request.user
	}

	initial_formset_factory = [
	{
		'patient': patients,
		'ic_number': icnumbers,
	}]

	if request.method == 'POST':
		formset = Cannula_FormSet_Factory(request.POST or None)
		if formset.is_valid():
			for item in formset:
				profile = Cannula()
				profile.patient = patients
				profile.cannula_date = item.cleaned_data['cannula_date']
				profile.cannula_size = item.cleaned_data['cannula_size']
				profile.cannula_location = item.cleaned_data['cannula_location']
				profile.cannula_due_date = item.cleaned_data['cannula_due_date']
				profile.save()

			messages.success(request, _(page_title + ' form was created.'))
			return redirect('patient:patientdata_detail', username=patients.username)
		else:
			messages.warning(request, formset.errors)

	else:
		formset = Cannula_FormSet_Factory(initial=initial_formset_factory)

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
		'icnumbers': icnumbers,
		'formset': formset,
	}

	return render(request, 'patient/cannula/cannula_form.html', context)


class CannulaUpdateView(BSModalUpdateView):
	model = Cannula
	template_name = 'patient/cannula/partial_edit.html'
	form_class = CannulaForm
	page_title = _('Cannula Form')
	success_message = _(page_title + ' form has been save successfully.')

	def get_success_url(self):
		username = self.kwargs['username']
		return reverse_lazy('patient:cannula_list', kwargs={'username': username})


cannula_edit = CannulaUpdateView.as_view()


class CannulaDeleteView(BSModalDeleteView):
	model = Cannula
	template_name = 'patient/cannula/partial_delete.html'
	page_title = _('Cannula Form')
	success_message = _(page_title + ' form was deleted.')

	def get_success_url(self):
		username = self.kwargs['username']
		return reverse_lazy('patient:cannula_list', kwargs={'username': username})


cannula_delete = CannulaDeleteView.as_view()
