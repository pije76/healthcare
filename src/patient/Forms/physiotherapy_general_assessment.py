from django import forms
from django.utils.translation import ugettext_lazy as _

from ..models import *
from ..forms import *
from ..lookups import *
from ..choices import *
#from .custom_layout import *
from accounts.models import *

from bootstrap_modal_forms.forms import *


class PhysiotherapyGeneralAssessment_ModelForm(BSModalModelForm):
    class Meta:
        model = PhysiotherapyGeneralAssessment
#       fields = '__all__'
        fields = [
            'patient',
            'doctor_diagnosis',
            'doctor_management',
            'problem',
            'front_body',
            'back_body',
            'pain_scale',
            'comments',
            'special_question',
            'general_health',
            'pmx_surgery',
            'ix_mri_x_ray',
            'medications_steroids',
            'occupation_recreation',
            'palpation',
            'pacemaker_hearing_aid',
            'splinting',
            'physical_examination_movement',
            'muscle_power',
            'functional_activities',
            'special_test',
            'date_time',
            'attending_physiotherapist',
            'current_history',
            'past_history',
            'neurological_reflexes',
            'neurological_motor',
            'neurological_sensation',
            'clearing_test_other_joint',
            'physiotherapists_impression',
            'short_term_goals',
            'long_term_goals',
            'plan_treatment',
        ]
        widgets = {
            'patient': forms.HiddenInput(),
        }

    doctor_diagnosis = forms.CharField(required=False, label="", widget=forms.Textarea(
        attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
    doctor_management = forms.CharField(required=False, label="", widget=forms.Textarea(
        attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
    problem = forms.CharField(required=False, label="", widget=forms.Textarea(
        attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
    front_body = forms.ImageField(required=False, label='', widget=forms.FileInput(
        attrs={'class': "form-control"}))
    back_body = forms.ImageField(required=False, label='', widget=forms.FileInput(
        attrs={'class': "form-control"}))
    pain_scale = forms.ChoiceField(
        required=False, label="", widget=HorizontalRadioSelect(), choices=PAIN_SCALE_CHOICES)
    comments = forms.CharField(required=False, label="", widget=forms.Textarea(
        attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
    special_question = forms.CharField(required=False, label="", widget=forms.Textarea(
        attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
    general_health = forms.CharField(required=False, label="", widget=forms.Textarea(
        attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
    pmx_surgery = forms.CharField(required=False, label="", widget=forms.Textarea(
        attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
    ix_mri_x_ray = forms.CharField(required=False, label="", widget=forms.Textarea(
        attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
    medications_steroids = forms.CharField(required=False, label="", widget=forms.Textarea(
        attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
    occupation_recreation = forms.CharField(required=False, label="", widget=forms.Textarea(
        attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
    palpation = forms.CharField(required=False, label="", widget=forms.Textarea(
        attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
    pacemaker_hearing_aid = forms.CharField(required=False, label="", widget=forms.Textarea(
        attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
    splinting = forms.CharField(required=False, label="", widget=forms.Textarea(
        attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
    physical_examination_movement = forms.ChoiceField(required=False, label="", widget=forms.Select(
        attrs={'class': "form-control"}), choices=PHYSICAL_EXAMINATION_MOVEMENT_CHOICES)
    muscle_power = forms.CharField(required=False, label="", widget=forms.Textarea(
        attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
    functional_activities = forms.CharField(required=False, label="", widget=forms.Textarea(
        attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
    special_test = forms.CharField(required=False, label="", widget=forms.Textarea(
        attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
    date_time = forms.DateTimeField(required=False, label="", initial=timezone.now, input_formats=settings.DATETIME_INPUT_FORMATS,
                                    widget=DateTimePickerInput(format="%d-%m-%Y %H:%M", attrs={'class': "form-control"}))
    attending_physiotherapist = forms.CharField(required=False, label="", widget=forms.Textarea(
        attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
    current_history = forms.CharField(required=False, label="", widget=forms.Textarea(
        attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
    past_history = forms.CharField(required=False, label="", widget=forms.Textarea(
        attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
    neurological_reflexes = forms.CharField(required=False, label=_(
        "Reflexes"), widget=forms.Textarea(attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
    neurological_motor = forms.CharField(required=False, label=_(
        "Motor"), widget=forms.Textarea(attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
    neurological_sensation = forms.CharField(required=False, label=_(
        "Sensation"), widget=forms.Textarea(attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
    clearing_test_other_joint = forms.CharField(required=False, label="", widget=forms.Textarea(
        attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
    physiotherapists_impression = forms.CharField(required=False, label="", widget=forms.Textarea(
        attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
    short_term_goals = forms.CharField(required=False, label="", widget=forms.Textarea(
        attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
    long_term_goals = forms.CharField(required=False, label="", widget=forms.Textarea(
        attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
    plan_treatment = forms.CharField(required=False, label="", widget=forms.Textarea(
        attrs={'class': "form-control", 'rows': 5, 'cols': 10}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.fields['front_body'].label = ''
        self.fields['back_body'].label = ''
        self.helper.layout = Layout(
            InlineRadios('pain_scale')
        )


class PhysiotherapyGeneralAssessment_Form(BSModalForm):

    patient = forms.CharField(required=False, label="", widget=forms.TextInput(
        attrs={'class': "form-control"}))
    doctor_diagnosis = forms.CharField(required=False, label="", widget=forms.Textarea(
        attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
    doctor_management = forms.CharField(required=False, label="", widget=forms.Textarea(
        attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
    problem = forms.CharField(required=False, label="", widget=forms.Textarea(
        attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
    front_body = forms.ImageField(required=False, label='', widget=forms.FileInput(
        attrs={'class': "form-control"}))
    back_body = forms.ImageField(required=False, label='', widget=forms.FileInput(
        attrs={'class': "form-control"}))
    pain_scale = forms.ChoiceField(
        required=False, label="", widget=HorizontalRadioSelect(), choices=PAIN_SCALE_CHOICES)
    comments = forms.CharField(required=False, label="", widget=forms.Textarea(
        attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
    special_question = forms.CharField(required=False, label="", widget=forms.Textarea(
        attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
    general_health = forms.CharField(required=False, label="", widget=forms.Textarea(
        attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
    pmx_surgery = forms.CharField(required=False, label="", widget=forms.Textarea(
        attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
    ix_mri_x_ray = forms.CharField(required=False, label="", widget=forms.Textarea(
        attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
    medications_steroids = forms.CharField(required=False, label="", widget=forms.Textarea(
        attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
    occupation_recreation = forms.CharField(required=False, label="", widget=forms.Textarea(
        attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
    palpation = forms.CharField(required=False, label="", widget=forms.Textarea(
        attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
    pacemaker_hearing_aid = forms.CharField(required=False, label="", widget=forms.Textarea(
        attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
    splinting = forms.CharField(required=False, label="", widget=forms.Textarea(
        attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
    physical_examination_movement = forms.ChoiceField(required=False, label="", widget=forms.Select(
        attrs={'class': "form-control"}), choices=PHYSICAL_EXAMINATION_MOVEMENT_CHOICES)
    muscle_power = forms.CharField(required=False, label="", widget=forms.Textarea(
        attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
    functional_activities = forms.CharField(required=False, label="", widget=forms.Textarea(
        attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
    special_test = forms.CharField(required=False, label="", widget=forms.Textarea(
        attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
    date_time = forms.DateTimeField(required=False, label="", initial=timezone.now, input_formats=settings.DATETIME_INPUT_FORMATS,
                                    widget=DateTimePickerInput(format="%d-%m-%Y %H:%M", attrs={'class': "form-control"}))
    attending_physiotherapist = forms.CharField(required=False, label="", widget=forms.Textarea(
        attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
    current_history = forms.CharField(required=False, label="", widget=forms.Textarea(
        attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
    past_history = forms.CharField(required=False, label="", widget=forms.Textarea(
        attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
    neurological_reflexes = forms.CharField(required=False, label=_(
        "Reflexes"), widget=forms.Textarea(attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
    neurological_motor = forms.CharField(required=False, label=_(
        "Motor"), widget=forms.Textarea(attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
    neurological_sensation = forms.CharField(required=False, label=_(
        "Sensation"), widget=forms.Textarea(attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
    clearing_test_other_joint = forms.CharField(required=False, label="", widget=forms.Textarea(
        attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
    physiotherapists_impression = forms.CharField(required=False, label="", widget=forms.Textarea(
        attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
    short_term_goals = forms.CharField(required=False, label="", widget=forms.Textarea(
        attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
    long_term_goals = forms.CharField(required=False, label="", widget=forms.Textarea(
        attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
    plan_treatment = forms.CharField(required=False, label="", widget=forms.Textarea(
        attrs={'class': "form-control", 'rows': 5, 'cols': 10}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.fields['front_body'].label = ''
        self.fields['back_body'].label = ''
        self.helper.layout = Layout(
            InlineRadios('pain_scale')
        )

    def clean_doctor_diagnosis(self):
        return self.cleaned_data['doctor_diagnosis'].capitalize()

    def clean_doctor_management(self):
        return self.cleaned_data['doctor_management'].capitalize()

    def clean_problem(self):
        return self.cleaned_data['problem'].capitalize()

    def clean_comments(self):
        return self.cleaned_data['comments'].capitalize()

    def clean_special_question(self):
        return self.cleaned_data['special_question'].capitalize()

    def clean_general_health(self):
        return self.cleaned_data['general_health'].capitalize()

    def clean_pmx_surgery(self):
        return self.cleaned_data['pmx_surgery'].capitalize()

    def clean_ix_mri_x_ray(self):
        return self.cleaned_data['ix_mri_x_ray'].capitalize()

    def clean_medications_steroidst(self):
        return self.cleaned_data['medications_steroids'].capitalize()

    def clean_palpation(self):
        return self.cleaned_data['palpation'].capitalize()

    def clean_pacemaker_hearing_aid(self):
        return self.cleaned_data['pacemaker_hearing_aid'].capitalize()

    def clean_splinting(self):
        return self.cleaned_data['splinting'].capitalize()

    def clean_muscle_power(self):
        return self.cleaned_data['muscle_power'].capitalize()

    def clean_functional_activities(self):
        return self.cleaned_data['functional_activities'].capitalize()

    def clean_special_test(self):
        return self.cleaned_data['special_test'].capitalize()

    def clean_attending_physiotherapist(self):
        return self.cleaned_data['attending_physiotherapist'].capitalize()

    def clean_current_history(self):
        return self.cleaned_data['current_history'].capitalize()

    def clean_past_history(self):
        return self.cleaned_data['past_history'].capitalize()

    def clean_neurological_reflexes(self):
        return self.cleaned_data['neurological_reflexes'].capitalize()

    def clean_neurological_motor(self):
        return self.cleaned_data['neurological_motor'].capitalize()

    def clean_neurological_sensation(self):
        return self.cleaned_data['neurological_sensation'].capitalize()

    def clean_clearing_test_other_joint(self):
        return self.cleaned_data['clearing_test_other_joint'].capitalize()

    def clean_physiotherapists_impression(self):
        return self.cleaned_data['physiotherapists_impression'].capitalize()

    def clean_short_term_goals(self):
        return self.cleaned_data['short_term_goals'].capitalize()

    def clean_long_term_goals(self):
        return self.cleaned_data['long_term_goals'].capitalize()

    def clean_plan_treatment(self):
        return self.cleaned_data['plan_treatment'].capitalize()
