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
	profiles = UserProfile.objects.filter(pk=patientid)
	get_lastdate = DischargeCheckList.objects.filter(patient=patientid).order_by('-date_time').values_list('date_time', flat=True).first()
	patients = DischargeCheckList.objects.filter(patient=patientid, date_time=get_lastdate).filter(medication_reconcilation_patient__isnull=False)

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
			discharge_form_data.discharge_status = ', '.join(form.cleaned_data['discharge_status'])
			discharge_form_data.nasogastric_tube_date = form.cleaned_data['nasogastric_tube_date']
			discharge_form_data.nasogastric_tube = ', '.join(form.cleaned_data['nasogastric_tube'])
			discharge_form_data.urinary_catheter_date = form.cleaned_data['urinary_catheter_date']
			discharge_form_data.urinary_catheter = ', '.join(form.cleaned_data['urinary_catheter'])
			discharge_form_data.surgical_dressing_intact = ', '.join(form.cleaned_data['surgical_dressing_intact'])
			discharge_form_data.spectacle_walking_aid_denture = ', '.join(form.cleaned_data['spectacle_walking_aid_denture'])
			discharge_form_data.appointment_card_returned = ', '.join(form.cleaned_data['appointment_card_returned'])
			discharge_form_data.own_medication_return = ', '.join(form.cleaned_data['own_medication_return'])
			discharge_form_data.medication_reconcilation = ', '.join(form.cleaned_data['medication_reconcilation'])
			discharge_form_data.given_by = form.cleaned_data['given_by']
			discharge_form_data.save()

		if formset.is_valid():
			get_date_time = DischargeCheckList.objects.filter(patient=patients).values_list("date_time", flat=True).first()
			get_discharge_status = DischargeCheckList.objects.filter(patient=patients).values_list("discharge_status", flat=True).first()
			get_nasogastric_tube_date = DischargeCheckList.objects.filter(patient=patients).values_list("nasogastric_tube_date", flat=True).first()
			get_nasogastric_tube = DischargeCheckList.objects.filter(patient=patients).values_list("nasogastric_tube", flat=True).first()
			get_urinary_catheter_date = DischargeCheckList.objects.filter(patient=patients).values_list("urinary_catheter_date", flat=True).first()
			get_urinary_catheter = DischargeCheckList.objects.filter(patient=patients).values_list("urinary_catheter", flat=True).first()
			get_surgical_dressing_intact = DischargeCheckList.objects.filter(patient=patients).values_list("surgical_dressing_intact", flat=True).first()
			get_spectacle_walking_aid_denture = DischargeCheckList.objects.filter(patient=patients).values_list("spectacle_walking_aid_denture", flat=True).first()
			get_appointment_card_returned = DischargeCheckList.objects.filter(patient=patients).values_list("appointment_card_returned", flat=True).first()
			get_own_medication_return = DischargeCheckList.objects.filter(patient=patients).values_list("own_medication_return", flat=True).first()
			get_medication_reconcilation = DischargeCheckList.objects.filter(patient=patients).values_list("medication_reconcilation", flat=True).first()
			get_given_by = DischargeCheckList.objects.filter(patient=patients).values_list("given_by", flat=True).first()

			for item in formset:
				discharge_formset_data = DischargeCheckList()
#				discharge_formset_data = item.save(commit=False)
				discharge_formset_data.patient = patients
				discharge_formset_data.date_time = get_date_time
				discharge_formset_data.discharge_status = get_discharge_status
				discharge_formset_data.nasogastric_tube_date = get_nasogastric_tube_date
				discharge_formset_data.nasogastric_tube = get_nasogastric_tube
				discharge_formset_data.urinary_catheter_date = get_urinary_catheter_date
				discharge_formset_data.urinary_catheter = get_urinary_catheter
				discharge_formset_data.surgical_dressing_intact = get_surgical_dressing_intact
				discharge_formset_data.spectacle_walking_aid_denture = get_spectacle_walking_aid_denture
				discharge_formset_data.appointment_card_returned = get_appointment_card_returned
				discharge_formset_data.own_medication_return = get_own_medication_return
				discharge_formset_data.medication_reconcilation = get_medication_reconcilation
				discharge_formset_data.given_by = get_given_by
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


@login_required
def discharge_checklist_edit(request, username, pk):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Edit Discharge Checklist')
	patients = get_object_or_404(UserProfile, username=username)
	patientid = UserProfile.objects.get(username=username).id
	profiles = UserProfile.objects.filter(username=username)
	icnumbers = UserProfile.objects.filter(username=username).values_list('ic_number', flat=True).first()
	admissions = DischargeCheckList.objects.get(patient_id=patientid, id=pk)

	initial = {
		'id': pk,
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
		formset = DischargeCheckList_ModelFormSet(request.POST or None, queryset=DischargeCheckList.objects.filter(patient_id=patientid).filter(id=pk))

		if formset.is_valid():
			for item in formset:
#				discharge_formset_data = DischargeCheckList()
				discharge_formset_data = item.save(commit=False)
				discharge_formset_data.patient = patients
#				discharge_formset_data.id = pk
#				discharge_formset_data.id = item.cleaned_data['id']
				discharge_formset_data.date_time = item.cleaned_data['date_time']
				discharge_formset_data.discharge_status = ', '.join(item.cleaned_data['discharge_status'])
				discharge_formset_data.nasogastric_tube_date = item.cleaned_data['nasogastric_tube_date']
				discharge_formset_data.nasogastric_tube = ', '.join(item.cleaned_data['nasogastric_tube'])
				discharge_formset_data.urinary_catheter_date = item.cleaned_data['urinary_catheter_date']
				discharge_formset_data.urinary_catheter = ', '.join(item.cleaned_data['urinary_catheter'])
				discharge_formset_data.surgical_dressing_intact = ', '.join(item.cleaned_data['surgical_dressing_intact'])
				discharge_formset_data.spectacle_walking_aid_denture = ', '.join(item.cleaned_data['spectacle_walking_aid_denture'])
				discharge_formset_data.appointment_card_returned = ', '.join(item.cleaned_data['appointment_card_returned'])
				discharge_formset_data.own_medication_return = ', '.join(item.cleaned_data['own_medication_return'])
				discharge_formset_data.medication_reconcilation = ', '.join(item.cleaned_data['medication_reconcilation'])
				discharge_formset_data.given_by = item.cleaned_data['given_by']
				discharge_formset_data.medication_reconcilation_patient = item.cleaned_data['medication_reconcilation_patient']
				discharge_formset_data.save()

			messages.success(request, _(page_title + ' form has been save successfully.'))
			return redirect('patient:discharge_checklist_list', username=patients.username)
		else:
			messages.warning(request, formset.errors)
	else:
		formset = DischargeCheckList_ModelFormSet(queryset=DischargeCheckList.objects.filter(patient_id=patientid).filter(id=pk))

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
		'icnumbers': icnumbers,
		'formset': formset,
	}

	return render(request, 'patient/discharge_checklist/partial_edit.html', context)


class DischargeCheckListDeleteView(BSModalDeleteView):
	model = DischargeCheckList
	template_name = 'patient/discharge_checklist/partial_delete.html'
	page_title = _('Discharge CheckList Form')
	success_message = _(page_title + ' form was deleted.')

	def get_success_url(self):
		username = self.kwargs['username']
		return reverse_lazy('patient:discharge_checklist_list', kwargs={'username': username})


discharge_checklist_delete = DischargeCheckListDeleteView.as_view()
