from django import forms
from django.contrib.auth.models import *
from django.utils.translation import ugettext as _

from .models import *
from patient.models import *
from patient.forms import *
from patient.choices import *

from allauth.account.forms import LoginForm, SignupForm

ic_number_validator = RegexValidator("\d{6}\-\d{2}\-\d{4}", "IC Number format needs to be yymmdd-xx-zzzz.")


class MyLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)

    password = forms.CharField(max_length=100, required=True, label=_('Password'), widget=forms.PasswordInput(attrs={'class': "form-control", 'placeholder': _("Password")}))


class MySignUpForm(SignupForm):

    username = forms.CharField(max_length=100, required=True, label=_('Username:'), widget=forms.TextInput(attrs={'class': "form-control"}))
    full_name = forms.CharField(max_length=100, required=False, label=_('Full Name:'), widget=forms.TextInput(attrs={'class': "form-control"}))
    is_patient = forms.BooleanField(required=False, label='', widget=forms.HiddenInput())
    is_staff = forms.BooleanField(required=False, label='', widget=forms.HiddenInput())

    def save(self, request):
        user = super().save(request)
        user.full_name = self.cleaned_data['full_name']
        user.username = self.cleaned_data['username']
        user.is_active = True
        user.is_admin = False
        user.is_staff = self.cleaned_data['is_staff']
        user.is_patient = self.cleaned_data['is_patient']
        user.save()
        return user


class ChangeUserProfile(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    full_name = forms.CharField(max_length=100, required=True, label='', widget=forms.TextInput(attrs={'class': "form-control"}))
    email = forms.EmailField(required=False, label='', widget=forms.TextInput(attrs={'class': "form-control"}))
    ic_number = forms.CharField(max_length=14, required=False, label="", initial='yymmdd-xx-zzzz', validators=[ic_number_validator], widget=forms.TextInput(attrs={'class': "form-control"}))

    class Meta:
        model = UserProfile
        fields = ('full_name', 'email', 'ic_number')


class ChangeAdmission(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean_ic_number(self):
        ic_number = self.cleaned_data['ic_number']
        try:
            ic_number = Admission.objects.get(ic_number=ic_number)
        except Admission.DoesNotExist:
            return ic_number
        raise forms.ValidationError('%s already exists' % ic_number)

    ic_number = forms.CharField(max_length=14, required=False, label="", initial='yymmdd-xx-zzzz', validators=[ic_number_validator], widget=forms.TextInput(attrs={'class': "form-control"}))

    class Meta:
        model = Admission
        fields = ('ic_number',)


class PatientProfile_ModelForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
        widgets = {
            'date_joined': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(InlineRadios('')),
        )

    full_name = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    username = forms.CharField(required=False, label="", widget=forms.HiddenInput(attrs={'class': "form-control"}))
    is_patient = forms.BooleanField(required=False, label='', widget=forms.HiddenInput())
    is_active = forms.BooleanField(required=False, label='', widget=forms.HiddenInput())
    email = forms.EmailField(required=False, label="", widget=forms.HiddenInput(attrs={'class': "form-control"}))
    password = forms.CharField(required=False, label="", widget=forms.HiddenInput(attrs={'class': "form-control"}))
    date_joined = forms.DateTimeField(required=False, label="", input_formats=settings.DATETIME_INPUT_FORMATS, widget=DateTimePickerInput(format="%d-%m-%Y %H:%M", attrs={'class': "form-control"}))
    ic_number = forms.CharField(max_length=14, required=False, label=_('IC No:'), validators=[ic_number_validator], widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': _("yymmdd-xx-zzzz")}))
    ic_upload = forms.ImageField(required=False, label=_('IC Upload:'), widget=forms.FileInput(attrs={'class': "form-control"}))
    birth_date = forms.DateField(required=False, label="", initial=get_today, input_formats=settings.DATE_INPUT_FORMATS, widget=DatePickerInput(format="%d-%m-%Y", attrs={'class': "form-control"}))
    age = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control", 'readonly': 'readonly', 'placeholder': _("*auto fill-in")}))
    gender = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=GENDER_CHOICES)
    marital_status = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=MARITAL_CHOICES)
    marital_status_others = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    religion = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=RELIGION_CHOICES)
    religion_others = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    occupation = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=OCCUPATION_CHOICES)
    occupation_others = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    communication_sight = forms.ChoiceField(required=False, label=_("Sight"), widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=COMMUNICATION_SIGHT_CHOICES)
    communication_hearing = forms.ChoiceField(required=False, label=_("Hearing"), widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=COMMUNICATION_HEARING_CHOICES)
    communication_hearing_others = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control", 'style': "margin-top:1.0rem;"}))
    address = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4, 'cols': 15}))

    def clean(self):
        cleaned_data = super().clean()
        marital_status_others = cleaned_data.get('marital_status_others')
        religion_others = cleaned_data.get('religion_others')
        occupation_others = cleaned_data.get('occupation_others')
        communication_hearing_others = cleaned_data.get('communication_hearing_others')

        if marital_status_others:
            cleaned_data['marital_status'] = marital_status_others
        if religion_others:
            cleaned_data['religion'] = religion_others
        if occupation_others:
            cleaned_data['occupation'] = occupation_others
        if communication_hearing_others:
            cleaned_data['communication_hearing'] = communication_hearing_others

    def clean_marital_status_others(self):
        return self.cleaned_data['marital_status_others'].capitalize()

    def clean_religion_others(self):
        return self.cleaned_data['religion_others'].capitalize()

    def clean_occupation_others(self):
        return self.cleaned_data['occupation_others'].capitalize()

    def clean_communication_hearing_others(self):
        return self.cleaned_data['communication_hearing_others'].capitalize()

    def clean_address(self):
        return self.cleaned_data['address'].capitalize()


class Family_Form(forms.Form):

    patient = forms.CharField(required=False, label="", widget=forms.HiddenInput(attrs={'class': "form-control"}))
    ec_name = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    ec_ic_number = forms.CharField(max_length=14, required=False, label="", validators=[ic_number_validator], widget=forms.TextInput(attrs={'class': "form-control"}))
    ec_ic_upload = forms.ImageField(required=False, label="", widget=forms.FileInput(attrs={'class': "form-control"}))
    ec_relationship = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    ec_phone = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    ec_address = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4, 'cols': 15}))

    def clean_ec_name(self):
        return self.cleaned_data['ec_name'].capitalize()

    def clean_ec_relationship(self):
        return self.cleaned_data['ec_relationship'].capitalize()

    def clean_ec_address(self):
        return self.cleaned_data['ec_address'].capitalize()


Family_FormSet = formset_factory(
    Family_Form,
    extra=1,
    max_num=5,
)


class Family_ModelForm(forms.Form):
    patient = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control", 'style': "display:none;"}))
    ec_name = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    ec_ic_number = forms.CharField(max_length=14, required=False, label="", validators=[ic_number_validator], widget=forms.TextInput(attrs={'class': "form-control"}))
    ec_ic_upload = forms.ImageField(required=False, label="", widget=forms.FileInput(attrs={'class': "form-control"}))
    ec_relationship = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    ec_phone = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    ec_address = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4, 'cols': 15}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(InlineRadios('')),
        )

    def clean_ec_name(self):
        return self.cleaned_data['ec_name'].capitalize()

    def clean_ec_relationship(self):
        return self.cleaned_data['ec_relationship'].capitalize()

    def clean_ec_address(self):
        return self.cleaned_data['ec_address'].capitalize()


Family_ModelFormSet = formset_factory(
    Family_ModelForm,
    extra=0,
    max_num=4,
)
