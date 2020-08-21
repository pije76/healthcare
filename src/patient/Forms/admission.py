from django import forms
from django.utils.translation import ugettext_lazy as _

from ..models import *
from ..forms import *
from ..lookups import *
#from .custom_layout import *
from accounts.models import *

from bootstrap_modal_forms.forms import *


class Admission_FormSet_Helper(FormHelper):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.layout = Layout(
			'ec_name',
			'ec_ic_number',
			'ec_relationship',
			'ec_phone',
			'ec_address'
		)
		self.template = 'bootstrap/table_inline_formset.html'

# class PatientFamilyNameWidget(s2forms.ModelSelect2Widget):
#	search_fields = [
#		"full_name__icontains",
#	]


class AdmissionFormSet_Form(BSModalForm):
	#	class Meta:
	#		model = Admission
	#		fields = 'ec_name', 'ec_ic_number', 'ec_relationship', 'ec_phone', 'ec_address'
	#		widgets = {
	#			'patient': forms.HiddenInput(),
	#			'age': forms.HiddenInput(),
	#		}

	#	class Media(object):
	#		js = formset_media_js

	def __init__(self, *args, **kwargs):
		#		queryset = kwargs.pop('choices')
		super().__init__(*args, **kwargs)
#		self.fields['old_transaction'].queryset = queryset
		self.helper = FormHelper()
		self.helper.layout = Layout(
			Div(InlineRadios('')),
		)

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
		if adaptive_aids_with_patient_others:
			cleaned_data['adaptive_aids_with_patient'] = adaptive_aids_with_patient_others
		if surgical_history_none:
			cleaned_data['surgical_history'] = surgical_history_none
		return cleaned_data

	patient = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	ic_number = forms.CharField(max_length=14, required=False, label="", validators=[ic_number_validator], widget=forms.TextInput(attrs={'class': "form-control"}))
	date = forms.DateField(required=False, label=_("Date:"), initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d/%m/%Y", attrs={'class': "form-control"}))
	time = forms.TimeField(required=False, label=_("Time:"), initial=get_time, widget=TimePickerInput(format="%H:%M", attrs={'class': "form-control"}))
	admitted = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.ADMITTED_CHOICES)
#	admitted = ChoiceWithOtherField(required=False, label="", choices=Admission.ADMITTED_CHOICES)
	admitted_others = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	mode = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.MODE_CHOICES)

	birth_date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d/%m/%Y", attrs={'class': "form-control"}))
	age = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
#	age = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	gender = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.GENDER_CHOICES)
	marital_status = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.MARITAL_CHOICES)
	marital_status_others = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	address = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4, 'cols': 15}))
#	phone = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	religion = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.RELIGION_CHOICES)
	religion_others = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	occupation = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.OCCUPATION_CHOICES)
	occupation_others = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	communication_sight = forms.ChoiceField(required=False, label=_("Sight"), widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.COMMUNICATION_SIGHT_CHOICES)
	communication_hearing = forms.ChoiceField(required=False, label=_("Hearing"), widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.COMMUNICATION_HEARING_CHOICES)
	communication_hearing_others = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control", 'style': "margin-top:1.0rem;"}))

	general_condition = forms.MultipleChoiceField(required=False, label="", widget=forms.CheckboxSelectMultiple(attrs={'class': "form-control"}), choices=Admission.GENERAL_CONDITION_CHOICES)
	vital_sign_temperature = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	vital_sign_pulse = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	vital_sign_bp = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	vital_sign_resp = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	vital_sign_spo2 = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	vital_sign_on_oxygen_therapy = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.BOOLEAN_CHOICES)
	vital_sign_on_oxygen_therapy_flow_rate = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control form-horizontal"}))
	vital_sign_hgt = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	allergy_drug = forms.CharField(required=False, label=_("Drug(s):"), widget=forms.TextInput(attrs={'class': "form-control"}))
	allergy_food = forms.CharField(required=False, label=_("Food:"), widget=forms.TextInput(attrs={'class': "form-control"}))
	allergy_others = forms.CharField(required=False, label=_("Others:"), widget=forms.TextInput(attrs={'class': "form-control"}))
	biohazard_infectious_disease = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.BOOLEAN_CHOICES)
	biohazard_infectious_disease_others = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	invasive_line_insitu = forms.MultipleChoiceField(required=False, label="", widget=forms.CheckboxSelectMultiple(attrs={'class': "form-control"}), choices=Admission.INVASIVE_LINE_INSITU_CHOICES)
	invasive_line_insitu_others = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	medical_history = forms.MultipleChoiceField(required=False, label="", widget=forms.CheckboxSelectMultiple(attrs={'class': "form-control"}), choices=Admission.MEDICAL_HISTORY_CHOICES)
	medical_history_others = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
