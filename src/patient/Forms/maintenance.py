from django import forms
from django.utils.translation import ugettext_lazy as _

from ..models import *
from ..forms import *
from ..lookups import *
from ..choices import *
#from .custom_layout import *
from accounts.models import *

from bootstrap_modal_forms.forms import *
from selectable.forms import *

from selectable import forms as form


class Maintenance_ModelForm(BSModalModelForm):
    class Meta:
        model = ApplicationForHomeLeave
        fields = [
            'patient',
            'date',
            'items',
            'location_room',
            'reported_by',
            'status',
        ]
        widgets = {
            'patient': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS,
                           widget=DatePickerInput(format="%d-%m-%Y", attrs={'class': "form-control"}))
    items = forms.CharField(required=False, label="", widget=forms.TextInput(
        attrs={'class': "form-control"}))
    location_room = forms.CharField(
        required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    reported_by = forms.CharField(required=False, label="", widget=forms.TextInput(
        attrs={'class': "form-control", 'readonly': 'readonly'}))
    status = forms.ChoiceField(required=False, label="", widget=forms.Select(
        attrs={'class': "form-control"}), choices=STATUS_CHOICES)


class Maintenance_Form(BSModalForm):

    patient = forms.CharField(required=False, label="", widget=forms.TextInput(
        attrs={'class': "form-control"}))
    date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS,
                           widget=DatePickerInput(format="%d-%m-%Y", attrs={'class': "form-control"}))
    items = forms.CharField(required=False, label="", widget=forms.TextInput(
        attrs={'class': "form-control"}))
    location_room = forms.CharField(
        required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    reported_by = forms.CharField(required=False, label="", widget=forms.TextInput(
        attrs={'class': "form-control", 'readonly': 'readonly'}))
    status = forms.ChoiceField(required=False, label="", widget=forms.Select(
        attrs={'class': "form-control"}), choices=STATUS_CHOICES)

    def clean_items(self):
        return self.cleaned_data['items'].capitalize()

    def clean_location_room(self):
        return self.cleaned_data['location_room'].capitalize()


Maintenance_FormSet = formset_factory(
    Maintenance_Form,
    #   formset = MedicationAdministrationRecord_BaseFormSetFactory,
    extra=0,
    #    max_num=0,
    #   can_delete=True,
)
