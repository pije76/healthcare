from django import forms
from django.utils.translation import ugettext_lazy as _

from ..models import *
from ..forms import *
from ..lookups import *
#from .custom_layout import *
from accounts.models import *

from bootstrap_modal_forms.forms import *

class CannulaForm(BSModalModelForm):

	class Meta:
		model = Cannula
		fields = '__all__'
		widgets = {
			'patient': forms.HiddenInput(),
		}

	cannula_date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d/%m/%Y", attrs={'class': "form-control"}))
	cannula_size = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	cannula_location = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4}))
	cannula_due_date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d/%m/%Y", attrs={'class': "form-control"}))

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
