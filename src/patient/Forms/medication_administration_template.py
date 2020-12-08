from django import forms
from django.utils.translation import ugettext_lazy as _

from ..models import *
from ..forms import *
from ..lookups import *
from ..choices import *
#from .custom_layout import *
from accounts.models import *

from bootstrap_modal_forms.forms import *


default_desimal_mar = Decimal('0.0')


class MedicationAdministrationRecordTemplate_ModelForm(BSModalModelForm):
    class Meta:
        model = MedicationAdministrationRecordTemplate
        fields = [
            'patient',
            'medication_date',
            'medication_time',
            'medication_drug_name',
            'medication_dosage',
            'medication_unit',
            'medication_tablet_capsule',
            'medication_frequency',
        ]
        widgets = {
            'id': forms.HiddenInput(),
            'patient': forms.HiddenInput(),
        }

    medication_date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS,
                                      widget=DatePickerInput(format="%d-%m-%Y", attrs={'class': "form-control"}))
    medication_time = forms.TimeField(required=False, label="", input_formats=settings.TIME_INPUT_FORMATS,
                                      widget=TimePickerInput(format="%H:%M", attrs={'class': "form-control"}))
    medication_drug_name = forms.ModelChoiceField(queryset=Medicine.objects.all(
    ), required=False, label="", widget=forms.Select(attrs={'class': "form-control"}))
    medication_dosage = forms.IntegerField(
        required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
    medication_unit = forms.ChoiceField(required=False, label="", widget=forms.Select(
        attrs={'class': "form-control"}), choices=UNIT_CHOICES)
    medication_tablet_capsule = forms.DecimalField(required=False, label="", initial=default_desimal_mar,
                                                   min_value=0.0, widget=forms.NumberInput(attrs={'class': "form-control", 'step': 0.1}))
    medication_frequency = forms.ChoiceField(required=False, label="", widget=forms.Select(
        attrs={'class': "form-control"}), choices=MEDICATION_ADMINISTRATION_FREQUENCY_CHOICES)


MedicationAdministrationRecordTemplate_FormSet = modelformset_factory(
    MedicationAdministrationRecordTemplate,
    form=MedicationAdministrationRecordTemplate_ModelForm,
    extra=0,
    max_num=0,
)
