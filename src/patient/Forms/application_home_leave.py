from django import forms
from django.utils.translation import ugettext_lazy as _

from ..models import *
from ..forms import *
from ..lookups import *
#from .custom_layout import *
from accounts.models import *

from bootstrap_modal_forms.forms import *
from selectable.forms import AutoCompleteWidget

class ApplicationForHomeLeaveForm(BSModalModelForm):
    class Meta:
        model = ApplicationForHomeLeave
        fields = '__all__'
        widgets = {
                    #           'patient': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
#       self.fields['ic_number'].queryset = UserProfile.objects.none()
#       self.fields['ic_number'].label = ''

#       if 'country' in self.data:
#           try:
#               country_id = int(self.data.get('country'))
#               self.fields['city'].queryset = City.objects.filter(country_id=country_id).order_by('name')
#           except (ValueError, TypeError):
#               pass  # invalid input from the client; ignore and fallback to empty City queryset
#           elif self.instance.pk:
#               self.fields['city'].queryset = self.instance.country.city_set.order_by('name')


#   patient = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
#   patient = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}))
    patient = forms.CharField(required=False, label="", widget=AutoCompleteWidget(FullnameLookup, attrs={'class': "form-control", 'placeholder': _("type min. 3 characters & select")}))
#   patient = forms.CharField(max_length=14, required=False, label="", validators=[ic_number_validator], widget=AutoCompleteWidget(FullnameLookup, attrs={'class': "form-control", 'placeholder': _("yymmdd-xx-zzzz")}))
#   patient = AutoCompleteSelectField(required=False, label="", lookup_class=ECNumberLookup, widget=AutoComboboxSelectWidget)
#   ic_number = AutoCompleteSelectField(required=False, label="", lookup_class=ECNumberLookup, widget=AutoCompleteWidget(ECNumberLookup, attrs={'class': "form-control", 'placeholder': _("type min. 3 characters & select")}))
#   ic_number = AutoCompleteSelectField(required=False, label="", lookup_class=ECNumberLookup, widget=AutoCompleteWidget(ECNumberLookup, attrs={'class': "form-control", 'placeholder': _("yymmdd-xx-zzzz")}))
#   ic_number = forms.CharField(required=False, label="", widget=AutoCompleteWidget(ECNumberLookup, attrs={'class': "form-control", 'placeholder': _("yymmdd-xx-zzzz")}))
#   ic_number = AutoCompleteSelectField(required=False, label="", lookup_class=ECNumberLookup, widget=AutoComboboxSelectWidget)
#   ic_number = AutoCompleteSelectField(required=False, label="", lookup_class=ECNumberLookup)
#   ic_number = forms.CharField(required=False, label="", widget=AutoCompleteWidget(ECNumberLookup, attrs={'class': "form-control", 'placeholder': _("yymmdd-xx-zzzz")}))
    ic_number = forms.CharField(max_length=14, required=False, label="", validators=[ic_number_validator], widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': _("yymmdd-xx-zzzz")}))
##  ic_number = forms.CharField(required=False, label="")
#   family_name = forms.CharField(required=False, label="", initial="name", widget=forms.TextInput(attrs={'class': "form-control"}))
#   family_name = AutoCompleteSelectField('full_name', required=True, label='', help_text=None)
#   family_name = forms.CharField(required=False, label="", initial="name", widget=PatientFamilyNameWidget(attrs={'class': "form-control"}))
#   family_name = apply_select2(forms.Select)
#   family_name = AutoCompleteSelectField(lookup_class=FamilyNameLookup, label='')
    family_name = forms.CharField(required=False, label="", widget=AutoCompleteWidget(FamilyNameLookup, attrs={'class': "form-control", 'placeholder': _("type min. 3 characters & select")}))
#    family_name = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': _("type min. 3 characters & select")}))
#   family_name = forms.ModelChoiceField(queryset=Admission.objects.all(), widget=autocomplete.ModelSelect2(url='application_home_leave'))
#   family_ic_number = forms.CharField(max_length=14, required=False, label="", validators=[ic_number_validator], widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': _("yymmdd-xx-zzzz")}))
    family_ic_number = forms.CharField(required=False, label="", validators=[ic_number_validator], widget=AutoCompleteWidget(ECNumberLookup, attrs={'class': "form-control", 'placeholder': _("yymmdd-xx-zzzz")}))
    family_relationship = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': _("myself or relationship")}))
    family_phone = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': _("+6012345678")}))
    designation = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': _("designation")}))
    signature = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': _("signature")}))
#    signature = JSignatureField()
    date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d/%m/%Y", attrs={'class': "form-control"}))
