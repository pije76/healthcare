from django import forms
from django.core.validators import RegexValidator
from django.utils import timezone
from django.forms import ModelForm, renderers, RadioSelect, formset_factory, modelform_factory, modelformset_factory, inlineformset_factory, BaseModelFormSet, BaseInlineFormSet

from django.forms.widgets import ChoiceWidget
from django.utils.functional import lazy
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _
#from djangoformsetjs.utils import formset_media_js
from django.conf import settings


from crispy_forms.bootstrap import *
from crispy_forms.helper import *
from crispy_forms.layout import *


from mptt.forms import TreeNodeChoiceField
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput
from selectable.forms import AutoCompleteWidget
from durationwidget.widgets import TimeDurationWidget
from bootstrap4_datetime.widgets import DateTimePicker
#from ajax_select.fields import AutoCompleteSelectField, AutoCompleteSelectMultipleField
#from django_select2 import forms as s2forms
#from django_select2.forms import *
#from easy_select2 import select2_modelform, select2_modelform_meta
#from easy_select2.utils import apply_select2
#from jsignature.forms import JSignatureField
from djangoyearlessdate.forms import *

from .models import *
from .lookups import *
from .custom_layout import *
from accounts.models import *


import datetime
#from datetime import *

#now = date.today
#now = datetime.now()

def get_datetime():
	return timezone.now()
#	return datetime.date.strftime(datetime.today().date(), format="%d/%m/%Y %H:%M")
#	return datetime.now().strftime("%d/%m/%Y %H:%M")
#	return datetime.date.today().strftime('%d/%m/%Y %H:%M"')

def get_today():
#	return date.strftime(datetime.now().date(), format="%d/%m/%Y")
	return datetime.date.today().strftime('%d/%m/%Y')
#	return datetime.now().strftime('%d/%m/%Y')
#	return date.today
#	return datetime.now().date()

def get_time():
#	return datetime.now().time()
	return datetime.datetime.now().strftime("%H:%M")


messageserror = _("*IC Number format needs to be yymmdd-xx-zzzz.")
#ic_number_validator = RegexValidator("\d{6}\-\d{2}\-\d{4}", "IC Number format needs to be yymmdd-xx-zzzz.")
ic_number_validator = RegexValidator(regex='\d{6}\-\d{2}\-\d{4}', message=messageserror, code="invalid")
#ic_number_validator = RegexValidator(regex='^.{6}$-^.{2}$-^.{4}$', message=messageserror, code="invalid")
alphanumeric = RegexValidator(r'^[a-zA-Z]*$', 'Only alphanumeric characters are allowed.')

#now = date.today


mark_safe_lazy = lazy(mark_safe, six.text_type)


class SlimRadioSelect(RadioSelect):
	input_type = 'radio'
	template_name = 'django/forms/widgets/checkbox_select.html'
	option_template_name = 'django/forms/widgets/checkbox_option.html'


class PlaceholderInput(forms.widgets.Input):
	template_name = 'patient_form/placeholder.html'
	input_type = 'text'

	def get_context(self, name, value, attrs):
		context = super(PlaceholderInput, self).get_context(name, value, attrs)
		context['widget']['attrs']['maxlength'] = 50
		context['widget']['attrs']['placeholder'] = name.title()
		return context


class HorizontalRadioSelect(RadioSelect):
	template_name = 'patient_form/horizontal_radios.html'
	option_template_name = 'patient_form/horizontal_option.html'


class AdmissionForm(forms.ModelForm):
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
	admitted = forms.ChoiceField(required=False, label="", initial=_("Hospital"), widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.ADMITTED_CHOICES)
#	admitted = ChoiceWithOtherField(required=False, label="", choices=Admission.ADMITTED_CHOICES)
	admitted_others = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	mode = forms.ChoiceField(required=False, label="", initial=_("Walked-in"), widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.MODE_CHOICES)

	birth_date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d/%m/%Y", attrs={'class': "form-control"}))
#	age = forms.CharField(required=False, label="", initial=_("*Automatically fill-in"), widget=forms.TextInput(attrs={'class': "form-control"}))
	age = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	gender = forms.ChoiceField(required=False, label="", initial=_("Male"), widget=forms.RadioSelect(attrs={'class': "form-control col-4 tesr"}), choices=Admission.GENDER_CHOICES)
	marital_status = forms.ChoiceField(required=False, label="", initial=_("Single"), widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.MARITAL_CHOICES)
	marital_status_others = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	address = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4, 'cols': 15}))
