from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import ugettext as _
from django.http import JsonResponse

from patient.models import *
from patient.Forms.physiotherapy_general_assessment import *
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
def physiotherapy_general_assessment_list(request, username):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
    page_title = _('Physiotherapy General Assessment Form')
    patientid = UserProfile.objects.get(username=username).id
    patients = PhysiotherapyGeneralAssessment.objects.filter(patient=patientid)
    profiles = UserProfile.objects.filter(pk=patientid)

    context = {
        'logos': logos,
        'titles': titles,
        'page_title': page_title,
        'patients': patients,
        'profiles': profiles,
    }

    return render(request, 'patient/physiotherapy_general_assessment/physiotherapy_general_assessment_data.html', context)


@login_required
def physiotherapy_general_assessment_create(request, username):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
    page_title = _('Physiotherapy General Assessment Form')
    patients = get_object_or_404(UserProfile, username=username)
    profiles = UserProfile.objects.filter(username=username)
    icnumbers = UserProfile.objects.filter(username=username).values_list('ic_number', flat=True).first()

    initial = {
        'patient': patients,
        'ic_number': icnumbers,
    }

    if request.method == 'POST':
        form = PhysiotherapyGeneralAssessmentForm(request.POST or None)
        if form.is_valid():
            profile = PhysiotherapyGeneralAssessment()
            profile.patient = patients
            profile.doctor_diagnosis = form.cleaned_data['doctor_diagnosis']
            profile.doctor_management = form.cleaned_data['doctor_management']
            profile.problem = form.cleaned_data['problem']
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

            profile.physical_examination_movement = form.cleaned_data['physical_examination_movement']
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
        form = PhysiotherapyGeneralAssessmentForm(initial=initial)

    context = {
        'logos': logos,
        'titles': titles,
        'page_title': page_title,
        'patients': patients,
        'profiles': profiles,
        'icnumbers': icnumbers,
        'form': form,
    }

    return render(request, 'patient/physiotherapy_general_assessment/physiotherapy_general_assessment_form.html', context)



class PhysiotherapyGeneralAssessmentUpdateView(BSModalUpdateView):
    model = PhysiotherapyGeneralAssessment
    template_name = 'patient/physiotherapy_general_assessment/partial_edit.html'
    form_class = PhysiotherapyGeneralAssessmentForm
    page_title = _('PhysiotherapyGeneralAssessment Form')
    success_message = _(page_title + ' form has been save successfully.')

    def get_success_url(self):
        username = self.kwargs['username']
        return reverse_lazy('patient:physiotherapy_general_assessment_data', kwargs={'username': username})


physiotherapy_general_assessment_edit = PhysiotherapyGeneralAssessmentUpdateView.as_view()


class PhysiotherapyGeneralAssessmentDeleteView(BSModalDeleteView):
    model = PhysiotherapyGeneralAssessment
    template_name = 'patient/physiotherapy_general_assessment/partial_delete.html'
    page_title = _('PhysiotherapyGeneralAssessment Form')
    success_message = _(page_title + ' form was deleted.')

    def get_success_url(self):
        username = self.kwargs['username']
        return reverse_lazy('patient:physiotherapy_general_assessment_data', kwargs={'username': username})


physiotherapy_general_assessment_delete = PhysiotherapyGeneralAssessmentDeleteView.as_view()

