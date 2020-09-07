from django import forms
from django.utils.translation import ugettext_lazy as _

from ..models import *
from ..forms import *
from ..lookups import *
#from .custom_layout import *
from accounts.models import *

from bootstrap_modal_forms.forms import *


class MedicationAdministrationRecord_ModelForm(BSModalModelForm):
	class Meta:
		model = MedicationAdministrationRecord
		fields = '__all__'
		widgets = {
			'patient': forms.Select(),
		}

#   patient = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}))
#   patient = forms.HiddenInput()
	allergy = forms.CharField(required=False, label=_("Allergy"), widget=forms.TextInput(attrs={'class': "form-control"}))
	stat = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=MedicationAdministrationRecord.STAT_CHOICES)
	medicationstat_date_time = forms.DateTimeField(required=False, label="", initial=timezone.now, input_formats=settings.DATETIME_INPUT_FORMATS, widget=DateTimePickerInput(format="%d/%m/%Y %H:%M", attrs={'class': "form-control"}))
	given_by = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))


# for modelform_factory
MedicationAdministrationRecord_ModelForm1 = modelform_factory(
	MedicationAdministrationRecord,
	fields=(
		'patient',
		'allergy',
		'medication',
#		'medication_name',
#		'medication_dosage',
#		'medication_tab_cap_mls',
#		'medication_frequency',
#		'medication_route',
		'medication_date',
		'medication_time',
		'status_nurse',
		'stat',
		'medicationstat_date_time',
		'given_by'
	),
)

# for modelform_factory
MedicationAdministrationRecord_ModelForm2 = modelform_factory(
	MedicationAdministrationRecord,
	form=MedicationAdministrationRecord_ModelForm,
	widgets={
		'patient': forms.Select(),
		'patient': forms.HiddenInput(),
		'medication': forms.TextInput(attrs={'class': "form-control"}),
#		'medication_name': forms.TextInput(attrs={'class': "form-control"}),
#		'medication_dosage': forms.NumberInput(attrs={'class': "form-control"}),
#		'medication_tab_cap_mls': forms.Select(attrs={'class': "form-control"}, choices=MedicationAdministrationRecord.TAB_CHOICES),
#		'medication_frequency': forms.Select(attrs={'class': "form-control"}, choices=MedicationAdministrationRecord.MEDICATION_ADMINISTRATION_FREQUENCY_CHOICES),
#		'medication_route': forms.Select(attrs={'class': "form-control"}, choices=MedicationAdministrationRecord.ROUTE_CHOICES),
		'medication_date': DatePickerInput(attrs={'class': "form-control"}),
		'medication_time': TimePickerInput(attrs={'class': "form-control"}),
		'status_nurse': forms.Select(attrs={'class': "form-control"}, choices=MedicationAdministrationRecord.SIGNATURE_CHOICES),
		'stat': forms.Select(attrs={'class': "form-control"}, choices=MedicationAdministrationRecord.STAT_CHOICES),
		'medicationstat_date_time': DateTimePickerInput(attrs={'class': "form-control"}),
		'given_by': forms.TextInput(attrs={'class': "form-control"}),
	},
)

MedicationAdministrationRecord_ModelFormSetFactory = modelformset_factory(
	MedicationAdministrationRecord,
	form=MedicationAdministrationRecord_ModelForm,
	#   formset = MedicationAdministrationRecord_BaseFormSetFactory,
	#   exclude = ['patient'],
	extra=0
	#   max_num=1,
	#   can_delete=True,
)


class MedicationAdministrationRecord_BaseFormSetFactory(BaseModelFormSet):
	def __init__(self, *args, **kwargs):
		patient = kwargs.pop('patient', None)
		super().__init__(*args, **kwargs)
#        if patient:
#            for obj in self.forms:
#                if obj.instance.pk is None:
#                    obj.fields['patient'].initial = patient #or obj.initial['patient'] = patient

		for obj in self.forms:
			if obj.instance.pk is None:
				obj.instance.patient = patient


class MedicationAdministrationRecord_InlineForm(BSModalModelForm):
	class Meta:
		model = MedicationAdministrationRecord
		fields = '__all__'
#       exclude = ('patient', )
		widgets = {
#           'patient': forms.Select(),
		}

	patient = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
