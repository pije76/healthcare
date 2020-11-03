from django import forms
from django.utils.translation import ugettext_lazy as _

from ..models import *
from ..forms import *
from ..lookups import *
from ..choices import *
#from .custom_layout import *
from accounts.models import *

from bootstrap_modal_forms.forms import *


class MedicationAdministrationRecordTemplate_ModelForm(BSModalModelForm):
	class Meta:
		model = MedicationAdministrationRecordTemplate
		fields = [
			'patient',
			'medication_date',
			'medication_time',
			'medication_drug_name',
			'medication_dosage',
			'medication_tablet_capsule',
			'medication_frequency',
		]
		widgets = {
			'id': forms.HiddenInput(),
			'patient': forms.HiddenInput(),
		}

#   patient = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
#   patient = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control", 'style': "display:none;"}))
#    medication_time = forms.TimeField(required=False, label="", initial=get_time, input_formats=settings.TIME_INPUT_FORMATS, widget=TimePickerInput(format="%H:%M", attrs={'class': "form-control"}))
	medication_date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d-%m-%Y", attrs={'class': "form-control"}))
	medication_time = forms.TimeField(required=False, label="", input_formats=settings.TIME_INPUT_FORMATS, widget=TimePickerInput(format="%H:%M", attrs={'class': "form-control"}))
#    medication_drug_name = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	medication_drug_name = forms.ModelChoiceField(queryset=Medicine.objects.all(), required=False, label="", widget=forms.Select(attrs={'class': "form-control"}))
	medication_dosage = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	medication_tablet_capsule = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	medication_frequency = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=MEDICATION_ADMINISTRATION_FREQUENCY_CHOICES)

#   def __init__(self, *args, **kwargs):
#       super().__init__(*args, **kwargs)
#       instance = getattr(self, 'instance', None)
#       if instance and instance.pk:
#           self.fields['medication_time'].disabled = True

##  def save(self, commit=True):
		# do something with self.cleaned_data['new_artist']
##      get_time1 = MedicationAdministrationRecordTemplate.objects.filter(medication_time='00:00')
##      if get_time1.exists():
##          pass
##      else:
			# Create and save new artist and save song to the
			# new artist.
##          pass
##      return super().save(commit=commit)


MedicationAdministrationRecordTemplate_FormSet = modelformset_factory(
#MedicationAdministrationRecordTemplate_FormSet = inlineformset_factory(
#   UserProfile,
	MedicationAdministrationRecordTemplate,
	form=MedicationAdministrationRecordTemplate_ModelForm,
#   MedicationAdministrationRecordTemplate_ModelForm,
#   formset = MedicationAdministrationRecordTemplateAdministrationRecord_BaseFormSetFactory,
#    fields=(
#        'patient',
#        'medication_date',
#        'medication_time',
#        'medication_drug_name',
#        'medication_dosage',
#        'medication_tablet_capsule',
#        'medication_frequency',
#    ),
	extra=0,
	max_num=0,
#   can_delete=True,
)
