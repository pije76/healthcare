from django import forms
from django.utils.translation import ugettext_lazy as _

from ..models import *
from ..forms import *
from ..lookups import *
#from .custom_layout import *
from accounts.models import *

from bootstrap_modal_forms.forms import *


class VisitingConsultant_ModelForm(BSModalModelForm):
    class Meta:
        model = VisitingConsultant
        fields = [
            'patient',
            'date_time',
            'complaints',
            'treatment_orders',
            'consultant',
        ]
        widgets = {
            'patient': forms.HiddenInput(),
        }

    date_time = forms.DateTimeField(required=False, label="", initial=timezone.now, input_formats=settings.DATETIME_INPUT_FORMATS,
                                    widget=DateTimePickerInput(format="%d-%m-%Y %H:%M", attrs={'class': "form-control"}))
    complaints = forms.CharField(required=False, label="", widget=forms.Textarea(
        attrs={'class': "form-control"}))
    treatment_orders = forms.CharField(
        required=False, label="", widget=forms.Textarea(attrs={'class': "form-control"}))
    consultant = forms.CharField(required=False, label="", widget=forms.TextInput(
        attrs={'class': "form-control"}))


class VisitingConsultant_Form(BSModalForm):

    patient = forms.CharField(required=False, label="", widget=forms.TextInput(
        attrs={'class': "form-control"}))
    date_time = forms.DateTimeField(required=False, label="", initial=timezone.now, input_formats=settings.DATETIME_INPUT_FORMATS,
                                    widget=DateTimePickerInput(format="%d-%m-%Y %H:%M", attrs={'class': "form-control"}))
    complaints = forms.CharField(required=False, label="", widget=forms.Textarea(
        attrs={'class': "form-control"}))
    treatment_orders = forms.CharField(
        required=False, label="", widget=forms.Textarea(attrs={'class': "form-control"}))
    consultant = forms.CharField(required=False, label="", widget=forms.TextInput(
        attrs={'class': "form-control"}))

    def clean_complaints(self):
        return self.cleaned_data['complaints'].capitalize()

    def clean_treatment_orders(self):
        return self.cleaned_data['treatment_orders'].capitalize()

    def clean_consultant(self):
        return self.cleaned_data['consultant'].capitalize()


VisitingConsultant_FormSet = formset_factory(
    VisitingConsultant_Form,
    #   formset = MedicationAdministrationRecord_BaseFormSetFactory,
    extra=0,
    #    max_num=0,
    #   can_delete=True,
)