#   patient = forms.HiddenInput()
	allergy = forms.CharField(required=False, label=_("Allergy"), widget=forms.TextInput(attrs={'class': "form-control"}))
	medication = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
#	medication_name = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
#	medication_dosage = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
#	medication_tab_cap_mls = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=MedicationAdministrationRecord.TAB_CHOICES)
#	medication_frequency = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=MedicationAdministrationRecord.MEDICATION_ADMINISTRATION_FREQUENCY_CHOICES)
#	medication_route = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=MedicationAdministrationRecord.ROUTE_CHOICES)
	medication_date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d/%m/%Y", attrs={'class': "form-control"}))
	medication_time = forms.TimeField(required=False, label="", initial=get_time, input_formats=settings.TIME_INPUT_FORMATS, widget=TimePickerInput(format="%H:%M", attrs={'class': "form-control"}))
	status_nurse = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=MedicationAdministrationRecord.SIGNATURE_CHOICES)
	stat = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=MedicationAdministrationRecord.STAT_CHOICES)
	medicationstat_date_time = forms.DateTimeField(required=False, label="", initial=timezone.now, input_formats=settings.DATETIME_INPUT_FORMATS, widget=DateTimePickerInput(format="%d/%m/%Y %H:%M", attrs={'class': "form-control"}))
	given_by = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))


MedicationAdministrationRecord_InlineFormSetFactory = inlineformset_factory(
	UserProfile,
	MedicationAdministrationRecord,
#   form = MedicationAdministrationRecord_InlineForm,
	extra=0,
#   max_num=1,
#   can_delete=False,
	fields=(
		'patient',
		'allergy',
		'medication',
#		'medication_name',
#		'medication_dosage',
#		'medication_tab_cap_mls',
#		'medication_frequency',
#		'medication_route',
		'medication_date',
		'medication_time',
		'status_nurse',
		'stat',
		'medicationstat_date_time',
		'given_by'
	),
	#   labels = {
	#       'allergy': 'Allergy',
	#       'medication_name': '',
	#       'medication_dosage': '',
	#       'medication_tab_cap_mls': '',
	#       'medication_frequency': '',
	#       'medication_route': '',
	#       'medication_date': '',
	#       'medication_time': '',
	#       'status_nurse': '',
	#       'stat': '',
	#       'medicationstat_date_time': '',
	#       'given_by': '',
	#   },
	#   widgets={
	#       'patient': forms.Select(),
	#       'patient': forms.HiddenInput(),
	#       'medication_name': forms.TextInput(attrs={'class': "form-control"}),
	#       'medication_dosage': forms.NumberInput(attrs={'class': "form-control"}),
	#       'medication_tab_cap_mls': forms.Select(attrs={'class': "form-control"}, choices=MedicationAdministrationRecord.TAB_CHOICES),
	#       'medication_frequency': forms.Select(attrs={'class': "form-control"}, choices=MedicationAdministrationRecord.MEDICATION_ADMINISTRATION_FREQUENCY_CHOICES),
	#       'medication_route': forms.Select(attrs={'class': "form-control"}, choices=MedicationAdministrationRecord.ROUTE_CHOICES),
	#       'medication_date': DatePickerInput(attrs={'class': "form-control"}),
	#       'medication_time': TimePickerInput(attrs={'class': "form-control"}),
	#       'status_nurse': forms.Select(attrs={'class': "form-control"}, choices=MedicationAdministrationRecord.SIGNATURE_CHOICES),
	#       'stat': forms.Select(attrs={'class': "form-control"}, choices=MedicationAdministrationRecord.STAT_CHOICES),
	#       'medicationstat_date_time': DateTimePickerInput(attrs={'class': "form-control"}),
	#       'given_by': forms.TextInput(attrs={'class': "form-control"}),
	#   },
	#   help_texts = {
	#       'medication_name': _('Some useful help text.'),
	#   },
)


class MedicationAdministrationRecord_Form(BSModalForm):

	patient = forms.CharField(required=False, label="", widget=forms.HiddenInput(attrs={'class': "form-control"}))
#   patient = forms.HiddenInput()
	allergy = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	medication = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
