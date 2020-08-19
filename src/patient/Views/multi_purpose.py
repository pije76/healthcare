from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import ugettext as _
from django.http import JsonResponse

from patient.models import *
from patient.Forms.multi_purpose import *
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
def multi_purpose_list(request, username):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
    page_title = _('Multipurpose Chart')
    patientid = UserProfile.objects.get(username=username).id
    patients = Multipurpose.objects.filter(patient=patientid)
    profiles = UserProfile.objects.filter(pk=patientid)

    context = {
        'logos': logos,
        'titles': titles,
        'page_title': page_title,
        'patients': patients,
        'profiles': profiles,
    }

    return render(request, 'patient/multi_purpose/multi_purpose_chart_data.html', context)


@login_required
def multi_purpose_create(request, username):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
    page_title = _('Multipurpose Chart')
    patients = get_object_or_404(UserProfile, username=username)
    profiles = UserProfile.objects.filter(username=username)
    icnumbers = UserProfile.objects.filter(username=username).values_list('ic_number', flat=True).first()

    initial = {
        'patient': patients,
        'ic_number': icnumbers,
    }

    if request.method == 'POST':
        form = MultipurposeForm(request.POST or None)
        if form.is_valid():
            profile = Multipurpose()
            profile.patient = patients
            profile.date_time = form.cleaned_data['date_time']
            profile.symptom = form.cleaned_data['symptom']
            profile.remark = form.cleaned_data['remark']
            profile.save()

            messages.success(request, _(page_title + ' form was created.'))
            return redirect('patient:patientdata_detail', username=patients.username)
        else:
            messages.warning(request, form.errors)
    else:
        form = MultipurposeForm(initial=initial)

    context = {
        'logos': logos,
        'titles': titles,
        'page_title': page_title,
        'patients': patients,
        'profiles': profiles,
        'icnumbers': icnumbers,
        'form': form,
    }

    return render(request, 'patient/multi_purpose/multi_purpose_chart_form.html', context)


class MultipurposeUpdateView(BSModalUpdateView):
    model = Multipurpose
    template_name = 'patient/multi_purpose/partial_edit.html'
    form_class = MultipurposeForm
    page_title = _('Multipurpose Form')
    success_message = _(page_title + ' form has been save successfully.')

    def get_success_url(self):
        username = self.kwargs['username']
        return reverse_lazy('patient:multi_purpose_data', kwargs={'username': username})


multi_purpose_edit = MultipurposeUpdateView.as_view()


class MultipurposeDeleteView(BSModalDeleteView):
    model = Multipurpose
    template_name = 'patient/multi_purpose/partial_delete.html'
    page_title = _('Multipurpose Form')
    success_message = _(page_title + ' form was deleted.')

    def get_success_url(self):
        username = self.kwargs['username']
        return reverse_lazy('patient:multi_purpose_data', kwargs={'username': username})


multi_purpose_delete = MultipurposeDeleteView.as_view()
