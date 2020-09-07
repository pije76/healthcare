from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import ugettext as _
from django.urls import reverse, reverse_lazy

from patient.models import *
from patient.Forms.nursing import *
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
def nursing_list(request, username):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
    page_title = _('Nursing Report')
    patientid = UserProfile.objects.get(username=username).id
    patients = Nursing.objects.filter(patient=patientid)
    profiles = UserProfile.objects.filter(pk=patientid)

    context = {
        'logos': logos,
        'titles': titles,
        'page_title': page_title,
        'patients': patients,
        'profiles': profiles,
    }

    return render(request, 'patient/nursing/nursing_data.html', context)


@login_required
def nursing_create(request, username):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
    page_title = _('Nursing Report')
    patients = get_object_or_404(UserProfile, username=username)
    profiles = UserProfile.objects.filter(username=username)
    icnumbers = UserProfile.objects.filter(username=username).values_list('ic_number', flat=True).first()

    initial = {
        'patient': patients,
        'ic_number': icnumbers,
    }

    initial_formset = [{
        'patient': item.full_name,
        'nasogastric_tube_inserted_by': request.user,
        'nasogastric_remove_by': request.user,
    }
    for item in profiles]

    if request.method == 'POST':
        formset = Nursing_FormSet(request.POST or None)

        if formset.is_valid():
            for item in formset:
                profile = Nursing()
                profile.patient = patients
                profile.date_time = item.cleaned_data['date_time']
                profile.report = item.cleaned_data['report']
                profile.save()

            messages.success(request, _(page_title + ' form was created.'))
            return redirect('patient:patientdata_detail', username=patients.username)
        else:
            messages.warning(request, formset.errors)
    else:
        formset = Nursing_FormSet(initial=initial_formset)

    context = {
        'logos': logos,
        'titles': titles,
        'page_title': page_title,
        'patients': patients,
        'profiles': profiles,
        'icnumbers': icnumbers,
        'formset': formset,
    }

    return render(request, 'patient/nursing/nursing_form.html', context)


class NursingUpdateView(BSModalUpdateView):
    model = Nursing
    template_name = 'patient/nursing/partial_edit.html'
    form_class = Nursing_ModelForm
    page_title = _('Nursing Form')
    success_message = _(page_title + ' form has been save successfully.')

    def get_success_url(self):
        username = self.kwargs['username']
        return reverse_lazy('patient:nursing_list', kwargs={'username': username})


nursing_edit = NursingUpdateView.as_view()


class NursingDeleteView(BSModalDeleteView):
    model = Nursing
    template_name = 'patient/nursing/partial_delete.html'
    page_title = _('Nursing Form')
    success_message = _(page_title + ' form was deleted.')

    def get_success_url(self):
        username = self.kwargs['username']
        return reverse_lazy('patient:nursing_list', kwargs={'username': username})


nursing_delete = NursingDeleteView.as_view()
