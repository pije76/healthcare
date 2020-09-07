from django import forms
from django.utils.translation import ugettext_lazy as _

from ..models import *
from ..forms import *
from ..lookups import *
#from .custom_layout import *
from accounts.models import *

from bootstrap_modal_forms.forms import *


class Admission_ModelForm(BSModalModelForm):
	class Meta:
		model = UserProfile
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.layout = Layout(
			Div(InlineRadios('')),
		)

	patient = forms.CharField(required=False, label="", widget=forms.HiddenInput(attrs={'class': "form-control"}))
	ic_number = forms.CharField(max_length=14, required=False, label=_('IC No:'), validators=[ic_number_validator], widget=forms.TextInput(attrs={'class': "form-control"}))
	ic_upload = forms.ImageField(required=False, label=_('Upload IC:'), widget=forms.FileInput(attrs={'class': "form-control"}))
	date = forms.DateField(required=False, label=_("Date:"), initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d/%m/%Y", attrs={'class': "form-control"}))
	time = forms.TimeField(required=False, label=_("Time:"), initial=get_time, widget=TimePickerInput(format="%H:%M", attrs={'class': "form-control"}))
	admitted = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.ADMITTED_CHOICES)
	admitted_others = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	mode = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.MODE_CHOICES)

	general_condition = forms.MultipleChoiceField(required=False, label="", widget=forms.CheckboxSelectMultiple(attrs={'class': "form-control"}), choices=Admission.GENERAL_CONDITION_CHOICES)
	vital_sign_temperature = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	vital_sign_pulse = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	vital_sign_bp = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	vital_sign_resp = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	vital_sign_spo2 = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	vital_sign_on_oxygen_therapy = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.BOOLEAN_CHOICES)
	vital_sign_on_oxygen_therapy_flow_rate = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control form-horizontal"}))
	vital_sign_hgt = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))

	biohazard_infectious_disease = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.BOOLEAN_CHOICES)
	biohazard_infectious_disease_others = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	invasive_line_insitu = forms.MultipleChoiceField(required=False, label="", widget=forms.CheckboxSelectMultiple(attrs={'class': "form-control"}), choices=Admission.INVASIVE_LINE_INSITU_CHOICES)
	invasive_line_insitu_others = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	medical_history = forms.MultipleChoiceField(required=False, label="", widget=forms.CheckboxSelectMultiple(attrs={'class': "form-control"}), choices=Admission.MEDICAL_HISTORY_CHOICES)
	medical_history_others = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	surgical_history_none = forms.MultipleChoiceField(required=False, label="", widget=forms.CheckboxSelectMultiple(attrs={'class': "form-control"}), choices=Admission.SURGICAL_CHOICES)
	surgical_history = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4, 'cols': 15}))
	adaptive_aids_with_patient = forms.MultipleChoiceField(required=False, label="", widget=forms.CheckboxSelectMultiple(attrs={'class': "form-control"}), choices=Admission.ADAPTIVE_AIDS_WITH_PATIENT_CHOICES)
	adaptive_aids_with_patient_others = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	orientation = forms.MultipleChoiceField(required=False, label="", widget=forms.CheckboxSelectMultiple(attrs={'class': "form-control"}), choices=Admission.ORIENTATION_CHOICES)
	special_information = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	admission_by = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))

	date_diagnosis = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d/%m/%Y", attrs={'class': 'form-control'}))
	diagnosis = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4, 'cols': 15}))
	date_operation = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d/%m/%Y", attrs={'class': 'form-control'}))
	operation = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4, 'cols': 15}))

	medication = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.BOOLEAN_CHOICES)
	medication_drug_name = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	medication_dosage = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	medication_tablet_capsule = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	medication_frequency = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=Admission.MEDICATION_ADMINISTRATION_FREQUENCY_CHOICES)

	def clean(self):
		cleaned_data = super().clean()
		admitted_others = cleaned_data.get('admitted_others')
		marital_status_others = cleaned_data.get('marital_status_others')
		religion_others = cleaned_data.get('religion_others')
		occupation_others = cleaned_data.get('occupation_others')
		communication_hearing_others = cleaned_data.get('communication_hearing_others')
		vital_sign_on_oxygen_therapy_flow_rate = cleaned_data.get('vital_sign_on_oxygen_therapy_flow_rate')
		biohazard_infectious_disease_others = cleaned_data.get('biohazard_infectious_disease_others')
		invasive_line_insitu_others = cleaned_data.get('invasive_line_insitu_others')
		medical_history_others = cleaned_data.get('medical_history_others')
		adaptive_aids_with_patient_others = cleaned_data.get('adaptive_aids_with_patient_others')
		surgical_history_none = cleaned_data.get('surgical_history_none')

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
		if invasive_line_insitu_others:
			cleaned_data['invasive_line_insitu'] = invasive_line_insitu_others
		if medical_history_others:
			cleaned_data['medical_history'] = medical_history_others
		if surgical_history_none:
			cleaned_data['surgical_history'] = surgical_history_none
		if adaptive_aids_with_patient_others:
			cleaned_data['adaptive_aids_with_patient'] = adaptive_aids_with_patient_others
		return cleaned_data