#	phone = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	religion = forms.ChoiceField(required=False, label="", initial=_("Buddhist"), widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.RELIGION_CHOICES)
	religion_others = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	occupation = forms.ChoiceField(required=False, label="", initial=_("Retired"), widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.OCCUPATION_CHOICES)
	occupation_others = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	communication_sight = forms.ChoiceField(required=False, label=_("Sight"), initial=_("Good"), widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.COMMUNICATION_SIGHT_CHOICES)
	communication_hearing = forms.ChoiceField(required=False, label=_("Hearing"), initial=_("Good"), widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.COMMUNICATION_HEARING_CHOICES)
	communication_hearing_others = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))

	general_condition = forms.ChoiceField(required=False, label="", initial=_("Stable"), widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.GENERAL_CONDITION_CHOICES)
	vital_sign_temperature = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	vital_sign_pulse = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	vital_sign_bp = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	vital_sign_resp = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	vital_sign_spo2 = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	vital_sign_on_oxygen_therapy = forms.ChoiceField(required=False, label="", initial=False, widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.BOOLEAN_CHOICES)
	vital_sign_on_oxygen_therapy_flow_rate = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control form-horizontal"}))
	vital_sign_hgt = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	allergy_drug = forms.CharField(required=False, label=_("Drug(s):"), widget=forms.TextInput(attrs={'class': "form-control"}))
	allergy_food = forms.CharField(required=False, label=_("Food:"), widget=forms.TextInput(attrs={'class': "form-control"}))
	allergy_others = forms.CharField(required=False, label=_("Others:"), widget=forms.TextInput(attrs={'class': "form-control"}))
	biohazard_infectious_disease = forms.ChoiceField(required=False, label="", initial=False, widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.BOOLEAN_CHOICES)
	biohazard_infectious_disease_others = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	invasive_line_insitu = forms.ChoiceField(required=False, label="", initial=_("None"), widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.INVASIVE_LINE_INSITU_CHOICES)
	invasive_line_insitu_others = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	medical_history = forms.ChoiceField(required=False, label="", initial=_("No Chronic Illness"), widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.MEDICAL_HISTORY_CHOICES)
	medical_history_others = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
#	surgical_history_none = forms.ChoiceField(required=False, label=_("None"), initial=_("None"), widget=forms.CheckboxInput(attrs={'class': "form-control"}))
#	surgical_history_none = forms.ChoiceField(required=False, label="", initial=_("None"), widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.SURGICAL_CHOICES)
	surgical_history_none = forms.MultipleChoiceField(required=False, label="", initial=_("None"), widget=forms.CheckboxSelectMultiple(attrs={'class': "form-control"}), choices=Admission.SURGICAL_CHOICES)
	surgical_history = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4, 'cols': 15}))
	adaptive_aids_with_patient = forms.ChoiceField(required=False, label="", initial=_("Denture"), widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.ADAPTIVE_AIDS_WITH_PATIENT_CHOICES)
	adaptive_aids_with_patient_others = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	orientation = forms.ChoiceField(required=False, label="", initial=_("Nurse call system"), widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.ORIENTATION_CHOICES)
	special_information = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	admission_by = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))

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


class AdmissionFormSetForm(forms.Form):
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
		super().__init__(*args, **kwargs)
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
	date = forms.DateField(required=False, label=_("Date:"), initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d/%m/%Y", attrs={'class': "form-control"}))
	time = forms.TimeField(required=False, label=_("Time:"), initial=get_time, widget=TimePickerInput(format="%H:%M", attrs={'class': "form-control"}))
	admitted = forms.ChoiceField(required=False, label="", initial=_("Hospital"), widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.ADMITTED_CHOICES)
#	admitted = ChoiceWithOtherField(required=False, label="", choices=Admission.ADMITTED_CHOICES)
	admitted_others = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	mode = forms.ChoiceField(required=False, label="", initial=_("Walked-in"), widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.MODE_CHOICES)

	birth_date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d/%m/%Y", attrs={'class': "form-control"}))
	age = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
#	age = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	gender = forms.ChoiceField(required=False, label="", initial=_("Male"), widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.GENDER_CHOICES)
	marital_status = forms.ChoiceField(required=False, label="", initial=_("Single"), widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.MARITAL_CHOICES)
	marital_status_others = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	address = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4, 'cols': 15}))
