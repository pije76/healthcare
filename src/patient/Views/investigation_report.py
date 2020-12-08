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
from patient.Forms.investigation_report import *
from accounts.models import *
from customers.models import *

from bootstrap_modal_forms.generic import *


@login_required
def investigation_report_list(request, username):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(
        schema_name=schema_name).values_list('title', flat=True).first()
    page_title = _('Investigation Report Chart')
    patientid = UserProfile.objects.get(username=username).id
    patients = InvestigationReport.objects.filter(patient=patientid)
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

    return render(request, 'patient/investigation_report/investigation_report_data.html', context)


@login_required
def investigation_report_create(request, username):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(
        schema_name=schema_name).values_list('title', flat=True).first()
    page_title = _('Investigation Report Chart')
    patients = get_object_or_404(UserProfile, username=username)
    profiles = UserProfile.objects.filter(username=username)
    icnumbers = UserProfile.objects.filter(
        username=username).values_list('ic_number', flat=True).first()
    themes = request.session.get('theme')

    initial = {
        'patient': patients,
        'ic_number': icnumbers,
        'done_by': request.user,
    }

    initial_formset_factory = [
        {
            'patient': patients,
            'ic_number': icnumbers,
        }]

    if request.method == 'POST':
        form = InvestigationReport_Form(
            request.POST or None, request.FILES or None)

        if form.is_valid():
            profile = InvestigationReport()
            profile.patient = patients
            profile.date = form.cleaned_data['date']
            profile.file_upload = form.cleaned_data['file_upload']
            profile.save()

            messages.success(request, _(page_title + ' form was created.'))
            return redirect('patient:patientdata_detail', username=patients.username)
        else:
            messages.warning(request, form.errors)
    else:
        form = InvestigationReport_Form(initial=initial)

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

    return render(request, 'patient/investigation_report/investigation_report_form.html', context)


class InvestigationReportUpdateView(BSModalUpdateView):
    model = InvestigationReport
    template_name = 'patient/investigation_report/partial_edit.html'
    form_class = InvestigationReport_ModelForm
    page_title = _('InvestigationReport Form')
    success_message = _(page_title + ' form has been save successfully.')

    def get_form(self, form_class=None):
        form = super().get_form(form_class=None)
        form.fields['date'].label = _("Date")
        form.fields['file_upload'].label = _("File Upload")
        return form

    def get_success_url(self):
        username = self.kwargs['username']
        return reverse_lazy('patient:investigation_report_list', kwargs={'username': username})


investigation_report_edit = InvestigationReportUpdateView.as_view()


class InvestigationReportDeleteView(BSModalDeleteView):
    model = InvestigationReport
    template_name = 'patient/investigation_report/partial_delete.html'
    page_title = _('InvestigationReport Form')
    success_message = _(page_title + ' form was deleted.')

    def get_success_url(self):
        username = self.kwargs['username']
        return reverse_lazy('patient:investigation_report_list', kwargs={'username': username})


investigation_report_delete = InvestigationReportDeleteView.as_view()
