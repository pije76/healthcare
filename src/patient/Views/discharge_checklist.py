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
from patient.Forms.discharge_checklist import *
from accounts.models import *
from customers.models import *

from bootstrap_modal_forms.generic import *


@login_required
def discharge_checklist_list(request, username):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Discharge CheckList')
	patientid = UserProfile.objects.get(username=username).id
	patients = DischargeCheckList.objects.filter(patient=patientid)
	profiles = UserProfile.objects.filter(pk=patientid)

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
	}

	return render(request, 'patient/discharge_checklist/discharge_checklist_data.html', context)


@login_required
def discharge_checklist_create(request, username):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Discharge CheckList')
	patients = get_object_or_404(UserProfile, username=username)
	profiles = UserProfile.objects.filter(username=username)
	icnumbers = UserProfile.objects.filter(username=username).values_list('ic_number', flat=True).first()

	initial = {
		'patient': patients,
		'given_by': request.user,
	}

	initial_formset = [{
		'patient': item,
#		'patient': item.id,
#		'patient': item.username,
#		'patient': patients,
		'given_by': request.user,
	}
	for item in profiles]

	if request.method == 'POST':
		form = DischargeCheckList_Form(request.POST or None, request.FILES or None)
		formset = DischargeCheckList_FormSet(request.POST or None)

		if form.is_valid():
			discharge_form_data = DischargeCheckList()
			discharge_form_data.patient = patients
			discharge_form_data.date_time = form.cleaned_data['date_time']
			discharge_form_data.discharge_status = form.cleaned_data['discharge_status']
			discharge_form_data.nasogastric_tube_date = form.cleaned_data['nasogastric_tube_date']
			discharge_form_data.nasogastric_tube = form.cleaned_data['nasogastric_tube']
			discharge_form_data.urinary_catheter_date = form.cleaned_data['urinary_catheter_date']
			discharge_form_data.urinary_catheter = form.cleaned_data['urinary_catheter']
			discharge_form_data.surgical_dressing_intact = form.cleaned_data['surgical_dressing_intact']
			discharge_form_data.spectacle_walking_aid_denture = form.cleaned_data['spectacle_walking_aid_denture']
			discharge_form_data.appointment_card_returned = form.cleaned_data['appointment_card_returned']
			discharge_form_data.own_medication_return = form.cleaned_data['own_medication_return']
			discharge_form_data.medication_reconcilation = form.cleaned_data['medication_reconcilation']
			discharge_form_data.given_by = form.cleaned_data['given_by']
			discharge_form_data.save()

		if formset.is_valid():
			for item in formset:
				discharge_formset_data = DischargeCheckList()
#				discharge_formset_data = item.save(commit=False)
				discharge_formset_data.patient = patients
#				discharge_formset_data.patient = item.cleaned_data['patient']
				discharge_formset_data.medication_reconcilation_patient = item.cleaned_data['medication_reconcilation_patient']
				discharge_formset_data.save()

			messages.success(request, _(page_title + ' form was created.'))
			return redirect('patient:patientdata_detail', username=patients.username)
		else:
			messages.warning(request, form.errors)
			messages.warning(request, formset.errors)
	else:
		form = DischargeCheckList_Form(initial=initial)
		formset = DischargeCheckList_FormSet(initial=initial_formset)

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
		'icnumbers': icnumbers,
		'form': form,
		'formset': formset,
	}

	return render(request, 'patient/discharge_checklist/discharge_checklist_form.html', context)


class DischargeCheckListUpdateView(BSModalUpdateView):
	model = DischargeCheckList
	template_name = 'patient/discharge_checklist/partial_edit.html'
	form_class = DischargeCheckList_ModelForm
	page_title = _('Discharge CheckList Form')
	success_message = _(page_title + ' form has been save successfully.')

	def get_form(self, form_class=None):
		form = super().get_form(form_class=None)
		form.fields['date_time'].label = _("Date & Time")
		form.fields['discharge_status'].label = _("Status")
		form.fields['nasogastric_tube_date'].label = _("Nasogastric Date")
		form.fields['nasogastric_tube'].label = _("Nasogastric")
		form.fields['urinary_catheter_date'].label = _("Urinary Date")
		form.fields['urinary_catheter'].label = _("Urinary")
		form.fields['surgical_dressing_intact'].label = _("Surgical Intact")
		form.fields['spectacle_walking_aid_denture'].label = _("Spectacle/Walking Aid/Denture")
		form.fields['appointment_card_returned'].label = _("Appointment")
		form.fields['own_medication_return'].label = _("Own Medication")
		form.fields['medication_reconcilation'].label = _("Medication Reconcilation")
		form.fields['medication_reconcilation_patient'].label = _("Medication Reconcilation Patient/Relative")
		form.fields['given_by'].label = _("Given by")
		return form

	def get_success_url(self):
		username = self.kwargs['username']
		return reverse_lazy('patient:discharge_checklist_list', kwargs={'username': username})


discharge_checklist_edit = DischargeCheckListUpdateView.as_view()


class DischargeCheckListDeleteView(BSModalDeleteView):
	model = DischargeCheckList
	template_name = 'patient/discharge_checklist/partial_delete.html'
	page_title = _('Discharge CheckList Form')
	success_message = _(page_title + ' form was deleted.')

	def get_success_url(self):
		username = self.kwargs['username']
		return reverse_lazy('patient:discharge_checklist_list', kwargs={'username': username})


discharge_checklist_delete = DischargeCheckListDeleteView.as_view()
