from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import ugettext as _
from django.http import JsonResponse

from patient.models import *
from patient.Forms.maintenance import *
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
def maintenance_list(request, username):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
    page_title = _('Maintenance Form')
    patientid = UserProfile.objects.get(username=username).id
    patients = Maintenance.objects.filter(patient=patientid)
    profiles = UserProfile.objects.filter(pk=patientid)

    context = {
        'logos': logos,
        'titles': titles,
        'page_title': page_title,
        'patients': patients,
        'profiles': profiles,
    }

    return render(request, 'patient/maintenance/maintenance_data.html', context)


@login_required
def maintenance_create(request, username):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
    page_title = _('Maintenance Form')
    patients = get_object_or_404(UserProfile, username=username)
    profiles = UserProfile.objects.filter(username=username)
    icnumbers = UserProfile.objects.filter(username=username).values_list('ic_number', flat=True).first()

    initial = {
        'patient': patients,
        'ic_number': icnumbers,
        'reported_by': request.user,
    }

    initial_formset_factory = [
    {
        'patient': patients,
        'ic_number': icnumbers,
    }]

    if request.method == 'POST':
        formset = Maintenance_FormSet_Factory(request.POST or None)
        if formset.is_valid():
            for item in formset:
                profile = Maintenance()
                profile.patient = patients
                profile.date = item.cleaned_data['date']
                profile.items = item.cleaned_data['items']
                profile.location_room = item.cleaned_data['location_room']
                profile.reported_by = item.cleaned_data['reported_by']
                profile.status = item.cleaned_data['status']
                profile.save()

            messages.success(request, _(page_title + ' form was created.'))
            return redirect('patient:patientdata_detail', username=patients.username)
        else:
            messages.warning(request, formset.errors)
    else:
        formset = Maintenance_FormSet_Factory(initial=initial_formset_factory)

    context = {
        'logos': logos,
        'titles': titles,
        'page_title': page_title,
        'patients': patients,
        'profiles': profiles,
        'icnumbers': icnumbers,
        'formset': formset,
    }

    return render(request, 'patient/maintenance/maintenance_form.html', context)


class MaintenanceUpdateView(BSModalUpdateView):
    model = Maintenance
    template_name = 'patient/maintenance/partial_edit.html'
    form_class = MaintenanceForm
    page_title = _('Maintenance Form')
    success_message = _(page_title + ' form has been save successfully.')

    def get_success_url(self):
        username = self.kwargs['username']
        return reverse_lazy('patient:maintenance_list', kwargs={'username': username})


maintenance_edit = MaintenanceUpdateView.as_view()


class MaintenanceDeleteView(BSModalDeleteView):
    model = Maintenance
    template_name = 'patient/maintenance/partial_delete.html'
    page_title = _('Maintenance Form')
    success_message = _(page_title + ' form was deleted.')

    def get_success_url(self):
        username = self.kwargs['username']
        return reverse_lazy('patient:maintenance_list', kwargs={'username': username})


maintenance_delete = MaintenanceDeleteView.as_view()
