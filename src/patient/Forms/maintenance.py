from django import forms
from django.utils.translation import ugettext_lazy as _

from ..models import *
from ..forms import *
from ..lookups import *
#from .custom_layout import *
from accounts.models import *

from bootstrap_modal_forms.forms import *

class Maintenance_ModelForm(BSModalModelForm):

    class Meta:
        model = Maintenance
        fields = '__all__'
        widgets = {
            'patient': forms.HiddenInput(),
        }

    date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d/%m/%Y", attrs={'class': "form-control"}))
    items = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    location_room = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    reported_by = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    status = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=Maintenance.STATUS_CHOICES)


class Maintenance_Form(BSModalForm):

    patient = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d/%m/%Y", attrs={'class': "form-control"}))
    items = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    location_room = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    reported_by = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    status = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=Maintenance.STATUS_CHOICES)


Maintenance_FormSet = formset_factory(
    Maintenance_Form,
    #   formset = MedicationAdministrationRecord_BaseFormSetFactory,
    extra=0,
#    max_num=0,
    #   can_delete=True,
)
