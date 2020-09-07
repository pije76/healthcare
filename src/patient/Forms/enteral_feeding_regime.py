from django import forms
from django.utils.translation import ugettext_lazy as _
from django.forms import BaseFormSet

from ..models import *
from ..forms import *
from ..lookups import *
#from .custom_layout import *
from accounts.models import *

from bootstrap_modal_forms.forms import *

import datetime

midnight = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)


class TestBaseFormSet(BaseFormSet):
	def get_form_kwargs(self, index):
		kwargs = super().get_form_kwargs(index)
		kwargs['custom_kwarg'] = index
#		kwargs.update({'get_username': self.username})
#		kwargs['username'] = kwargs.pop('username')
#		kwargs['instance'] = index
		return kwargs


class EnteralFeedingRegime_ModelForm(BSModalModelForm):

	class Meta:
		model = EnteralFeedingRegime
		fields = '__all__'
		widgets = {
#			'patient': forms.HiddenInput(),
		}

	patient = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d/%m/%Y", attrs={'class': "form-control"}))
	time = forms.TimeField(required=False, label="", initial=get_time, input_formats=settings.TIME_INPUT_FORMATS, widget=TimePickerInput(format="%H:%M", attrs={'class': "form-control"}))
	type_of_milk = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	amount = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	warm_water_before = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control calc"}))
	warm_water_after = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control calc"}))

##	def __init__(self, *args, **kwargs):
#	def __init__(self, username, *args, **kwargs):
#		user_details = kwargs.pop('user_details', None)
#		get_username = kwargs.pop('get_username')
#		get_username = kwargs.get('get_username')
#		self.get_username = kwargs.pop("get_username")
##		custom_kwarg = kwargs.pop('custom_kwarg')
#		qs = kwargs.pop("group_qs")
#		profiles = UserProfile.objects.filter(username=username)
#		username = kwargs.pop('instance')
##		super().__init__(*args, **kwargs)
#		my_user = kwargs.get('username')
#		first_name = my_user

#		self.fields['patient'].initial = get_username
#		self.fields['patient'].initial = username
#		self.fields['patient'].initial = user.username
#		self.fields['patient'].initial = self.instance.patient
#		self.fields["group"].queryset = qs
#		if user_details:
#			self.fields['patient'].initial = user_details[0]['username']
#		self.fields["patient"].initial = (item.full_name for item in profiles)
#		self.fields['patient'].initial = (username.full_name for username in UserProfile.objects.filter())
##		self.fields['time'].initial = midnight + datetime.timedelta(hours=custom_kwarg)


EnteralFeedingRegime_ModelFormSet = formset_factory(EnteralFeedingRegime_ModelForm, extra=24, formset=TestBaseFormSet)


class EnteralFeedingRegime_Form(BSModalForm):

	patient = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d/%m/%Y", attrs={'class': "form-control"}))
	time = forms.TimeField(required=False, label="", input_formats=settings.TIME_INPUT_FORMATS, widget=TimePickerInput(format="%H:%M", attrs={'class': "form-control"}))
	type_of_milk = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	amount = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	warm_water_before = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control calc"}))
	warm_water_after = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control calc"}))

#	def __init__(self, *args, **kwargs):
#		custom_kwarg = kwargs.pop('custom_kwarg')
#		super().__init__(*args, **kwargs)
#		self.fields['time'].initial = midnight + datetime.timedelta(hours=custom_kwarg)


#EnteralFeedingRegime_FormSet = formset_factory(EnteralFeedingRegime_Form, extra=0)
#EnteralFeedingRegime_FormSet = formset_factory(EnteralFeedingRegime_Form, extra=24, formset=TestBaseFormSet)

EnteralFeedingRegime_FormSet = formset_factory(
	EnteralFeedingRegime_Form,
#	formset=TestBaseFormSet,
	extra=0,
#    max_num=0,
#   can_delete=True,
)
