from django import forms
from django.utils.translation import ugettext_lazy as _

from ..models import *
from ..forms import *
from ..lookups import *
from ..choices import *
#from .custom_layout import *
from accounts.models import *

from bootstrap_modal_forms.forms import *
from crispy_forms.layout import Field


default_desimal_mar = Decimal('0.0')


class CustomCheckbox(Field):
    template = 'patient/medication_administration/custom_checkbox.html'


class MedicationAdministrationRecord_Form(forms.Form):

    #    id = forms.CharField()
    #    patient = forms.ChoiceField()
    patient = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    medication_date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d-%m-%Y", attrs={'class': "form-control"}))
    medication_time = forms.TimeField(required=False, label="", input_formats=settings.TIME_INPUT_FORMATS, widget=TimePickerInput(format="%H:%M", attrs={'class': "form-control"}))
    medication_medicine = forms.ModelChoiceField(queryset=Medicine.objects.all(), required=False, label="", widget=forms.Select(attrs={'class': "form-control"}))
    medication_dosage = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
    medication_unit = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=UNIT_CHOICES)
    medication_tablet_capsule = forms.DecimalField(required=False, label="", initial=default_desimal_mar, min_value=0.0, widget=forms.NumberInput(attrs={'class': "form-control", 'step': 0.1}))
    medication_frequency = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=MEDICATION_ADMINISTRATION_FREQUENCY_CHOICES)

    medication_route = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=ROUTE_CHOICES)
    medication_status = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=SIGNATURE_CHOICES)
    medication_source = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=SOURCE_CHOICES)
    medication_done = forms.ChoiceField(required=False, label="", initial=False, widget=forms.CheckboxInput(attrs={'class': "form-control"}), choices=BOOLEAN_CHOICES)


MedicationAdministrationRecordTemplate_FormSet = formset_factory(
    form=MedicationAdministrationRecord_Form,
    extra=0,
    max_num=0,
)


class MedicationAdministrationRecord_ModelForm_Set(forms.ModelForm):
    # class MedicationAdministrationRecord_Model_Form(forms.ModelForm):
    class Meta:
        model = MedicationAdministrationRecord
#        fields = '__all__'
        fields = [
            'id',
            'patient',
            'allergy_drug',
            'allergy_food',
            'allergy_others',
            #           'medication_template',
            'medication_date',
            'medication_time',
            'medication_medicine',
            'medication_dosage',
            'medication_unit',
            'medication_tablet_capsule',
            'medication_frequency',
            'medication_route',
            'medication_status',
            'medication_source',
            'medication_done',
        ]
#        exclude = ('id',)
        widgets = {
            #            'id': forms.HiddenInput(),
            'patient': forms.HiddenInput(),
        }
        labels = {
            'medication_done': '',
        }


#   def __init__(self, user, *args, **kwargs):
#       super().__init__(*args, **kwargs)
#       self.fields['medication_date'].queryset = MedicationAdministrationRecord.objects.filter(patient=user)
#       self.request = request

#   patient = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
#   allergy = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    allergy_drug = forms.CharField(required=False, label=_("Medicine(s):"), widget=forms.TextInput(attrs={'class': "form-control"}))
    allergy_food = forms.CharField(required=False, label=_("Food:"), widget=forms.TextInput(attrs={'class': "form-control"}))
    allergy_others = forms.CharField(required=False, label=_("Others:"), widget=forms.TextInput(attrs={'class': "form-control"}))
#   medication = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
#   medication = forms.ModelChoiceField(queryset=MedicationAdministrationRecordTemplate.objects.all(), required=False, label="", widget=forms.Select(attrs={'class': "form-control"}))

#   medication_template = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    medication_date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d-%m-%Y", attrs={'class': "form-control"}))
    medication_time = forms.TimeField(required=False, label="", input_formats=settings.TIME_INPUT_FORMATS, widget=TimePickerInput(format="%H:%M", attrs={'class': "form-control"}))
#    medication_medicine = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    medication_medicine = forms.ModelChoiceField(queryset=Medicine.objects.all(), required=False, label="", widget=forms.Select(attrs={'class': "form-control"}))
    medication_dosage = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
    medication_unit = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=UNIT_CHOICES)
    medication_tablet_capsule = forms.DecimalField(required=False, label="", initial=default_desimal_mar, min_value=0.0, widget=forms.NumberInput(attrs={'class': "form-control", 'step': 0.1}))
    medication_frequency = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=MEDICATION_ADMINISTRATION_FREQUENCY_CHOICES)

    medication_route = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=ROUTE_CHOICES)
    medication_status = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=SIGNATURE_CHOICES)
    medication_source = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=SOURCE_CHOICES)

#   medication_done = forms.BooleanField(required=False, label='', widget=forms.TextInput())
#   medication_done = forms.BooleanField(required=False, label="")
#   medication_done = forms.ChoiceField(required=False, label="", initial=False, widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=BOOLEAN_CHOICES)

