from django import forms
from django.utils.translation import ugettext_lazy as _

from ..models import *
from ..forms import *
from ..lookups import *
from ..choices import *
#from .custom_layout import *
from accounts.models import *

from bootstrap_modal_forms.forms import *


class Nasogastric_ModelForm(BSModalModelForm):
    class Meta:
        model = Nasogastric
#       fields = '__all__'
        fields = [
            'patient',
            'nasogastric_tube_date',
            'nasogastric_tube_size',
            'nasogastric_tube_type',
            'nasogastric_tube_location',
            'nasogastric_tube_due_date',
            'nasogastric_tube_inserted_by',
            'nasogastric_remove_date',
            'nasogastric_remove_by',
        ]
        widgets = {
            'patient': forms.HiddenInput(),
        }

    nasogastric_tube_date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS,
                                            widget=DatePickerInput(format="%d-%m-%Y", attrs={'class': "form-control"}))
    nasogastric_tube_size = forms.IntegerField(
        required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
#	nasogastric_tube_type = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4}))
    nasogastric_tube_type = forms.ChoiceField(required=False, label="", widget=forms.Select(
        attrs={'class': "form-control"}), choices=NASOGASTRIC_TUBE_TYPE_CHOICES)
    nasogastric_tube_location = forms.CharField(
        required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4}))
    nasogastric_tube_due_date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(
        format="%d-%m-%Y", attrs={'class': "form-control"}))
    nasogastric_tube_inserted_by = forms.CharField(required=False, label="", widget=forms.TextInput(
        attrs={'class': "form-control", 'readonly': 'readonly'}))
    nasogastric_remove_date = forms.DateField(required=False, label="", input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(
        format="%d-%m-%Y", attrs={'class': "form-control"}))
    nasogastric_remove_by = forms.CharField(required=False, label="", widget=forms.TextInput(
        attrs={'class': "form-control", 'readonly': 'readonly'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()


class Nasogastric_Form(BSModalForm):

    patient = forms.CharField(required=False, label="", widget=forms.TextInput(
        attrs={'class': "form-control"}))
    nasogastric_tube_date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS,
                                            widget=DatePickerInput(format="%d-%m-%Y", attrs={'class': "form-control"}))
    nasogastric_tube_size = forms.IntegerField(
        required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
#	nasogastric_tube_type = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4}))
    nasogastric_tube_type = forms.ChoiceField(required=False, label="", widget=forms.Select(
        attrs={'class': "form-control"}), choices=NASOGASTRIC_TUBE_TYPE_CHOICES)
    nasogastric_tube_location = forms.CharField(
        required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4}))
    nasogastric_tube_due_date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(
        format="%d-%m-%Y", attrs={'class': "form-control"}))
    nasogastric_tube_inserted_by = forms.CharField(required=False, label="", widget=forms.TextInput(
        attrs={'class': "form-control", 'readonly': 'readonly'}))
    nasogastric_remove_date = forms.DateField(required=False, label="", input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(
        format="%d-%m-%Y", attrs={'class': "form-control"}))
    nasogastric_remove_by = forms.CharField(required=False, label="", widget=forms.TextInput(
        attrs={'class': "form-control", 'readonly': 'readonly'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

    def clean_nasogastric_tube_location(self):
        return self.cleaned_data['nasogastric_tube_location'].capitalize()


Nasogastric_FormSet = formset_factory(
    Nasogastric_Form,
    #   formset = MedicationAdministrationRecord_BaseFormSetFactory,
    extra=0,
    #    max_num=0,
    #   can_delete=True,
)
