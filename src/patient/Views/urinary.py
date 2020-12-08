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


@login_required
def urinary_list(request, username):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(
        schema_name=schema_name).values_list('title', flat=True).first()
    page_title = _('Urinary Catheter Chart')
    patientid = UserProfile.objects.get(username=username).id
    patients = Urinary.objects.filter(patient=patientid)
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

    return render(request, 'patient/urinary/urinary_data.html', context)


@login_required
def urinary_create(request, username):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(
        schema_name=schema_name).values_list('title', flat=True).first()
    page_title = _('Urinary Catheter Chart')
    patients = get_object_or_404(UserProfile, username=username)
    profiles = UserProfile.objects.filter(username=username)
    icnumbers = UserProfile.objects.filter(
        username=username).values_list('ic_number', flat=True).first()
    themes = request.session.get('theme')

    initial_formset = [{
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
                profile.urinary_catheter_inserted_by = item.cleaned_data[
                    'urinary_catheter_inserted_by']
                profile.urinary_catheter_remove_date = item.cleaned_data[
                    'urinary_catheter_remove_date']
                profile.urinary_catheter_remove_by = item.cleaned_data['urinary_catheter_remove_by']
                profile.save()

            messages.success(request, _(page_title + ' form was created.'))
            return redirect('patient:patientdata_detail', username=patients.username)
        else:
            messages.warning(request, formset.errors)

    else:
        formset = Urinary_FormSet(initial=initial_formset)

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

    return render(request, 'patient/urinary/urinary_form.html', context)


class UrinaryUpdateView(BSModalUpdateView):
    model = Urinary
    template_name = 'patient/urinary/partial_edit.html'
    form_class = Urinary_ModelForm
    page_title = _('Urinary Form')
    success_message = _(page_title + ' form has been save successfully.')

    def get_form(self, form_class=None):
        form = super().get_form(form_class=None)
        form.fields['urinary_catheter_date'].label = _("Date")
        form.fields['urinary_catheter_size'].label = _("Size")
        form.fields['urinary_catheter_type'].label = _("Type")
        form.fields['urinary_catheter_due_date'].label = _("Due Date")
        form.fields['urinary_catheter_inserted_by'].label = _("Inserted by")
        form.fields['urinary_catheter_remove_date'].label = _("Remove Date")
        form.fields['urinary_catheter_remove_by'].label = _("Remove by")
        return form

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
