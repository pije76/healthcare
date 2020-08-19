from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import ugettext as _
from django.http import JsonResponse

from patient.models import *
from patient.Forms.medication import *
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
def medication_list(request, username):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
    page_title = _('Medication Records')
    patientid = UserProfile.objects.get(username=username).id
    patients = MedicationRecord.objects.filter(patient=patientid)
    profiles = UserProfile.objects.filter(pk=patientid)

    context = {
        'logos': logos,
        'titles': titles,
        'page_title': page_title,
        'patients': patients,
        'profiles': profiles,
    }

    return render(request, 'patient/medication/medication_data.html', context)




@login_required
def medication_record_create(request, username):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
    page_title = _('Medication Records')
    patients = get_object_or_404(UserProfile, username=username)
    profiles = UserProfile.objects.filter(username=username)
    icnumbers = UserProfile.objects.filter(username=username).values_list('ic_number', flat=True).first()

    initial = {
        'patient': patients,
        'ic_number': icnumbers,
        'staff': request.user,
    }

    if request.method == 'POST':
        form = MedicationRecordForm(request.POST or None)
        if form.is_valid():
            profile = MedicationRecord()
            profile.patient = patients
            profile.date = form.cleaned_data['date']
            profile.time = form.cleaned_data['time']
            profile.medication = form.cleaned_data['medication']
            profile.dosage = form.cleaned_data['dosage']
            profile.topup = form.cleaned_data['topup']
            profile.balance = form.cleaned_data['balance']
            profile.remark = form.cleaned_data['remark']
            profile.staff = form.cleaned_data['staff']
            profile.save()

            messages.success(request, _(page_title + ' form was created.'))
            return redirect('patient:patientdata_detail', username=patients.username)
        else:
            messages.warning(request, form.errors)
    else:
        form = MedicationRecordForm(initial=initial)

    context = {
        'logos': logos,
        'titles': titles,
        'page_title': page_title,
        'patients': patients,
        'profiles': profiles,
        'icnumbers': icnumbers,
        'form': form,
    }

    return render(request, 'patient/medication/medication_form.html', context)


class MedicationRecordUpdateView(BSModalUpdateView):
    model = MedicationRecord
    template_name = 'patient/medication/partial_edit.html'
    form_class = MedicationRecordForm
    page_title = _('MedicationRecord Form')
    success_message = _(page_title + ' form has been save successfully.')

    def get_success_url(self):
        username = self.kwargs['username']
        return reverse_lazy('patient:medication_data', kwargs={'username': username})


medication_edit = MedicationRecordUpdateView.as_view()


class MedicationRecordDeleteView(BSModalDeleteView):
    model = MedicationRecord
    template_name = 'patient/medication/partial_delete.html'
    page_title = _('MedicationRecord Form')
    success_message = _(page_title + ' form was deleted.')

    def get_success_url(self):
        username = self.kwargs['username']
        return reverse_lazy('patient:medication_data', kwargs={'username': username})


medication_delete = MedicationRecordDeleteView.as_view()

