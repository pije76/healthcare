from django import forms
from django.utils.translation import ugettext_lazy as _

from ..models import *
from ..forms import *
from ..lookups import *
#from .custom_layout import *
from accounts.models import *

from bootstrap_modal_forms.forms import *


class EnteralFeedingRegimeForm(BSModalModelForm):

    class Meta:
        model = EnteralFeedingRegime
        fields = '__all__'
        widgets = {
            'patient': forms.HiddenInput(),
        }

    date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d/%m/%Y", attrs={'class': "form-control"}))
    time = forms.TimeField(required=False, label="", initial=get_time, input_formats=settings.TIME_INPUT_FORMATS, widget=TimePickerInput(format="%H:%M", attrs={'class': "form-control"}))
    type_of_milk = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    amount = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
    warm_water_before = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control calc"}))
    warm_water_after = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control calc"}))
