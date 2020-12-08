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
from djangoyearlessdate import forms as form
from bootstrap_modal_forms.forms import *
from bootstrap_datepicker_plus import YearPickerInput


from .models import *
#from .lookups import *
#from .custom_layout import *
from accounts.models import *

import datetime

get_today = datetime.date.today()


class Medicine_ModelForm(BSModalModelForm):
    class Meta:
        model = Medicine
        fields = '__all__'
        widgets = {
            'patient': forms.HiddenInput(),
        }

    drug_name = forms.CharField(required=False, label="", widget=forms.TextInput(
        attrs={'class': "form-control"}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

    def clean_drug_name(self):
        return self.cleaned_data['drug_name'].capitalize()


class Medicine_Form(BSModalForm):
    drug_name = forms.CharField(required=False, label="", widget=forms.TextInput(
        attrs={'class': "form-control"}))

    def clean_drug_name(self):
        return self.cleaned_data['drug_name'].capitalize()


class WoundCondition_ModelForm(BSModalModelForm):
    class Meta:
        model = WoundCondition
        fields = '__all__'
        widgets = {
            'patient': forms.HiddenInput(),
        }

    name = forms.CharField(required=False, label="", widget=forms.TextInput(
        attrs={'class': "form-control"}))
    parent = TreeNodeChoiceField(required=False, label="", queryset=WoundCondition.objects,
                                 widget=forms.Select(attrs={'class': "form-control"}),)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

    def clean_name(self):
        return self.cleaned_data['name'].capitalize()

    def clean_parent(self):
        return self.cleaned_data['parent'].capitalize()


class WoundCondition_Form(BSModalForm):
    name = forms.CharField(required=False, label="", widget=forms.TextInput(
        attrs={'class': "form-control"}))
#   parent = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    parent = TreeNodeChoiceField(required=False, label="", queryset=WoundCondition.objects,
                                 widget=forms.Select(attrs={'class': "form-control"}),)

    def clean_name(self):
        return self.cleaned_data['name'].capitalize()


class Allergy_Model_Form(forms.ModelForm):
    class Meta:
        model = Allergy
#       fields = '__all__'
        fields = [
            'patient',
            'allergy_drug',
            'allergy_food',
            'allergy_others',
        ]
        widgets = {
            'patient': forms.HiddenInput(),
            'medication_date': forms.HiddenInput(),
        }

#   medication_date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d-%m-%Y", attrs={'class': "form-control", 'style': "display:none;"}))
    medication_date = forms.CharField(
        required=False, label="", widget=forms.HiddenInput(attrs={'class': "form-control"}))
    allergy_drug = forms.CharField(
        required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    allergy_food = forms.CharField(
        required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    allergy_others = forms.CharField(
        required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))

    def clean_allergy_drug(self):
        return self.cleaned_data['allergy_drug'].capitalize()

    def clean_allergy_food(self):
        return self.cleaned_data['allergy_food'].capitalize()

    def clean_allergy_others(self):
        return self.cleaned_data['allergy_others'].capitalize()


class Allergy_ModelForm(BSModalModelForm):
    class Meta:
        model = Allergy
#       fields = '__all__'
        fields = [
            'patient',
            'allergy_drug',
            'allergy_food',
            'allergy_others',
        ]
        widgets = {
            'patient': forms.HiddenInput(),
        }

#   patient = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))

#   allergy_drug = forms.CharField(required=False, label=_("Medicine(s):"), widget=forms.TextInput(attrs={'class': "form-control"}))
    allergy_drug = forms.CharField(
        required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
#   allergy_food = forms.CharField(required=False, label=_("Food:"), widget=forms.TextInput(attrs={'class': "form-control"}))
    allergy_food = forms.CharField(
        required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
#   allergy_others = forms.CharField(required=False, label=_("Others:"), widget=forms.TextInput(attrs={'class': "form-control"}))
    allergy_others = forms.CharField(
        required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))

    def clean_allergy_drug(self):
        return self.cleaned_data['allergy_drug'].capitalize()

    def clean_allergy_food(self):
        return self.cleaned_data['allergy_food'].capitalize()

    def clean_allergy_others(self):
        return self.cleaned_data['allergy_others'].capitalize()


class Allergy_Form(BSModalForm):

    patient = forms.CharField(required=False, label="", widget=forms.HiddenInput(
        attrs={'class': "form-control"}))
    allergy_drug = forms.CharField(required=False, label=_(
        "Drug(s):"), widget=forms.TextInput(attrs={'class': "form-control"}))
    allergy_food = forms.CharField(required=False, label=_(
        "Food:"), widget=forms.TextInput(attrs={'class': "form-control"}))
    allergy_others = forms.CharField(required=False, label=_(
        "Others:"), widget=forms.TextInput(attrs={'class': "form-control"}))

    def clean_allergy_drug(self):
        return self.cleaned_data['allergy_drug'].capitalize()

    def clean_allergy_food(self):
        return self.cleaned_data['allergy_food'].capitalize()

    def clean_allergy_others(self):
        return self.cleaned_data['allergy_others'].capitalize()
