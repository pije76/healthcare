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
from patient.Forms.application_home_leave import *
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
def application_home_leave_list(request, username):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Application For Home Leave')
	patientid = UserProfile.objects.get(username=username).id
	patients = ApplicationForHomeLeave.objects.filter(patient=patientid)
	profiles = UserProfile.objects.filter(pk=patientid)

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
	}

	return render(request, 'patient/application_home_leave/application_home_leave_data.html', context)

@login_required
def application_home_leave_create(request, username):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Application For Home Leave')
	patients = get_object_or_404(UserProfile, username=username)
	profiles = UserProfile.objects.filter(username=username)
	icnumbers = UserProfile.objects.filter(username=username).values_list('ic_number', flat=True).first()

	initial = {
			#       'patient': patients,
			#       'ic_number': icnumbers,
	}

	if request.method == 'POST':
		form = ApplicationForHomeLeaveForm(request.POST or None, instance=request.user)
		if form.is_valid():
			profile = form.save(commit=False)
			profile.patient = form.cleaned_data['patient']
			profile.family_name = form.cleaned_data['family_name']
			profile.family_ic_number = form.cleaned_data['family_ic_number']
			profile.family_relationship = form.cleaned_data['family_relationship']
			profile.family_phone = form.cleaned_data['family_phone']
			profile.designation = form.cleaned_data['designation']
			profile.signature = form.cleaned_data['signature']
			profile.date = form.cleaned_data['date']
			profile.save()

			messages.success(request, _(page_title + ' form was created.'))
			return redirect('patient:patientdata_detail', username=patients.username)
		else:
			messages.warning(request, form.errors)
	else:
		form = ApplicationForHomeLeaveForm()
#       form = ApplicationForHomeLeaveForm(initial=initial)
#       form = ApplicationForHomeLeaveForm(instance=request.user)
#       form = ApplicationForHomeLeaveForm(initial=initial, instance=request.user)
#       form = ApplicationForHomeLeaveForm()

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
		'icnumbers': icnumbers,
		'form': form,
	}

	return render(request, 'patient/application_home_leave/application_home_leave_form.html', context)


class ApplicationForHomeLeaveUpdateView(BSModalUpdateView):
	model = ApplicationForHomeLeave
	template_name = 'patient/application_home_leave/partial_edit.html'
	form_class = ApplicationForHomeLeaveForm
	page_title = _('ApplicationForHomeLeave Form')
	success_message = _(page_title + ' form has been save successfully.')

	def get_success_url(self):
		username = self.kwargs['username']
		return reverse_lazy('patient:application_home_leave_data', kwargs={'username': username})


application_home_leave_edit = ApplicationForHomeLeaveUpdateView.as_view()


class ApplicationForHomeLeaveDeleteView(BSModalDeleteView):
	model = ApplicationForHomeLeave
	template_name = 'patient/application_home_leave/partial_delete.html'
	page_title = _('ApplicationForHomeLeave Form')
	success_message = _(page_title + ' form was deleted.')

	def get_success_url(self):
		username = self.kwargs['username']
		return reverse_lazy('patient:application_home_leave_data', kwargs={'username': username})


application_home_leave_delete = ApplicationForHomeLeaveDeleteView.as_view()

