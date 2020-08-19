from django import forms
from django.utils.translation import ugettext_lazy as _

from ..models import *
from ..forms import *
from ..lookups import *
#from .custom_layout import *
from accounts.models import *

from bootstrap_modal_forms.forms import *


class MedicationRecordForm(BSModalModelForm):

    class Meta:
        model = MedicationRecord
        fields = '__all__'
        widgets = {
            'patient': forms.HiddenInput(),
        }

    date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d/%m/%Y", attrs={'class': "form-control"}))
    time = forms.TimeField(required=False, label="", initial=get_time, input_formats=settings.TIME_INPUT_FORMATS, widget=TimePickerInput(format="%H:%M", attrs={'class': "form-control"}))
    medication = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    dosage = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
    topup = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    balance = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
    remark = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    staff = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
