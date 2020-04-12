from django import forms
from django.conf import settings

from crispy_forms.bootstrap import Field, InlineRadios, TabHolder, Tab
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, Fieldset, Field

from .models import *


MODE_CHOICES = (
    ('ambulance', 'Ambulance'),
    ('own', 'Own Transport'),
)

GENDER_CHOICES = (
    ('male', 'Male'),
    ('female', 'Female'),
)

MARITAL_CHOICES = (
    ('single', 'Single'),
    ('married', 'Married'),
    ('divorced', 'Divorced'),
)

RELIGION_CHOICES = (
    ('islam', 'Islam'),
    ('buddhism', 'Buddhism'),
    ('christianity', 'Christianity'),
    ('hinduism', 'Hinduism'),
    ('chinese', 'Traditional Chinese'),
)

WOUND_CHOICES = (
    ('od', 'OD'),
    ('pd', 'PD'),
)


class CustomCheckbox(Field):
    template = 'checkbox.html'


class AdmissionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AdmissionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal checkbox-inline'
        self.helper.label_class = 'col-lg-3'
        self.helper.field_class = 'col-lg-8 modeku'
        self.helper.layout = Layout(
            #   CustomCheckbox('mode'),
            #   Submit('submit', 'Sign in'),
            Field('modeku', css_class="modeku")
        )

    class Meta:
        model = Admission
        fields = '__all__'

    date = forms.DateField(required=False, label="Date:", widget=forms.DateInput(attrs={'class': "form-control dateku", 'type': "date"}))
    time = forms.CharField(required=False, label="Time:", widget=forms.TextInput(attrs={'class': "form-control"}))
    mode = forms.MultipleChoiceField(required=False, label="", widget=forms.CheckboxSelectMultiple(attrs={'class': "form-control"}), choices=MODE_CHOICES)
    full_name = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    ic_number = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    birth_date = forms.DateField(required=False, label="", widget=forms.DateInput(attrs={'class': "form-control", 'type': "date"}))
    age = forms.IntegerField(required=False, label="", widget=forms.NumberInput(attrs={'class': "form-control"}))
    gender = forms.ChoiceField(required=False, label="", widget=forms.CheckboxSelectMultiple(attrs={'class': "form-control"}), choices=GENDER_CHOICES)
    marital_status = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=MARITAL_CHOICES)
    address = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4, 'cols': 15}))
    phone = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    religion = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=RELIGION_CHOICES)
    occupation = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    ec_name = forms.CharField(required=False, label="Name:", widget=forms.TextInput(attrs={'class': "form-control"}))
    ec_ic_number = forms.CharField(required=False, label="IC No:", widget=forms.TextInput(attrs={'class': "form-control"}))
    ec_relationship = forms.CharField(required=False, label="Relationship:", widget=forms.TextInput(attrs={'class': "form-control"}))
    ec_phone = forms.CharField(required=False, label="Tel No:", widget=forms.TextInput(attrs={'class': "form-control"}))
    ec_address = forms.CharField(required=False, label="Address:", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4, 'cols': 15}))
    general_condition = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    temperature = forms.IntegerField(required=False, label="", widget=forms.NumberInput(attrs={'class': "form-control"}))
    pulse = forms.IntegerField(required=False, label="", widget=forms.NumberInput(attrs={'class': "form-control"}))
    BP = forms.IntegerField(required=False, label="", widget=forms.NumberInput(attrs={'class': "form-control"}))
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


class ApplicationForHomeLeaveForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ApplicationForHomeLeaveForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal checkbox-inline'
        self.helper.label_class = 'col-lg-3'
        self.helper.field_class = 'col-lg-7'

    class Meta:
        model = ApplicationForHomeLeave
        fields = '__all__'

    full_name = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    ic_number = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    date_time_of_appointment = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    hospital_clinic = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4, 'cols': 15}))
    treatment_order = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))


class AppointmentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

    class Meta:
        model = Appointment
        fields = '__all__'

    full_name = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    ic_number = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    appointment = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4}))
    hospital_clinic = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4}))
    treatment_order = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4}))


class CannulationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CannulationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

    class Meta:
        model = Cannulation
        fields = '__all__'

    full_name = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    ic_number = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    date_time = forms.DateField(required=False, label="", widget=forms.DateInput(attrs={'class': "form-control", 'type': "date"}))
    cannula_cbd_ryles_tube = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4}))
    due_date = forms.DateField(required=False, label="", widget=forms.DateInput(attrs={'class': "form-control", 'type': "date"}))
    done_by = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))


class ChargesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ChargesForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

    class Meta:
        model = Charges
        fields = '__all__'

    full_name = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    ic_number = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    date = forms.DateField(required=False, label="", widget=forms.DateInput(attrs={'class': "form-control", 'type': "date"}))
    items = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    amount_unit = forms.IntegerField(required=False, label="", widget=forms.NumberInput(attrs={'class': "form-control"}))
    given_by = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))


class DressingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DressingForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

    class Meta:
        model = Dressing
        fields = '__all__'

    full_name = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    ic_number = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    date = forms.DateField(required=False, label="", widget=forms.DateInput(attrs={'class': "form-control", 'type': "date"}))
    time = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    frequency = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=WOUND_CHOICES)
    wound_condition = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    wound_location = forms.CharField(required=False, label="", widget=forms.FileInput(attrs={'class': "form-control"}))
    done_by = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))


class EnteralFeedingRegineForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EnteralFeedingRegineForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

    class Meta:
        model = EnteralFeedingRegine
        fields = '__all__'

    full_name = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    ic_number = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    date = forms.DateField(required=False, label="", widget=forms.DateInput(attrs={'class': "form-control", 'type': "date"}))
    time = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    type_of_milk = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    amount = forms.IntegerField(required=False, label="", widget=forms.NumberInput(attrs={'class': "form-control"}))


class HGTChartForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(HGTChartForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

    class Meta:
        model = HGTChart
        fields = '__all__'

    full_name = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    ic_number = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    date = forms.DateField(required=False, label="", widget=forms.DateInput(attrs={'class': "form-control", 'type': "date"}))
    time = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    blood_glucose_reading = forms.IntegerField(required=False, label="", widget=forms.NumberInput(attrs={'class': "form-control"}))
    remark = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    done_by = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))


class IntakeOutputChartForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(IntakeOutputChartForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

    class Meta:
        model = IntakeOutputChart
        fields = '__all__'

    full_name = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    ic_number = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    date = forms.DateField(required=False, label="", widget=forms.DateInput(attrs={'class': "form-control", 'type': "date"}))
    time = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    type_frequency_of_dressing = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    wound_condition = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    photo = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    done_by = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))


class MaintainanceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MaintainanceForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

    class Meta:
        model = Maintainance
        fields = '__all__'

    full_name = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    ic_number = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    date = forms.DateField(required=False, label="", widget=forms.DateInput(attrs={'class': "form-control", 'type': "date"}))
    items = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    location_room = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    remark = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    staff_name = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))


class MedicationAdministrationRecordForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MedicationAdministrationRecordForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

    class Meta:
        model = MedicationAdministrationRecord
        fields = '__all__'

    full_name = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    ic_number = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    date = forms.DateField(required=False, label="", widget=forms.DateInput(attrs={'class': "form-control", 'type': "date"}))
    items = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    location_room = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    remark = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    staff_name = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))


class MedicationRecordForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MedicationRecordForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

    class Meta:
        model = MedicationRecord
        fields = '__all__'

    full_name = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    ic_number = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    date = forms.DateField(required=False, label="", widget=forms.DateInput(attrs={'class': "form-control", 'type': "date"}))
    time = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    medication = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    tablet = forms.IntegerField(required=False, label="", widget=forms.NumberInput(attrs={'class': "form-control"}))
    dosage = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    frequency = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    topup = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    balance = forms.IntegerField(required=False, label="", widget=forms.NumberInput(attrs={'class': "form-control"}))
    remark = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    staff = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))


class NursingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(NursingForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

    class Meta:
        model = Nursing
        fields = '__all__'

    full_name = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    ic_number = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    date = forms.DateField(required=False, label="", widget=forms.DateInput(attrs={'class': "form-control", 'type': "date"}))
    time = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    medication = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    tablet = forms.IntegerField(required=False, label="", widget=forms.NumberInput(attrs={'class': "form-control"}))
    dosage = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    frequency = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    topup = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    balance = forms.IntegerField(required=False, label="", widget=forms.NumberInput(attrs={'class': "form-control"}))
    remark = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    staff = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))


class PhysioProgressNoteBackForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PhysioProgressNoteBackForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

    class Meta:
        model = PhysioProgressNoteBack
        fields = '__all__'

    full_name = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    ic_number = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    date = forms.DateField(required=False, label="", widget=forms.DateInput(attrs={'class': "form-control", 'type': "date"}))
    time = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    medication = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    tablet = forms.IntegerField(required=False, label="", widget=forms.NumberInput(attrs={'class': "form-control"}))
    dosage = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    frequency = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    topup = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    balance = forms.IntegerField(required=False, label="", widget=forms.NumberInput(attrs={'class': "form-control"}))
    remark = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    staff = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))


class PhysioProgressNoteFrontForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PhysioProgressNoteFrontForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

    class Meta:
        model = PhysioProgressNoteFront
        fields = '__all__'

    full_name = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    ic_number = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    date = forms.DateField(required=False, label="", widget=forms.DateInput(attrs={'class': "form-control", 'type': "date"}))
    time = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    medication = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    tablet = forms.IntegerField(required=False, label="", widget=forms.NumberInput(attrs={'class': "form-control"}))
    dosage = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    frequency = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    topup = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    balance = forms.IntegerField(required=False, label="", widget=forms.NumberInput(attrs={'class': "form-control"}))
    remark = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    staff = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))


class PhysiotherapyGeneralAssessmentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PhysiotherapyGeneralAssessmentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

    class Meta:
        model = PhysiotherapyGeneralAssessment
        fields = '__all__'

    full_name = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    ic_number = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    date = forms.DateField(required=False, label="", widget=forms.DateInput(attrs={'class': "form-control", 'type': "date"}))
    time = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    medication = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    tablet = forms.IntegerField(required=False, label="", widget=forms.NumberInput(attrs={'class': "form-control"}))
    dosage = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    frequency = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    topup = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    balance = forms.IntegerField(required=False, label="", widget=forms.NumberInput(attrs={'class': "form-control"}))
    remark = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    staff = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))


class StoolForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(StoolForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

    class Meta:
        model = Stool
        fields = '__all__'

    full_name = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    ic_number = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    date = forms.DateField(required=False, label="", widget=forms.DateInput(attrs={'class': "form-control", 'type': "date"}))
    time = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    frequency = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    consistency = forms.IntegerField(required=False, label="", widget=forms.NumberInput(attrs={'class': "form-control"}))
    amount = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    remark = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    name = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))


class VitalSignFlowForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(VitalSignFlowForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

    class Meta:
        model = VitalSignFlow
        fields = '__all__'

    full_name = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    ic_number = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    date = forms.DateField(required=False, label="", widget=forms.DateInput(attrs={'class': "form-control", 'type': "date"}))
    time = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    temp = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    pulse = forms.IntegerField(required=False, label="", widget=forms.NumberInput(attrs={'class': "form-control"}))
    blood_pressure = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    respiration = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
    spo2 = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))

