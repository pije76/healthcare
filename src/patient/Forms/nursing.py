from django import forms
from django.utils.translation import ugettext_lazy as _

from ..models import *
from ..forms import *
from ..lookups import *
#from .custom_layout import *
from accounts.models import *

from bootstrap_modal_forms.forms import *
from django_summernote.widgets import SummernoteWidget
from django_summernote.fields import SummernoteTextFormField, SummernoteTextField


class Nursing_ModelForm(BSModalModelForm):
	class Meta:
		model = Nursing
#       fields = '__all__'
		fields = [
			'patient',
			'date_time',
			'report',
		]
		widgets = {
			'patient': forms.HiddenInput(),
		}

	date_time = forms.DateTimeField(required=False, label="", initial=timezone.now, input_formats=settings.DATETIME_INPUT_FORMATS, widget=DateTimePickerInput(format="%d-%m-%Y %H:%M", attrs={'class': "form-control"}))
	report = forms.CharField(required=False, label="", widget=SummernoteWidget(attrs={'class': "form-control", 'summernote': {'width': '100%', 'height': '400px'}}))


class Nursing_Form(BSModalForm):

	patient = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	date_time = forms.DateTimeField(required=False, label="", initial=timezone.now, input_formats=settings.DATETIME_INPUT_FORMATS, widget=DateTimePickerInput(format="%d-%m-%Y %H:%M", attrs={'class': "form-control"}))
	report = forms.CharField(required=False, label="", widget=SummernoteWidget(attrs={'class': "form-control", 'summernote': {'width': '100%', 'height': '400px'}}))

	def clean_report(self):
		return self.cleaned_data['report'].capitalize()


Nursing_FormSet = formset_factory(
	Nursing_Form,
#   formset = MedicationAdministrationRecord_BaseFormSetFactory,
	extra=0,
#    max_num=0,
#   can_delete=True,
)
