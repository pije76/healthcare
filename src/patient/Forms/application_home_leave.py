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


class ApplicationForHomeLeave_Form(forms.Form):
#    class Meta:
#        model = ApplicationForHomeLeave
#        fields = '__all__'

#    patient = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    patient = forms.CharField(required=False, label="", widget=AutoCompleteWidget(FullnameLookup, attrs={'class': "form-control", 'placeholder': _("type min. 3 characters & select")}))
    ic_number = forms.CharField(max_length=14, required=False, label="", validators=[ic_number_validator], widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': _("yymmdd-xx-zzzz")}))
    family_name = forms.CharField(required=False, label="", widget=AutoCompleteWidget(FamilyNameLookup, attrs={'class': "form-control", 'placeholder': _("type min. 3 characters & select")}))
#    family_name = AutoCompleteSelectMultipleField(lookup_class=FamilyNameLookup)
#    family_ic_number = forms.CharField(required=False, label="", validators=[ic_number_validator], widget=AutoCompleteWidget(ECNumberLookup, attrs={'class': "form-control", 'placeholder': _("yymmdd-xx-zzzz")}))
    family_ic_number = forms.CharField(max_length=14, required=False, label="", validators=[ic_number_validator], widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': _("yymmdd-xx-zzzz")}))
    family_relationship = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': _("myself or relationship")}))
    family_phone = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': _("+6012345678")}))

    signature_name = forms.CharField(required=False, label="", widget=AutoCompleteWidget(FamilyNameLookup, attrs={'class': "form-control", 'placeholder': _("type min. 3 characters & select")}))
    signature_relationship = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': _("myself or relationship")}))
    signature_ic_number = forms.CharField(max_length=14, required=False, label="", validators=[ic_number_validator], widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': _("yymmdd-xx-zzzz")}))

    witnessed_name = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    witnessed_designation = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': _("designation")}))
    witnessed_signature = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': _("signature")}))
    witnessed_date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d/%m/%Y", attrs={'class': "form-control"}))

##    def __init__(self, *args, **kwargs):
#        user = kwargs.pop('get_user')
#        print("user: ", user)
##        user = None
##        if kwargs.get('patient', False):
##            user = UserProfile.objects.get(pk=kwargs.get('patient'))
##        print("user: ", user)
##        super().__init__(*args, **kwargs)
#        self.fields['family_name'].queryset = UserProfile.objects.filter(pk = user.id)
##        if user:
##            self.fields['family_name'] = forms.CharField(required=False, label="", widget=AutoCompleteWidget(FullnameLookup, attrs={'class': "form-control", 'placeholder': _("type min. 3 characters & select")}))
##        else:
##            self.fields['family_name'] = forms.CharField(required=False, label="", widget=AutoCompleteWidget(FamilyNameLookup, attrs={'class': "form-control", 'placeholder': _("type min. 3 characters & select")}))



class Family_Form(forms.ModelForm):
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

