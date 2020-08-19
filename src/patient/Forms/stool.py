from django import forms
from django.utils.translation import ugettext_lazy as _

from ..models import *
from ..forms import *
from ..lookups import *
#from .custom_layout import *
from accounts.models import *

from bootstrap_modal_forms.forms import *


class StoolForm(BSModalModelForm):

    class Meta:
        model = Stool
        fields = '__all__'
        widgets = {
            'patient': forms.HiddenInput(),
        }

    date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d/%m/%Y", attrs={'class': "form-control"}))
    time = forms.TimeField(required=False, label="", initial=get_time, input_formats=settings.TIME_INPUT_FORMATS, widget=TimePickerInput(format="%H:%M", attrs={'class': "form-control"}))
    frequency = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=Stool.STOOL_FREQUENCY_CHOICES)
    consistency = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=Stool.CONSISTENCY_CHOICES)
    amount = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=Stool.AMOUNT_CHOICES)
    remark = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    done_by = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
