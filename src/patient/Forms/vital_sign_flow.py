from django import forms
from django.utils.translation import ugettext_lazy as _

from ..models import *
from ..forms import *
from ..lookups import *
#from .custom_layout import *
from accounts.models import *

from bootstrap_modal_forms.forms import *
from decimal import Decimal

default_desimal=Decimal('0.00')


class VitalSignFlow_ModelForm(BSModalModelForm):
    class Meta:
        model = VitalSignFlow
        fields = [
            'patient',
            'date',
            'time',
            'temp',
            'pulse',
            'blood_pressure_systolic',
            'blood_pressure_diastolic',
            'respiration',
            'spo2_percentage',
            'spo2_o2',
        ]
        widgets = {
            'patient': forms.HiddenInput(),
        }
        localized_fields = '__all__'

    date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d-%m-%Y", attrs={'class': "form-control"}))
    time = forms.TimeField(required=False, label="", initial=get_time, input_formats=settings.TIME_INPUT_FORMATS, widget=TimePickerInput(format="%H:%M", attrs={'class': "form-control"}))
    temp = forms.DecimalField(required=False, label="", initial=default_desimal, min_value=0.0, widget=forms.NumberInput(attrs={'class': "form-control", 'step': 0.01}))
    pulse = forms.IntegerField(required=False, label="", initial=default_desimal, widget=forms.NumberInput(attrs={'class': "form-control"}))
    blood_pressure_systolic = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
    blood_pressure_diastolic = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
    respiration = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
    spo2_percentage = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
    spo2_o2 = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))


class VitalSignFlow_Form(BSModalForm):

    patient = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d-%m-%Y", attrs={'class': "form-control"}))
    time = forms.TimeField(required=False, label="", initial=get_time, input_formats=settings.TIME_INPUT_FORMATS, widget=TimePickerInput(format="%H:%M", attrs={'class': "form-control"}))
#    temp = forms.DecimalField(required=False, label="", initial="0", min_value=0.0, widget=forms.NumberInput(attrs={'class': "form-control"}))
    temp = forms.DecimalField(required=False, label="", initial=default_desimal, widget=forms.NumberInput(attrs={'class': "form-control", 'step': 0.01}))
    pulse = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
    blood_pressure_systolic = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
    blood_pressure_diastolic = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
    respiration = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
    spo2_percentage = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
    spo2_o2 = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))

VitalSignFlow_FormSet = formset_factory(
    VitalSignFlow_Form,
#   formset = MedicationAdministrationRecord_BaseFormSetFactory,
    extra=0,
#    max_num=0,
#   can_delete=True,
)
