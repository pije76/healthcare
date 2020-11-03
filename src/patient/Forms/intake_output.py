from django import forms
from django.utils.translation import ugettext_lazy as _

from ..models import *
from ..views import *
from ..forms import *
from ..lookups import *
from accounts.models import *

from bootstrap_modal_forms.forms import *


class IntakeOutput_ModelForm(BSModalModelForm):
	class Meta:
		model = IntakeOutput
		fields = [
			'patient',
			'date',
			'time',
			'intake_oral_type',
			'intake_oral_ml',
			'intake_parenteral_type',
			'intake_parenteral_ml',
			'intake_other_type',
			'intake_other_ml',
			'output_urine_type',
			'output_urine_ml',
			'output_gastric_ml',
			'output_other_type',
			'output_other_ml',
		]
		widgets = {
			'patient': forms.HiddenInput(),
		}

	date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d-%m-%Y", attrs={'class': "form-control"}))
	time = forms.TimeField(required=False, label="", initial=get_time, input_formats=settings.TIME_INPUT_FORMATS, widget=TimePickerInput(format="%H:%M", attrs={'class': "form-control"}))
	intake_oral_type = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	intake_oral_ml = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	intake_parenteral_type = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	intake_parenteral_ml = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	intake_other_type = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	intake_other_ml = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	output_urine_type = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	output_urine_ml = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	output_gastric_ml = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	output_other_type = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	output_other_ml = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))

#   def __init__(self, *args, **kwargs):
#       super().__init__(*args, **kwargs)
#       if not self.instance.time:
#           self.initial['time'] = self.instance.time


IntakeOutput_ModelFormSet = modelformset_factory(
	IntakeOutput,
	form=IntakeOutput_ModelForm,
	fields=(
		'time',
		'intake_oral_type',
		'intake_oral_ml',
		'intake_parenteral_type',
		'intake_parenteral_ml',
		'intake_other_type',
		'intake_other_ml',
		'output_urine_type',
		'output_urine_ml',
		'output_gastric_ml',
		'output_other_type',
		'output_other_ml',
	),
	extra=0,
#    max_num=0,
#   can_delete=True,
)


class IntakeOutput_Form(BSModalForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.fields['date'].widget = forms.HiddenInput()
		self.helper.layout = Layout(
			Div(InlineRadios('')),
		)

	patient = forms.CharField(required=False, label="", widget=forms.HiddenInput(attrs={'class': "form-control"}))
	date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d-%m-%Y", attrs={'class': "form-control", 'style': "display:none;"}))
	time = forms.TimeField(required=False, label="", initial=get_time, input_formats=settings.TIME_INPUT_FORMATS, widget=TimePickerInput(format="%H:%M", attrs={'class': "form-control"}))
	intake_oral_type = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	intake_oral_ml = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	intake_parenteral_type = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	intake_parenteral_ml = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	intake_other_type = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	intake_other_ml = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	output_urine_type = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	output_urine_ml = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	output_gastric_ml = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	output_other_type = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	output_other_ml = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))

	def clean_intake_oral_type(self):
		return self.cleaned_data['intake_oral_type'].capitalize()

	def clean_intake_parenteral_type(self):
		return self.cleaned_data['intake_parenteral_type'].capitalize()

	def clean_intake_other_type(self):
		return self.cleaned_data['intake_other_type'].capitalize()

	def clean_output_other_type(self):
		return self.cleaned_data['output_other_type'].capitalize()


IntakeOutput_FormSet = formset_factory(
	IntakeOutput_Form,
#   formset = MedicationAdministrationRecord_BaseFormSetFactory,
	extra=0,
	max_num=0,
#   can_delete=True,
)


class IntakeOutputForm(BSModalForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.layout = Layout(
			Div(InlineRadios('')),
		)

	date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d-%m-%Y", attrs={'class': "form-control"}))
