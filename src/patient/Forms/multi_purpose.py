from django import forms
from django.utils.translation import ugettext_lazy as _

from ..models import *
from ..forms import *
from ..lookups import *
#from .custom_layout import *
from accounts.models import *

from bootstrap_modal_forms.forms import *


class Multipurpose_ModelForm(BSModalModelForm):
    class Meta:
        model = Multipurpose
#       fields = '__all__'
        fields = [
            'patient',
            'date_time',
            'symptom',
            'remark',
        ]
        widgets = {
            'patient': forms.HiddenInput(),
        }

    date_time = forms.DateTimeField(required=False, label="", initial=timezone.now, input_formats=settings.DATETIME_INPUT_FORMATS, widget=DateTimePickerInput(format="%d-%m-%Y %H:%M", attrs={'class': "form-control"}))
    symptom = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    remark = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))


class Multipurpose_Form(BSModalForm):

    patient = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    date_time = forms.DateTimeField(required=False, label="", initial=timezone.now, input_formats=settings.DATETIME_INPUT_FORMATS, widget=DateTimePickerInput(format="%d-%m-%Y %H:%M", attrs={'class': "form-control"}))
    symptom = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    remark = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))

    def clean_symptom(self):
        return self.cleaned_data['symptom'].capitalize()

    def clean_remark(self):
        return self.cleaned_data['remark'].capitalize()

Multipurpose_FormSet = formset_factory(
    Multipurpose_Form,
    #   formset = MedicationAdministrationRecord_BaseFormSetFactory,
    extra=0,
#    max_num=0,
    #   can_delete=True,
)
