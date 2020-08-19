from django import forms
from django.utils.translation import ugettext_lazy as _

from ..models import *
from ..forms import *
from ..lookups import *
#from .custom_layout import *
from accounts.models import *

from bootstrap_modal_forms.forms import *


class VitalSignFlowForm(BSModalModelForm):

    class Meta:
        model = VitalSignFlow
        fields = '__all__'
        widgets = {
            'patient': forms.HiddenInput(),
        }

    date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d/%m/%Y", attrs={'class': "form-control"}))
    time = forms.TimeField(required=False, label="", initial=get_time, input_formats=settings.TIME_INPUT_FORMATS, widget=TimePickerInput(format="%H:%M", attrs={'class': "form-control"}))
    temp = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
    pulse = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
    blood_pressure_systolic = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
    blood_pressure_diastolic = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
    respiration = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
    spo2_percentage = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
    spo2_o2 = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
