from django import forms
from django.utils.translation import ugettext_lazy as _
from django.db import IntegrityError

from ..models import *
from ..forms import *
from ..lookups import *
from ..choices import *
#from .custom_layout import *
from accounts.models import *

from bootstrap_modal_forms.forms import *


default_desimal = Decimal('0.00')
default_desimal_mar = Decimal('0.0')


class Admission_ModelForm(forms.ModelForm):
    class Meta:
        model = Admission
        fields = '__all__'
        widgets = {
            'patient': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(InlineRadios('')),
        )

    ic_number = forms.CharField(max_length=14, required=False, label=_('IC No:'), validators=[
                                ic_number_validator], widget=forms.TextInput(attrs={'class': "form-control"}))
    ic_upload = forms.ImageField(required=False, label=_(
        'IC Upload:'), widget=forms.FileInput(attrs={'class': "form-control"}))
    date_admission = forms.DateField(required=False, label=_("Date:"), initial=get_today, input_formats=settings.DATE_INPUT_FORMATS,
                                     widget=DatePickerInput(format="%d-%m-%Y", attrs={'class': "form-control"}))
    time_admission = forms.TimeField(required=False, label=_(
        "Time:"), initial=get_time, widget=TimePickerInput(format="%H:%M", attrs={'class': "form-control"}))
    admitted_admission = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(
        attrs={'class': "form-control"}), choices=ADMITTED_CHOICES)
    admitted_others = forms.CharField(
        required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    mode_admission = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(
        attrs={'class': "form-control"}), choices=MODE_CHOICES)

    general_condition = forms.MultipleChoiceField(required=False, label="", widget=forms.CheckboxSelectMultiple(
        attrs={'class': "form-control"}), choices=GENERAL_CONDITION_CHOICES)
    vital_sign_temperature = forms.DecimalField(required=False, label="", initial=default_desimal,
                                                min_value=0.0, widget=forms.NumberInput(attrs={'class': "form-control", 'step': 0.01}))
    vital_sign_pulse = forms.IntegerField(
        required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
    vital_sign_bp_upper = forms.IntegerField(
        required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
    vital_sign_bp_lower = forms.IntegerField(
        required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
    vital_sign_resp = forms.IntegerField(
        required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
    vital_sign_spo2 = forms.IntegerField(
        required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
    vital_sign_on_oxygen_therapy = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(
        attrs={'class': "form-control"}), choices=BOOLEAN_CHOICES)
    vital_sign_on_oxygen_therapy_flow_rate = forms.IntegerField(
        required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control form-horizontal"}))
    vital_sign_hgt = forms.IntegerField(required=False, label="", initial="0",
                                        min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))

    biohazard_infectious_disease = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(
        attrs={'class': "form-control"}), choices=YES_NO_CHOICES)
    biohazard_infectious_disease_others = forms.CharField(
        required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    invasive_line_insitu = forms.MultipleChoiceField(required=False, label="", widget=forms.CheckboxSelectMultiple(
        attrs={'class': "form-control"}), choices=INVASIVE_LINE_INSITU_CHOICES)
    invasive_line_insitu_others = forms.CharField(
        required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    medical_history = forms.MultipleChoiceField(required=False, label="", widget=forms.CheckboxSelectMultiple(
        attrs={'class': "form-control"}), choices=MEDICAL_HISTORY_CHOICES)
    medical_history_others = forms.CharField(
        required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    surgical_history_none = forms.MultipleChoiceField(required=False, label="", widget=forms.CheckboxSelectMultiple(
        attrs={'class': "form-control"}), choices=SURGICAL_CHOICES)
    surgical_history = forms.CharField(required=False, label="", widget=forms.Textarea(
        attrs={'class': "form-control", 'rows': 4, 'cols': 15}))

    date_diagnosis = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS,
                                     widget=DatePickerInput(format="%d-%m-%Y", attrs={'class': "form-control"}))
    diagnosis = forms.CharField(required=False, label="", widget=forms.Textarea(
        attrs={'class': "form-control", 'rows': 4, 'cols': 15}))
    date_operation = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS,
                                     widget=DatePickerInput(format="%d-%m-%Y", attrs={'class': "form-control"}))
    operation = forms.CharField(required=False, label="", widget=forms.Textarea(
        attrs={'class': "form-control", 'rows': 4, 'cols': 15}))

    own_medication = forms.ChoiceField(required=False, label="", initial='No', widget=forms.RadioSelect(
        attrs={'class': "form-control"}), choices=YES_NO_CHOICES)
    medication_time = forms.TimeField(required=False, label="", initial=get_time, input_formats=settings.TIME_INPUT_FORMATS,
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
        attrs={'class': "form-control"}), choices=ADMISSION_FREQUENCY_CHOICES)

    adaptive_aids_with_patient = forms.MultipleChoiceField(required=False, label="", widget=forms.CheckboxSelectMultiple(
        attrs={'class': "form-control"}), choices=ADAPTIVE_AIDS_WITH_PATIENT_CHOICES)
    adaptive_aids_with_patient_others = forms.CharField(
        required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    orientation = forms.MultipleChoiceField(required=False, label="", widget=forms.CheckboxSelectMultiple(
        attrs={'class': "form-control"}), choices=ORIENTATION_CHOICES)
    special_information = forms.CharField(
        required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    admission_by = forms.CharField(required=False, label="", widget=forms.TextInput(
        attrs={'class': "form-control", 'readonly': 'readonly'}))

    def clean_admitted_others(self):
        return self.cleaned_data['admitted_others'].capitalize()

    def clean_biohazard_infectious_disease_others(self):
        return self.cleaned_data['biohazard_infectious_disease_others'].capitalize()

    def clean_invasive_line_insitu_others(self):
        return self.cleaned_data['invasive_line_insitu_others'].capitalize()

    def clean_medical_history_others(self):
        return self.cleaned_data['medical_history_others'].capitalize()

    def clean_surgical_history(self):
        return self.cleaned_data['surgical_history'].capitalize()

    def clean_adaptive_aids_with_patient_others(self):
        return self.cleaned_data['adaptive_aids_with_patient_others'].capitalize()

    def clean_special_information(self):
        return self.cleaned_data['special_information'].capitalize()

    def clean_diagnosis(self):
        return self.cleaned_data['diagnosis'].capitalize()

    def clean_operation(self):
        return self.cleaned_data['operation'].capitalize()

    def clean(self):
        cleaned_data = super().clean()
        admitted_others = cleaned_data.get('admitted_others')
        marital_status_others = cleaned_data.get('marital_status_others')
        religion_others = cleaned_data.get('religion_others')
        occupation_others = cleaned_data.get('occupation_others')
        communication_hearing_others = cleaned_data.get(
            'communication_hearing_others')
        vital_sign_on_oxygen_therapy_flow_rate = cleaned_data.get(
            'vital_sign_on_oxygen_therapy_flow_rate')
        biohazard_infectious_disease_others = cleaned_data.get(
            'biohazard_infectious_disease_others')

        if admitted_others:
            cleaned_data['admitted'] = admitted_others
        if marital_status_others:
            cleaned_data['marital_status'] = marital_status_others
        if religion_others:
            cleaned_data['religion'] = religion_others
        if occupation_others:
            cleaned_data['occupation'] = occupation_others
        if communication_hearing_others:
            cleaned_data['communication_hearing'] = communication_hearing_others
        if vital_sign_on_oxygen_therapy_flow_rate:
            cleaned_data['vital_sign_on_oxygen_therapy'] = vital_sign_on_oxygen_therapy_flow_rate
        if biohazard_infectious_disease_others:
            cleaned_data['biohazard_infectious_disease'] = biohazard_infectious_disease_others
        return cleaned_data


class Admission_Form(BSModalForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(InlineRadios('')),
        )

    patient = forms.CharField(required=False, label="", widget=forms.HiddenInput(
        attrs={'class': "form-control"}))
    date_admission = forms.DateField(required=False, label=_("Date:"), initial=get_today, input_formats=settings.DATE_INPUT_FORMATS,
                                     widget=DatePickerInput(format="%d-%m-%Y", attrs={'class': "form-control"}))
    time_admission = forms.TimeField(required=False, label=_(
        "Time:"), initial=get_time, widget=TimePickerInput(format="%H:%M", attrs={'class': "form-control"}))
    admitted = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(
        attrs={'class': "form-control"}), choices=ADMITTED_CHOICES)
    admitted_others = forms.CharField(
        required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    mode = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(
        attrs={'class': "form-control"}), choices=MODE_CHOICES)

    date_diagnosis = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS,
                                     widget=DatePickerInput(format="%d-%m-%Y", attrs={'class': "form-control"}))
    diagnosis = forms.CharField(required=False, label="", widget=forms.Textarea(
        attrs={'class': "form-control", 'rows': 4, 'cols': 15}))
    date_operation = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS,
                                     widget=DatePickerInput(format="%d-%m-%Y", attrs={'class': "form-control"}))
    operation = forms.CharField(required=False, label="", widget=forms.Textarea(
        attrs={'class': "form-control", 'rows': 4, 'cols': 15}))

    general_condition = forms.MultipleChoiceField(required=False, label="", widget=forms.CheckboxSelectMultiple(
        attrs={'class': "form-control"}), choices=GENERAL_CONDITION_CHOICES)
    vital_sign_temperature = forms.DecimalField(required=False, label="", initial=default_desimal,
                                                min_value=0.0, widget=forms.NumberInput(attrs={'class': "form-control", 'step': 0.01}))
    vital_sign_pulse = forms.IntegerField(
        required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
    vital_sign_bp_upper = forms.IntegerField(
        required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
    vital_sign_bp_lower = forms.IntegerField(
        required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
    vital_sign_resp = forms.IntegerField(
        required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
    vital_sign_spo2 = forms.IntegerField(
        required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
    vital_sign_on_oxygen_therapy = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(
        attrs={'class': "form-control"}), choices=BOOLEAN_CHOICES)
    vital_sign_on_oxygen_therapy_flow_rate = forms.IntegerField(
        required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control form-horizontal"}))
    vital_sign_hgt = forms.IntegerField(required=False, label="", initial="0",
                                        min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))

    biohazard_infectious_disease = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(
        attrs={'class': "form-control"}), choices=YES_NO_CHOICES)
    biohazard_infectious_disease_others = forms.CharField(
        required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    invasive_line_insitu = forms.MultipleChoiceField(required=False, label="", widget=forms.CheckboxSelectMultiple(
        attrs={'class': "form-control"}), choices=INVASIVE_LINE_INSITU_CHOICES)
    invasive_line_insitu_others = forms.CharField(
        required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    medical_history = forms.MultipleChoiceField(required=False, label="", widget=forms.CheckboxSelectMultiple(
        attrs={'class': "form-control"}), choices=MEDICAL_HISTORY_CHOICES)
    medical_history_others = forms.CharField(
        required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    surgical_history_none = forms.MultipleChoiceField(required=False, label="None", widget=forms.CheckboxSelectMultiple(
        attrs={'class': "form-control"}), choices=SURGICAL_CHOICES)
    surgical_history = forms.CharField(required=False, label="", widget=forms.Textarea(
        attrs={'class': "form-control", 'rows': 4, 'cols': 15}))

    adaptive_aids_with_patient = forms.MultipleChoiceField(required=False, label="", widget=forms.CheckboxSelectMultiple(
        attrs={'class': "form-control"}), choices=ADAPTIVE_AIDS_WITH_PATIENT_CHOICES)
    adaptive_aids_with_patient_others = forms.CharField(
        required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    orientation = forms.MultipleChoiceField(required=False, label="", widget=forms.CheckboxSelectMultiple(
        attrs={'class': "form-control"}), choices=ORIENTATION_CHOICES)
    special_information = forms.CharField(
        required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    admission_by = forms.CharField(required=False, label="", widget=forms.TextInput(
        attrs={'class': "form-control", 'readonly': 'readonly'}))

    own_medication = forms.ChoiceField(required=False, label="", initial='No', widget=forms.RadioSelect(
        attrs={'class': "form-control"}), choices=YES_NO_CHOICES)
    medication_time = forms.TimeField(required=False, label="", initial=get_time, input_formats=settings.TIME_INPUT_FORMATS,
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
        attrs={'class': "form-control"}), choices=ADMISSION_FREQUENCY_CHOICES)

    def clean_admitted_others(self):
        return self.cleaned_data['admitted_others'].capitalize()

    def clean_biohazard_infectious_disease_others(self):
        return self.cleaned_data['biohazard_infectious_disease_others'].capitalize()

    def clean_invasive_line_insitu_others(self):
        return self.cleaned_data['invasive_line_insitu_others'].capitalize()

    def clean_medical_history_others(self):
        return self.cleaned_data['medical_history_others'].capitalize()

    def clean_surgical_history(self):
        return self.cleaned_data['surgical_history'].capitalize()

    def clean_adaptive_aids_with_patient_others(self):
        return self.cleaned_data['adaptive_aids_with_patient_others'].capitalize()

    def clean_special_information(self):
        return self.cleaned_data['special_information'].capitalize()

    def clean_diagnosis(self):
        return self.cleaned_data['diagnosis'].capitalize()

    def clean_operation(self):
        return self.cleaned_data['operation'].capitalize()

    def clean(self):
        cleaned_data = super().clean()
        admitted_others = cleaned_data.get('admitted_others')
        marital_status_others = cleaned_data.get('marital_status_others')
        religion_others = cleaned_data.get('religion_others')
        occupation_others = cleaned_data.get('occupation_others')
        communication_hearing_others = cleaned_data.get(
            'communication_hearing_others')
        vital_sign_on_oxygen_therapy_flow_rate = cleaned_data.get(
            'vital_sign_on_oxygen_therapy_flow_rate')
        biohazard_infectious_disease_others = cleaned_data.get(
            'biohazard_infectious_disease_others')

        if admitted_others:
            cleaned_data['admitted'] = admitted_others
        if marital_status_others:
            cleaned_data['marital_status'] = marital_status_others
        if religion_others:
            cleaned_data['religion'] = religion_others
        if occupation_others:
            cleaned_data['occupation'] = occupation_others
        if communication_hearing_others:
            cleaned_data['communication_hearing'] = communication_hearing_others
        if vital_sign_on_oxygen_therapy_flow_rate:
            cleaned_data['vital_sign_on_oxygen_therapy'] = vital_sign_on_oxygen_therapy_flow_rate
        if biohazard_infectious_disease_others:
            cleaned_data['biohazard_infectious_disease'] = biohazard_infectious_disease_others
        return cleaned_data


Admission_FormSet = formset_factory(
    Admission_Form,
    extra=0,
    max_num=5,
)


Admission_ModelFormSet = formset_factory(
    Admission_ModelForm,
    extra=1,
    max_num=5,
)


class Admission_ModelForm_Update(BSModalModelForm):
    class Meta:
        model = Admission
        fields = '__all__'
        widgets = {
            #           'patient': forms.HiddenInput(),
            #           'patient': forms.Select(),
            'patient': forms.Select(),
            #           'age': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(InlineRadios('')),
        )
#       self.fields['patient'].label = ':'

#   patient = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control", 'readonly': 'readonly'}))
#   patient = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}))
    date_admission = forms.DateField(required=False, label=_("Date:"), initial=get_today, input_formats=settings.DATE_INPUT_FORMATS,
                                     widget=DatePickerInput(format="%d-%m-%Y", attrs={'class': "form-control"}))
    time_admission = forms.TimeField(required=False, label=_(
        "Time:"), initial=get_time, widget=TimePickerInput(format="%H:%M", attrs={'class': "form-control"}))
    admitted_admission = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(
        attrs={'class': "form-control"}), choices=ADMITTED_CHOICES)
    admitted_others = forms.CharField(
        required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    mode_admission = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(
        attrs={'class': "form-control"}), choices=MODE_CHOICES)

    full_name = forms.CharField(required=False, label="", widget=forms.TextInput(
        attrs={'class': "form-control"}))
    ic_number = forms.CharField(max_length=14, required=False, label=_('IC No:'), validators=[
                                ic_number_validator], widget=forms.TextInput(attrs={'class': "form-control"}))
    ic_upload = forms.ImageField(required=False, label=_(
        'IC Upload:'), widget=forms.FileInput(attrs={'class': "form-control"}))
    age = forms.CharField(required=False, label="", widget=forms.TextInput(
        attrs={'class': "form-control", 'readonly': 'readonly'}))
    birth_date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS,
                                 widget=DatePickerInput(format="%d-%m-%Y", attrs={'class': "form-control"}))
    gender = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(
        attrs={'class': "form-control"}), choices=GENDER_CHOICES)
    marital_status = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(
        attrs={'class': "form-control"}), choices=MARITAL_CHOICES)
    marital_status_others = forms.CharField(
        required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    religion = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(
        attrs={'class': "form-control"}), choices=RELIGION_CHOICES)
    religion_others = forms.CharField(
        required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    occupation = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(
        attrs={'class': "form-control"}), choices=OCCUPATION_CHOICES)
    occupation_others = forms.CharField(
        required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    communication_sight = forms.ChoiceField(required=False, label=_("Sight"), widget=forms.RadioSelect(
        attrs={'class': "form-control"}), choices=COMMUNICATION_SIGHT_CHOICES)
    communication_hearing = forms.ChoiceField(required=False, label=_("Hearing"), widget=forms.RadioSelect(
        attrs={'class': "form-control"}), choices=COMMUNICATION_HEARING_CHOICES)
    communication_hearing_others = forms.CharField(required=False, label="", widget=forms.TextInput(
        attrs={'class': "form-control", 'style': "margin-top:1.0rem;"}))
    address = forms.CharField(required=False, label="", widget=forms.Textarea(
        attrs={'class': "form-control", 'rows': 4, 'cols': 15}))

    ec_name = forms.CharField(required=False, label="", widget=forms.TextInput(
        attrs={'class': "form-control"}))
    ec_ic_number = forms.CharField(max_length=14, required=False, label="", validators=[
                                   ic_number_validator], widget=forms.TextInput(attrs={'class': "form-control"}))
    ec_ic_upload = forms.ImageField(
        required=False, label="", widget=forms.FileInput(attrs={'class': "form-control"}))
    ec_relationship = forms.CharField(
        required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    ec_phone = forms.CharField(required=False, label="", widget=forms.TextInput(
        attrs={'class': "form-control"}))
    ec_address = forms.CharField(required=False, label="", widget=forms.Textarea(
        attrs={'class': "form-control", 'rows': 4, 'cols': 15}))

    general_condition = forms.MultipleChoiceField(required=False, label="", widget=forms.CheckboxSelectMultiple(
        attrs={'class': "form-control"}), choices=GENERAL_CONDITION_CHOICES)
    vital_sign_temperature = forms.DecimalField(required=False, label="", initial=default_desimal,
                                                min_value=0.0, widget=forms.NumberInput(attrs={'class': "form-control", 'step': 0.01}))
    vital_sign_pulse = forms.IntegerField(
        required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
    vital_sign_bp_upper = forms.IntegerField(
        required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
    vital_sign_bp_lower = forms.IntegerField(
        required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
    vital_sign_resp = forms.IntegerField(
        required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
    vital_sign_spo2 = forms.IntegerField(
        required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
    vital_sign_on_oxygen_therapy = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(
        attrs={'class': "form-control"}), choices=BOOLEAN_CHOICES)
    vital_sign_on_oxygen_therapy_flow_rate = forms.IntegerField(
        required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control form-horizontal"}))
    vital_sign_hgt = forms.IntegerField(required=False, label="", initial="0",
                                        min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))

    allergy_drug = forms.CharField(required=False, label=_(
        "Drug:"), widget=forms.TextInput(attrs={'class': "form-control"}))
    allergy_food = forms.CharField(required=False, label=_(
        "Food:"), widget=forms.TextInput(attrs={'class': "form-control"}))
    allergy_others = forms.CharField(required=False, label=_(
        "Others:"), widget=forms.TextInput(attrs={'class': "form-control"}))

    biohazard_infectious_disease = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(
        attrs={'class': "form-control"}), choices=YES_NO_CHOICES)
    biohazard_infectious_disease_others = forms.CharField(
        required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    invasive_line_insitu = forms.MultipleChoiceField(required=False, label="", widget=forms.CheckboxSelectMultiple(
        attrs={'class': "form-control"}), choices=INVASIVE_LINE_INSITU_CHOICES)
    invasive_line_insitu_others = forms.CharField(
        required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    medical_history = forms.MultipleChoiceField(required=False, label="", widget=forms.CheckboxSelectMultiple(
        attrs={'class': "form-control"}), choices=MEDICAL_HISTORY_CHOICES)
    medical_history_others = forms.CharField(
        required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    surgical_history_none = forms.MultipleChoiceField(required=False, label="None", widget=forms.CheckboxSelectMultiple(
        attrs={'class': "form-control"}), choices=SURGICAL_CHOICES)
    surgical_history = forms.CharField(required=False, label="", widget=forms.Textarea(
        attrs={'class': "form-control", 'rows': 4, 'cols': 15}))

    date_diagnosis = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS,
                                     widget=DatePickerInput(format="%d-%m-%Y", attrs={'class': "form-control"}))
    diagnosis = forms.CharField(required=False, label="", widget=forms.Textarea(
        attrs={'class': "form-control", 'rows': 4, 'cols': 15}))
    date_operation = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS,
                                     widget=DatePickerInput(format="%d-%m-%Y", attrs={'class': "form-control"}))
    operation = forms.CharField(required=False, label="", widget=forms.Textarea(
        attrs={'class': "form-control", 'rows': 4, 'cols': 15}))

    own_medication = forms.ChoiceField(required=False, label="", initial='No', widget=forms.RadioSelect(
        attrs={'class': "form-control"}), choices=YES_NO_CHOICES)
    medication_time = forms.TimeField(required=False, label="", initial=get_time, input_formats=settings.TIME_INPUT_FORMATS,
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
        attrs={'class': "form-control"}), choices=ADMISSION_FREQUENCY_CHOICES)

    adaptive_aids_with_patient = forms.MultipleChoiceField(required=False, label="", widget=forms.CheckboxSelectMultiple(
        attrs={'class': "form-control"}), choices=ADAPTIVE_AIDS_WITH_PATIENT_CHOICES)
    adaptive_aids_with_patient_others = forms.CharField(
        required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    orientation = forms.MultipleChoiceField(required=False, label="", widget=forms.CheckboxSelectMultiple(
        attrs={'class': "form-control"}), choices=ORIENTATION_CHOICES)
    special_information = forms.CharField(
        required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    admission_by = forms.CharField(required=False, label="", widget=forms.TextInput(
        attrs={'class': "form-control", 'readonly': 'readonly'}))

    def clean_admitted_others(self):
        return self.cleaned_data['admitted_others'].capitalize()

    def clean_biohazard_infectious_disease_others(self):
        return self.cleaned_data['biohazard_infectious_disease_others'].capitalize()

    def clean_invasive_line_insitu_others(self):
        return self.cleaned_data['invasive_line_insitu_others'].capitalize()

    def clean_medical_history_others(self):
        return self.cleaned_data['medical_history_others'].capitalize()

    def clean_surgical_history(self):
        return self.cleaned_data['surgical_history'].capitalize()

    def clean_adaptive_aids_with_patient_others(self):
        return self.cleaned_data['adaptive_aids_with_patient_others'].capitalize()

    def clean_special_information(self):
        return self.cleaned_data['special_information'].capitalize()

    def clean_diagnosis(self):
        return self.cleaned_data['diagnosis'].capitalize()

    def clean_operation(self):
        return self.cleaned_data['operation'].capitalize()

    def clean(self):
        cleaned_data = super().clean()
        admitted_others = cleaned_data.get('admitted_others')
        marital_status_others = cleaned_data.get('marital_status_others')
        religion_others = cleaned_data.get('religion_others')
        occupation_others = cleaned_data.get('occupation_others')
        communication_hearing_others = cleaned_data.get(
            'communication_hearing_others')
        vital_sign_on_oxygen_therapy_flow_rate = cleaned_data.get(
            'vital_sign_on_oxygen_therapy_flow_rate')
        biohazard_infectious_disease_others = cleaned_data.get(
            'biohazard_infectious_disease_others')

        if admitted_others:
            cleaned_data['admitted'] = admitted_others
        if marital_status_others:
            cleaned_data['marital_status'] = marital_status_others
        if religion_others:
            cleaned_data['religion'] = religion_others
        if occupation_others:
            cleaned_data['occupation'] = occupation_others
        if communication_hearing_others:
            cleaned_data['communication_hearing'] = communication_hearing_others
        if vital_sign_on_oxygen_therapy_flow_rate:
            cleaned_data['vital_sign_on_oxygen_therapy'] = vital_sign_on_oxygen_therapy_flow_rate
        if biohazard_infectious_disease_others:
            cleaned_data['biohazard_infectious_disease'] = biohazard_infectious_disease_others
        return cleaned_data


class MedicationAdministrationRecordTemplate_Form(BSModalForm):
    patient = forms.ChoiceField(required=False, label="", widget=forms.Select(
        attrs={'class': "form-control", 'style': "display:none;"}))
#   medication_template = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    medication_template = forms.CharField(
        required=False, label="", widget=forms.HiddenInput(attrs={'class': "form-control"}))
    own_medication = forms.ChoiceField(required=False, label="", initial='No', widget=forms.RadioSelect(
        attrs={'class': "form-control"}), choices=YES_NO_CHOICES)
    medication_date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS,
                                      widget=DatePickerInput(format="%d-%m-%Y", attrs={'class': "form-control"}))
    medication_time = forms.TimeField(required=False, label="", initial=get_time, input_formats=settings.TIME_INPUT_FORMATS,
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['own_medication'].widget = forms.HiddenInput()
        self.fields['medication_date'].widget = forms.HiddenInput()
        self.helper.layout = Layout(
            Div(InlineRadios('')),
        )


MedicationAdministrationRecordTemplate_FormSet = formset_factory(
    MedicationAdministrationRecordTemplate_Form,
    extra=0,
    max_num=24,
)


class MedicationAdministrationRecordTemplate_OwnForm(BSModalForm):
    patient = forms.ChoiceField(required=False, label="", widget=forms.Select(
        attrs={'class': "form-control", 'style': "display:none;"}))
    own_medication = forms.ChoiceField(required=False, label="", initial='No', widget=forms.RadioSelect(
        attrs={'class': "form-control"}), choices=YES_NO_CHOICES)
    medication_date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS,
                                      widget=DatePickerInput(format="%d-%m-%Y", attrs={'class': "form-control"}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['medication_date'].widget = forms.HiddenInput()
        self.helper.layout = Layout(
            Div(InlineRadios('')),
        )


class MedicationAdministrationRecordTemplate_ModelForm(BSModalModelForm):
    class Meta:
        model = MedicationAdministrationRecordTemplate
        fields = '__all__'
        widgets = {
            'patient': forms.Select(),
            'medication_template': forms.HiddenInput(),
            #           'own_medication': forms.HiddenInput(),
            #           'medication_date': forms.HiddenInput(),
        }

#   medication_template = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}))
#   medication_time = forms.TimeField(required=False, label="", initial=get_time, input_formats=settings.TIME_INPUT_FORMATS, widget=TimePickerInput(format="%H:%M", attrs={'class': "form-control"}))
#   medication_drug_name = forms.ModelChoiceField(queryset=Medicine.objects.all(), required=False, label="", widget=forms.Select(attrs={'class': "form-control"}))
#   medication_dosage = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
#   medication_unit = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=UNIT_CHOICES)
#   medication_tablet_capsule = forms.DecimalField(required=False, label="", initial=default_desimal_mar, min_value=0.0, widget=forms.NumberInput(attrs={'class': "form-control", 'step': 0.1}))
#   medication_frequency = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=MEDICATION_ADMINISTRATION_FREQUENCY_CHOICES)


MedicationAdministrationRecordTemplate_ModelFormSet = formset_factory(
    MedicationAdministrationRecordTemplate_Form,
    extra=0,
    max_num=24,
)