#	phone = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	religion = forms.ChoiceField(required=False, label="", initial=_("Buddhist"), widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.RELIGION_CHOICES)
	religion_others = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	occupation = forms.ChoiceField(required=False, label="", initial=_("Retired"), widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.OCCUPATION_CHOICES)
	occupation_others = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	communication_sight = forms.ChoiceField(required=False, label=_("Sight"), initial=_("Good"), widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.COMMUNICATION_SIGHT_CHOICES)
	communication_hearing = forms.ChoiceField(required=False, label=_("Hearing"), initial=_("Good"), widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.COMMUNICATION_HEARING_CHOICES)
	communication_hearing_others = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))

	general_condition = forms.ChoiceField(required=False, label="", initial=_("Stable"), widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.GENERAL_CONDITION_CHOICES)
	vital_sign_temperature = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	vital_sign_pulse = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	vital_sign_bp = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	vital_sign_resp = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	vital_sign_spo2 = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	vital_sign_on_oxygen_therapy = forms.ChoiceField(required=False, label="", initial=False, widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.BOOLEAN_CHOICES)
	vital_sign_on_oxygen_therapy_flow_rate = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control form-horizontal"}))
	vital_sign_hgt = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	allergy_drug = forms.CharField(required=False, label=_("Drug(s):"), widget=forms.TextInput(attrs={'class': "form-control"}))
	allergy_food = forms.CharField(required=False, label=_("Food:"), widget=forms.TextInput(attrs={'class': "form-control"}))
	allergy_others = forms.CharField(required=False, label=_("Others:"), widget=forms.TextInput(attrs={'class': "form-control"}))
	biohazard_infectious_disease = forms.ChoiceField(required=False, label="", initial=False, widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.BOOLEAN_CHOICES)
	biohazard_infectious_disease_others = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	invasive_line_insitu = forms.ChoiceField(required=False, label="", initial=_("None"), widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.INVASIVE_LINE_INSITU_CHOICES)
	invasive_line_insitu_others = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	medical_history = forms.ChoiceField(required=False, label="", initial=_("No Chronic Illness"), widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.MEDICAL_HISTORY_CHOICES)
	medical_history_others = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
#	surgical_history_none = forms.ChoiceField(required=False, label=_("None"), initial=_("None"), widget=forms.CheckboxInput(attrs={'class': "form-control"}))
#	surgical_history_none = forms.ChoiceField(required=False, label="", initial=_("None"), widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.SURGICAL_CHOICES)
	surgical_history_none = forms.MultipleChoiceField(required=False, label="", initial=_("None"), widget=forms.CheckboxSelectMultiple(attrs={'class': "form-control"}), choices=Admission.SURGICAL_CHOICES)
	surgical_history = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4, 'cols': 15}))
	adaptive_aids_with_patient = forms.ChoiceField(required=False, label="", initial=_("Denture"), widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.ADAPTIVE_AIDS_WITH_PATIENT_CHOICES)
	adaptive_aids_with_patient_others = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	orientation = forms.ChoiceField(required=False, label="", initial=_("Nurse call system"), widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.ORIENTATION_CHOICES)
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

	own_medication = forms.ChoiceField(required=False, label="", initial=False, widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=Admission.BOOLEAN_CHOICES)
	own_medication_drug_name = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	own_medication_dosage = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	own_medication_tablet_capsule = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	own_medication_frequency = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))


#	AdmissionFormSet = modelformset_factory(Admission, form=AdmissionForm, extra=2)
#	AdmissionFormSet = inlineformset_factory(Admission, form=AdmissionForm, fields=['ec_name', 'ec_ic_number', 'ec_relationship', 'ec_phone', 'ec_address'], extra=1, can_delete=True)
AdmissionFormSet = formset_factory(
#	Admission,
	AdmissionFormSetForm,
#	form=AdmissionFormSetForm,
#	form=EmergencyForm,
	extra=0,
	max_num=1,
#	can_delete=True,

)


# class MyFormSetHelper(FormHelper):
#	def __init__(self, *args, **kwargs):
#		super(MyFormSetHelper, self).__init__(*args, **kwargs)
#		self.layout = Layout(
#			'ec_name',
#			'ec_ic_number',
#			'ec_relationship',
#			'ec_phone',
#			'ec_address'
#		)
#		self.template = 'bootstrap/table_inline_formset.html'

# class PatientFamilyNameWidget(s2forms.ModelSelect2Widget):
#	search_fields = [
#		"full_name__icontains",
#	]

class ApplicationForHomeLeaveForm(forms.ModelForm):
	class Meta:
		model = ApplicationForHomeLeave
		fields = '__all__'
		widgets = {
			'patient': forms.HiddenInput(),
		}

	patient = forms.CharField(required=False, label="", initial="patient", widget=forms.TextInput(attrs={'class': "form-control"}))
#	patient_family_name = forms.CharField(required=False, label="", initial="name", widget=forms.TextInput(attrs={'class': "form-control"}))
#	patient_family_name = AutoCompleteSelectField('full_name', required=True, label='', help_text=None)
#	patient_family_name = forms.CharField(required=False, label="", initial="name", widget=PatientFamilyNameWidget(attrs={'class': "form-control"}))
#	patient_family_name = apply_select2(forms.Select)
	patient_family_name = forms.CharField(required=False, label="", widget=AutoCompleteWidget(FullnameLookup, attrs={'class': "form-control"}))
	nric_number = forms.CharField(max_length=14, required=False, label="", initial='yymmdd-xx-zzzz', validators=[ic_number_validator], widget=forms.TextInput(attrs={'class': "form-control"}))
	patient_family_relationship = forms.CharField(required=False, label="", initial="myself/relationship", widget=forms.TextInput(attrs={'class': "form-control"}))
	patient_family_phone = forms.CharField(required=False, label="", initial="+60xxxxxxxx", widget=forms.TextInput(attrs={'class': "form-control"}))
	designation = forms.CharField(required=False, label="", initial="designation", widget=forms.TextInput(attrs={'class': "form-control"}))
	signature = forms.CharField(required=False, label="", initial="signature", widget=forms.TextInput(attrs={'class': "form-control"}))
