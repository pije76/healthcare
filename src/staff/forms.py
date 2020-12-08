from django import forms
from django.conf import settings
from django.core.validators import RegexValidator
from django.forms import ModelForm, RadioSelect, formset_factory, modelform_factory, modelformset_factory, inlineformset_factory, BaseModelFormSet, BaseInlineFormSet
from django.utils import timezone
from django.utils.functional import lazy
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _

from crispy_forms.bootstrap import *
from crispy_forms.helper import *
from crispy_forms.layout import *


from mptt.forms import TreeNodeChoiceField
from bootstrap_datepicker_plus import *
from selectable.forms import *
from durationwidget.widgets import TimeDurationWidget
#from bootstrap4_datetime.widgets import DateTimePicker
#from ajax_select.fields import AutoCompleteSelectField, AutoCompleteSelectMultipleField
#from django_select2 import forms as s2forms
#from django_select2.forms import *
#from easy_select2 import select2_modelform, select2_modelform_meta
#from easy_select2.utils import apply_select2
#from jsignature.forms import JSignatureField
from djangoyearlessdate import forms as form
from bootstrap_modal_forms.forms import *
#from dal import autocomplete
from bootstrap_datepicker_plus import YearPickerInput


from .models import *
from patient.lookups import *
#from .custom_layout import *
from accounts.models import *


import datetime
#from datetime import *

#now = date.today
#now = datetime.now()


def get_datetime():
    return timezone.now()
#	return datetime.date.strftime(datetime.today().date(), format="%d-%m-%Y %H:%M")
#	return datetime.now().strftime("%d-%m-%Y %H:%M")
#	return datetime.date.today().strftime('%d-%m-%Y %H:%M"')


def get_today():
    #	return date.strftime(datetime.now().date(), format="%d-%m-%Y")
    return datetime.date.today().strftime('%d-%m-%Y')
#	return datetime.now().strftime('%d-%m-%Y')
#	return date.today
#	return datetime.now().date()


def get_time():
    #	return datetime.now().time()
    return datetime.datetime.now().strftime("%H:%M")


messageserror = _("*IC Number format needs to be yymmdd-xx-zzzz.")
#ic_number_validator = RegexValidator("\d{6}\-\d{2}\-\d{4}", "IC Number format needs to be yymmdd-xx-zzzz.")
ic_number_validator = RegexValidator(
    regex='\d{6}\-\d{2}\-\d{4}', message=messageserror, code="invalid")
#ic_number_validator = RegexValidator(regex='^.{6}$-^.{2}$-^.{4}$', message=messageserror, code="invalid")
alphanumeric = RegexValidator(
    r'^[a-zA-Z]*$', 'Only alphanumeric characters are allowed.')

#now = date.today


#mark_safe_lazy = lazy(mark_safe, six.text_type)


class SlimRadioSelect(RadioSelect):
    input_type = 'radio'
    template_name = 'django/forms/widgets/checkbox_select.html'
    option_template_name = 'django/forms/widgets/checkbox_option.html'


class PlaceholderInput(forms.widgets.Input):
    template_name = 'patient/placeholder.html'
    input_type = 'text'

    def get_context(self, name, value, attrs):
        context = super(PlaceholderInput, self).get_context(name, value, attrs)
        context['widget']['attrs']['maxlength'] = 50
        context['widget']['attrs']['placeholder'] = name.title()
        return context


class HorizontalRadioSelect(RadioSelect):
    template_name = 'patient/horizontal_radios.html'
    option_template_name = 'patient/horizontal_option.html'

#######################

class OvertimeClaim_Form(BSModalForm):

    staff = forms.CharField(required=False, label="", widget=forms.TextInput(
        attrs={'class': "form-control"}))
    date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS,
                           widget=DatePickerInput(format="%d-%m-%Y", attrs={'class': "form-control"}))
#	duration_time_from = forms.DurationField(required=False, label="", initial="00:05:00", widget=TimeDurationWidget(show_days=False, show_hours=True, show_minutes=True, show_seconds=False, attrs={'class': "form-control"}))
    duration_time_from = forms.TimeField(required=False, label="", initial="00:00", input_formats=settings.TIME_INPUT_FORMATS,
                                         widget=TimePickerInput(format="%H:%M", attrs={'class': "form-control"}))
