from django import forms
from django.utils.translation import ugettext_lazy as _

from ..models import *
from ..forms import *
from ..lookups import *
from ..choices import *
#from .custom_layout import *
from accounts.models import *

from bootstrap_modal_forms.forms import *

class Urinary_ModelForm(BSModalModelForm):
	class Meta:
		model = Urinary
		fields = [
			'patient',
			'urinary_catheter_date',
			'urinary_catheter_size',
			'urinary_catheter_type',
			'urinary_catheter_due_date',
			'urinary_catheter_inserted_by',
			'urinary_catheter_remove_date',
			'urinary_catheter_remove_by',
		]
		widgets = {
			'patient': forms.HiddenInput(),
		}

	urinary_catheter_date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d-%m-%Y", attrs={'class': "form-control"}))
	urinary_catheter_size = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
#	urinary_catheter_type = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4}))
	urinary_catheter_type = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=URINARY_CATHETER_TYPE_CHOICES)
	urinary_catheter_due_date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d-%m-%Y", attrs={'class': "form-control"}))
	urinary_catheter_inserted_by = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control", 'readonly': 'readonly'}))
	urinary_catheter_remove_date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d-%m-%Y", attrs={'class': "form-control"}))
	urinary_catheter_remove_by = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control", 'readonly': 'readonly'}))

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()


class Urinary_Form(BSModalForm):

	patient = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	urinary_catheter_date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d-%m-%Y", attrs={'class': "form-control"}))
	urinary_catheter_size = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
#	urinary_catheter_type = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4}))
	urinary_catheter_type = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=URINARY_CATHETER_TYPE_CHOICES)
	urinary_catheter_due_date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d-%m-%Y", attrs={'class': "form-control"}))
	urinary_catheter_inserted_by = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control", 'readonly': 'readonly'}))
	urinary_catheter_remove_date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d-%m-%Y", attrs={'class': "form-control"}))
	urinary_catheter_remove_by = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control", 'readonly': 'readonly'}))

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()


Urinary_FormSet = formset_factory(
	Urinary_Form,
	#   formset = MedicationAdministrationRecord_BaseFormSetFactory,
	extra=0,
#    max_num=0,
	#   can_delete=True,
)
