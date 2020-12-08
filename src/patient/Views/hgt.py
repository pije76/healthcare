from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.db.models import F, Func, Value, CharField
from django.db.models import Value, CharField
from django.db.models.functions import Cast, Concat, ExtractYear, ExtractMonth, ExtractDay, ExtractHour, ExtractMinute
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.utils.translation import ugettext as _
from django.views.generic import View
from django.views.generic.detail import DetailView

from patient.models import *
from patient.Forms.hgt import *
from accounts.models import *
from customers.models import *

from bootstrap_modal_forms.generic import *


@login_required
def hgt_list(request, username):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(
        schema_name=schema_name).values_list('title', flat=True).first()
    page_title = _('HGT Chart')
    patientid = UserProfile.objects.get(username=username).id
    patients = HGT.objects.filter(patient=patientid)
    profiles = UserProfile.objects.filter(pk=patientid)
    username = UserProfile.objects.get(username=username).username
    themes = request.session.get('theme')

    context = {
        'logos': logos,
        'titles': titles,
        'page_title': page_title,
        'patients': patients,
        'profiles': profiles,
        'username': username,
        "themes": themes,
    }

    return render(request, 'patient/hgt/hgt_data.html', context)


@login_required
def hgt_create(request, username):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(
        schema_name=schema_name).values_list('title', flat=True).first()
    page_title = _('HGT Chart')
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
        formset = HGT_FormSet(request.POST or None)

        if formset.is_valid():
            for item in formset:
                profile = HGT()
                profile.patient = patients
                profile.date = item.cleaned_data['date']
                profile.time = item.cleaned_data['time']
                profile.blood_glucose_reading = item.cleaned_data['blood_glucose_reading']
                profile.remark = item.cleaned_data['remark']
                profile.done_by = item.cleaned_data['done_by']
                profile.save()

            messages.success(request, _(page_title + ' form was created.'))
            return redirect('patient:patientdata_detail', username=patients.username)
        else:
            messages.warning(request, formset.errors)
    else:
        formset = HGT_FormSet(initial=initial)

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

    return render(request, 'patient/hgt/hgt_form.html', context)


class HGTUpdateView(BSModalUpdateView):
    model = HGT
    template_name = 'patient/hgt/partial_edit.html'
    form_class = HGT_ModelForm
    page_title = _('HGT Form')
    success_message = _(page_title + ' form has been save successfully.')

    def get_form(self, form_class=None):
        form = super().get_form(form_class=None)
        form.fields['date'].label = _("Date")
        form.fields['time'].label = _("Time")
        form.fields['blood_glucose_reading'].label = _("Blood Glucose Reading")
        form.fields['remark'].label = _("Remark")
        form.fields['done_by'].label = _("Done by")
        return form

    def get_success_url(self):
        username = self.kwargs['username']
        return reverse_lazy('patient:hgt_list', kwargs={'username': username})


hgt_edit = HGTUpdateView.as_view()


class HGTDeleteView(BSModalDeleteView):
    model = HGT
    template_name = 'patient/hgt/partial_delete.html'
    page_title = _('HGT Form')
    success_message = _(page_title + ' form was deleted.')

    def get_success_url(self):
        username = self.kwargs['username']
        return reverse_lazy('patient:hgt_list', kwargs={'username': username})


hgt_delete = HGTDeleteView.as_view()