#	duration_time_to = forms.DurationField(required=False, label="", initial="00:05:00", widget=TimeDurationWidget(show_days=False, show_hours=True, show_minutes=True, show_seconds=False, attrs={'class': "form-control"}))
    duration_time_to = forms.TimeField(required=False, label="", initial=get_time, input_formats=settings.TIME_INPUT_FORMATS,
                                       widget=TimePickerInput(format="%H:%M", attrs={'class': "form-control"}))
    hours = forms.TimeField(required=False, label="", initial=get_time, input_formats=settings.TIME_INPUT_FORMATS,
                            widget=TimePickerInput(format="%H:%M", attrs={'class': "form-control"}))
    total_hours = forms.CharField(required=False, label="", widget=forms.HiddenInput(
        attrs={'class': "form-control"}))
    checked_sign_by = forms.CharField(required=False, label="", widget=forms.TextInput(
        attrs={'class': "form-control", 'readonly': 'readonly'}))
#	checked_sign_by = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}))
#	checked_sign_by = forms.CharField(required=False, label="", widget=AutoCompleteWidget(StaffnameLookup, attrs={'class': "form-control", 'placeholder': _("type min. 3 characters & select")}))
    verify_by = forms.CharField(required=False, label="", widget=AutoCompleteWidget(
        StaffnameLookup, attrs={'class': "form-control", 'placeholder': _("type min. 3 characters & select")}))


class OvertimeClaim_ModelForm(BSModalModelForm):
    class Meta:
        model = OvertimeClaim
        fields = [
            'staff',
            'date',
            'duration_time_from',
            'duration_time_to',
            'total_hours',
            'checked_sign_by',
            'verify_by',
        ]
        widgets = {
            'staff': forms.HiddenInput(),
            'total_hours': forms.HiddenInput(),
            #			'checked_sign_by': forms.TextInput(attrs={'class': "form-control"}),
            #			'checked_sign_by': forms.HiddenInput(),
            'checked_sign_by': forms.Select(),
            'verify_by': forms.Select(),
            #			'verify_by': forms.HiddenInput(),
            # 'verify_by': forms.TextInput(attrs={'class': "form-control"}),
        }

#	def __init__(self, *args, **kwargs):
#		super().__init__(*args, **kwargs)
#		self.helper = FormHelper()
#		self.fields['checked_sign_by'].label = ''

    date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS,
                           widget=DatePickerInput(format="%d-%m-%Y", attrs={'class': "form-control"}))
#   date = forms.DateTimeField(required=False, label="", widget=DatePickerInput(attrs={'class': "form-control"}))
#   date = forms.DateTimeField(required=False, label="", initial=timezone.now, input_formats=settings.DATETIME_INPUT_FORMATS, widget=DatePickerInput(format="%d-%m-%Y", attrs={'class': "form-control"}))
#    duration_time = forms.DurationField(required=True, label="", initial="01:00:00", widget=forms.TextInput(attrs={'class': "form-control"}))
#	duration_time_from = forms.DurationField(required=False, label="", initial="00:05:00", widget=TimeDurationWidget(show_days=False, show_hours=True, show_minutes=True, show_seconds=False, attrs={'class': "form-control"}))
    duration_time_from = forms.TimeField(required=False, label="", initial=get_time, input_formats=settings.TIME_INPUT_FORMATS,
                                         widget=TimePickerInput(format="%H:%M", attrs={'class': "form-control"}))
#	duration_time_to = forms.DurationField(required=False, label="", initial="00:05:00", widget=TimeDurationWidget(show_days=False, show_hours=True, show_minutes=True, show_seconds=False, attrs={'class': "form-control"}))
    duration_time_to = forms.TimeField(required=False, label="", initial=get_time, input_formats=settings.TIME_INPUT_FORMATS,
                                       widget=TimePickerInput(format="%H:%M", attrs={'class': "form-control"}))
    hours = forms.TimeField(required=False, label="", initial=get_time, input_formats=settings.TIME_INPUT_FORMATS,
                            widget=TimePickerInput(format="%H:%M", attrs={'class': "form-control"}))
