from django import forms
from django.utils.translation import ugettext_lazy as _

from ..models import *
from ..forms import *
from ..lookups import *
#from .custom_layout import *
from accounts.models import *

from bootstrap_modal_forms.forms import *
from crispy_forms.layout import Layout, Fieldset, Div, Submit, Reset, HTML, Field, Hidden


class DressingForm(BSModalModelForm):
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
#   wound_condition = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=Dressing.WOUND_CONDITION_CHOICES)
	photos = forms.ImageField(required=False, label='', widget=forms.FileInput(attrs={'class': "form-control"}))
	note = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4, 'cols': 15}))
	done_by = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.fields['photos'].label = ''


Dressing_FormSet_Factory = formset_factory(
	DressingForm,
	#   formset = MedicationAdministrationRecord_BaseFormSetFactory,
	extra=0,
	max_num=0,
	#   can_delete=True,
)
