from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import ugettext as _
from django.urls import reverse, reverse_lazy

from patient.models import *
from patient.Forms.miscellaneous_charges_slip import *
from accounts.models import *
from customers.models import *

from bootstrap_modal_forms.generic import *


@login_required
def miscellaneous_charges_slip_list(request, username):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(
        schema_name=schema_name).values_list('title', flat=True).first()
    page_title = _('Miscellaneous Charges Slip')
    patientid = UserProfile.objects.get(username=username).id
    patients = MiscellaneousChargesSlip.objects.filter(patient=patientid)
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

    return render(request, 'patient/miscellaneous_charges_slip/miscellaneous_charges_slip_data.html', context)


@login_required
def miscellaneous_charges_slip_create(request, username):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(
        schema_name=schema_name).values_list('title', flat=True).first()
    page_title = _('Miscellaneous Charges Slip')
    patients = get_object_or_404(UserProfile, username=username)
    profiles = UserProfile.objects.filter(username=username)
    icnumbers = UserProfile.objects.filter(
        username=username).values_list('ic_number', flat=True).first()
    themes = request.session.get('theme')

    initial = [{
        'patient': item.full_name,
        'given_by': request.user,
    }
        for item in profiles]

    initial_formset_factory = [
        {
            'patient': patients,
            'ic_number': icnumbers,
        }]

    if request.method == 'POST':
        formset = MiscellaneousChargesSlip_FormSet(request.POST or None)
        if formset.is_valid():
            for item in formset:
                profile = MiscellaneousChargesSlip()
                profile.patient = patients
                profile.date = item.cleaned_data['date']
                profile.items_procedures = item.cleaned_data['items_procedures']
                profile.unit = item.cleaned_data['unit']
                profile.amount = item.cleaned_data['amount']
                profile.given_by = item.cleaned_data['given_by']
                profile.save()

            messages.success(request, _(page_title + ' form was created.'))
            return redirect('patient:patientdata_detail', username=patients.username)
        else:
            messages.warning(request, formset.errors)
    else:
        formset = MiscellaneousChargesSlip_FormSet(initial=initial)

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

    return render(request, 'patient/miscellaneous_charges_slip/miscellaneous_charges_slip_form.html', context)


class MiscellaneousChargesSlipUpdateView(BSModalUpdateView):
    model = MiscellaneousChargesSlip
    template_name = 'patient/miscellaneous_charges_slip/partial_edit.html'
    form_class = MiscellaneousChargesSlip_ModelForm
    page_title = _('MiscellaneousChargesSlip Form')
    success_message = _(page_title + ' form has been save successfully.')

    def get_form(self, form_class=None):
        form = super().get_form(form_class=None)
        form.fields['date'].label = _("Date")
        form.fields['items_procedures'].label = _("Items Procedures")
        form.fields['unit'].label = _("Unit")
        form.fields['amount'].label = _("Amount")
        form.fields['given_by'].label = _("Given by")
        return form

    def get_success_url(self):
        username = self.kwargs['username']
        return reverse_lazy('patient:miscellaneous_charges_slip_list', kwargs={'username': username})


miscellaneous_charges_slip_edit = MiscellaneousChargesSlipUpdateView.as_view()


class MiscellaneousChargesSlipDeleteView(BSModalDeleteView):
    model = MiscellaneousChargesSlip
    template_name = 'patient/miscellaneous_charges_slip/partial_delete.html'
    page_title = _('MiscellaneousChargesSlip Form')
    success_message = _(page_title + ' form was deleted.')

    def get_success_url(self):
        username = self.kwargs['username']
        return reverse_lazy('patient:miscellaneous_charges_slip_list', kwargs={'username': username})


miscellaneous_charges_slip_delete = MiscellaneousChargesSlipDeleteView.as_view()
