from django import forms
from django.utils.translation import ugettext_lazy as _
from django.forms.formsets import BaseFormSet
from django.utils.datastructures import MultiValueDict

from ..models import *
from ..forms import *
from ..lookups import *
#from .custom_layout import *
from accounts.models import *

from bootstrap_modal_forms.forms import *


class Stool_ModelForm(BSModalModelForm):
	class Meta:
		model = Stool
		fields = '__all__'
		widgets = {
#           patient': forms.HiddenInput(),
		}

#	patient = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d/%m/%Y", attrs={'class': "form-control"}))
	time = forms.TimeField(required=False, label="", initial=get_time, input_formats=settings.TIME_INPUT_FORMATS, widget=TimePickerInput(format="%H:%M", attrs={'class': "form-control"}))
	frequency = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=Stool.STOOL_FREQUENCY_CHOICES)
	consistency = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=Stool.CONSISTENCY_CHOICES)
	amount = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=Stool.AMOUNT_CHOICES)
	remark = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	done_by = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))


class Stool_Form(BSModalForm):
#	def __init__(self, *args, **kwargs):
#	def __init__(self, *args, user, **kwargs):
#	def __init__(self, done_by, *args, **kwargs):
#	def __init__(self, data, **kwargs):
#		initial = kwargs.get("initial", {})
#		data = MultiValueDict({**{k: [v] for k, v in initial.items()}, **data})
#		self.request = kwargs.pop('request', None)
#		self.user = kwargs.pop('user', None)
#		full_name = kwargs.pop('full_name')
#		done_by = kwargs.pop('done_by', None)
#		self.user = user
#		super().__init__(*args, **kwargs)
#		super().__init__(data, **kwargs)
#		self.fields['done_by'].queryset = UserProfile.objects.filter(done_by=done_by)
#		initial = kwargs.pop('initial', {})
#		self.done_by = kwargs.pop('done_by')
#		self.done_by = request.user
#		self.fields['done_by'] = request.user
#		for item in self.initial_fields:
#			if hasattr(self.done_by, item):
#				initial[item] = initial.get(item) or getattr(self.done_by, item)
#		kwargs['initial'] = initial
#		super().__init__(*args, **kwargs)

	patient = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
#	patient = forms.ModelChoiceField(queryset=None, widget=forms.Select, required=True)
	date = forms.DateField(required=False, label="", input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d/%m/%Y", attrs={'class': "form-control"}))
	time = forms.TimeField(required=False, label="", input_formats=settings.TIME_INPUT_FORMATS, widget=TimePickerInput(format="%H:%M", attrs={'class': "form-control"}))
	frequency = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=Stool.STOOL_FREQUENCY_CHOICES)
	consistency = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=Stool.CONSISTENCY_CHOICES)
	amount = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=Stool.AMOUNT_CHOICES)
	remark = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	done_by = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))


Stool_ModelFormSet = modelformset_factory(
	Stool,
	form=Stool_ModelForm,
	extra=1,
	max_num=1,
#    can_delete=False
)

Stool_InlineFormSet = inlineformset_factory(
	UserProfile,
	Stool,
	form=Stool_ModelForm,
	extra=1,
	max_num=1,
#    can_delete=False
)


StoolFormSet = formset_factory(
	Stool_Form,
#   formset = Stool_ModelForm,
	extra=1,
	max_num=1,
	#   can_delete=True,
)