#    signature = JSignatureField()
	date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d/%m/%Y", attrs={'class': "form-control"}))

class AppointmentForm(forms.ModelForm):

	class Meta:
		model = Appointment
		fields = '__all__'
#		exclude = ['patient']
		widgets = {
			'patient': forms.HiddenInput(),
		}

	date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d/%m/%Y", attrs={'class': "form-control"}))
	time = forms.TimeField(required=False, label="", initial=get_time, input_formats=settings.TIME_INPUT_FORMATS, widget=TimePickerInput(format="%H:%M", attrs={'class': "form-control"}))
	hospital_clinic_center = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4}))
	department = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4}))
	planning_investigation = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4}))
	treatment_order = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4}))


class CannulationForm(forms.ModelForm):

	class Meta:
		model = CatheterizationCannulation
		fields = '__all__'
		widgets = {
			'patient': forms.HiddenInput(),
		}

	nasogastric_tube_date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d/%m/%Y", attrs={'class': "form-control"}))
	nasogastric_tube_size = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
#	nasogastric_tube_type = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4}))
	nasogastric_tube_type = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=CatheterizationCannulation.NASOGASTRIC_TUBE_TYPE_CHOICES)	
	nasogastric_tube_location = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4}))
	nasogastric_tube_due_date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d/%m/%Y", attrs={'class': "form-control"}))
	nasogastric_tube_inserted_by = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	urinary_catheter_date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d/%m/%Y", attrs={'class': "form-control"}))
	urinary_catheter_size = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
#	urinary_catheter_type = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4}))
	urinary_catheter_type = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=CatheterizationCannulation.URINARY_CATHETER_TYPE_CHOICES)	
	urinary_catheter_due_date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d/%m/%Y", attrs={'class': "form-control"}))
	urinary_catheter_inserted_by = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	cannula_date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d/%m/%Y", attrs={'class': "form-control"}))
	cannula_size = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	cannula_location = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4}))
	cannula_due_date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d/%m/%Y", attrs={'class': "form-control"}))


class ChargesForm(forms.ModelForm):

	class Meta:
		model = Charges
		fields = '__all__'
		widgets = {
			'patient': forms.HiddenInput(),
		}

	date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d/%m/%Y", attrs={'class': "form-control"}))
	items = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	amount_unit = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	given_by = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))


class DressingForm(forms.ModelForm):
	class Meta:
		model = Dressing
		fields = '__all__'
		widgets = {
			'patient': forms.HiddenInput(),
		}

	date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d/%m/%Y", attrs={'class': "form-control"}))
	time = forms.TimeField(required=False, label="", initial=get_time, input_formats=settings.TIME_INPUT_FORMATS, widget=TimePickerInput(format="%H:%M", attrs={'class': "form-control"}))
	frequency_dressing = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=Dressing.WOUND_FREQUENCY_CHOICES)
	type_dressing = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	wound_location = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=Dressing.WOUND_LOCATION_CHOICES)
	wound_condition = TreeNodeChoiceField(required=False, label="", queryset=WoundCondition.objects, widget=forms.Select(attrs={'class': "form-control"}),)
#	wound_condition = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=Dressing.WOUND_CONDITION_CHOICES)
	photos = forms.FileInput()
	done_by = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.fields['photos'].label = ''


class EnteralFeedingRegimeForm(forms.ModelForm):

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


class HGTChartForm(forms.ModelForm):

	class Meta:
		model = HGTChart
		fields = '__all__'
		widgets = {
			'patient': forms.HiddenInput(),
		}

	date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d/%m/%Y", attrs={'class': "form-control"}))
	time = forms.TimeField(required=False, label="", initial=get_time, input_formats=settings.TIME_INPUT_FORMATS, widget=TimePickerInput(format="%H:%M", attrs={'class': "form-control"}))
	blood_glucose_reading = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
#	remark = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	remark = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control", 'autocomplete': 'off', 'pattern': '[A-Za-z ]+', 'title': 'Enter Characters Only '}))
	done_by = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))