#	surgical_history_none = forms.ChoiceField(required=False, label=_("None"), widget=forms.CheckboxInput(attrs={'class': "form-control"}))
#	surgical_history_none = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.SURGICAL_CHOICES)
	surgical_history_none = forms.MultipleChoiceField(required=False, label="", widget=forms.CheckboxSelectMultiple(attrs={'class': "form-control"}), choices=Admission.SURGICAL_CHOICES)
	surgical_history = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4, 'cols': 15}))
	adaptive_aids_with_patient = forms.MultipleChoiceField(required=False, label="", widget=forms.CheckboxSelectMultiple(attrs={'class': "form-control"}), choices=Admission.ADAPTIVE_AIDS_WITH_PATIENT_CHOICES)
	adaptive_aids_with_patient_others = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	orientation = forms.MultipleChoiceField(required=False, label="", widget=forms.CheckboxSelectMultiple(attrs={'class': "form-control"}), choices=Admission.ORIENTATION_CHOICES)
	special_information = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	admission_by = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))

	ec_name = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	ec_ic_number = forms.CharField(max_length=14, required=False, label="", validators=[ic_number_validator], widget=forms.TextInput(attrs={'class': "form-control"}))
	ec_relationship = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
#	ec_phone = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	ec_phone = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	ec_address = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4, 'cols': 15}))

	date_diagnosis = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d/%m/%Y", attrs={'class': 'form-control'}))
	diagnosis = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4, 'cols': 15}))
	date_operation = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d/%m/%Y", attrs={'class': 'form-control'}))
	operation = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4, 'cols': 15}))

	own_medication = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.BOOLEAN_CHOICES)
	own_medication_drug_name = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	own_medication_dosage = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	own_medication_tablet_capsule = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	own_medication_frequency = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=Admission.MEDICATION_ADMINISTRATION_FREQUENCY_CHOICES)


AdmissionFormSet = formset_factory(
#	Admission,
	AdmissionFormSet_Form,
#	form=AdmissionFormSet_Form,
#	form=EmergencyForm,
	extra=0,
	max_num=1,
#	can_delete=True,

)



# class Admission_ModelForm(forms.ModelForm):
class Admission_ModelForm(BSModalModelForm):
	class Meta:
		model = Admission
		fields = '__all__'
		widgets = {
#			'patient': forms.HiddenInput(),
#			'age': forms.HiddenInput(),
		}

#	class Media:
#	class Media(object):
#		js = formset_media_js

	patient = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	date = forms.DateField(required=False, label=_("Date:"), initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d/%m/%Y", attrs={'class': "form-control"}))
	time = forms.TimeField(required=False, label=_("Time:"), initial=get_time, widget=TimePickerInput(format="%H:%M", attrs={'class': "form-control"}))
	admitted = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.ADMITTED_CHOICES)
#	admitted = ChoiceWithOtherField(required=False, label="", choices=Admission.ADMITTED_CHOICES)
	admitted_others = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	mode = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.MODE_CHOICES)

	birth_date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d/%m/%Y", attrs={'class': "form-control"}))
#	age = forms.CharField(required=False, label="", initial=_("*Automatically fill-in"), widget=forms.TextInput(attrs={'class': "form-control"}))
	age = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	gender = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.GENDER_CHOICES)
	marital_status = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.MARITAL_CHOICES)
	marital_status_others = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	address = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4, 'cols': 15}))
#	phone = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	religion = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.RELIGION_CHOICES)
	religion_others = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	occupation = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.OCCUPATION_CHOICES)
	occupation_others = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	communication_sight = forms.ChoiceField(required=False, label=_("Sight"), widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.COMMUNICATION_SIGHT_CHOICES)
	communication_hearing = forms.ChoiceField(required=False, label=_("Hearing"), widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.COMMUNICATION_HEARING_CHOICES)
	communication_hearing_others = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))

	general_condition = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.GENERAL_CONDITION_CHOICES)
	vital_sign_temperature = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	vital_sign_pulse = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	vital_sign_bp = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	vital_sign_resp = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	vital_sign_spo2 = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	vital_sign_on_oxygen_therapy = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.BOOLEAN_CHOICES)
	vital_sign_on_oxygen_therapy_flow_rate = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control form-horizontal"}))
	vital_sign_hgt = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	allergy_drug = forms.CharField(required=False, label=_("Drug(s):"), widget=forms.TextInput(attrs={'class': "form-control"}))
	allergy_food = forms.CharField(required=False, label=_("Food:"), widget=forms.TextInput(attrs={'class': "form-control"}))
	allergy_others = forms.CharField(required=False, label=_("Others:"), widget=forms.TextInput(attrs={'class': "form-control"}))
	biohazard_infectious_disease = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.BOOLEAN_CHOICES)
	biohazard_infectious_disease_others = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	invasive_line_insitu = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.INVASIVE_LINE_INSITU_CHOICES)
	invasive_line_insitu_others = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	medical_history = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.MEDICAL_HISTORY_CHOICES)
	medical_history_others = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