#   hours = forms.DateTimeField(required=False, label="", initial=get_time, input_formats=settings.TIME_INPUT_FORMATS, widget=DatePickerInput(format="%H:%M", attrs={'class': "form-control"}))
#	total_hours = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control", 'style': "display:none;"}))
#	checked_sign_by = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control", 'readonly': 'readonly'}))
#	checked_sign_by = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
#	checked_sign_by = forms.CharField(required=False, label="", widget=AutoCompleteWidget(StaffnameLookup, attrs={'class': "form-control", 'placeholder': _("type min. 3 characters & select")}))
#	verify_by = forms.CharField(required=False, label="", initial="None", widget=forms.TextInput(attrs={'class': "form-control"}))
#	verify_by = forms.CharField(required=False, label="", widget=AutoCompleteWidget(StaffnameLookup, attrs={'class': "form-control", 'placeholder': _("type min. 3 characters & select")}))
#	verify_by = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control",}))


class StaffRecord_ModelForm(BSModalModelForm):
    class Meta:
        model = StaffRecords
        fields = [
            'staff',
            'date',
            'annual_leave_days',
            'public_holiday_days',
            'replacement_public_holiday',
            'medical_certificate',
            'siri_no_diagnosis',
            'emergency_leaves',
            'emergency_leaves_reasons',
            'unpaid_leaves',
            'unpaid_leaves_reasons',
        ]
        widgets = {
            'staff': forms.HiddenInput(),
            'date': YearPickerInput(format="%Y"),
            #			'total_hours': forms.HiddenInput(),
            #			'checked_sign_by': forms.TextInput(attrs={'class': "form-control"}),
            #			'verify_by': forms.TextInput(attrs={'class': "form-control"}),
        }
#	staff = forms.CharField(required=False, label="", widget=forms.HiddenInput(attrs={'class': "form-control"}))
#	date = forms.DateField(required=False, label="", widget=YearPickerInput(format="%Y", attrs={'class': "form-control"}))
    annual_leave_days = forms.IntegerField(
        required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
    public_holiday_days = forms.IntegerField(
        required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
    replacement_public_holiday = forms.IntegerField(
        required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
    medical_certificate = forms.CharField(
        required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    siri_no_diagnosis = forms.CharField(
        required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    emergency_leaves = forms.CharField(
        required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    emergency_leaves_reasons = forms.CharField(
        required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    unpaid_leaves = forms.CharField(
        required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    unpaid_leaves_reasons = forms.CharField(
        required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))


class StaffRecords_Form(BSModalForm):

    staff = forms.CharField(required=False, label="", widget=forms.HiddenInput(
        attrs={'class': "form-control"}))
    date = form.YearField(required=False, label="", initial=datetime.datetime.now(
    ).year, widget=YearPickerInput(format="%Y", attrs={'class': "form-control"}))
    annual_leave_days = forms.IntegerField(
        required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
    public_holiday_days = forms.IntegerField(
        required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
    replacement_public_holiday = forms.IntegerField(
        required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
    medical_certificate = forms.CharField(
        required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    siri_no_diagnosis = forms.CharField(
        required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    emergency_leaves = forms.CharField(
        required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    emergency_leaves_reasons = forms.CharField(
        required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    unpaid_leaves = forms.CharField(
        required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    unpaid_leaves_reasons = forms.CharField(
        required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))

    def clean_medical_certificate(self):
        return self.cleaned_data['medical_certificate'].capitalize()

    def clean_siri_no_diagnosis(self):
        return self.cleaned_data['siri_no_diagnosis'].capitalize()

    def clean_emergency_leaves(self):
        return self.cleaned_data['emergency_leaves'].capitalize()

    def clean_emergency_leaves_reasons(self):
        return self.cleaned_data['emergency_leaves_reasons'].capitalize()

    def clean_unpaid_leaves(self):
        return self.cleaned_data['unpaid_leaves'].capitalize()

    def clean_unpaid_leaves_reasons(self):
        return self.cleaned_data['unpaid_leaves_reasons'].capitalize()


class Medicine_Form(BSModalForm):
    name = forms.CharField(required=False, label="", widget=forms.HiddenInput(
        attrs={'class': "form-control"}))