class IntakeOutputChartForm(forms.Form):
	patient = forms.CharField(required=False, label="", widget=forms.HiddenInput(attrs={'class': "form-control"}))
	date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d/%m/%Y", attrs={'class': "form-control"}))
	time_intake = forms.TimeField(required=False, label="", initial=get_time, input_formats=settings.TIME_INPUT_FORMATS, widget=TimePickerInput(format="%H:%M", attrs={'class': "form-control"}))
	intake_oral_type = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	intake_oral_ml = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	intake_parenteral_type = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	intake_parenteral_ml = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	intake_other_type = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	intake_other_ml = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	time_output = forms.TimeField(required=False, label="", initial=get_time, input_formats=settings.TIME_INPUT_FORMATS, widget=TimePickerInput(format="%H:%M", attrs={'class': "form-control"}))
	output_urine_ml = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	output_urine_cum = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	output_gastric_ml = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	output_other_type = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	output_other_ml = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))


class IntakeOutputChartModelForm(forms.ModelForm):

	class Meta:
		model = IntakeOutputChart
		fields = '__all__'
		widgets = {
			'patient': forms.HiddenInput(),
		}

	date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d/%m/%Y", attrs={'class': "form-control"}))
	time_intake = forms.TimeField(required=False, label="", initial=get_time, input_formats=settings.TIME_INPUT_FORMATS, widget=TimePickerInput(format="%H:%M", attrs={'class': "form-control"}))
	intake_oral_type = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	intake_oral_ml = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	intake_parenteral_type = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	intake_parenteral_ml = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	intake_other_type = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	intake_other_ml = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	time_output = forms.TimeField(required=False, label="", initial=get_time, input_formats=settings.TIME_INPUT_FORMATS, widget=TimePickerInput(format="%H:%M", attrs={'class': "form-control"}))
	output_urine_ml = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	output_urine_cum = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	output_gastric_ml = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	output_other_type = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	output_other_ml = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
#		if not self.instance.time_intake:
#			self.initial['time_intake'] = self.instance.time_intake

IntakeOutputChart_FormSet_Factory = formset_factory(
	IntakeOutputChartForm,
#	formset = MedicationAdministrationRecord_BaseFormSetFactory,
	extra=0,
	max_num=0,
#	can_delete=True,
)

IntakeOutputChartFormSet = modelformset_factory(
	IntakeOutputChart,
	form=IntakeOutputChartModelForm,
#	form=EmergencyForm,
	fields=(
		'time_intake',
		'intake_oral_type',
		'intake_oral_ml',
		'intake_parenteral_type',
		'intake_parenteral_ml',
		'intake_other_type',
		'intake_other_ml',
		'time_output',
		'output_urine_ml',
		'output_urine_cum',
		'output_gastric_ml',
		'output_other_type',
		'output_other_ml',
	),
	extra=1,
	max_num=1,
#	can_delete=True,

)

class MaintainanceForm(forms.ModelForm):

	class Meta:
		model = Maintainance
		fields = '__all__'
		widgets = {
			'patient': forms.HiddenInput(),
		}

	date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d/%m/%Y", attrs={'class': "form-control"}))
	items = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	location_room = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	reported_by = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	status = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=Maintainance.STATUS_CHOICES)


class MedicationAdministrationRecord_BaseFormSetFactory(BaseModelFormSet):
	def __init__(self, *args, **kwargs):
		patient = kwargs.pop('patient', None)
		super().__init__(*args, **kwargs)
#        if patient:
#            for obj in self.forms:
#                if obj.instance.pk is None:
#                    obj.fields['patient'].initial = patient #or obj.initial['patient'] = patient

		for obj in self.forms:
			if obj.instance.pk is None:
				obj.instance.patient = patient 


class MedicationAdministrationRecord_FormSetHelper(FormHelper):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.layout = Layout(
			Fieldset(
				'medication_name',
				'medication_dosage',
				'medication_tab',
				'medication_frequency',
				'medication_route',
				'medication_date',
				'medication_time',
				'signature_nurse',
				'stat',
				'medicationstat_date_time',
				'given_by'
			),
			ButtonHolder(

			)
		)
		self.template = 'bootstrap/table_inline_formset.html'
#		self.template = 'bootstrap4/display_form.html'


class MedicationAdministrationRecord_Form(forms.Form):

	patient = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
#	patient = forms.HiddenInput()
	allergy = forms.CharField(required=False, label=_("Allergy"), widget=forms.TextInput(attrs={'class': "form-control"}))
	medication_name = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	medication_dosage = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	medication_tab = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=MedicationAdministrationRecord.TAB_CHOICES)
	medication_frequency = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=MedicationAdministrationRecord.MEDICATION_ADMINISTRATION_FREQUENCY_CHOICES)
	medication_route = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=MedicationAdministrationRecord.ROUTE_CHOICES)
	medication_date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d/%m/%Y", attrs={'class': "form-control"}))
	medication_time = forms.TimeField(required=False, label="", initial=get_time, input_formats=settings.TIME_INPUT_FORMATS, widget=TimePickerInput(format="%H:%M", attrs={'class': "form-control"}))
	signature_nurse = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=MedicationAdministrationRecord.SIGNATURE_CHOICES)
	stat = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=MedicationAdministrationRecord.STAT_CHOICES)
	medicationstat_date_time = forms.DateTimeField(required=False, label="", initial=timezone.now, input_formats=settings.DATETIME_INPUT_FORMATS, widget=DateTimePickerInput(format="%d/%m/%Y %H:%M", attrs={'class': "form-control"}))
	given_by = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))