#    id = forms.CharField()
#    patient = forms.ChoiceField()
#    patient = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    medication_date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d-%m-%Y", attrs={'class': "form-control"}))
    medication_time = forms.TimeField(required=False, label="", input_formats=settings.TIME_INPUT_FORMATS, widget=TimePickerInput(format="%H:%M", attrs={'class': "form-control"}))
    medication_medicine = forms.ModelChoiceField(queryset=Medicine.objects.all(), required=False, label="", widget=forms.Select(attrs={'class': "form-control"}))
    medication_dosage = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
    medication_unit = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=UNIT_CHOICES)
    medication_tablet_capsule = forms.DecimalField(required=False, label="", initial=default_desimal_mar, min_value=0.0, widget=forms.NumberInput(attrs={'class': "form-control", 'step': 0.1}))
    medication_frequency = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=MEDICATION_ADMINISTRATION_FREQUENCY_CHOICES)

    medication_route = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=ROUTE_CHOICES)
    medication_status = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=SIGNATURE_CHOICES)
    medication_source = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=SOURCE_CHOICES)
    medication_done = forms.ChoiceField(required=False, label="", initial=False, widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=BOOLEAN_CHOICES)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
#       if 'instance' in kwargs:
#           medication_template = kwargs['instance']
#       self.fields['patient']  = forms.CharField(max_length=30)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            CustomCheckbox('medication_done'),
        )


MedicationAdministrationRecord_ModelFormSet = modelformset_factory(
    MedicationAdministrationRecord,
    #    form=MedicationAdministrationRecord_Model_Form,
    form=MedicationAdministrationRecord_ModelForm_Set,
    #   fields=(
    #       'id',
    #       'patient',
    #       'allergy',
    #       'medication_template',
    #       'medication_date',
    #       'medication_time',
    #       'medication_medicine',
    #       'medication_dosage',
    #       'medication_tablet_capsule',
    #       'medication_frequency',
    #       'medication_route',
    #       'medication_status',
    #       'medication_source',
    #       'medication_done',
    #   ),
    extra=0,
    #   max_num=0,
)


class MedicationAdministrationRecordTemplate_ModelForm_Set(forms.ModelForm):
    class Meta:
        model = MedicationAdministrationRecordTemplate
        fields = [
#            'id',
            'patient',
            'medication_date',
            'medication_time',
            'medication_medicine',
            'medication_dosage',
            'medication_unit',
            'medication_tablet_capsule',
            'medication_frequency',
        ]
        widgets = {
            'patient': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            CustomCheckbox('medication_done'),
        )

    medication_date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d-%m-%Y", attrs={'class': "form-control"}))
    medication_time = forms.TimeField(required=False, label="", input_formats=settings.TIME_INPUT_FORMATS, widget=TimePickerInput(format="%H:%M", attrs={'class': "form-control"}))
    medication_medicine = forms.ModelChoiceField(queryset=Medicine.objects.all(), required=False, label="", widget=forms.Select(attrs={'class': "form-control"}))
    medication_dosage = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
    medication_unit = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=UNIT_CHOICES)
    medication_tablet_capsule = forms.DecimalField(required=False, label="", initial=default_desimal_mar, min_value=0.0, widget=forms.NumberInput(attrs={'class': "form-control", 'step': 0.1}))
    medication_frequency = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=MEDICATION_ADMINISTRATION_FREQUENCY_CHOICES)

    medication_route = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=ROUTE_CHOICES)
    medication_status = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=SIGNATURE_CHOICES)
    medication_source = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=SOURCE_CHOICES)
    medication_done = forms.BooleanField(required=False, label="", initial=False, widget=forms.CheckboxInput(attrs={'class': "form-control", 'style': 'width:15px;height:15px;margin-left:10px;margin-top:10px;'}))
    given_by = forms.CharField(required=False, label="", widget=forms.HiddenInput(attrs={'class': "form-control", 'readonly': 'readonly'}))


MedicationAdministrationRecordTemplate_ModelFormSet = modelformset_factory(
    MedicationAdministrationRecordTemplate,
    form=MedicationAdministrationRecordTemplate_ModelForm_Set,
    extra=0,
    max_num=0,
)


# class MedicationAdministrationRecordTemplateStat_Form_Set(forms.Form):
class MedicationAdministrationRecordTemplateStat_Form_Set(BSModalForm):

    #    id = forms.CharField()
    #    patient = forms.ChoiceField()
#    patient = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    patient = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control", 'style': "display:none;"}))
    medication_date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d-%m-%Y", attrs={'class': "form-control"}))
    medication_time = forms.TimeField(required=False, label="", input_formats=settings.TIME_INPUT_FORMATS, widget=TimePickerInput(format="%H:%M", attrs={'class': "form-control"}))
    medication_medicine = forms.ModelChoiceField(queryset=Medicine.objects.all(), required=False, label="", widget=forms.Select(attrs={'class': "form-control"}))
    medication_done = forms.BooleanField(required=False, label="", initial=False, widget=forms.CheckboxInput(attrs={'class': "form-control", 'style': 'width:15px;height:15px;margin-left:10px;margin-top:10px;'}))
#    medication_done = forms.TypedChoiceField(required=False, label="", initial=False, coerce=lambda x: x == 'True', choices=((False, 'No'), (True, 'Yes')), widget=forms.CheckboxInput(attrs={'class': "form-control", 'style': 'width:15px;height:15px;margin-left:10px;margin-top:10px;'}))
    medication_stat_date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d-%m-%Y", attrs={'class': "form-control"}))
    medication_stat_time = forms.TimeField(required=False, label="", input_formats=settings.TIME_INPUT_FORMATS, widget=TimePickerInput(format="%H:%M", attrs={'class': "form-control"}))
    given_by = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control", 'readonly': 'readonly'}))


MedicationAdministrationRecordTemplateStat_FormSet = formset_factory(
    MedicationAdministrationRecordTemplateStat_Form_Set,
    extra=0,
    # max_num=3,
)
