from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import ugettext as _
from django.urls import reverse, reverse_lazy

from patient.models import *
from patient.Forms.physiotherapy_general_assessment import *
from accounts.models import *
from customers.models import *

from bootstrap_modal_forms.generic import *


@login_required
def physiotherapy_general_assessment_list(request, username):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(
        schema_name=schema_name).values_list('title', flat=True).first()
    page_title = _('Physiotherapy General Assessment Form')
    patientid = UserProfile.objects.get(username=username).id
    patients = PhysiotherapyGeneralAssessment.objects.filter(patient=patientid)
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

    return render(request, 'patient/physiotherapy_general_assessment/physiotherapy_general_assessment_data.html', context)


@login_required
def physiotherapy_general_assessment_create(request, username):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(
        schema_name=schema_name).values_list('title', flat=True).first()
    page_title = _('Physiotherapy General Assessment Form')
    patients = get_object_or_404(UserProfile, username=username)
    profiles = UserProfile.objects.filter(username=username)
    icnumbers = UserProfile.objects.filter(
        username=username).values_list('ic_number', flat=True).first()
    themes = request.session.get('theme')

    initial = {
        'patient': patients,
        'ic_number': icnumbers,
    }

    if request.method == 'POST':
        form = PhysiotherapyGeneralAssessment_Form(
            request.POST or None, request.FILES or None)
        if form.is_valid():
            profile = PhysiotherapyGeneralAssessment()
            profile.patient = patients
            profile.doctor_diagnosis = form.cleaned_data['doctor_diagnosis']
            profile.doctor_management = form.cleaned_data['doctor_management']
            profile.problem = form.cleaned_data['problem']
            profile.front_body = form.cleaned_data['front_body']
            profile.back_body = form.cleaned_data['back_body']
            profile.pain_scale = form.cleaned_data['pain_scale']
            profile.comments = form.cleaned_data['comments']
            profile.current_history = form.cleaned_data['current_history']
            profile.past_history = form.cleaned_data['past_history']
            profile.special_question = form.cleaned_data['special_question']
            profile.general_health = form.cleaned_data['general_health']
            profile.pmx_surgery = form.cleaned_data['pmx_surgery']
            profile.ix_mri_x_ray = form.cleaned_data['ix_mri_x_ray']
            profile.medications_steroids = form.cleaned_data['medications_steroids']
            profile.occupation_recreation = form.cleaned_data['occupation_recreation']
            profile.palpation = form.cleaned_data['palpation']
            profile.pacemaker_hearing_aid = form.cleaned_data['pacemaker_hearing_aid']
            profile.splinting = form.cleaned_data['splinting']

            profile.physical_examination_movement = form.cleaned_data[
                'physical_examination_movement']
            profile.neurological_reflexes = form.cleaned_data['neurological_reflexes']
            profile.neurological_motor = form.cleaned_data['neurological_motor']
            profile.neurological_sensation = form.cleaned_data['neurological_sensation']

            profile.muscle_power = form.cleaned_data['muscle_power']
            profile.clearing_test_other_joint = form.cleaned_data['clearing_test_other_joint']
            profile.physiotherapists_impression = form.cleaned_data['physiotherapists_impression']

            profile.functional_activities = form.cleaned_data['functional_activities']
            profile.short_term_goals = form.cleaned_data['short_term_goals']
            profile.long_term_goals = form.cleaned_data['long_term_goals']
            profile.special_test = form.cleaned_data['special_test']
            profile.plan_treatment = form.cleaned_data['plan_treatment']
            profile.date_time = form.cleaned_data['date_time']
            profile.attending_physiotherapist = form.cleaned_data['attending_physiotherapist']
            profile.save()

            messages.success(request, _(page_title + ' form was created.'))
            return redirect('patient:patientdata_detail', username=patients.username)
        else:
            messages.warning(request, form.errors)
    else:
        form = PhysiotherapyGeneralAssessment_Form(initial=initial)

    context = {
        'logos': logos,
        'titles': titles,
        'page_title': page_title,
        'patients': patients,
        'profiles': profiles,
        'icnumbers': icnumbers,
        'form': form,
        "themes": themes,
    }

    return render(request, 'patient/physiotherapy_general_assessment/physiotherapy_general_assessment_form.html', context)


