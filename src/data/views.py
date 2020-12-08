from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext as _
from django.db import connection
from django.utils.decorators import method_decorator
from django.db.models import Sum, Count

from accounts.models import *
from accounts.decorators import *
from customers.models import *
from .models import *
from .forms import *

from bootstrap_modal_forms.generic import *


# Create your views here.

@login_required
def data_list(request):
    schema_name = connection.schema_name
    patients = UserProfile.objects.filter(username=request.user.username)
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(
        schema_name=schema_name).values_list('title', flat=True).first()
    page_title = _('Data List')
    druglist = Medicine.objects.all()
    woundconditionlist = WoundCondition.objects.all()
    themes = request.session.get('theme')

#   if request.user.is_superuser or request.user.is_staff:
#       datastaff = UserProfile.objects.filter(is_patient=True).order_by("id")
#       q = Q()
#       for item in city_list:
#           q = q | Q(address__city__icontains=city)
#       fullname_data = datastaff.values_list('id', flat=True)
#       datapatients = Admission.objects.filter(patient__in=fullname_data).order_by('patient')
#       datapatients = UserProfile.objects.filter(username=request.user.username)
#       datapatients = Admission.objects.all()
#       results = chain(datapatients, datastaff)

#   if request.user.is_data:
#       datastaff = UserProfile.objects.filter(full_name=request.user).order_by("id")
#       datapatients = Admission.objects.filter(patient__in=datastaff)

    context = {
        'patients': patients,
        'logos': logos,
        'titles': titles,
        'page_title': page_title,
        #       'datastaff': datastaff,
        'druglist': druglist,
        'woundconditionlist': woundconditionlist,
        "themes": themes,
    }

    return render(request, 'data/data_list.html', context)


@login_required
def drug_list(request):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(
        schema_name=schema_name).values_list('title', flat=True).first()
    page_title = _('Medicine View')
#    patientid = UserProfile.objects.get(username=username).id
#    patients = HGT.objects.filter(patient=patientid)
#    profiles = UserProfile.objects.filter(pk=patientid)
    datas = Medicine.objects.all()
    themes = request.session.get('theme')

    context = {
        'logos': logos,
        'titles': titles,
        'page_title': page_title,
        #        'patients': patients,
        #        'profiles': profiles,
        'datas': datas,
        "themes": themes,
    }

    return render(request, 'data/drug/drug_data.html', context)


@login_required
def drug_create(request):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(
        schema_name=schema_name).values_list('title', flat=True).first()
    page_title = _('Medicine')
    themes = request.session.get('theme')

    initial = {
        #       'staff': staffs,
        #       'ic_number': icnumbers,
        #       'date': thisyear,
    }

    if request.method == 'POST':
        form = Medicine_Form(request.POST or None)

        if form.is_valid():
            profile = Medicine()
            profile.drug_name = form.cleaned_data['drug_name']
            profile.save()

            messages.success(request, _(page_title + ' form was created.'))
            return redirect('data:data_list')
        else:
            messages.warning(request, form.errors)
    else:
        form = Medicine_Form()

    context = {
        'logos': logos,
        'titles': titles,
        'page_title': page_title,
        'form': form,
        "themes": themes,
    }

    return render(request, 'data/drug/drug_form.html', context)


class MedicineUpdateView(BSModalUpdateView):
    model = Medicine
    template_name = 'data/drug/partial_edit.html'
    form_class = Medicine_ModelForm
    page_title = _('Medicine Form')
    success_message = _(page_title + ' form has been save successfully.')

    def get_form(self, form_class=None):
        form = super().get_form(form_class=None)
        form.fields['allergy_drug'].label = _("Allergy Drug")
        form.fields['allergy_food'].label = _("Allergy Dood")
        form.fields['allergy_others'].label = _("Allergy Others")
        return form

    def get_success_url(self):
        username = self.kwargs['username']
        return reverse_lazy('data:drug_list')
#       return reverse_lazy('patient:medication_administration_list', kwargs={'username': username})


drug_edit = MedicineUpdateView.as_view()


class MedicineDeleteView(BSModalDeleteView):
    model = Medicine
    template_name = 'data/drug/partial_delete.html'
    page_title = _('Medicine Form')
    success_message = _(page_title + ' form was deleted.')

    def get_success_url(self):
        username = self.kwargs['username']
        return reverse_lazy('data:drug_list', kwargs={'username': username})


drug_delete = MedicineDeleteView.as_view()


@login_required
def wound_condition_list(request):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(
        schema_name=schema_name).values_list('title', flat=True).first()
    page_title = _('Wound Condition View')
#    patientid = UserProfile.objects.get(username=username).id
#    patients = HGT.objects.filter(patient=patientid)
#    profiles = UserProfile.objects.filter(pk=patientid)
    woundconditions = WoundCondition.objects.all()
    themes = request.session.get('theme')

    context = {
        'logos': logos,
        'titles': titles,
        'page_title': page_title,
        #        'patients': patients,
        #        'profiles': profiles,
        'woundconditions': woundconditions,
        "themes": themes,
    }

    return render(request, 'data/wound_condition/wound_condition_data.html', context)


@login_required
def wound_condition_create(request):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(
        schema_name=schema_name).values_list('title', flat=True).first()
    page_title = _('Wound Condition')
    themes = request.session.get('theme')

    initial = {
        #       'staff': staffs,
        #       'ic_number': icnumbers,
        #       'date': thisyear,
    }

    if request.method == 'POST':
        form = WoundCondition_Form(request.POST or None)

        if form.is_valid():
            profile = WoundCondition()
            profile.name = form.cleaned_data['name']
            profile.parent = form.cleaned_data['parent']
            profile.save()

            messages.success(request, _(page_title + ' form was created.'))
            return redirect('data:data_list')
        else:
            messages.warning(request, form.errors)
    else:
        form = WoundCondition_Form()

    context = {
        'logos': logos,
        'titles': titles,
        'page_title': page_title,
        'form': form,
        "themes": themes,
    }

    return render(request, 'data/wound_condition/wound_condition_form.html', context)


class WoundConditionUpdateView(BSModalUpdateView):
    model = WoundCondition
    template_name = 'data/wound_condition/partial_edit.html'
    form_class = WoundCondition_ModelForm
    page_title = _('WoundCondition Form')
    success_message = _(page_title + ' form has been save successfully.')

    def get_form(self, form_class=None):
        form = super().get_form(form_class=None)
        form.fields['name'].label = _("Name")
        form.fields['parent'].label = _("Parent")
        return form

    def get_success_url(self):
        username = self.kwargs['username']
        return reverse_lazy('data:wound_condition_list')


wound_condition_edit = WoundConditionUpdateView.as_view()


class WoundConditionDeleteView(BSModalDeleteView):
    model = WoundCondition
    template_name = 'data/wound_condition/partial_delete.html'
    page_title = _('WoundCondition Form')
    success_message = _(page_title + ' form was deleted.')

    def get_success_url(self):
        username = self.kwargs['username']
        return reverse_lazy('data:wound_condition_list', kwargs={'username': username})


wound_condition_delete = WoundConditionDeleteView.as_view()
