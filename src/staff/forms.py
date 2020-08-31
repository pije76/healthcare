from django import forms
from django.conf import settings
from django.core.validators import RegexValidator
from django.forms import ModelForm, RadioSelect, formset_factory, modelform_factory, modelformset_factory, inlineformset_factory, BaseModelFormSet, BaseInlineFormSet
from django.utils import timezone
from django.utils.functional import lazy
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _


from crispy_forms.bootstrap import *
from crispy_forms.helper import *
from crispy_forms.layout import *


from mptt.forms import TreeNodeChoiceField
from bootstrap_datepicker_plus import *
from selectable.forms import *
#from durationwidget.widgets import TimeDurationWidget
#from bootstrap4_datetime.widgets import DateTimePicker
#from ajax_select.fields import AutoCompleteSelectField, AutoCompleteSelectMultipleField
#from django_select2 import forms as s2forms
#from django_select2.forms import *
#from easy_select2 import select2_modelform, select2_modelform_meta
#from easy_select2.utils import apply_select2
#from jsignature.forms import JSignatureField
from djangoyearlessdate import forms as form
from bootstrap_modal_forms.forms import *
#from dal import autocomplete
from bootstrap_datepicker_plus import YearPickerInput


from .models import *
#from .lookups import *
#from .custom_layout import *
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


#mark_safe_lazy = lazy(mark_safe, six.text_type)


class SlimRadioSelect(RadioSelect):
	input_type = 'radio'
	template_name = 'django/forms/widgets/checkbox_select.html'
	option_template_name = 'django/forms/widgets/checkbox_option.html'


class PlaceholderInput(forms.widgets.Input):
	template_name = 'patient/placeholder.html'
	input_type = 'text'

	def get_context(self, name, value, attrs):
		context = super(PlaceholderInput, self).get_context(name, value, attrs)
		context['widget']['attrs']['maxlength'] = 50
		context['widget']['attrs']['placeholder'] = name.title()
		return context


class HorizontalRadioSelect(RadioSelect):
	template_name = 'patient/horizontal_radios.html'
	option_template_name = 'patient/horizontal_option.html'


class StaffRecord_ModelForm(BSModalModelForm):

	class Meta:
		model = StaffRecords
		fields = '__all__'
		widgets = {
			'staff': forms.HiddenInput(),
		}

#	staff = forms.CharField(required=False, label="", widget=forms.HiddenInput(attrs={'class': "form-control"}))
	date = forms.DateField(required=False, label="", initial=datetime.datetime.now().year, widget=YearPickerInput(format="%Y", attrs={'class': "form-control"}))
	annual_leave_days = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	public_holiday_days = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	replacement_public_holiday = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	medical_certificate = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	siri_no_diagnosis = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	emergency_leaves = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	emergency_leaves_reasons = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	unpaid_leaves = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	unpaid_leaves_reasons = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))


class StaffRecords_Form(BSModalForm):

	staff = forms.CharField(required=False, label="", widget=forms.HiddenInput(attrs={'class': "form-control"}))
	date = form.YearField(required=False, label="", initial=datetime.datetime.now().year, widget=YearPickerInput(format="%Y", attrs={'class': "form-control"}))
	annual_leave_days = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	public_holiday_days = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	replacement_public_holiday = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	medical_certificate = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	siri_no_diagnosis = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	emergency_leaves = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	emergency_leaves_reasons = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	unpaid_leaves = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	unpaid_leaves_reasons = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))



