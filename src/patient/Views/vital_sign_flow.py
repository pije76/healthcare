from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import ugettext as _
from django.http import JsonResponse

from patient.models import *
from patient.Forms.vital_sign_flow import *
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
def vital_sign_flow_list(request, username):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
    page_title = _('Vital Sign Flow Sheet')
    patientid = UserProfile.objects.get(username=username).id
    patients = VitalSignFlow.objects.filter(patient=patientid)
    profiles = UserProfile.objects.filter(pk=patientid)

    context = {
        'logos': logos,
        'titles': titles,
        'page_title': page_title,
        'patients': patients,
        'profiles': profiles,
    }

    return render(request, 'patient/vital_sign_flow/vital_sign_flow_data.html', context)



@login_required
def vital_sign_flow_create(request, username):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
    page_title = _('Vital Sign Flow Sheet')
    patients = get_object_or_404(UserProfile, username=username)
    profiles = UserProfile.objects.filter(username=username)
    icnumbers = UserProfile.objects.filter(username=username).values_list('ic_number', flat=True).first()

    initial = {
        'patient': patients,
        'ic_number': icnumbers,
    }

    if request.method == 'POST':
        form = VitalSignFlowForm(request.POST or None)
        if form.is_valid():
            profile = VitalSignFlow()
            profile.patient = patients
            profile.date = form.cleaned_data['date']
            profile.time = form.cleaned_data['time']
            profile.temp = form.cleaned_data['temp']
            profile.pulse = form.cleaned_data['pulse']
            profile.blood_pressure_systolic = form.cleaned_data['blood_pressure_systolic']
            profile.blood_pressure_diastolic = form.cleaned_data['blood_pressure_diastolic']
            profile.respiration = form.cleaned_data['respiration']
            profile.spo2_percentage = form.cleaned_data['spo2_percentage']
            profile.spo2_o2 = form.cleaned_data['spo2_o2']
            profile.save()

            messages.success(request, _(page_title + ' form was created.'))
            return redirect('patient:patientdata_detail', username=patients.username)
        else:
            messages.warning(request, form.errors)
    else:
        form = VitalSignFlowForm(initial=initial)

    context = {
        'logos': logos,
        'titles': titles,
        'page_title': page_title,
        'patients': patients,
        'profiles': profiles,
        'icnumbers': icnumbers,
        'form': form,
    }

    return render(request, 'patient/vital_sign_flow/vital_sign_flow_form.html', context)

class VitalSignFlowUpdateView(BSModalUpdateView):
    model = VitalSignFlow
    template_name = 'patient/vital_sign_flow/partial_edit.html'
    form_class = VitalSignFlowForm
    page_title = _('VitalSignFlow Form')
    success_message = _(page_title + ' form has been save successfully.')

    def get_success_url(self):
        username = self.kwargs['username']
        return reverse_lazy('patient:vital_sign_flow_data', kwargs={'username': username})


vital_sign_flow_edit = VitalSignFlowUpdateView.as_view()


class VitalSignFlowDeleteView(BSModalDeleteView):
    model = VitalSignFlow
    template_name = 'patient/vital_sign_flow/partial_delete.html'
    page_title = _('VitalSignFlow Form')
    success_message = _(page_title + ' form was deleted.')

    def get_success_url(self):
        username = self.kwargs['username']
        return reverse_lazy('patient:vital_sign_flow_data', kwargs={'username': username})


vital_sign_flow_delete = VitalSignFlowDeleteView.as_view()