class MedicationAdministrationRecord_ModelForm(forms.ModelForm):
	class Meta:
		model = MedicationAdministrationRecord
		fields = '__all__'
		widgets = {
			'patient': forms.Select(),
		}

#	patient = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}))
#	patient = forms.HiddenInput()
	allergy = forms.CharField(required=False, label=_("Allergy"), widget=forms.TextInput(attrs={'class': "form-control"}))
	stat = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=MedicationAdministrationRecord.STAT_CHOICES)
	medicationstat_date_time = forms.DateTimeField(required=False, label="", initial=timezone.now, input_formats=settings.DATETIME_INPUT_FORMATS, widget=DateTimePickerInput(format="%d/%m/%Y %H:%M", attrs={'class': "form-control"}))
	given_by = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))


class MedicationAdministrationRecord_InlineForm(forms.ModelForm):
	class Meta:
		model = MedicationAdministrationRecord
		fields = '__all__'
#		exclude = ('patient', )
		widgets = {
#			'patient': forms.Select(),
		}

	patient = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
#	patient = forms.HiddenInput()
	allergy = forms.CharField(required=False, label=_("Allergy"), widget=forms.TextInput(attrs={'class': "form-control"}))
	medication_name = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	medication_dosage = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	medication_tab = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=MedicationAdministrationRecord.TAB_CHOICES)
	medication_frequency = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=MedicationAdministrationRecord.MEDICATION_ADMINISTRATION_FREQUENCY_CHOICES)
	medication_route = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=MedicationAdministrationRecord.ROUTE_CHOICES)
	medication_date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d/%m/%Y", attrs={'class': "form-control"}))
	medication_time = forms.TimeField(required=False, label="", initial=get_time, input_formats=settings.TIME_INPUT_FORMATS, widget=TimePickerInput(format="%H:%M", attrs={'class': "form-control"}))
	signature_nurse = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=MedicationAdministrationRecord.SIGNATURE_CHOICES)
	stat = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=MedicationAdministrationRecord.STAT_CHOICES)
	medicationstat_date_time = forms.DateTimeField(required=False, label="", initial=timezone.now, input_formats=settings.DATETIME_INPUT_FORMATS, widget=DateTimePickerInput(format="%d/%m/%Y %H:%M", attrs={'class': "form-control"}))
	given_by = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))


MedicationAdministrationRecord_FormSet_Factory = formset_factory(
	MedicationAdministrationRecord_Form,
#	formset = MedicationAdministrationRecord_BaseFormSetFactory,
	extra=0,
	max_num=0,
#	can_delete=True,
)

# for modelform_factory
MedicationAdministrationRecord_ModelForm_Factory1 = modelform_factory(
	MedicationAdministrationRecord,
	fields=(
		'patient',
		'allergy',
		'medication_name',
		'medication_dosage',
		'medication_tab',
		'medication_frequency',
		'medication_route',
		'medication_date',
		'medication_time',
		'signature_nurse',
		'stat',
		'medicationstat_date_time',
		'given_by'
	),
)

# for modelform_factory
MedicationAdministrationRecord_ModelForm_Factory2 = modelform_factory(
	MedicationAdministrationRecord,
	form = MedicationAdministrationRecord_ModelForm,
	widgets={
		'patient': forms.Select(),
		'patient': forms.HiddenInput(),
		'medication_name': forms.TextInput(attrs={'class': "form-control"}),
		'medication_dosage': forms.NumberInput(attrs={'class': "form-control"}),
		'medication_tab': forms.Select(attrs={'class': "form-control"}, choices=MedicationAdministrationRecord.TAB_CHOICES),
		'medication_frequency': forms.Select(attrs={'class': "form-control"}, choices=MedicationAdministrationRecord.MEDICATION_ADMINISTRATION_FREQUENCY_CHOICES),
		'medication_route': forms.Select(attrs={'class': "form-control"}, choices=MedicationAdministrationRecord.ROUTE_CHOICES),
		'medication_date': DatePickerInput(attrs={'class': "form-control"}),
		'medication_time': TimePickerInput(attrs={'class': "form-control"}),
		'signature_nurse': forms.Select(attrs={'class': "form-control"}, choices=MedicationAdministrationRecord.SIGNATURE_CHOICES),
		'stat': forms.Select(attrs={'class': "form-control"}, choices=MedicationAdministrationRecord.STAT_CHOICES),
		'medicationstat_date_time': DateTimePickerInput(attrs={'class': "form-control"}),
		'given_by': forms.TextInput(attrs={'class': "form-control"}),
	},
)

