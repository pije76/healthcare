from django import forms
from django.utils.translation import ugettext_lazy as _

from ..models import *
from ..forms import *
from ..lookups import *
#from .custom_layout import *
from accounts.models import *

from bootstrap_modal_forms.forms import *


class Appointment_ModelForm(BSModalModelForm):

	class Meta:
		model = Appointment
		fields = [
			'patient',
			'date_time',
			'hospital_clinic_center',
			'department',
			'planning_investigation',
			'treatment_order',
		]
		widgets = {
			'patient': forms.HiddenInput(),
		}

#	patient = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}))
#	patient = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
#	date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d-%m-%Y", attrs={'class': "form-control"}))
#	time = forms.TimeField(required=False, label="", initial=get_time, input_formats=settings.TIME_INPUT_FORMATS, widget=TimePickerInput(format="%H:%M", attrs={'class': "form-control", 'style': "border:none;"}))
#	date_time = forms.DateTimeField(required=False, label="", initial=timezone.now, input_formats=settings.DATETIME_INPUT_FORMATS, widget=forms.SplitDateTimeWidget(date_format="%d-%m-%Y", time_format="%H:%M", attrs={'class': "form-control"}))
#	date_time = forms.SplitDateTimeField(required=False, label="", initial=timezone.now, widget=forms.SplitDateTimeWidget(date_format="%d-%m-%Y", time_format="%H:%M", date_attrs={'class': 'form-control datepickerinput'}, time_attrs={'class': 'form-control timepickerinput'}, attrs={'attrs': "attrs"}))
#	date_time = forms.SplitDateTimeField(required=False, label="", initial=timezone.now, widget=forms.SplitDateTimeWidget(attrs={'class': "form-control"}))
	date_time = forms.SplitDateTimeField(required=False, label="", initial=timezone.now, input_date_formats=settings.DATE_INPUT_FORMATS, input_time_formats=settings.TIME_INPUT_FORMATS, widget=forms.SplitDateTimeWidget(date_format="%d-%m-%Y", time_format="%H:%M", date_attrs={'class': 'form-control datepickerinput'}, time_attrs={'class': 'form-control timepickerinput'}, attrs={'class': "form-control"}))
#	date_time = forms.SplitDateTimeField(required=False, widget=DateTimePicker(options={"format": "DD-MM-YYYY HH:mm", "pickSeconds": True}))
	hospital_clinic_center = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4}))
	department = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4}))
	planning_investigation = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4}))
	treatment_order = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4}))

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
#		self.helper.layout = Layout(
#			MultiWidgetField('date_time'),
#		)


class Appointment_Form(BSModalForm):

	patient = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	date_time = forms.SplitDateTimeField(required=False, label="", initial=timezone.now, input_date_formats=settings.DATE_INPUT_FORMATS, input_time_formats=settings.TIME_INPUT_FORMATS, widget=forms.SplitDateTimeWidget(date_format="%d-%m-%Y", time_format="%H:%M", date_attrs={'class': 'form-control datepickerinput'}, time_attrs={'class': 'form-control timepickerinput'}, attrs={'class': "form-control"}))
	hospital_clinic_center = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4}))
	department = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4}))
	planning_investigation = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4}))
	treatment_order = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4}))

	def clean_hospital_clinic_center(self):
		return self.cleaned_data['hospital_clinic_center'].capitalize()

	def clean_department(self):
		return self.cleaned_data['department'].capitalize()

	def clean_planning_investigation(self):
		return self.cleaned_data['planning_investigation'].capitalize()

	def clean_treatment_order(self):
		return self.cleaned_data['treatment_order'].capitalize()

#	def __init__(self, *args, **kwargs):
#		super().__init__(*args, **kwargs)
#		self.helper = FormHelper()
#		self.helper.layout = Layout(
#			MultiWidgetField('date_time'),
#		)

