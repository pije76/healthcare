from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import ugettext as _
from django.urls import reverse, reverse_lazy

from patient.models import *
from patient.Forms.medication_record import *
from accounts.models import *
from customers.models import *

from bootstrap_modal_forms.generic import *


@login_required
def medication_record_list(request, username):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(
        schema_name=schema_name).values_list('title', flat=True).first()
    page_title = _('Medication Records')
    patientid = UserProfile.objects.get(username=username).id
    patients = MedicationRecord.objects.filter(patient=patientid)
    profiles = UserProfile.objects.filter(pk=patientid)
    themes = request.session.get('theme')

    context = {
        'logos': logos,
        'titles': titles,
        'page_title': page_title,
        'patients': patients,
        'profiles': profiles,
        "themes": themes,
    }

    return render(request, 'patient/medication_record/medication_data.html', context)


@login_required
def medication_record_create(request, username):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(
        schema_name=schema_name).values_list('title', flat=True).first()
    page_title = _('Medication Records')
    patients = get_object_or_404(UserProfile, username=username)
    profiles = UserProfile.objects.filter(username=username)
    icnumbers = UserProfile.objects.filter(
        username=username).values_list('ic_number', flat=True).first()
    themes = request.session.get('theme')

    initial = [{
        'patient': item.full_name,
        'staff': request.user,
    }
        for item in profiles]

    initial_formset_factory = [
        {
            'patient': patients,
            'ic_number': icnumbers,
        }]

    if request.method == 'POST':
        formset = MedicationRecord_FormSet(request.POST or None)
        if formset.is_valid():
            for item in formset:
                profile = MedicationRecord()
                profile.patient = patients
                profile.date = item.cleaned_data['date']
                profile.time = item.cleaned_data['time']
                profile.medication_medicine = item.cleaned_data['medication_medicine']
                profile.dosage = item.cleaned_data['dosage']
                profile.unit = item.cleaned_data['unit']
                profile.topup = item.cleaned_data['topup']
                profile.balance = item.cleaned_data['balance']
                profile.remark = item.cleaned_data['remark']
                profile.staff = item.cleaned_data['staff']
                profile.save()

            messages.success(request, _(page_title + ' form was created.'))
            return redirect('patient:patientdata_detail', username=patients.username)
        else:
            messages.warning(request, formset.errors)
    else:
        formset = MedicationRecord_FormSet(initial=initial)

    context = {
        'logos': logos,
        'titles': titles,
        'page_title': page_title,
        'patients': patients,
        'profiles': profiles,
        'icnumbers': icnumbers,
        'formset': formset,
        "themes": themes,
    }

    return render(request, 'patient/medication_record/medication_form.html', context)


class MedicationRecordUpdateView(BSModalUpdateView):
    model = MedicationRecord
    template_name = 'patient/medication_record/partial_edit.html'
    form_class = MedicationRecord_ModelForm
    page_title = _('MedicationRecord Form')
    success_message = _(page_title + ' form has been save successfully.')

    def get_form(self, form_class=None):
        form = super().get_form(form_class=None)
        form.fields['date'].label = _("Date")
        form.fields['time'].label = _("Time")
        form.fields['medication_medicine'].label = _("Drug Name")
        form.fields['dosage'].label = _("Dosage")
        form.fields['unit'].label = _("Unit")
        form.fields['topup'].label = _("Top Up")
        form.fields['balance'].label = _("Balance")
        form.fields['remark'].label = _("Remark")
        form.fields['staff'].label = _("Staff")
        return form

    def get_success_url(self):
        username = self.kwargs['username']
        return reverse_lazy('patient:medication_record_list', kwargs={'username': username})


medication_record_edit = MedicationRecordUpdateView.as_view()


class MedicationRecordDeleteView(BSModalDeleteView):
    model = MedicationRecord
    template_name = 'patient/medication_record/partial_delete.html'
    page_title = _('MedicationRecord Form')
    success_message = _(page_title + ' form was deleted.')

    def get_success_url(self):
        username = self.kwargs['username']
        return reverse_lazy('patient:medication_record_list', kwargs={'username': username})


medication_record_delete = MedicationRecordDeleteView.as_view()