MedicationAdministrationRecord_ModelFormSetFactory = modelformset_factory(
	MedicationAdministrationRecord,
	form = MedicationAdministrationRecord_ModelForm,
#	formset = MedicationAdministrationRecord_BaseFormSetFactory,
#	exclude = ['patient'], 
	extra=1
#	max_num=1,
#	can_delete=True,
)

MedicationAdministrationRecord_InlineFormSetFactory = inlineformset_factory(
	UserProfile,
	MedicationAdministrationRecord,
#	form = MedicationAdministrationRecord_InlineForm,
	extra=1,
#	max_num=1,
#	can_delete=False,
	fields=(
		'patient',
		'allergy',
		'medication_name',
		'medication_dosage',
		'medication_tab',
		'medication_frequency',
		'medication_route',
		'medication_date',
		'medication_time',
		'signature_nurse',
		'stat',
		'medicationstat_date_time',
		'given_by'
	),
#	labels = {
#		'allergy': 'Allergy',
#		'medication_name': '',
#		'medication_dosage': '',
#		'medication_tab': '',
#		'medication_frequency': '',
#		'medication_route': '',
#		'medication_date': '',
#		'medication_time': '',
#		'signature_nurse': '',
#		'stat': '',
#		'medicationstat_date_time': '',
#		'given_by': '',
#	},	
#	widgets={
#		'patient': forms.Select(),
#		'patient': forms.HiddenInput(),
#		'medication_name': forms.TextInput(attrs={'class': "form-control"}),
#		'medication_dosage': forms.NumberInput(attrs={'class': "form-control"}),
#		'medication_tab': forms.Select(attrs={'class': "form-control"}, choices=MedicationAdministrationRecord.TAB_CHOICES),
#		'medication_frequency': forms.Select(attrs={'class': "form-control"}, choices=MedicationAdministrationRecord.MEDICATION_ADMINISTRATION_FREQUENCY_CHOICES),
#		'medication_route': forms.Select(attrs={'class': "form-control"}, choices=MedicationAdministrationRecord.ROUTE_CHOICES),
#		'medication_date': DatePickerInput(attrs={'class': "form-control"}),
#		'medication_time': TimePickerInput(attrs={'class': "form-control"}),
#		'signature_nurse': forms.Select(attrs={'class': "form-control"}, choices=MedicationAdministrationRecord.SIGNATURE_CHOICES),
#		'stat': forms.Select(attrs={'class': "form-control"}, choices=MedicationAdministrationRecord.STAT_CHOICES),
#		'medicationstat_date_time': DateTimePickerInput(attrs={'class': "form-control"}),
#		'given_by': forms.TextInput(attrs={'class': "form-control"}),
#	},
#	help_texts = {
#		'medication_name': _('Some useful help text.'),
#	},
)

class MedicationRecordForm(forms.ModelForm):

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


class MiscellaneousChargesSlipForm(forms.ModelForm):

	class Meta:
		model = MiscellaneousChargesSlip
		fields = '__all__'
		widgets = {
			'patient': forms.HiddenInput(),
		}

	date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d/%m/%Y", attrs={'class': "form-control"}))
	items_procedures = forms.CharField(required=False, label="", initial="I'm still confused about this", widget=forms.TextInput(attrs={'class': "form-control"}))
	amount_unit = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	given_by = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))


class NursingForm(forms.ModelForm):

	class Meta:
		model = Nursing
		fields = '__all__'
		widgets = {
			'patient': forms.HiddenInput(),
		}

	date_time = forms.DateTimeField(required=False, label="", initial=timezone.now, input_formats=settings.DATETIME_INPUT_FORMATS, widget=DateTimePickerInput(format="%d/%m/%Y %H:%M", attrs={'class': "form-control"}))
	report = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 6, 'cols': 15}))


class OvertimeClaimForm(forms.ModelForm):

	class Meta:
		model = OvertimeClaim
		fields = '__all__'
		widgets = {
			'patient': forms.HiddenInput(),
			'total_hours': forms.HiddenInput(),
		}

	date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d/%m/%Y", attrs={'class': "form-control"}))
#	date = forms.DateTimeField(required=False, label="", widget=DatePickerInput(attrs={'class': "form-control"}))
#	date = forms.DateTimeField(required=False, label="", initial=timezone.now, input_formats=settings.DATETIME_INPUT_FORMATS, widget=DatePickerInput(format="%d/%m/%Y", attrs={'class': "form-control"}))
	duration_time = forms.DurationField(required=True, label="", initial="01:00:00", widget=forms.TextInput(attrs={'class': "form-control"}))
