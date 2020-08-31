from django import forms
from django.utils.translation import ugettext_lazy as _
from django.forms import BaseFormSet

from ..models import *
from ..forms import *
from ..lookups import *
#from .custom_layout import *
from accounts.models import *

from bootstrap_modal_forms.forms import *

#def get_time_inc():
#    delta = datetime.datetime.now() + datetime.timedelta(hours=1)
#    for item in delta:
#        return item

class EnteralFeedingRegime_ModelForm(BSModalModelForm):

	class Meta:
		model = EnteralFeedingRegime
		fields = '__all__'
		widgets = {
			'patient': forms.HiddenInput(),
		}

	date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d/%m/%Y", attrs={'class': "form-control"}))
	time = forms.TimeField(required=False, label="", initial=get_time, input_formats=settings.TIME_INPUT_FORMATS, widget=TimePickerInput(format="%H:%M", attrs={'class': "form-control"}))
	type_of_milk = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	amount = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	warm_water_before = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control calc"}))
	warm_water_after = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control calc"}))


class TestBaseFormSet(BaseFormSet):
	def get_form_kwargs(self, index):
		kwargs = super().get_form_kwargs(index)
		kwargs['custom_kwarg'] = index
#		kwargs['custom_kwarg'] = kwargs['time'][index]
		return kwargs

#EnteralFeedingRegime_FormSet = formset_factory(EnteralFeedingRegime_Form, extra=24, formset=TestBaseFormSet)

class EnteralFeedingRegime_Form(forms.Form):
	patient = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d/%m/%Y", attrs={'class': "form-control"}))
	time = forms.TimeField(required=False, label="", input_formats=settings.TIME_INPUT_FORMATS, widget=TimePickerInput(format="%H:%M", attrs={'class': "form-control"}))
#	time = forms.DateTimeField()
	type_of_milk = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	amount = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	warm_water_before = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control calc"}))
	warm_water_after = forms.IntegerField(required=False, label="", initial="0", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control calc"}))

##	def __init__(self, *args, **kwargs):
##		custom_kwarg = kwargs.pop('custom_kwarg')
##		super().__init__(*args, **kwargs)
#        for p, i in numb.items():
#		self.fields['time'] = forms.TimeField(required=True, label="", initial=[for x in initial_list], widget=TimePickerInput())
##		self.fields['time'].initial = datetime.datetime.now() + datetime.timedelta(hours=custom_kwarg)

EnteralFeedingRegime_FormSet = formset_factory(EnteralFeedingRegime_Form, extra=0)
#EnteralFeedingRegime_FormSet = formset_factory(EnteralFeedingRegime_Form, extra=24, formset=TestBaseFormSet)