class PhysiotherapyGeneralAssessmentUpdateView(BSModalUpdateView):
    model = PhysiotherapyGeneralAssessment
    template_name = 'patient/physiotherapy_general_assessment/partial_edit.html'
    form_class = PhysiotherapyGeneralAssessment_ModelForm
    page_title = _('PhysiotherapyGeneralAssessment Form')
    success_message = _(page_title + ' form has been save successfully.')

    def get_form(self, form_class=None):
        form = super().get_form(form_class=None)
        form.fields['doctor_diagnosis'].label = _("Doctor Diagnosis")
        form.fields['doctor_management'].label = _("Doctor Management")
        form.fields['problem'].label = _("Problem")
        form.fields['front_body'].label = _("Front Body")
        form.fields['back_body'].label = _("Back Body")
        form.fields['pain_scale'].label = _("Pain Scale")
        form.fields['comments'].label = _("Comments")
        form.fields['current_history'].label = _("Current History")
        form.fields['past_history'].label = _("Past History")
        form.fields['special_question'].label = _("Special Question")
        form.fields['general_health'].label = _("General Health")
        form.fields['pmx_surgery'].label = _("PMX Surgery")
        form.fields['ix_mri_x_ray'].label = _("IX MRI X-Ray")
        form.fields['medications_steroids'].label = _("Medications Steroids")
        form.fields['occupation_recreation'].label = _("Occupation Recreation")
        form.fields['palpation'].label = _("Palpation")
        form.fields['pacemaker_hearing_aid'].label = _("Pacemaker Hearing Aid")
        form.fields['splinting'].label = _("Splinting")
        form.fields['physical_examination_movement'].label = _(
            "Physical Examination Movement")
        form.fields['neurological_reflexes'].label = _("Neurological Reflexes")
        form.fields['neurological_motor'].label = _("Neurological Motor")
        form.fields['neurological_sensation'].label = _(
            "Neurological Sensation")
        form.fields['muscle_power'].label = _("Muscle Power")
        form.fields['clearing_test_other_joint'].label = _(
            "Clearing Test Other Joint")
        form.fields['physiotherapists_impression'].label = _(
            "Physiotherapists Impression")
        form.fields['functional_activities'].label = _("Functional Activities")
        form.fields['short_term_goals'].label = _("Short Term Goals")
        form.fields['long_term_goals'].label = _("Long Term Goals")
        form.fields['special_test'].label = _("Special Test")
        form.fields['plan_treatment'].label = _("Plan Treatment")
        form.fields['date_time'].label = _("Date & Time")
        form.fields['attending_physiotherapist'].label = _(
            "Attending Physiotherapist")
        return form

    def get_success_url(self):
        username = self.kwargs['username']
        return reverse_lazy('patient:physiotherapy_general_assessment_list', kwargs={'username': username})


physiotherapy_general_assessment_edit = PhysiotherapyGeneralAssessmentUpdateView.as_view()


class PhysiotherapyGeneralAssessmentDeleteView(BSModalDeleteView):
    model = PhysiotherapyGeneralAssessment
    template_name = 'patient/physiotherapy_general_assessment/partial_delete.html'
    page_title = _('PhysiotherapyGeneralAssessment Form')
    success_message = _(page_title + ' form was deleted.')

    def get_success_url(self):
        username = self.kwargs['username']
        return reverse_lazy('patient:physiotherapy_general_assessment_list', kwargs={'username': username})


physiotherapy_general_assessment_delete = PhysiotherapyGeneralAssessmentDeleteView.as_view()