#	duration_time = forms.DurationField(required=False, label="", initial="00:05:00", widget=TimeDurationWidget(show_days=False, show_hours=True, show_minutes=True, show_seconds=False, attrs={'class': "form-control"}))
	hours = forms.TimeField(required=False, label="", initial=get_time, input_formats=settings.TIME_INPUT_FORMATS, widget=TimePickerInput(format="%H:%M", attrs={'class': "form-control"}))
#	hours = forms.DateTimeField(required=False, label="", initial=get_time, input_formats=settings.TIME_INPUT_FORMATS, widget=DatePickerInput(format="%H:%M", attrs={'class': "form-control"}))
#	total_hours = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	checked_sign_by = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	verify_by = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'class': "form-control"}))


class PhysioProgressNoteForm(forms.ModelForm):

	class Meta:
		model = PhysioProgressNote
		fields = '__all__'
		widgets = {
			'patient': forms.HiddenInput(),
		}

	report = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 6, 'cols': 15}))


class PhysiotherapyGeneralAssessmentForm(forms.ModelForm):
	class Meta:
		model = PhysiotherapyGeneralAssessment
		fields = '__all__'
		widgets = {
			'patient': forms.HiddenInput(),
		}

	doctor_diagnosis = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
	doctor_management = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
	problem = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
	pain_scale = forms.ChoiceField(required=False, label="", widget=HorizontalRadioSelect(), choices=PhysiotherapyGeneralAssessment.PAIN_SCALE_CHOICES)
	comments = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
	special_question = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
	general_health = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
	pmx_surgery = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
	ix_mri_x_ray = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
	medications_steroids = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
	occupation_recreation = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
	palpation = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
	pacemaker_hearing_aid = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
	splinting = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
	physical_examination_movement = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=PhysiotherapyGeneralAssessment.PHYSICAL_EXAMINATION_MOVEMENT_CHOICES)
	muscle_power = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
	functional_activities = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
	special_test = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
	date_time = forms.DateTimeField(required=False, label="", initial=timezone.now, input_formats=settings.DATETIME_INPUT_FORMATS, widget=DateTimePickerInput(format="%d/%m/%Y %H:%M", attrs={'class': "form-control"}))
	attending_physiotherapist = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
	current_history = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
	past_history = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
	neurological_reflexes = forms.CharField(required=False, label=_("Reflexes"), widget=forms.Textarea(attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
	neurological_motor = forms.CharField(required=False, label=_("Motor"), widget=forms.Textarea(attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
	neurological_sensation = forms.CharField(required=False, label=_("Sensation"), widget=forms.Textarea(attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
	clearing_test_other_joint = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
	physiotherapists_impression = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
	short_term_goals = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
	long_term_goals = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
	plan_treatment = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 5, 'cols': 10}))

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		helper = FormHelper()
		helper.layout = Layout(
			InlineRadios('pain_scale')
		)


class StaffRecordsForm(forms.ModelForm):

	class Meta:
		model = StaffRecords
		fields = '__all__'
		widgets = {
			'patient': forms.HiddenInput(),
		}

#	date = forms.DateField(required=False, label="", initial=datetime.datetime.now().year, input_formats=settings.DATE_INPUT_FORMATS, widget=YearPickerInput(format="%Y", attrs={'class': "form-control"}))
	date = forms.CharField(required=False, label="", initial=datetime.datetime.now().year, widget=YearPickerInput(format="%Y", attrs={'class': "form-control"}))
	annual_leave_days = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	public_holiday_days = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	replacement_public_holiday = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	medical_certificate = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	siri_no_diagnosis = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	emergency_leaves = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	emergency_leaves_reasons = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	unpaid_leaves = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	unpaid_leaves_reasons = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))


class StoolForm(forms.ModelForm):

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
	name = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))


class VisitingConsultantForm(forms.ModelForm):

	class Meta:
		model = VisitingConsultant
		fields = '__all__'
		widgets = {
			'patient': forms.HiddenInput(),
		}

	date_time = forms.DateTimeField(required=False, label="", initial=timezone.now, input_formats=settings.DATETIME_INPUT_FORMATS, widget=DateTimePickerInput(format="%d/%m/%Y %H:%M", attrs={'class': "form-control"}))
	complaints = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	treatment_orders = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	consultant = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))


class VitalSignFlowForm(forms.ModelForm):

	class Meta:
		model = VitalSignFlow
		fields = '__all__'
		widgets = {
			'patient': forms.HiddenInput(),
		}

	date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d/%m/%Y", attrs={'class': "form-control"}))
	time = forms.TimeField(required=False, label="", initial=get_time, input_formats=settings.TIME_INPUT_FORMATS, widget=TimePickerInput(format="%H:%M", attrs={'class': "form-control"}))
	temp = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	pulse = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	blood_pressure_systolic = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	blood_pressure_diastolic = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	respiration = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	spo2_percentage = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	spo2_o2 = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
