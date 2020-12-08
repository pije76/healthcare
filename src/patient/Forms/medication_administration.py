from django import forms
from django.utils.translation import ugettext_lazy as _

from ..models import *
from ..forms import *
from ..lookups import *
from ..choices import *
#from .custom_layout import *
from accounts.models import *

from bootstrap_modal_forms.forms import *
from crispy_forms.layout import Field


default_desimal_mar = Decimal('0.0')


class CustomCheckbox(Field):
    template = 'patient/medication_administration/custom_checkbox.html'


class MedicationAdministrationRecord_ModelForm(forms.ModelForm):
    class Meta:
        model = MedicationAdministrationRecord
        fields = [
            'patient',
            'allergy_drug',
            'allergy_food',
            'allergy_others',
            #			'medication_template',
            #			'medication_date',
            #			'medication_time',
            #			'medication_drug_name',
            #			'medication_dosage',
            #			'medication_unit',
            #			'medication_tablet_capsule',
            #			'medication_frequency',
            'medication_route',
            'medication_status',
            'medication_source',
            'medication_done',
        ]
        widgets = {
            'id': forms.HiddenInput(),
            'patient': forms.HiddenInput(),
            'medication_template': forms.HiddenInput(),
        }
        labels = {
            'medication_done': '',
        }

#	def __init__(self, user, *args, **kwargs):
#		super().__init__(*args, **kwargs)
#		self.fields['medication_date'].queryset = MedicationAdministrationRecord.objects.filter(patient=user)
#		self.request = request

#	patient = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
#	allergy = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    allergy_drug = forms.CharField(required=False, label=_(
        "Medicine(s):"), widget=forms.TextInput(attrs={'class': "form-control"}))
    allergy_food = forms.CharField(required=False, label=_(
        "Food:"), widget=forms.TextInput(attrs={'class': "form-control"}))
    allergy_others = forms.CharField(required=False, label=_(
        "Others:"), widget=forms.TextInput(attrs={'class': "form-control"}))
#	medication = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
#	medication = forms.ModelChoiceField(queryset=MedicationAdministrationRecordTemplate.objects.all(), required=False, label="", widget=forms.Select(attrs={'class': "form-control"}))

#	medication_template = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    medication_date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS,
                                      widget=DatePickerInput(format="%d-%m-%Y", attrs={'class': "form-control"}))
    medication_time = forms.TimeField(required=False, label="", input_formats=settings.TIME_INPUT_FORMATS,
                                      widget=TimePickerInput(format="%H:%M", attrs={'class': "form-control"}))
#    medication_drug_name = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
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

    medication_route = forms.ChoiceField(required=False, label="", widget=forms.Select(
        attrs={'class': "form-control"}), choices=ROUTE_CHOICES)
    medication_status = forms.ChoiceField(required=False, label="", widget=forms.Select(
        attrs={'class': "form-control"}), choices=SIGNATURE_CHOICES)
    medication_source = forms.ChoiceField(required=False, label="", widget=forms.Select(
        attrs={'class': "form-control"}), choices=SOURCE_CHOICES)

#	medication_done = forms.BooleanField(required=False, label='', widget=forms.TextInput())
#	medication_done = forms.BooleanField(required=False, label="")
#	medication_done = forms.ChoiceField(required=False, label="", initial=False, widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=BOOLEAN_CHOICES)

#	def __init__(self, *args, **kwargs):
#		super().__init__(*args, **kwargs)
#		if 'instance' in kwargs:
#			medication_template = kwargs['instance']
#		self.fields['patient']  = forms.CharField(max_length=30)
#		self.helper = FormHelper()
#		self.helper.layout = Layout(
#			CustomCheckbox('medication_done'),
#		)


# MedicationAdministrationRecord_ModelFormSet = modelform_factory(
MedicationAdministrationRecord_ModelFormSet = modelformset_factory(
    # MedicationAdministrationRecord_ModelFormSet = inlineformset_factory(
    #	MedicationAdministrationRecordTemplate,
    MedicationAdministrationRecord,
    form=MedicationAdministrationRecord_ModelForm,
    #	fields=(
    #		'id',
    #		'patient',
    # 'allergy',
    #		'medication_template',
    #		'medication_date',
    #		'medication_time',
    #		'medication_drug_name',
    #		'medication_dosage',
    #		'medication_tablet_capsule',
    #		'medication_frequency',
    #		'medication_route',
    #		'medication_status',
    #		'medication_source',
    #		'medication_done',
    #	),
    extra=0,
    #	max_num=0,
)
