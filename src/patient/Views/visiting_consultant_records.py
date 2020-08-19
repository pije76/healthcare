from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import ugettext as _
from django.http import JsonResponse

from patient.models import *
from patient.Forms.visiting_consultant_records import *
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
def visiting_consultant_records_list(request, username):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
    page_title = _('Visiting Consultant Records')
    patientid = UserProfile.objects.get(username=username).id
    patients = VisitingConsultant.objects.filter(patient=patientid)
    profiles = UserProfile.objects.filter(pk=patientid)

    context = {
        'logos': logos,
        'titles': titles,
        'page_title': page_title,
        'patients': patients,
        'profiles': profiles,
    }

    return render(request, 'patient/visiting_consultant_records/visiting_consultant_records_data.html', context)



@login_required
def visiting_consultant_records_create(request, username):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
    page_title = _('Visiting Consultant Records')
    patients = get_object_or_404(UserProfile, username=username)
    profiles = UserProfile.objects.filter(username=username)
    icnumbers = UserProfile.objects.filter(username=username).values_list('ic_number', flat=True).first()

    initial = {
        'patient': patients,
        'ic_number': icnumbers,
    }

    if request.method == 'POST':
        form = VisitingConsultantForm(request.POST or None)
        if form.is_valid():
            profile = VisitingConsultant()
            profile.patient = patients
            profile.date_time = form.cleaned_data['date_time']
            profile.complaints = form.cleaned_data['complaints']
            profile.treatment_orders = form.cleaned_data['treatment_orders']
            profile.consultant = form.cleaned_data['consultant']
            profile.save()

            messages.success(request, _(page_title + ' form was created.'))
            return redirect('patient:patientdata_detail', username=patients.username)
        else:
            messages.warning(request, form.errors)
    else:
        form = VisitingConsultantForm(initial=initial)

    context = {
        'logos': logos,
        'titles': titles,
        'page_title': page_title,
        'patients': patients,
        'profiles': profiles,
        'icnumbers': icnumbers,
        'form': form,
    }

    return render(request, 'patient/visiting_consultant_records/visiting_consultant_records_form.html', context)

class VisitingConsultantUpdateView(BSModalUpdateView):
    model = VisitingConsultant
    template_name = 'patient/visiting_consultant_records/partial_edit.html'
    form_class = VisitingConsultantForm
    page_title = _('VisitingConsultant Form')
    success_message = _(page_title + ' form has been save successfully.')

    def get_success_url(self):
        username = self.kwargs['username']
        return reverse_lazy('patient:visiting_consultant_records_data', kwargs={'username': username})


visiting_consultant_records_edit = VisitingConsultantUpdateView.as_view()


class VisitingConsultantDeleteView(BSModalDeleteView):
    model = VisitingConsultant
    template_name = 'patient/visiting_consultant_records/partial_delete.html'
    page_title = _('VisitingConsultant Form')
    success_message = _(page_title + ' form was deleted.')

    def get_success_url(self):
        username = self.kwargs['username']
        return reverse_lazy('patient:visiting_consultant_records_data', kwargs={'username': username})


visiting_consultant_records_delete = VisitingConsultantDeleteView.as_view()
