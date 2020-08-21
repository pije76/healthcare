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
from patient.Forms.investigationreport import *
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
def investigationreport_list(request, username):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('InvestigationReport Chart')
	patientid = UserProfile.objects.get(username=username).id
	patients = InvestigationReport.objects.filter(patient=patientid)
	profiles = UserProfile.objects.filter(pk=patientid)

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
	}

	return render(request, 'patient/investigationreport/investigationreport_data.html', context)



@login_required
def investigationreport_create(request, username):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('InvestigationReport Chart')
	patients = get_object_or_404(UserProfile, username=username)
	profiles = UserProfile.objects.filter(username=username)
	icnumbers = UserProfile.objects.filter(username=username).values_list('ic_number', flat=True).first()

	initial = {
		'patient': patients,
		'ic_number': icnumbers,
		'done_by': request.user,
	}

	initial_formset_factory = [
	{
		'patient': patients,
		'ic_number': icnumbers,
	}]

	if request.method == 'POST':
		formset = InvestigationReport_FormSet_Factory(request.POST or None, request.FILES or None)
		if formset.is_valid():
			for item in formset:
				profile = InvestigationReport()
				profile.patient = patients
				profile.date = item.cleaned_data['date']
				profile.file_upload = item.cleaned_data['file_upload']
				profile.save()

			messages.success(request, _(page_title + ' form was created.'))
			return redirect('patient:patientdata_detail', username=patients.username)
		else:
			messages.warning(request, formset.errors)
	else:
		formset = InvestigationReport_FormSet_Factory(initial=initial_formset_factory)

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
		'icnumbers': icnumbers,
		'formset': formset,
	}

	return render(request, 'patient/investigationreport/investigationreport_form.html', context)


class InvestigationReportUpdateView(BSModalUpdateView):
	model = InvestigationReport
	template_name = 'patient/investigationreport/partial_edit.html'
	form_class = InvestigationReportForm
	page_title = _('InvestigationReport Form')
	success_message = _(page_title + ' form has been save successfully.')

	def get_success_url(self):
		username = self.kwargs['username']
		return reverse_lazy('patient:investigationreport_list', kwargs={'username': username})


investigationreport_edit = InvestigationReportUpdateView.as_view()


class InvestigationReportDeleteView(BSModalDeleteView):
	model = InvestigationReport
	template_name = 'patient/investigationreport/partial_delete.html'
	page_title = _('InvestigationReport Form')
	success_message = _(page_title + ' form was deleted.')

	def get_success_url(self):
		username = self.kwargs['username']
		return reverse_lazy('patient:investigationreport_list', kwargs={'username': username})


investigationreport_delete = InvestigationReportDeleteView.as_view()