#	surgical_history_none = forms.ChoiceField(required=False, label=_("None"), widget=forms.CheckboxInput(attrs={'class': "form-control"}))
#	surgical_history_none = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.SURGICAL_CHOICES)
	surgical_history_none = forms.MultipleChoiceField(required=False, label="", widget=forms.CheckboxSelectMultiple(attrs={'class': "form-control"}), choices=Admission.SURGICAL_CHOICES)
	surgical_history = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4, 'cols': 15}))
	adaptive_aids_with_patient = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.ADAPTIVE_AIDS_WITH_PATIENT_CHOICES)
	adaptive_aids_with_patient_others = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	orientation = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.ORIENTATION_CHOICES)
	special_information = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	admission_by = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))

	ec_name = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	ec_ic_number = forms.CharField(max_length=14, required=False, label="", validators=[ic_number_validator], widget=forms.TextInput(attrs={'class': "form-control"}))
	ec_relationship = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
#	ec_phone = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	ec_phone = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	ec_address = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4, 'cols': 15}))

	date_diagnosis = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d/%m/%Y", attrs={'class': 'form-control'}))
	diagnosis = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4, 'cols': 15}))
	date_operation = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d/%m/%Y", attrs={'class': 'form-control'}))
	operation = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4, 'cols': 15}))

	own_medication = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.BOOLEAN_CHOICES)
	own_medication_drug_name = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	own_medication_dosage = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	own_medication_tablet_capsule = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	own_medication_frequency = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=Admission.MEDICATION_ADMINISTRATION_FREQUENCY_CHOICES)

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
#		formtag_prefix = re.sub('-[0-9]+$', '', kwargs.get('prefix', ''))
		self.helper = FormHelper()
#		self.helper.form_tag = True
#		self.helper.form_class = 'form-horizontal'
#		self.helper.label_class = 'col-md-3 create-label'
#		self.helper.field_class = 'col-md-9'
#		self.helper.layout = Layout(
#			Div(
#				Field('ec_name'),
#				Field('ec_ic_number'),
#				Field('ec_relationship'),
#				Field('ec_phone'),
#				Field('ec_address'),
#				Fieldset('Add another', FormSet('formset')),
#				FormSet('formset'),
#				Field('note'),
#				HTML("<br>"),
#				ButtonHolder(Submit('submit', 'save')),
#				Button('Add New', 'add-extra-formset-fields'),
#				css_class='formset_row-{}'.format(formtag_prefix)
#			),
#		)
#		self.fields['phone'].help_text = _('*Please enter valid phone number with following format: +[country code][area code][phone number]')
#		self.fields['ec_phone'].help_text = _('*Please enter valid phone number with following format: +[country code][area code][phone number]')
#		self.fields['ec_ic_number'].help_text = _('*IC Number format needs to be yymmdd-xx-zzzz.')

#	def get_age(self, request, obj=None, **kwargs):
#		form = super().get_age(request, obj, **kwargs)
#		if obj:
#			form.base_fields['age'].initial = int((datetime.now().date() - self.birth_date).days / 365.25)
#		return form

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
		if adaptive_aids_with_patient_others:
			cleaned_data['adaptive_aids_with_patient'] = adaptive_aids_with_patient_others
		if surgical_history_none:
			cleaned_data['surgical_history'] = surgical_history_none
		return cleaned_data


#	AdmissionFormSet = modelformset_factory(Admission, form=Admission_ModelForm, extra=2)
#	AdmissionFormSet = inlineformset_factory(Admission, form=Admission_ModelForm, fields=['ec_name', 'ec_ic_number', 'ec_relationship', 'ec_phone', 'ec_address'], extra=1, can_delete=True)

