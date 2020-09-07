from django import forms
from django.utils.translation import ugettext_lazy as _
from durationwidget.widgets import TimeDurationWidget

from ..models import *
from ..forms import *
from ..lookups import *
#from .custom_layout import *
from accounts.models import *

from bootstrap_modal_forms.forms import *
from selectable.forms import AutoCompleteWidget


class OvertimeClaim_ModelForm(BSModalModelForm):

	class Meta:
		model = OvertimeClaim
		fields = '__all__'
		widgets = {
			'patient': forms.HiddenInput(),
			'total_hours': forms.HiddenInput(),
#			'checked_sign_by': forms.TextInput(attrs={'class': "form-control"}),
#			'verify_by': forms.TextInput(attrs={'class': "form-control"}),
		}

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.fields['checked_sign_by'].label = ''

	date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d/%m/%Y", attrs={'class': "form-control"}))
#   date = forms.DateTimeField(required=False, label="", widget=DatePickerInput(attrs={'class': "form-control"}))
#   date = forms.DateTimeField(required=False, label="", initial=timezone.now, input_formats=settings.DATETIME_INPUT_FORMATS, widget=DatePickerInput(format="%d/%m/%Y", attrs={'class': "form-control"}))
#    duration_time = forms.DurationField(required=True, label="", initial="01:00:00", widget=forms.TextInput(attrs={'class': "form-control"}))
	duration_time_from = forms.DurationField(required=False, label="", initial="00:05:00", widget=TimeDurationWidget(show_days=False, show_hours=True, show_minutes=True, show_seconds=False, attrs={'class': "form-control"}))
	duration_time_to = forms.DurationField(required=False, label="", initial="00:05:00", widget=TimeDurationWidget(show_days=False, show_hours=True, show_minutes=True, show_seconds=False, attrs={'class': "form-control"}))
	hours = forms.TimeField(required=False, label="", initial=get_time, input_formats=settings.TIME_INPUT_FORMATS, widget=TimePickerInput(format="%H:%M", attrs={'class': "form-control"}))
#   hours = forms.DateTimeField(required=False, label="", initial=get_time, input_formats=settings.TIME_INPUT_FORMATS, widget=DatePickerInput(format="%H:%M", attrs={'class': "form-control"}))
#   total_hours = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
#    checked_sign_by = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
#	checked_sign_by = forms.CharField(required=False, label="", widget=AutoCompleteWidget(StaffnameLookup, attrs={'class': "form-control", 'placeholder': _("type min. 3 characters & select")}))
#    verify_by = forms.CharField(required=False, label="", initial="None", widget=forms.TextInput(attrs={'class': "form-control"}))
	verify_by = forms.CharField(required=False, label="", widget=AutoCompleteWidget(StaffnameLookup, attrs={'class': "form-control", 'placeholder': _("type min. 3 characters & select")}))


class OvertimeClaim_Form(BSModalForm):

	patient = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d/%m/%Y", attrs={'class': "form-control"}))
#	duration_time_from = forms.DurationField(required=False, label="", initial="00:05:00", widget=TimeDurationWidget(show_days=False, show_hours=True, show_minutes=True, show_seconds=False, attrs={'class': "form-control"}))
	duration_time_from = forms.TimeField(required=False, label="", initial="00:00", input_formats=settings.TIME_INPUT_FORMATS, widget=TimePickerInput(format="%H:%M", attrs={'class': "form-control"}))
#	duration_time_to = forms.DurationField(required=False, label="", initial="00:05:00", widget=TimeDurationWidget(show_days=False, show_hours=True, show_minutes=True, show_seconds=False, attrs={'class': "form-control"}))
	duration_time_to = forms.TimeField(required=False, label="", initial=get_time, input_formats=settings.TIME_INPUT_FORMATS, widget=TimePickerInput(format="%H:%M", attrs={'class': "form-control"}))
	hours = forms.TimeField(required=False, label="", initial=get_time, input_formats=settings.TIME_INPUT_FORMATS, widget=TimePickerInput(format="%H:%M", attrs={'class': "form-control"}))
	total_hours = forms.CharField(required=False, label="", widget=forms.HiddenInput(attrs={'class': "form-control"}))
	checked_sign_by = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
#	checked_sign_by = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}))
#	checked_sign_by = forms.CharField(required=False, label="", widget=AutoCompleteWidget(StaffnameLookup, attrs={'class': "form-control", 'placeholder': _("type min. 3 characters & select")}))
	verify_by = forms.CharField(required=False, label="", widget=AutoCompleteWidget(StaffnameLookup, attrs={'class': "form-control", 'placeholder': _("type min. 3 characters & select")}))

#	def __init__(self, *args, **kwargs):
#		super().__init__(*args, **kwargs)

#		self.helper = FormHelper()
#		self.fields['checked_sign_by'].label = ''
#		self.helper.layout = Layout(
#			InlineRadios('duration_time_from'),
#			Div(
#				Div('duration_time_from', css_class='col-md-6',),
#				css_class='row',
#			),
#		)
