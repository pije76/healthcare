from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.db import connection
from django.db.models import Count, Sum, F, Q
from django.db.models.functions import Trunc
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.translation import ugettext as _
from django.views.generic import ListView

from patient.models import *
from patient.Forms.medication_administration import *
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
def medication_administration_list(request, username):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Medication Administration Record')
	patientid = UserProfile.objects.get(username=username).id
	patients = MedicationAdministrationRecord.objects.filter(patient=patientid)
	profiles = UserProfile.objects.filter(pk=patientid)
	allergies = MedicationAdministrationRecord.objects.filter(patient=patientid).values_list('allergy', flat=True).first()

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
		'allergies': allergies,
	}

	return render(request, 'patient/medication_administration/medication_administration_data.html', context)




@login_required
def medication_administration_create(request, username):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Medication Administration Record')

	patientid = UserProfile.objects.get(username=username).id
	icnumbers = UserProfile.objects.get(username=username).ic_number
	patientusername = UserProfile.objects.get(username=username)
	profiles = UserProfile.objects.filter(username=username)
	patients = get_object_or_404(UserProfile, username=username)

	allergies = MedicationAdministrationRecord.objects.filter(patient=patientid).values_list('allergy', flat=True).first()
	stat = MedicationAdministrationRecord.objects.filter(patient=patientid).values_list('stat', flat=True).first()
	medicationstat_date_time = MedicationAdministrationRecord.objects.filter(patient=patientid).values_list('medicationstat_date_time', flat=True).first()
	given_by = MedicationAdministrationRecord.objects.filter(patient=patientid).values_list('given_by', flat=True).first()

	queryset = MedicationAdministrationRecord.objects.filter(patient=patientid).values()

	initial_form = {
		'patient': patients,
		'ic_number': icnumbers,
		'allergy': allergies,
		'stat': stat,
		'medicationstat_date_time': medicationstat_date_time,
		'given_by': request.user,
	}

	initial_formset_factory = [
	{
		'patient': patients,
		'medication_date': get_today,
		'medication_time': get_time,
		'medicationstat_date_time': get_datetime,
		'given_by': request.user,
	}]

	initial_modelform_factory = {
		'patient': patients,
		'medication_date': get_today,
		'medication_time': get_time,
		'medicationstat_date_time': get_datetime,
		'given_by': request.user,
	}
	initial_modelformset_factory = [
	{
		'patient': patients,
		'medication_date': get_today,
		'medication_time': get_time,
		'medicationstat_date_time': get_datetime,
	}]

	initial_inlineformset_factory = [
	{
				#       'patient': patients,
		'medication_date': get_today,
		'medication_time': get_time,
		'medicationstat_date_time': get_datetime,
	}]

	GROUP_SIZE = 4

	if request.method == 'POST':
		formset_factory = MedicationAdministrationRecord_FormSet_Factory(request.POST or None)

		if formset_factory.is_valid():
			for item in formset_factory:
				profile = MedicationAdministrationRecord()
				profile.patient = patients
				profile.allergy = item.cleaned_data['allergy']
				profile.medication_name = item.cleaned_data['medication_name']
				profile.medication_dosage = item.cleaned_data['medication_dosage']
				profile.medication_tab = item.cleaned_data['medication_tab']
				profile.medication_frequency = item.cleaned_data['medication_frequency']
				profile.medication_route = item.cleaned_data['medication_route']
				profile.medication_date = item.cleaned_data['medication_date']
				profile.medication_time = item.cleaned_data['medication_time']
				profile.signature_nurse = item.cleaned_data['signature_nurse']
				profile.stat = item.cleaned_data['stat']
				profile.medicationstat_date_time = item.cleaned_data['medicationstat_date_time']
				profile.given_by = item.cleaned_data['given_by']
				profile.save()

			messages.success(request, _(page_title + ' form was created.'))
			return redirect('patient:patientdata_detail', username=patients.username)
		else:
			messages.warning(request, formset_factory.errors)
	else:
		formset_factory = MedicationAdministrationRecord_FormSet_Factory(initial=initial_formset_factory)
#       formset_factory = MedicationAdministrationRecord_FormSet_Factory(initial=[{'medication_date': get_today} for medication_date in queryset])

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
		'icnumbers': icnumbers,
					#       'form': form,
		'formset': formset_factory,
					#       'formset1': formset1,
					#       'formset2': formset2,
					#       'helper': helper,
	}

#   return render(request, 'patient/_form/medication_administration_form.html', context)
	return render(request, 'patient/medication_administration/medication_administration_formset_factory.html', context)
#   return render(request, 'patient/_form/medication_administration_modelform_factory.html', context)
#   return render(request, 'patient/_form/medication_administration_modelformset_factory.html', context)
#   return render(request, 'patient/_form/medication_administration_inlineformset_factory.html', context)


class MedicationAdministrationRecordUpdateView(BSModalUpdateView):
	model = MedicationAdministrationRecord
	template_name = 'patient/medication_administration/partial_edit.html'
	form_class = MedicationAdministrationRecord_FormSet_Factory
	page_title = _('MedicationAdministrationRecord Form')
	success_message = _(page_title + ' form has been save successfully.')

	def get_success_url(self):
		username = self.kwargs['username']
		return reverse_lazy('patient:medication_administration_data', kwargs={'username': username})


medication_administration_edit = MedicationAdministrationRecordUpdateView.as_view()


class MedicationAdministrationRecordDeleteView(BSModalDeleteView):
	model = MedicationAdministrationRecord
	template_name = 'patient/medication_administration/partial_delete.html'
	page_title = _('MedicationAdministrationRecord Form')
	success_message = _(page_title + ' form was deleted.')

	def get_success_url(self):
		username = self.kwargs['username']
		return reverse_lazy('patient:medication_administration_data', kwargs={'username': username})


medication_administration_delete = MedicationAdministrationRecordDeleteView.as_view()

