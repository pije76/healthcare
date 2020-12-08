from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import ugettext as _
from django.urls import reverse, reverse_lazy

from patient.models import *
from patient.Forms.physio_progress_note_sheet import *
from accounts.models import *
from customers.models import *

from bootstrap_modal_forms.generic import *


@login_required
def physio_progress_note_sheet_list(request, username):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(
        schema_name=schema_name).values_list('title', flat=True).first()
    page_title = _('Physiotherapy Progress Note Sheet')
    patientid = UserProfile.objects.get(username=username).id
    patients = PhysioProgressNoteSheet.objects.filter(patient=patientid)
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

    return render(request, 'patient/physio_progress_note_sheet/physio_progress_note_sheet_data.html', context)


@login_required
def physio_progress_note_sheet_create(request, username):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(
        schema_name=schema_name).values_list('title', flat=True).first()
    page_title = _('Physiotherapy Progress Note Sheet')
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
        form = PhysioProgressNoteSheet_ModelForm(request.POST or None)
        if form.is_valid():
            profile = PhysioProgressNoteSheet()
            profile.patient = patients
            profile.date_time = form.cleaned_data['date_time']
            profile.report = form.cleaned_data['report']
            profile.save()

            messages.success(request, _(page_title + ' form was created.'))
            return redirect('patient:patientdata_detail', username=patients.username)
        else:
            messages.warning(request, form.errors)
    else:
        form = PhysioProgressNoteSheet_ModelForm(initial=initial)

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

    return render(request, 'patient/physio_progress_note_sheet/physio_progress_note_sheet_form.html', context)


class PhysioProgressNoteSheetUpdateView(BSModalUpdateView):
    model = PhysioProgressNoteSheet
    template_name = 'patient/physio_progress_note_sheet/partial_edit.html'
    form_class = PhysioProgressNoteSheet_ModelForm
    page_title = _('PhysioProgressNoteSheet Form')
    success_message = _(page_title + ' form has been save successfully.')

    def get_form(self, form_class=None):
        form = super().get_form(form_class=None)
        form.fields['date_time'].label = _("Date/Time")
        form.fields['report'].label = _("Report")
        return form

    def get_success_url(self):
        username = self.kwargs['username']
        return reverse_lazy('patient:physio_progress_note_sheet_list', kwargs={'username': username})


physio_progress_note_sheet_edit = PhysioProgressNoteSheetUpdateView.as_view()


class PhysioProgressNoteSheetDeleteView(BSModalDeleteView):
    model = PhysioProgressNoteSheet
    template_name = 'patient/physio_progress_note_sheet/partial_delete.html'
    page_title = _('PhysioProgressNoteSheet Form')
    success_message = _(page_title + ' form was deleted.')

    def get_success_url(self):
        username = self.kwargs['username']
        return reverse_lazy('patient:physio_progress_note_sheet_list', kwargs={'username': username})


physio_progress_note_sheet_delete = PhysioProgressNoteSheetDeleteView.as_view()
