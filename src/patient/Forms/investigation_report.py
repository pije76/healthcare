from django import forms
from django.utils.translation import ugettext_lazy as _

from ..models import *
from ..forms import *
from ..lookups import *
#from .custom_layout import *
from accounts.models import *

from bootstrap_modal_forms.forms import *
from crispy_forms.layout import Layout, Fieldset, Div, Submit, Reset, HTML, Field, Hidden


class InvestigationReport_ModelForm(BSModalModelForm):
	class Meta:
		model = InvestigationReport
		fields = [
			'patient',
			'date',
			'file_upload',
		]
		widgets = {
			'patient': forms.HiddenInput(),
		}

	date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d-%m-%Y", attrs={'class': "form-control"}))
	file_upload = forms.ImageField(required=False, label='', widget=forms.FileInput(attrs={'class': "form-control"}))

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.fields['file_upload'].label = ''


class InvestigationReport_Form(BSModalForm):

	patient = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d-%m-%Y", attrs={'class': "form-control"}))
	file_upload = forms.ImageField(required=False, label='', widget=forms.FileInput(attrs={'class': "form-control"}))

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.fields['file_upload'].label = ''

