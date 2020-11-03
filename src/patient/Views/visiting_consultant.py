from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import ugettext as _
from django.urls import reverse, reverse_lazy

from patient.models import *
from patient.Forms.visiting_consultant import *
from accounts.models import *
from customers.models import *

from bootstrap_modal_forms.generic import *


@login_required
def visiting_consultant_list(request, username):
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

    return render(request, 'patient/visiting_consultant/visiting_consultant_data.html', context)


@login_required
def visiting_consultant_create(request, username):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
    page_title = _('Visiting Consultant Records')
    patients = get_object_or_404(UserProfile, username=username)
    profiles = UserProfile.objects.filter(username=username)
    icnumbers = UserProfile.objects.filter(username=username).values_list('ic_number', flat=True).first()

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
        formset = VisitingConsultant_FormSet(request.POST or None)
        if formset.is_valid():
            for item in formset:
                profile = VisitingConsultant()
                profile.patient = patients
                profile.date_time = item.cleaned_data['date_time']
                profile.complaints = item.cleaned_data['complaints']
                profile.treatment_orders = item.cleaned_data['treatment_orders']
                profile.consultant = item.cleaned_data['consultant']
                profile.save()

            messages.success(request, _(page_title + ' form was created.'))
            return redirect('patient:patientdata_detail', username=patients.username)
        else:
            messages.warning(request, formset.errors)
    else:
        formset = VisitingConsultant_FormSet(initial=initial)

    context = {
        'logos': logos,
        'titles': titles,
        'page_title': page_title,
        'patients': patients,
        'profiles': profiles,
        'icnumbers': icnumbers,
        'formset': formset,
    }

    return render(request, 'patient/visiting_consultant/visiting_consultant_form.html', context)

class VisitingConsultantUpdateView(BSModalUpdateView):
    model = VisitingConsultant
    template_name = 'patient/visiting_consultant/partial_edit.html'
    form_class = VisitingConsultant_ModelForm
    page_title = _('VisitingConsultant Form')
    success_message = _(page_title + ' form has been save successfully.')

    def get_form(self, form_class=None):
        form = super().get_form(form_class=None)
        form.fields['date_time'].label = _("Date")
        form.fields['complaints'].label = _("Complaints")
        form.fields['treatment_orders'].label = _("Treatment Orders")
        form.fields['consultant'].label = _("Consultant")
        return form

    def get_success_url(self):
        username = self.kwargs['username']
        return reverse_lazy('patient:visiting_consultant_list', kwargs={'username': username})


visiting_consultant_edit = VisitingConsultantUpdateView.as_view()


class VisitingConsultantDeleteView(BSModalDeleteView):
    model = VisitingConsultant
    template_name = 'patient/visiting_consultant/partial_delete.html'
    page_title = _('VisitingConsultant Form')
    success_message = _(page_title + ' form was deleted.')

    def get_success_url(self):
        username = self.kwargs['username']
        return reverse_lazy('patient:visiting_consultant_list', kwargs={'username': username})


visiting_consultant_delete = VisitingConsultantDeleteView.as_view()

