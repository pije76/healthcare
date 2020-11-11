from django import forms
from django.utils.translation import ugettext_lazy as _

from ..models import *
from ..forms import *
from ..lookups import *
from ..choices import *
#from .custom_layout import *
from accounts.models import *

from bootstrap_modal_forms.forms import *
from crispy_forms.layout import *


class DischargeCheckList_ModelForm(forms.ModelForm):
	class Meta:
		model = DischargeCheckList
		fields = '__all__'
		widgets = {
			'id': forms.HiddenInput(),
			'patient': forms.HiddenInput(),
		}

#	def __init__(self, *args, **kwargs):
#	def __init__(self):
#		super().__init__(*args, **kwargs)
#		super().__init__()

	id = forms.CharField(required=False, label="", widget=forms.HiddenInput(attrs={'class': "form-control"}))
#	patient = forms.CharField(required=False, label="", widget=forms.HiddenInput(attrs={'class': "form-control"}))
#	date_time = forms.SplitDateTimeField(required=False, label="", initial=timezone.now, input_date_formats=settings.DATE_INPUT_FORMATS, input_time_formats=settings.TIME_INPUT_FORMATS, widget=forms.SplitDateTimeWidget(date_format="%d-%m-%Y", time_format="%H:%M", date_attrs={'class': 'form-control datepickerinput'}, time_attrs={'class': 'form-control timepickerinput'}, attrs={'class': "form-control"}))
	date_time = forms.DateTimeField(required=False, label="", initial=timezone.now, input_formats=settings.DATETIME_INPUT_FORMATS, widget=DateTimePickerInput(format="%d-%m-%Y %H:%M", attrs={'class': "form-control"}))
	discharge_status = forms.MultipleChoiceField(required=False, label="", widget=forms.CheckboxSelectMultiple(attrs={'class': "form-control"}), choices=DISCHARGE_STATUS)
	nasogastric_tube_date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d-%m-%Y", attrs={'class': "form-control"}))
	nasogastric_tube = forms.MultipleChoiceField(required=False, label="", widget=forms.CheckboxSelectMultiple(attrs={'class': "form-control"}), choices=DISCHARGE_CHECKLIST)
#	nasogastric_tube = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=DISCHARGE_CHECKLIST)
	urinary_catheter_date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d-%m-%Y", attrs={'class': "form-control"}))
	urinary_catheter = forms.MultipleChoiceField(required=False, label="", widget=forms.CheckboxSelectMultiple(attrs={'class': "form-control"}), choices=DISCHARGE_CHECKLIST)
	surgical_dressing_intact = forms.MultipleChoiceField(required=False, label="", widget=forms.CheckboxSelectMultiple(attrs={'class': "form-control"}), choices=DISCHARGE_CHECKLIST)
	spectacle_walking_aid_denture = forms.MultipleChoiceField(required=False, label="", widget=forms.CheckboxSelectMultiple(attrs={'class': "form-control"}), choices=DISCHARGE_CHECKLIST)
	appointment_card_returned = forms.MultipleChoiceField(required=False, label="", widget=forms.CheckboxSelectMultiple(attrs={'class': "form-control"}), choices=DISCHARGE_CHECKLIST)
	own_medication_return = forms.MultipleChoiceField(required=False, label="", widget=forms.CheckboxSelectMultiple(attrs={'class': "form-control"}), choices=DISCHARGE_CHECKLIST)
	medication_reconcilation = forms.MultipleChoiceField(required=False, label="", widget=forms.CheckboxSelectMultiple(attrs={'class': "form-control", 'style': "display: inline-flex;"}), choices=DISCHARGE_CHECKLIST)
	medication_reconcilation_patient = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	given_by = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control", 'readonly': 'readonly'}))


DischargeCheckList_ModelFormSet = modelformset_factory(
#DischargeCheckList_ModelFormSet = inlineformset_factory(
#	UserProfile,
	DischargeCheckList,
	form=DischargeCheckList_ModelForm,
#	fields=(
#		'date_time',
#		'discharge_status',
#		'nasogastric_tube_date',
#		'nasogastric_tube',
#		'urinary_catheter_date',
#		'urinary_catheter',
#		'surgical_dressing_intact',
#		'spectacle_walking_aid_denture',
#		'appointment_card_returned',
#		'own_medication_return',
#		'medication_reconcilation',
#		'medication_reconcilation_patient',
#		'given_by',
#	),
	extra=1,
	max_num=0,
#   can_delete=True,
)


class DischargeCheckList_Form_Set(forms.Form):
#	def __init__(self, *args, **kwargs):
#		request = kwargs.pop('request')
#		self.user = request.user
#		super().__init__(*args, **kwargs)
#		self.helper = FormHelper()
#		self.helper.layout = Layout(
#			Div(InlineRadios('')),
#		)

#	patient = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
#	patient = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(attrs={'class': "form-control"}))
#	patient = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}))
#	patient = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control", 'style': "display:none;"}))
	patient = forms.CharField(required=False, label="", widget=forms.HiddenInput(attrs={'class': "form-control"}))
	date_time = forms.SplitDateTimeField(required=False, label="", initial=timezone.now, input_date_formats=settings.DATE_INPUT_FORMATS, input_time_formats=settings.TIME_INPUT_FORMATS, widget=forms.SplitDateTimeWidget(date_format="%d-%m-%Y", time_format="%H:%M", date_attrs={'class': 'form-control datepickerinput'}, time_attrs={'class': 'form-control timepickerinput'}, attrs={'class': "form-control"}))
	discharge_status = forms.MultipleChoiceField(required=False, label="", widget=forms.CheckboxSelectMultiple(attrs={'class': "form-control"}), choices=DISCHARGE_STATUS)
	nasogastric_tube_date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d-%m-%Y", attrs={'class': "form-control"}))
	nasogastric_tube = forms.MultipleChoiceField(required=False, label="", widget=forms.CheckboxSelectMultiple(attrs={'class': "form-control"}), choices=DISCHARGE_CHECKLIST)
