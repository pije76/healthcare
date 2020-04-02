from django import forms
from django.conf import settings

from crispy_forms.bootstrap import Field, InlineRadios, TabHolder, Tab
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, Fieldset, Field

from .models import *


class CustomCheckbox(Field):
    template = 'checkbox.html'


class AdmissionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AdmissionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal checkbox-inline'
        self.helper.label_class = 'col-lg-3'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(
            CustomCheckbox('mode'),
            Submit('submit', 'Sign in')
        )

    class Meta:
        model = Admission
        fields = '__all__'

    date = forms.DateField(required=False, label="Date:", widget=forms.DateInput(attrs={'class': "form-control", 'type': "date"}))
    time = forms.CharField(required=False, label="Time:", widget=forms.TextInput(attrs={'class': "form-control"}))
    mode = forms.MultipleChoiceField(required=False, label="", widget=forms.CheckboxSelectMultiple(attrs={'class': "form-control"}), choices=MODE_CHOICES)
    full_name = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    ic_number = forms.IntegerField(required=False, label="", widget=forms.NumberInput(attrs={'class': "form-control"}))
    birth_date = forms.DateField(required=False, label="", widget=forms.DateInput(attrs={'class': "form-control", 'type': "date"}))
    age = forms.IntegerField(required=False, label="", widget=forms.NumberInput(attrs={'class': "form-control"}))
    gender = forms.ChoiceField(required=False, label="", widget=forms.CheckboxSelectMultiple(attrs={'class': "form-control"}), choices=GENDER_CHOICES)
    marital_status = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    address = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4, 'cols': 15}))
    phone = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    religion = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    occupation = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    ec_name = forms.CharField(required=False, label="Name:", widget=forms.TextInput(attrs={'class': "form-control"}))
    ec_ic_number = forms.CharField(required=False, label="IC No:", widget=forms.TextInput(attrs={'class': "form-control"}))
    ec_relationship = forms.CharField(required=False, label="Relationship:", widget=forms.TextInput(attrs={'class': "form-control"}))
    ec_phone = forms.CharField(required=False, label="Tel No:", widget=forms.TextInput(attrs={'class': "form-control"}))
    ec_address = forms.CharField(required=False, label="Address:", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4, 'cols': 15}))
    general_condition = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    temperature = forms.IntegerField(required=False, label="", widget=forms.NumberInput(attrs={'class': "form-control"}))
    pulse = forms.IntegerField(required=False, label="", widget=forms.NumberInput(attrs={'class': "form-control"}))
    BP = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    resp = forms.IntegerField(required=False, label="", widget=forms.NumberInput(attrs={'class': "form-control"}))
    spo2 = forms.IntegerField(required=False, label="", widget=forms.NumberInput(attrs={'class': "form-control"}))
    medication = forms.CharField(required=False, label="Medication:", widget=forms.TextInput(attrs={'class': "form-control"}))
    food = forms.CharField(required=False, label="Food:", widget=forms.TextInput(attrs={'class': "form-control"}))
    others = forms.CharField(required=False, label="Others:", widget=forms.TextInput(attrs={'class': "form-control"}))
    biohazard_infectious_disease = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    medical_history = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4, 'cols': 15}))
    surgical_history = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4, 'cols': 15}))
    diagnosis = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4, 'cols': 15}))
    own_medication = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4, 'cols': 15}))
    denture = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    admission_by = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    date_discharge = forms.DateField(required=False, label="", widget=forms.DateInput(attrs={'class': "form-control", 'type': "date"}))

    def as_p(self):
        return self._html_output(
            normal_row='<br />%(html_class_attr)s%(label)s %(field)s',
            error_row='%s',
            row_ender='</p>',
            help_text_html=' <span class="helptext">%s</span>',
            errors_on_separate_row=False)


class AppointmentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal checkbox-inline'
        self.helper.label_class = 'col-lg-3'
        self.helper.field_class = 'col-lg-7'
        self.helper.layout = Layout(
            CustomCheckbox('mode'),
            Submit('submit', 'Sign in')
        )

    class Meta:
        model = Admission
        fields = '__all__'

    full_name = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    ic_number = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    date_time_of_appointment = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    hospital_clinic = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4, 'cols': 15}))
    treatment_order = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))

    def as_p(self):
        return self._html_output(
            normal_row='<br />%(html_class_attr)s%(label)s %(field)s',
            error_row='%s',
            row_ender='</p>',
            help_text_html=' <span class="helptext">%s</span>',
            errors_on_separate_row=False)
