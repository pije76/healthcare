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
from patient.Forms.urinary import *
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
def urinary_list(request, username):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Urinary Chart')
	patientid = UserProfile.objects.get(username=username).id
	patients = Urinary.objects.filter(patient=patientid)
	profiles = UserProfile.objects.filter(pk=patientid)

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
	}

	return render(request, 'patient/urinary/urinary_data.html', context)


@login_required
def urinary_create(request, username):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Urinary Chart')
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
		form = UrinaryForm(request.POST or None)
		if form.is_valid():
			profile = Urinary()
			profile.patient = patients
			profile.urinary_catheter_date = form.cleaned_data['urinary_catheter_date']
			profile.urinary_catheter_size = form.cleaned_data['urinary_catheter_size']
			profile.urinary_catheter_type = form.cleaned_data['urinary_catheter_type']
			profile.urinary_catheter_due_date = form.cleaned_data['urinary_catheter_due_date']
			profile.urinary_catheter_inserted_by = form.cleaned_data['urinary_catheter_inserted_by']
			profile.save()

			messages.success(request, _(page_title + ' form was created.'))
			return redirect('patient:patientdata_detail', username=patients.username)
		else:
			messages.warning(request, form.errors)

	else:
		form = UrinaryForm(initial=initial)

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
		'icnumbers': icnumbers,
		'form': form,
	}

	return render(request, 'patient/urinary/urinary_form.html', context)


class UrinaryUpdateView(BSModalUpdateView):
	model = Urinary
	template_name = 'patient/urinary/partial_edit.html'
	form_class = UrinaryForm
	page_title = _('Urinary Form')
	success_message = _(page_title + ' form has been save successfully.')

	def get_success_url(self):
		username = self.kwargs['username']
		return reverse_lazy('patient:urinary_data', kwargs={'username': username})


urinary_edit = UrinaryUpdateView.as_view()


class UrinaryDeleteView(BSModalDeleteView):
	model = Urinary
	template_name = 'patient/urinary/partial_delete.html'
	page_title = _('Urinary Form')
	success_message = _(page_title + ' form was deleted.')

	def get_success_url(self):
		username = self.kwargs['username']
		return reverse_lazy('patient:urinary_data', kwargs={'username': username})


urinary_delete = UrinaryDeleteView.as_view()
