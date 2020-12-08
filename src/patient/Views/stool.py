from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import ugettext as _
from django.urls import reverse, reverse_lazy
from django.urls import reverse_lazy
from django.db import IntegrityError, transaction

from patient.models import *
from patient.Forms.stool import *
from accounts.models import *
from customers.models import *

from bootstrap_modal_forms.generic import *


@login_required
def stool_list(request, username):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(
        schema_name=schema_name).values_list('title', flat=True).first()
    page_title = _('Stool Chart')
    patientid = UserProfile.objects.get(username=username).id
    patients = Stool.objects.filter(patient=patientid)
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

    return render(request, 'patient/stool/stool_data.html', context)


@login_required
def stool_create(request, username):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(
        schema_name=schema_name).values_list('title', flat=True).first()
    page_title = _('Stool Chart')
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

    if request.method == 'POST':
        formset = Stool_FormSet(request.POST or None)

        if formset.is_valid():
            for item in formset:
                profile = Stool()
                profile.patient = patients
                profile.date = item.cleaned_data['date']
                profile.time = item.cleaned_data['time']
                profile.frequency = item.cleaned_data['frequency']
                profile.consistency = item.cleaned_data['consistency']
                profile.amount = item.cleaned_data['amount']
                profile.remark = item.cleaned_data['remark']
                profile.done_by = item.cleaned_data['done_by']
                profile.save()

            messages.success(request, _(page_title + ' form was created.'))
            return redirect('patient:patientdata_detail', username=patients.username)
        else:
            messages.warning(request, formset.errors)
    else:
        formset = Stool_FormSet(initial=initial)

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

    return render(request, 'patient/stool/stool_form.html', context)


class StoolUpdateView(BSModalUpdateView):
    model = Stool
    template_name = 'patient/stool/partial_edit.html'
    form_class = Stool_ModelForm
    page_title = _('Stool Form')
    success_message = _(page_title + ' form has been save successfully.')

    def get_form(self, form_class=None):
        form = super().get_form(form_class=None)
        form.fields['date'].label = _("Date")
        form.fields['time'].label = _("Time")
        form.fields['frequency'].label = _("Frequency")
        form.fields['consistency'].label = _("Consistency")
        form.fields['amount'].label = _("Amount")
        form.fields['remark'].label = _("Remark")
        form.fields['done_by'].label = _("Done by")
        return form

    def get_success_url(self):
        username = self.kwargs['username']
        return reverse_lazy('patient:stool_list', kwargs={'username': username})


stool_edit = StoolUpdateView.as_view()


class StoolDeleteView(BSModalDeleteView):
    model = Stool
    template_name = 'patient/stool/partial_delete.html'
    page_title = _('Stool Form')
    success_message = _(page_title + ' form was deleted.')

    def get_success_url(self):
        username = self.kwargs['username']
        return reverse_lazy('patient:stool_list', kwargs={'username': username})


stool_delete = StoolDeleteView.as_view()
