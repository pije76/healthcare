from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import ugettext as _
from django.urls import reverse, reverse_lazy

from patient.models import *
from patient.Forms.vital_sign_flow import *
from accounts.models import *
from customers.models import *

from bootstrap_modal_forms.generic import *


@login_required
def vital_sign_flow_list(request, username):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(
        schema_name=schema_name).values_list('title', flat=True).first()
    page_title = _('Vital Sign Chart')
    patientid = UserProfile.objects.get(username=username).id
    patients = VitalSignFlow.objects.filter(patient=patientid)
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

    return render(request, 'patient/vital_sign_flow/vital_sign_flow_data.html', context)


@login_required
def vital_sign_flow_create(request, username):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(
        schema_name=schema_name).values_list('title', flat=True).first()
    page_title = _('Vital Sign Chart')
    patients = get_object_or_404(UserProfile, username=username)
    profiles = UserProfile.objects.filter(username=username)
    icnumbers = UserProfile.objects.filter(
        username=username).values_list('ic_number', flat=True).first()
    themes = request.session.get('theme')

    initial = [{
        'patient': item.full_name,
        'done_by': request.user,
    }
        for item in profiles]

    initial_formset_factory = [
        {
            'patient': patients,
            'ic_number': icnumbers,
        }]

    if request.method == 'POST':
        formset = VitalSignFlow_FormSet(request.POST or None)

        if formset.is_valid():
            for item in formset:
                profile = VitalSignFlow()
                profile.patient = patients
                profile.date = item.cleaned_data['date']
                profile.time = item.cleaned_data['time']
                profile.temp = item.cleaned_data['temp']
                profile.pulse = item.cleaned_data['pulse']
                profile.blood_pressure_systolic = item.cleaned_data['blood_pressure_systolic']
                profile.blood_pressure_diastolic = item.cleaned_data['blood_pressure_diastolic']
                profile.respiration = item.cleaned_data['respiration']
                profile.spo2_percentage = item.cleaned_data['spo2_percentage']
                profile.spo2_o2 = item.cleaned_data['spo2_o2']
                profile.save()

            messages.success(request, _(page_title + ' form was created.'))
            return redirect('patient:patientdata_detail', username=patients.username)
        else:
            messages.warning(request, formset.errors)
    else:
        formset = VitalSignFlow_FormSet(initial=initial)

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

    return render(request, 'patient/vital_sign_flow/vital_sign_flow_form.html', context)


class VitalSignFlowUpdateView(BSModalUpdateView):
    model = VitalSignFlow
    template_name = 'patient/vital_sign_flow/partial_edit.html'
    form_class = VitalSignFlow_ModelForm
    page_title = _('VitalSignFlow Form')
    success_message = _(page_title + ' form has been save successfully.')

    def get_form(self, form_class=None):
        form = super().get_form(form_class=None)
        form.fields['date'].label = _("Date")
        form.fields['time'].label = _("Time")
        form.fields['temp'].label = _("Temp")
        form.fields['pulse'].label = _("Pulse")
        form.fields['blood_pressure_systolic'].label = _(
            "Blood Pressure Systolic")
        form.fields['blood_pressure_diastolic'].label = _(
            "Blood Pressure Diastolic")
        form.fields['respiration'].label = _("Respiration")
        form.fields['spo2_percentage'].label = _("SPO2-Percentage")
        form.fields['spo2_o2'].label = _("SPO2-O2")
        return form

    def get_success_url(self):
        username = self.kwargs['username']
        return reverse_lazy('patient:vital_sign_flow_list', kwargs={'username': username})


vital_sign_flow_edit = VitalSignFlowUpdateView.as_view()


class VitalSignFlowDeleteView(BSModalDeleteView):
    model = VitalSignFlow
    template_name = 'patient/vital_sign_flow/partial_delete.html'
    page_title = _('VitalSignFlow Form')
    success_message = _(page_title + ' form was deleted.')

    def get_success_url(self):
        username = self.kwargs['username']
        return reverse_lazy('patient:vital_sign_flow_list', kwargs={'username': username})


vital_sign_flow_delete = VitalSignFlowDeleteView.as_view()