Admission_ModelFormSet = formset_factory(
	Admission_ModelForm,
	extra=0,
)


class UserProfile_ModelForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.layout = Layout(
			Div(InlineRadios('')),
		)

	full_name = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	username = forms.CharField(required=False, label="", widget=forms.HiddenInput(attrs={'class': "form-control"}))
	is_patient = forms.BooleanField(required=False, label='', widget=forms.HiddenInput())
	is_active = forms.BooleanField(required=False, label='', widget=forms.HiddenInput())
	email = forms.EmailField(required=False, label="", widget=forms.HiddenInput(attrs={'class': "form-control"}))
	password = forms.CharField(required=False, label="", widget=forms.HiddenInput(attrs={'class': "form-control"}))
	date_joined = forms.DateTimeField(required=False, label="", input_formats=settings.DATETIME_INPUT_FORMATS, widget=DateTimePickerInput(format="%d/%m/%Y %H:%M", attrs={'class': "form-control"}))
#	date_joined = forms.DateTimeField(required=False, label="", input_formats=settings.DATETIME_INPUT_FORMATS, widget=forms.HiddenInput(attrs={'class': "form-control"}))
#	date_joined = forms.DateTimeField(widget=forms.HiddenInput())
	ic_number = forms.CharField(max_length=14, required=False, label=_('IC No:'), validators=[ic_number_validator], widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': _("yymmdd-xx-zzzz")}))
	ic_upload = forms.ImageField(required=False, label=_('Upload IC:'), widget=forms.FileInput(attrs={'class': "form-control"}))
	birth_date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d/%m/%Y", attrs={'class': "form-control"}))
	age = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': _("*auto fill-in")}))
	gender = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.GENDER_CHOICES)
	marital_status = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.MARITAL_CHOICES)
	marital_status_others = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	religion = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.RELIGION_CHOICES)
	religion_others = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	occupation = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.OCCUPATION_CHOICES)
	occupation_others = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	communication_sight = forms.ChoiceField(required=False, label=_("Sight"), widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.COMMUNICATION_SIGHT_CHOICES)
	communication_hearing = forms.ChoiceField(required=False, label=_("Hearing"), widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.COMMUNICATION_HEARING_CHOICES)
	communication_hearing_others = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control", 'style': "margin-top:1.0rem;"}))
	address = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4, 'cols': 15}))

	def clean(self):
		cleaned_data = super().clean()
		marital_status_others = cleaned_data.get('marital_status_others')
		religion_others = cleaned_data.get('religion_others')
		occupation_others = cleaned_data.get('occupation_others')
		communication_hearing_others = cleaned_data.get('communication_hearing_others')

		if marital_status_others:
			cleaned_data['marital_status'] = marital_status_others
		if religion_others:
			cleaned_data['religion'] = religion_others
		if occupation_others:
			cleaned_data['occupation'] = occupation_others
		if communication_hearing_others:
			cleaned_data['communication_hearing'] = communication_hearing_others

	def clean_marital_status_others(self):
		return self.cleaned_data['marital_status_others'].capitalize()

	def clean_religion_others(self):
		return self.cleaned_data['religion_others'].capitalize()

	def clean_occupation_others(self):
		return self.cleaned_data['occupation_others'].capitalize()

	def clean_communication_hearing_others(self):
		return self.cleaned_data['communication_hearing_others'].capitalize()

	def clean_address(self):
		return self.cleaned_data['address'].capitalize()


class Family_Form(forms.Form):

	patient = forms.CharField(required=False, label="", widget=forms.HiddenInput(attrs={'class': "form-control"}))
	ec_name = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	ec_ic_number = forms.CharField(max_length=14, required=False, label="", validators=[ic_number_validator], widget=forms.TextInput(attrs={'class': "form-control"}))
	ec_ic_upload = forms.ImageField(required=False, label="", widget=forms.FileInput(attrs={'class': "form-control"}))
	ec_relationship = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	ec_phone = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	ec_address = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4, 'cols': 15}))

	def clean_ec_name(self):
		return self.cleaned_data['ec_name'].capitalize()

	def clean_ec_relationship(self):
		return self.cleaned_data['ec_relationship'].capitalize()

	def clean_ec_address(self):
		return self.cleaned_data['ec_address'].capitalize()