#	medication_name = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
#	medication_dosage = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
#	medication_tab_cap_mls = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=MedicationAdministrationRecord.TAB_CHOICES)
#	medication_tab_cap_mls = forms.ChoiceField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
#	medication_frequency = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=MedicationAdministrationRecord.MEDICATION_ADMINISTRATION_FREQUENCY_CHOICES)
#	medication_route = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=MedicationAdministrationRecord.ROUTE_CHOICES)
	medication_date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d/%m/%Y", attrs={'class': "form-control"}))
	medication_time = forms.TimeField(required=False, label="", input_formats=settings.TIME_INPUT_FORMATS, widget=TimePickerInput(format="%H:%M", attrs={'class': "form-control"}))
	medication = forms.ModelChoiceField(queryset=Medication.objects.all(), required=False, label="", widget=forms.Select(attrs={'class': "form-control"}))
	status_nurse = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=MedicationAdministrationRecord.SIGNATURE_CHOICES)
	stat = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=MedicationAdministrationRecord.STAT_CHOICES)
	medicationstat_date_time = forms.DateTimeField(required=False, label="", initial=timezone.now, input_formats=settings.DATETIME_INPUT_FORMATS, widget=DateTimePickerInput(format="%d/%m/%Y %H:%M", attrs={'class': "form-control"}))
	given_by = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	done = forms.BooleanField(required=False, label='', widget=forms.TextInput())

MedicationAdministrationRecord_FormSet = formset_factory(
	MedicationAdministrationRecord_Form,
#   formset = MedicationAdministrationRecord_BaseFormSetFactory,
	extra=0,
#	max_num=0,
	#   can_delete=True,
)


class MedicationAdministrationRecord_ModelForm(BSModalModelForm):
	class Meta:
		model = MedicationAdministrationRecord
		fields = '__all__'
		widgets = {
#			'patient': forms.Select(),
		}

	patient = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	allergy = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	medication = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	medication_date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d/%m/%Y", attrs={'class': "form-control"}))
	medication_time = forms.TimeField(required=False, label="", input_formats=settings.TIME_INPUT_FORMATS, widget=TimePickerInput(format="%H:%M", attrs={'class': "form-control"}))
	medication = forms.ModelChoiceField(queryset=Medication.objects.all(), required=False, label="", widget=forms.Select(attrs={'class': "form-control"}))
	status_nurse = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=MedicationAdministrationRecord.SIGNATURE_CHOICES)
	stat = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=MedicationAdministrationRecord.STAT_CHOICES)
	medicationstat_date_time = forms.DateTimeField(required=False, label="", initial=timezone.now, input_formats=settings.DATETIME_INPUT_FORMATS, widget=DateTimePickerInput(format="%d/%m/%Y %H:%M", attrs={'class': "form-control"}))
	given_by = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	done = forms.BooleanField(required=False, label='', widget=forms.TextInput())


MedicationAdministrationRecord_ModelFormSet = modelformset_factory(
	MedicationAdministrationRecord,
	form=MedicationAdministrationRecord_ModelForm,
	extra=0,
)


class Allergy_ModelForm(forms.ModelForm):
	class Meta:
		model = Allergy
		fields = '__all__'
		widgets = {
			'patient': forms.HiddenInput(),
		}

#	patient = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
#   patient = forms.HiddenInput()
#	allergy = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	allergy_drug = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	allergy_food = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	allergy_others = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
#	allergy = forms.ModelChoiceField(queryset=Allergy.objects.all(), required=False, label="", widget=forms.Select(attrs={'class': "form-control"}))
##	extra_field = forms.CharField(required=True)

##	def __init__(self, data=None, *args, **kwargs):
###	def __init__(self, *args, get_patient=None, **kwargs):
##		if data is not None:
##			data = data.copy()
##			if data['allergy']:
##				obj = get_object_or_404(Allergy, batch_name=data['allergy'])
##				data['allergy'] = obj.id
###		super().__init__(*args, **kwargs)
#		super().__init__(data=data, *args, **kwargs)
#		patientid = UserProfile.objects.get(username=username).id
#		get_patient = get_patient.id
#		queryset = Allergy.objects.filter(question__prompt=kwargs['initial']['question'])
###		queryset = Allergy.objects.filter(patient=get_patient)
#		self.fields['allergy'].queryset = queryset
#		self.fields['allergy'].initial = queryset.first()
#		self.initial['allergy'] = allergies = Allergy.objects.filter(patient=patientid)
###		if get_patient is not None:
###			self.fields['allergy'].queryset = queryset
###		self.fields['allergy'].empty_label = None

