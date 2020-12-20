from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.db.models import F, Func, Value, CharField
from django.db.models import Value, CharField
from django.db.models.functions import Cast, Concat, ExtractYear, ExtractMonth, ExtractDay, ExtractHour, ExtractMinute
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext as _

from patient.models import *
from patient.Forms.cannula import *
from accounts.models import *
from customers.models import *
from accounts.models import *
from accounts.decorators import *

from bootstrap_modal_forms.generic import *


@login_required
def cannula_list(request, username):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(
        schema_name=schema_name).values_list('title', flat=True).first()
    page_title = _('Cannulation Chart')
    patientid = UserProfile.objects.get(username=username).id
    patients = Cannula.objects.filter(patient=patientid)
    profiles = UserProfile.objects.filter(pk=patientid)

    context = {
        'logos': logos,
        'titles': titles,
        'page_title': page_title,
        'patients': patients,
        'profiles': profiles,
    }

    return render(request, 'patient/cannula/cannula_data.html', context)


@login_required
def cannula_create(request, username):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
    page_title = _('Cannulation Chart')
    patients = get_object_or_404(UserProfile, username=username)
    profiles = UserProfile.objects.filter(username=username)
    icnumbers = UserProfile.objects.filter(username=username).values_list('ic_number', flat=True).first()

    initial = [{
        'patient': item.full_name,
        'cannula_remove_by': request.user,
    }
        for item in profiles]

    initial_formset_factory = [
        {
            'patient': patients,
            'ic_number': icnumbers,
        }]

    if request.method == 'POST':
        formset = Cannula_FormSet(request.POST or None)

        if formset.is_valid():
            for item in formset:
                profile = Cannula()
                profile.patient = patients
                profile.cannula_date = item.cleaned_data['cannula_date']
                profile.cannula_size = item.cleaned_data['cannula_size']
                profile.cannula_location = item.cleaned_data['cannula_location']
                profile.cannula_due_date = item.cleaned_data['cannula_due_date']
                profile.cannula_remove_date = item.cleaned_data['cannula_remove_date']
                profile.cannula_remove_by = item.cleaned_data['cannula_remove_by']
                profile.save()

            messages.success(request, _(page_title + ' form was created.'))
            return redirect('patient:patientdata_detail', username=patients.username)
        else:
            messages.warning(request, formset.errors)

    else:
        formset = Cannula_FormSet(initial=initial)

    context = {
        'logos': logos,
        'titles': titles,
        'page_title': page_title,
        'patients': patients,
        'profiles': profiles,
        'icnumbers': icnumbers,
        'formset': formset,
    }

    return render(request, 'patient/cannula/cannula_form.html', context)


@method_decorator(admin_required, name='dispatch')
class CannulaUpdateView(BSModalUpdateView):
    model = Cannula
    template_name = 'patient/cannula/partial_edit.html'
    form_class = Cannula_ModelForm
    page_title = _('Cannula Form')
    success_message = _(page_title + ' form has been save successfully.')

    def get_form(self, form_class=None):
        form = super().get_form(form_class=None)
        form.fields['cannula_date'].label = _("Date")
        form.fields['cannula_size'].label = _("Size")
        form.fields['cannula_location'].label = _("Location")
        form.fields['cannula_due_date'].label = _("Due Date")
        form.fields['cannula_remove_date'].label = _("Remove Date")
        form.fields['cannula_remove_by'].label = _("Remove by")
        return form

    def get_success_url(self):
        username = self.kwargs['username']
        return reverse_lazy('patient:cannula_list', kwargs={'username': username})


cannula_edit = CannulaUpdateView.as_view()


@method_decorator(admin_required, name='dispatch')
class CannulaDeleteView(BSModalDeleteView):
    model = Cannula
    template_name = 'patient/cannula/partial_delete.html'
    page_title = _('Cannula Form')
    success_message = _(page_title + ' form was deleted.')

    def get_success_url(self):
        username = self.kwargs['username']
        return reverse_lazy('patient:cannula_list', kwargs={'username': username})


cannula_delete = CannulaDeleteView.as_view()
