from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.db.models import F, Func, Value, CharField
from django.db.models import Value, CharField
from django.db.models.functions import Cast, Concat, ExtractYear, ExtractMonth, ExtractDay, ExtractHour, ExtractMinute
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.utils.translation import ugettext as _

from patient.models import *
from patient.Forms.urinary import *
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
def urinary_list(request, username):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
    page_title = _('Urinary Chart')
    patientid = UserProfile.objects.get(username=username).id
    patients = Urinary.objects.filter(patient=patientid)
    profiles = UserProfile.objects.filter(pk=patientid)

    context = {
        'logos': logos,
        'titles': titles,
        'page_title': page_title,
        'patients': patients,
        'profiles': profiles,
    }

    return render(request, 'patient/urinary/urinary_data.html', context)


@login_required
def urinary_create(request, username):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
    page_title = _('Urinary Chart')
    patients = get_object_or_404(UserProfile, username=username)
    profiles = UserProfile.objects.filter(username=username)
    icnumbers = UserProfile.objects.filter(username=username).values_list('ic_number', flat=True).first()

    initial = [{
        'patient': item.full_name,
        'urinary_catheter_inserted_by': request.user,
        'urinary_catheter_remove_by': request.user,
    }
    for item in profiles]

    if request.method == 'POST':
        formset = Urinary_FormSet(request.POST or None)

        if formset.is_valid():
            for item in formset:
                profile = Urinary()
                profile.patient = patients
                profile.urinary_catheter_date = item.cleaned_data['urinary_catheter_date']
                profile.urinary_catheter_size = item.cleaned_data['urinary_catheter_size']
                profile.urinary_catheter_type = item.cleaned_data['urinary_catheter_type']
                profile.urinary_catheter_due_date = item.cleaned_data['urinary_catheter_due_date']
                profile.urinary_catheter_inserted_by = item.cleaned_data['urinary_catheter_inserted_by']
                profile.urinary_catheter_remove_date = item.cleaned_data['urinary_catheter_remove_date']
                profile.urinary_catheter_remove_by = item.cleaned_data['urinary_catheter_remove_by']
                profile.save()

            messages.success(request, _(page_title + ' form was created.'))
            return redirect('patient:patientdata_detail', username=patients.username)
        else:
            messages.warning(request, formset.errors)

    else:
        formset = Urinary_FormSet(initial=initial)

    context = {
        'logos': logos,
        'titles': titles,
        'page_title': page_title,
        'patients': patients,
        'profiles': profiles,
        'icnumbers': icnumbers,
        'formset': formset,
    }

    return render(request, 'patient/urinary/urinary_form.html', context)


class UrinaryUpdateView(BSModalUpdateView):
    model = Urinary
    template_name = 'patient/urinary/partial_edit.html'
    form_class = Urinary_ModelForm
    page_title = _('Urinary Form')
    success_message = _(page_title + ' form has been save successfully.')

    def get_success_url(self):
        username = self.kwargs['username']
        return reverse_lazy('patient:urinary_list', kwargs={'username': username})


urinary_edit = UrinaryUpdateView.as_view()


class UrinaryDeleteView(BSModalDeleteView):
    model = Urinary
    template_name = 'patient/urinary/partial_delete.html'
    page_title = _('Urinary Form')
    success_message = _(page_title + ' form was deleted.')

    def get_success_url(self):
        username = self.kwargs['username']
        return reverse_lazy('patient:urinary_list', kwargs={'username': username})


urinary_delete = UrinaryDeleteView.as_view()