Family_FormSet = formset_factory(
	Family_Form,
	extra=0,
)


class Family_ModelForm(forms.ModelForm):
	class Meta:
		model = Family
		fields = '__all__'

	patient = forms.CharField(required=False, label="", widget=forms.HiddenInput(attrs={'class': "form-control"}))
	ec_name = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	ec_ic_number = forms.CharField(max_length=14, required=False, label="", validators=[ic_number_validator], widget=forms.TextInput(attrs={'class': "form-control"}))
	ec_ic_upload = forms.ImageField(required=False, label="", widget=forms.FileInput(attrs={'class': "form-control"}))
	ec_relationship = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	ec_phone = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	ec_address = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4, 'cols': 15}))


Family_ModelFormSet = modelformset_factory(
	Family,
	form=Family_Form,
	fields=(
		'patient',
		'ec_name',
		'ec_ic_number',
		'ec_ic_upload',
		'ec_relationship',
	),
	extra=0,
)


class Admission_Form(BSModalForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.layout = Layout(
			Div(InlineRadios('')),
		)

	patient = forms.CharField(required=False, label="", widget=forms.HiddenInput(attrs={'class': "form-control"}))
	date_admission = forms.DateField(required=False, label=_("Date:"), initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d/%m/%Y", attrs={'class': "form-control"}))
	time_admission = forms.TimeField(required=False, label=_("Time:"), initial=get_time, widget=TimePickerInput(format="%H:%M", attrs={'class': "form-control"}))
	admitted = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.ADMITTED_CHOICES)
	admitted_others = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	mode = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.MODE_CHOICES)

	general_condition = forms.MultipleChoiceField(required=False, label="", widget=forms.CheckboxSelectMultiple(attrs={'class': "form-control"}), choices=Admission.GENERAL_CONDITION_CHOICES)
	vital_sign_temperature = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	vital_sign_pulse = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	vital_sign_bp = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	vital_sign_resp = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	vital_sign_spo2 = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	vital_sign_on_oxygen_therapy = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.BOOLEAN_CHOICES)
	vital_sign_on_oxygen_therapy_flow_rate = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control form-horizontal"}))
	vital_sign_hgt = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))

	biohazard_infectious_disease = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.BOOLEAN_CHOICES)
	biohazard_infectious_disease_others = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	invasive_line_insitu = forms.MultipleChoiceField(required=False, label="", widget=forms.CheckboxSelectMultiple(attrs={'class': "form-control"}), choices=Admission.INVASIVE_LINE_INSITU_CHOICES)
	invasive_line_insitu_others = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	medical_history = forms.MultipleChoiceField(required=False, label="", widget=forms.CheckboxSelectMultiple(attrs={'class': "form-control"}), choices=Admission.MEDICAL_HISTORY_CHOICES)
	medical_history_others = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	surgical_history_none = forms.MultipleChoiceField(required=False, label="", widget=forms.CheckboxSelectMultiple(attrs={'class': "form-control"}), choices=Admission.SURGICAL_CHOICES)
	surgical_history = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4, 'cols': 15}))

	adaptive_aids_with_patient = forms.MultipleChoiceField(required=False, label="", widget=forms.CheckboxSelectMultiple(attrs={'class': "form-control"}), choices=Admission.ADAPTIVE_AIDS_WITH_PATIENT_CHOICES)
	adaptive_aids_with_patient_others = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	orientation = forms.MultipleChoiceField(required=False, label="", widget=forms.CheckboxSelectMultiple(attrs={'class': "form-control"}), choices=Admission.ORIENTATION_CHOICES)
	special_information = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	admission_by = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))

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


	def clean(self):
		cleaned_data = super().clean()
		admitted_others = cleaned_data.get('admitted_others')
		marital_status_others = cleaned_data.get('marital_status_others')
		religion_others = cleaned_data.get('religion_others')
		occupation_others = cleaned_data.get('occupation_others')
		communication_hearing_others = cleaned_data.get('communication_hearing_others')
		vital_sign_on_oxygen_therapy_flow_rate = cleaned_data.get('vital_sign_on_oxygen_therapy_flow_rate')
		biohazard_infectious_disease_others = cleaned_data.get('biohazard_infectious_disease_others')
		invasive_line_insitu_others = cleaned_data.get('invasive_line_insitu_others')
		medical_history_others = cleaned_data.get('medical_history_others')
		adaptive_aids_with_patient_others = cleaned_data.get('adaptive_aids_with_patient_others')
		surgical_history_none = cleaned_data.get('surgical_history_none')

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
		if invasive_line_insitu_others:
			cleaned_data['invasive_line_insitu'] = invasive_line_insitu_others
		if medical_history_others:
			cleaned_data['medical_history'] = medical_history_others
		if surgical_history_none:
			cleaned_data['surgical_history'] = surgical_history_none
		if adaptive_aids_with_patient_others:
			cleaned_data['adaptive_aids_with_patient'] = adaptive_aids_with_patient_others
		return cleaned_data