#	nasogastric_tube = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=DISCHARGE_CHECKLIST)
	urinary_catheter_date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d-%m-%Y", attrs={'class': "form-control"}))
	urinary_catheter = forms.MultipleChoiceField(required=False, label="", widget=forms.CheckboxSelectMultiple(attrs={'class': "form-control"}), choices=DISCHARGE_CHECKLIST)
	surgical_dressing_intact = forms.MultipleChoiceField(required=False, label="", widget=forms.CheckboxSelectMultiple(attrs={'class': "form-control"}), choices=DISCHARGE_CHECKLIST)
	spectacle_walking_aid_denture = forms.MultipleChoiceField(required=False, label="", widget=forms.CheckboxSelectMultiple(attrs={'class': "form-control"}), choices=DISCHARGE_CHECKLIST)
	appointment_card_returned = forms.MultipleChoiceField(required=False, label="", widget=forms.CheckboxSelectMultiple(attrs={'class': "form-control"}), choices=DISCHARGE_CHECKLIST)
	own_medication_return = forms.MultipleChoiceField(required=False, label="", widget=forms.CheckboxSelectMultiple(attrs={'class': "form-control"}), choices=DISCHARGE_CHECKLIST)
	medication_reconcilation = forms.MultipleChoiceField(required=False, label="", widget=forms.CheckboxSelectMultiple(attrs={'class': "form-control", 'style': "display: inline-flex;"}), choices=DISCHARGE_CHECKLIST)
	medication_reconcilation_patient = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	given_by = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control", 'readonly': 'readonly'}))


DischargeCheckList_FormSet = formset_factory(
	DischargeCheckList_Form_Set,
#   formset = MedicationAdministrationRecord_BaseFormSetFactory,
	extra=0,
	max_num=10,
#   can_delete=True,
)

class DischargeCheckList_Form(BSModalForm):

	patient = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
#	date_time = forms.DateTimeField(required=False, label="", initial=timezone.now, input_formats=settings.DATETIME_INPUT_FORMATS, widget=DateTimePickerInput(format="%d-%m-%Y %H:%M", attrs={'class': "form-control"}))
	date_time = forms.SplitDateTimeField(required=False, label="", initial=timezone.now, input_date_formats=settings.DATE_INPUT_FORMATS, input_time_formats=settings.TIME_INPUT_FORMATS, widget=forms.SplitDateTimeWidget(date_format="%d-%m-%Y", time_format="%H:%M", date_attrs={'class': 'form-control datepickerinput'}, time_attrs={'class': 'form-control timepickerinput'}, attrs={'class': "form-control"}))
	discharge_status = forms.MultipleChoiceField(required=False, label="", widget=forms.CheckboxSelectMultiple(attrs={'class': "form-control"}), choices=DISCHARGE_STATUS)
	nasogastric_tube_date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d-%m-%Y", attrs={'class': "form-control"}))
	nasogastric_tube = forms.MultipleChoiceField(required=False, label="", widget=forms.CheckboxSelectMultiple(attrs={'class': "form-control"}), choices=DISCHARGE_CHECKLIST)
#	nasogastric_tube = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=DISCHARGE_CHECKLIST)
	urinary_catheter_date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d-%m-%Y", attrs={'class': "form-control"}))
	urinary_catheter = forms.MultipleChoiceField(required=False, label="", widget=forms.CheckboxSelectMultiple(attrs={'class': "form-control"}), choices=DISCHARGE_CHECKLIST)
	surgical_dressing_intact = forms.MultipleChoiceField(required=False, label="", widget=forms.CheckboxSelectMultiple(attrs={'class': "form-control"}), choices=DISCHARGE_CHECKLIST)
	spectacle_walking_aid_denture = forms.MultipleChoiceField(required=False, label="", widget=forms.CheckboxSelectMultiple(attrs={'class': "form-control"}), choices=DISCHARGE_CHECKLIST)
	appointment_card_returned = forms.MultipleChoiceField(required=False, label="", widget=forms.CheckboxSelectMultiple(attrs={'class': "form-control"}), choices=DISCHARGE_CHECKLIST)
	own_medication_return = forms.MultipleChoiceField(required=False, label="", widget=forms.CheckboxSelectMultiple(attrs={'class': "form-control"}), choices=DISCHARGE_CHECKLIST)
	medication_reconcilation = forms.MultipleChoiceField(required=False, label="", widget=forms.CheckboxSelectMultiple(attrs={'class': "form-control", 'style': "display: inline-flex;"}), choices=DISCHARGE_CHECKLIST)
	given_by = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control", 'readonly': 'readonly'}))

#	def __init__(self, *args, **kwargs):
#		super().__init__(*args, **kwargs)
#		self.helper = FormHelper()
#		self.helper.form_class = 'form-inline'
##		self.helper.form_class = 'form-horizontal'
#		self.helper.layout = Layout(
#			InlineCheckboxes('discharge_status'),
#			Div(InlineRadios('discharge_status')),
#		)
