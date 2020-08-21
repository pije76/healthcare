from django import forms
from django.utils.translation import ugettext_lazy as _

from ..models import *
from ..forms import *
from ..lookups import *
#from .custom_layout import *
from accounts.models import *

from bootstrap_modal_forms.forms import *
from crispy_forms.layout import Layout, Fieldset, Div, Submit, Reset, HTML, Field, Hidden


class InvestigationReportForm(BSModalModelForm):
	class Meta:
		model = InvestigationReport
		fields = '__all__'
		widgets = {
			'patient': forms.HiddenInput(),
		}

	date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d/%m/%Y", attrs={'class': "form-control"}))
	file_upload = forms.ImageField(required=False, label='', widget=forms.FileInput(attrs={'class': "form-control"}))

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.fields['file_upload'].label = ''


InvestigationReport_FormSet_Factory = formset_factory(
	InvestigationReportForm,
	#   formset = MedicationAdministrationRecord_BaseFormSetFactory,
	extra=0,
	max_num=0,
	#   can_delete=True,
)