class Admission_FormSet(BSModalForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.layout = Layout(
			Div(InlineRadios('')),
		)

	patient = forms.CharField(required=False, label="", widget=forms.HiddenInput(attrs={'class': "form-control"}))
	date_diagnosis = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d/%m/%Y", attrs={'class': 'form-control'}))
	diagnosis = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4, 'cols': 15}))
	date_operation = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d/%m/%Y", attrs={'class': 'form-control'}))
	operation = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4, 'cols': 15}))

	def clean_diagnosis(self):
		return self.cleaned_data['diagnosis'].capitalize()

	def clean_operation(self):
		return self.cleaned_data['operation'].capitalize()


AdmissionFormSet = formset_factory(
	Admission_FormSet,
	extra=0,
)


class Allergy_ModelForm(BSModalModelForm):
	class Meta:
		model = Allergy
		fields = '__all__'

	patient = forms.CharField(required=False, label="", widget=forms.HiddenInput(attrs={'class': "form-control"}))
	allergy_drug = forms.CharField(required=False, label=_("Drug(s):"), widget=forms.TextInput(attrs={'class': "form-control"}))
	allergy_food = forms.CharField(required=False, label=_("Food:"), widget=forms.TextInput(attrs={'class': "form-control"}))
	allergy_others = forms.CharField(required=False, label=_("Others:"), widget=forms.TextInput(attrs={'class': "form-control"}))

	def clean_allergy_drug(self):
		return self.cleaned_data['allergy_drug'].capitalize()

	def clean_allergy_food(self):
		return self.cleaned_data['allergy_food'].capitalize()

	def clean_allergy_others(self):
		return self.cleaned_data['allergy_others'].capitalize()


class Allergy_Form(BSModalForm):

	patient = forms.CharField(required=False, label="", widget=forms.HiddenInput(attrs={'class': "form-control"}))
	allergy_drug = forms.CharField(required=False, label=_("Drug(s):"), widget=forms.TextInput(attrs={'class': "form-control"}))
	allergy_food = forms.CharField(required=False, label=_("Food:"), widget=forms.TextInput(attrs={'class': "form-control"}))
	allergy_others = forms.CharField(required=False, label=_("Others:"), widget=forms.TextInput(attrs={'class': "form-control"}))

	def clean_allergy_drug(self):
		return self.cleaned_data['allergy_drug'].capitalize()

	def clean_allergy_food(self):
		return self.cleaned_data['allergy_food'].capitalize()

	def clean_allergy_others(self):
		return self.cleaned_data['allergy_others'].capitalize()


class Medication_Form(BSModalForm):

	patient = forms.CharField(required=False, label="", widget=forms.HiddenInput(attrs={'class': "form-control"}))
	medication = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.BOOLEAN_CHOICES)
#	medication = forms.BooleanField(required=False, label="", widget=forms.RadioSelect(attrs={'class': "form-control"}))
#	medication = forms.BooleanField(required=False, label="", widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.BOOLEAN_CHOICES)
	medication_drug_name = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	medication_dosage = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	medication_tablet_capsule = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	medication_frequency = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=Admission.MEDICATION_ADMINISTRATION_FREQUENCY_CHOICES)

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.layout = Layout(
			Div(InlineRadios('')),
		)

	def clean_medication_drug_name(self):
		return self.cleaned_data['medication_drug_name'].capitalize()


Medication_FormSet = formset_factory(
	Medication_Form,
	extra=0,
)


class Medication_ModelForm(BSModalModelForm):
	class Meta:
		model = Medication
		fields = '__all__'


Medication_ModelFormSet = modelformset_factory(
	Medication,
	form=Medication_ModelForm,
	fields=(
		'patient',
		'medication',
		'medication_drug_name',
		'medication_dosage',
		'medication_tablet_capsule',
		'medication_frequency',
	),
	extra=0,
)
