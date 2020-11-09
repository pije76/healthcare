from django import forms
from django.utils.translation import ugettext_lazy as _

from ..models import *
from ..forms import *
from ..lookups import *
#from .custom_layout import *
from accounts.models import *

from bootstrap_modal_forms.forms import *
from selectable.forms import *

from selectable import forms as form


class ApplicationForHomeLeave_ModelForm(BSModalModelForm):
    class Meta:
        model = ApplicationForHomeLeave
#       fields = '__all__'
        fields = [
            'patient',
            'ic_number',
            'family_name',
            'family_ic_number',
            'family_relationship',
            'family_phone',
            'witnessed_designation',
            'witnessed_signature',
            'witnessed_date',
        ]
        widgets = {
            'patient': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
#       self.fields['ic_number'].queryset = UserProfile.objects.none()
#       self.fields['ic_number'].label = ''

    ic_number = forms.CharField(max_length=14, required=False, label="", validators=[ic_number_validator], widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': _("autofill")}))
    family_name = forms.CharField(required=False, label="", widget=AutoCompleteWidget(FamilyNameLookup, attrs={'class': "form-control", 'placeholder': _("(type min. 3 characters & select)")}))
    family_ic_number = forms.CharField(required=False, label="", validators=[ic_number_validator], widget=AutoCompleteWidget(ECNumberLookup, attrs={'class': "form-control", 'placeholder': _("autofill")}))
    family_relationship = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': _("autofill")}))
    family_phone = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': _("autofill")}))
    witnessed_designation = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': _("(designation)")}))
    witnessed_signature = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': _("(signature)")}))
    witnessed_date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d-%m-%Y", attrs={'class': "form-control"}))


class ApplicationForHomeLeave_Form(BSModalForm):
    patient = forms.CharField(required=False, label="", widget=AutoCompleteWidget(FullnameLookup, attrs={'class': "form-control", 'placeholder': _("(type min. 3 characters & select)")}))
    ic_number = forms.CharField(max_length=14, required=False, label="", validators=[ic_number_validator], widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': _("autofill")}))
    family_name = forms.CharField(required=False, label="", widget=AutoCompleteWidget(FamilyNameLookup, attrs={'class': "form-control", 'placeholder': _("(type min. 3 characters & select)")}))
    family_ic_number = forms.CharField(max_length=14, required=False, label="", validators=[ic_number_validator], widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': _("autofill")}))
    family_relationship = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': _("autofill")}))
    family_phone = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': _("autofill")}))

    signature_name = forms.CharField(required=False, label="", widget=AutoCompleteWidget(FamilyNameLookup, attrs={'class': "form-control", 'placeholder': _("autofill")}))
    signature_relationship = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': _("autofill")}))
    signature_ic_number = forms.CharField(max_length=14, required=False, label="", validators=[ic_number_validator], widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': _("autofill")}))

    witnessed_name = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': _("autofill")}))
    witnessed_designation = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': _("(designation)")}))
    witnessed_signature = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': _("(signature)")}))
    witnessed_date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d-%m-%Y", attrs={'class': "form-control"}))

    def clean_witnessed_designation(self):
        return self.cleaned_data['witnessed_designation'].capitalize()

    def clean_witnessed_signature(self):
        return self.cleaned_data['witnessed_signature'].capitalize()


class Family_Form(BSModalModelForm):
    class Meta:
        model = Family
        fields = '__all__'

    patient = forms.CharField(required=False, label="", widget=forms.HiddenInput(attrs={'class': "form-control"}))
    ec_name = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    ec_ic_number = forms.CharField(max_length=14, required=False, label="", validators=[ic_number_validator], widget=forms.TextInput(attrs={'class': "form-control"}))
    ec_ic_upload = forms.ImageField(required=False, label="", widget=forms.FileInput(attrs={'class': "form-control"}))
    ec_relationship = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    ec_phone = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    ec_address = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4, 'cols': 15}))

