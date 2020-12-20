from django import forms
from django.utils.translation import ugettext_lazy as _

from ..models import *
from ..forms import *
from ..lookups import *
from ..choices import *
#from .custom_layout import *
from accounts.models import *

from bootstrap_modal_forms.forms import *


class MedicationRecord_ModelForm(BSModalModelForm):
    class Meta:
        model = MedicationRecord
        fields = [
            'patient',
            'date',
            'time',
            'medication_medicine',
            'dosage',
            'unit',
            'topup',
            'balance',
            'remark',
            'staff',
        ]
        widgets = {
            'patient': forms.HiddenInput(),
        }

    date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS,
                           widget=DatePickerInput(format="%d-%m-%Y", attrs={'class': "form-control"}))
    time = forms.TimeField(required=False, label="", initial=get_time, input_formats=settings.TIME_INPUT_FORMATS,
                           widget=TimePickerInput(format="%H:%M", attrs={'class': "form-control"}))
    medication_medicine = forms.ModelChoiceField(queryset=Medicine.objects.all(
    ), required=False, label="", widget=forms.Select(attrs={'class': "form-control"}))
    dosage = forms.IntegerField(required=False, label="", initial="0",
                                min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
    unit = forms.ChoiceField(required=False, label="", widget=forms.Select(
        attrs={'class': "form-control"}), choices=UNIT_CHOICES)
    topup = forms.CharField(required=False, label="", widget=forms.TextInput(
        attrs={'class': "form-control"}))
    balance = forms.IntegerField(required=False, label="", initial="0",
                                 min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
    remark = forms.CharField(required=False, label="", widget=forms.TextInput(
        attrs={'class': "form-control"}))
    staff = forms.CharField(required=False, label="", widget=forms.TextInput(
        attrs={'class': "form-control"}))


class MedicationRecord_Form(BSModalForm):

    patient = forms.CharField(required=False, label="", widget=forms.TextInput(
        attrs={'class': "form-control"}))
    date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS,
                           widget=DatePickerInput(format="%d-%m-%Y", attrs={'class': "form-control"}))
    time = forms.TimeField(required=False, label="", initial=get_time, input_formats=settings.TIME_INPUT_FORMATS,
                           widget=TimePickerInput(format="%H:%M", attrs={'class': "form-control"}))
    medication_medicine = forms.ModelChoiceField(queryset=Medicine.objects.all(
    ), required=False, label="", widget=forms.Select(attrs={'class': "form-control"}))
    dosage = forms.IntegerField(required=False, label="", initial="0",
                                min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
    unit = forms.ChoiceField(required=False, label="", widget=forms.Select(
        attrs={'class': "form-control"}), choices=UNIT_CHOICES)
    topup = forms.CharField(required=False, label="", widget=forms.TextInput(
        attrs={'class': "form-control"}))
    balance = forms.IntegerField(required=False, label="", initial="0",
                                 min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
    remark = forms.CharField(required=False, label="", widget=forms.TextInput(
        attrs={'class': "form-control"}))
    staff = forms.CharField(required=False, label="", widget=forms.TextInput(
        attrs={'class': "form-control", 'readonly': 'readonly'}))

    def clean_medication(self):
        return self.cleaned_data['medication_medicine'].capitalize()

    def clean_topup(self):
        return self.cleaned_data['topup'].capitalize()

    def clean_remark(self):
        return self.cleaned_data['remark'].capitalize()


MedicationRecord_FormSet = formset_factory(
    MedicationRecord_Form,
    #   formset = MedicationAdministrationRecord_BaseFormSetFactory,
    extra=0,
    #    max_num=0,
    #   can_delete=True,
)
