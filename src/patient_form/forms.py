from django import forms
from django.core.validators import RegexValidator
from django.contrib.admin.widgets import AdminDateWidget
from django.shortcuts import get_list_or_404, get_object_or_404

from crispy_forms.helper import FormHelper
from crispy_forms import layout, bootstrap
from crispy_forms.bootstrap import InlineField, FormActions, StrictButton, Div
from crispy_forms.layout import Layout

from jsignature.forms import JSignatureField

from django_select2.forms import *
from ajax_select import make_ajax_field

from .models import *
from .lookups import *
from accounts.models import *

import datetime

ic_number_validator = RegexValidator("\d{6}\-\d{2}\-\d{4}", "IC Number format needs to be yymmdd-xx-zzzz.")

now = datetime.date.today


ADMITTED_CHOICES = (
	('hospital', 'Hospital'),
	('home', 'Home'),
	('others', 'Others'),
)

MODE_CHOICES = (
	('walked-in', 'Walked-in'),
	('wheel-chair', 'Wheelchair'),
	('stretcher', 'Stretcher'),
)

GENDER_CHOICES = (
	('male', 'Male'),
	('female', 'Female'),
)

MARITAL_CHOICES = (
	('single', 'Single'),
	('married', 'Married'),
	('others', 'Others'),
)

RELIGION_CHOICES = (
	('buddhist', 'Buddhist'),
	('christian', 'Christian'),
	('hinduism', 'Hinduism'),
	('islam', 'Islam'),
	('others', 'Others'),
)

OCCUPATION_CHOICES = (
	('retired', 'Retired'),
	('housewife', 'Housewife'),
	('others', 'Others'),
)

COMMUNICATION_SIGHT_CHOICES = (
	('good', 'Good'),
	('poor', 'Poor'),
	('glasses', 'Glasses'),
	('blind', 'Blind'),
)

COMMUNICATION_HEARING_CHOICES = (
	('good', 'Good'),
	('poor', 'Poor'),
	('aid', 'Aid'),
)

GENERAL_CONDITION_CHOICES = (
	('stable', 'Stable'),
	('ill', 'Ill'),
	('lethargic', 'Lethargic'),
	('weak', 'Weak'),
	('cachexic', 'Cachexic'),
	('coma', 'Coma'),
	('restless', 'Restless'),
	('depress', 'Depress'),
	('agitated', 'Agitated'),
)

INVASIVE_LINE_INSITU_CHOICES = (
	('none', 'None'),
	('ett', 'ETT'),
	('nasogastric_tube', 'Nasogastric tube'),
	('urinary_catheter', 'Urinary catheter'),
	('pacemaker', 'Pacemaker'),
	('others', 'Others'),
)

MEDICAL_HISTORY_CHOICES = (
	('no_chronic_illness', 'NO Chronic Illness'),
	('asthma', 'Asthma'),
	('diabetes_mellitus', 'Diabetes Mellitus'),
	('hypertension', 'Hypertension'),
	('heart_disease', 'Heart Disease'),
	('others', 'Others'),
)

ADAPTIVE_AIDS_WITH_PATIENT_CHOICES = (
	('denture', 'Denture'),
	('upper_set', 'Upper set'),
	('lower_set', 'Lower set'),
	('walking_aid', 'Walking aid'),
	('hearing_aid', 'Hearing aid'),
	('glasses', 'Glasses'),
	('others', 'Others'),
)

ORIENTATION_CHOICES = (
	('nurse_call_system', 'Nurse call system'),
	('bed_mechanic', 'Bed Mechanic'),
	('bathroom', 'Bathroom'),
	('visiting_hours', 'Visiting hours'),
	('care_of_valuables', 'Care of Valuables'),
	('fire_exits', 'Fire Exits'),
	('no_smoking_policy', 'No Smoking policy'),
	('patient_right_responsibilities', 'Patient Right/ Responsibilities'),
	('inform_nurse_if_patient_leaving_the_center', 'Inform nurse if patient leaving the center'),
)

WOUND_LOCATION_CHOICES = (
	('head', 'Head'),
	('face', 'Face'),
	('neck', 'Neck'),
	('chest', 'Chest'),
	('abdomen', 'Abdomen'),
	('back', 'Back'),
	('sacral', 'Sacral'),
	('buttock', 'Buttock'),
	('hand', 'Hand'),
	('leg', 'Leg'),
	('others', 'Others'),
)

WOUND_CONDITION_CHOICES = (
	('clean', 'Clean'),
	('slough', 'Slough'),
	('eschar', 'Eschar'),
	('Others', (
		('Exudate', (
			('sanguineous', 'Sanguineous'),
			('serous', 'Serous'),
			('haemoserous', 'Haemoserous'),
			('purulent', 'Purulent'),
		)),
		('Amount', (
			('scant', 'Scant'),
			('minimal', 'Minimal'),
			('moderate', 'Moderate'),
			('large', 'Large'),
		)),
	)),
)

PHYSICAL_EXAMINATION_MOVEMENT_CHOICES = (
	('joint', 'Joint'),
	('active', 'Active'),
	('passive', 'Passive'),
)

STATUS_CHOICES = (
	('-', '-'),
	('done', 'Done'),
	('pending', 'Pending'),
	('cancel', 'Cancel'),
)

NEUROLOGICAL_CHOICES = (
	('reflexes', 'Reflexes'),
	('motor', 'Motor'),
	('sensation', 'Sensation'),
)

FREQUENCY_CHOICES = (
	('-', '-'),
	('bo', 'BO'),
	('bno', 'BNO'),
)

CONSISTENCY_CHOICES = (
	('-', '-'),
	('normal', 'Normal'),
	('hard', 'Hard'),
	('loose', 'Loose'),
	('watery', 'Watery'),
)

AMOUNT_CHOICES = (
	('-', '-'),
	('scanty', 'Scanty'),
	('minimal', 'Minimal'),
	('moderate', 'Moderate'),
	('large', 'Large'),
)


PAIN_SCALE_CHOICES = (
	('1', '1'),
	('2', '2'),
	('3', '3'),
	('4', '4'),
	('5', '5'),
	('6', '6'),
	('7', '7'),
	('8', '8'),
	('9', '9'),
	('10', '10'),
)


class AdmissionForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_class = 'form-horizontal checkbox-inline'
		self.helper.label_class = 'col-lg-3'
		self.helper.field_class = 'col-lg-8'

	def clean_ic_number(self):
		ic_number = self.cleaned_data['ic_number']
		try:
			ic_number = Admission.objects.get(ic_number=ic_number)
		except Admission.DoesNotExist:
			return ic_number
		raise forms.ValidationError('%s already exists' % ic_number)

	class Meta:
		model = Admission
		exclude = ('full_name',)

	date = forms.DateField(required=False, label="Date:", initial=now, widget=forms.DateInput(attrs={'class': "form-control dateku", 'type': "date"}))
	time = forms.TimeField(required=False, label="Time:", widget=forms.TimeInput(attrs={'class': "form-control"}))
	admitted = forms.MultipleChoiceField(required=False, label="", widget=forms.CheckboxSelectMultiple(attrs={'class': "form-control"}), choices=ADMITTED_CHOICES)
	mode = forms.MultipleChoiceField(required=False, label="", widget=forms.CheckboxSelectMultiple(attrs={'class': "form-control"}), choices=MODE_CHOICES)
	full_name = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	ic_number = forms.CharField(max_length=14, required=False, label="", initial='yymmdd-xx-zzzz', validators=[ic_number_validator], widget=forms.TextInput(attrs={'class': "form-control"}))
	birth_date = forms.DateField(required=False, label="", initial=now, widget=forms.DateInput(attrs={'class': "form-control", 'type': "date"}))
	age = forms.IntegerField(required=False, label="", widget=forms.NumberInput(attrs={'class': "form-control"}))
	gender = forms.MultipleChoiceField(required=False, label="", widget=forms.CheckboxSelectMultiple(attrs={'class': "form-control"}), choices=GENDER_CHOICES)
	marital_status = forms.MultipleChoiceField(required=False, label="", widget=forms.CheckboxSelectMultiple(attrs={'class': "form-control"}), choices=MARITAL_CHOICES)
	address = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4, 'cols': 15}))
	phone = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	religion = forms.MultipleChoiceField(required=False, label="", widget=forms.CheckboxSelectMultiple(attrs={'class': "form-control"}), choices=RELIGION_CHOICES)
	occupation = forms.MultipleChoiceField(required=False, label="", widget=forms.CheckboxSelectMultiple(attrs={'class': "form-control"}), choices=OCCUPATION_CHOICES)
	communication_sight = forms.MultipleChoiceField(required=False, label="Sight:", widget=forms.CheckboxSelectMultiple(attrs={'class': "form-control"}), choices=COMMUNICATION_SIGHT_CHOICES)
	communication_hearing = forms.MultipleChoiceField(required=False, label="Hearing:", widget=forms.CheckboxSelectMultiple(attrs={'class': "form-control"}), choices=COMMUNICATION_HEARING_CHOICES)
	communication_others = forms.CharField(required=False, label="Others:", widget=forms.TextInput(attrs={'class': "form-control"}))
	ec_name = forms.CharField(required=False, label="Name:", widget=forms.TextInput(attrs={'class': "form-control"}))
	ec_ic_number = forms.CharField(required=False, label="IC No:", validators=[ic_number_validator], widget=forms.TextInput(attrs={'class': "form-control"}))
	ec_relationship = forms.CharField(required=False, label="Relationship:", widget=forms.TextInput(attrs={'class': "form-control"}))
	ec_phone = forms.CharField(required=False, label="Contact No:", widget=forms.TextInput(attrs={'class': "form-control"}))
	ec_address = forms.CharField(required=False, label="Address:", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4, 'cols': 15}))

#    general_condition = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4, 'cols': 15}))
	general_condition = forms.MultipleChoiceField(required=False, label="", widget=forms.CheckboxSelectMultiple(attrs={'class': "form-control"}), choices=GENERAL_CONDITION_CHOICES)
	vital_sign_temperature = forms.IntegerField(required=False, label="", widget=forms.NumberInput(attrs={'class': "form-control"}))
	vital_sign_pulse = forms.IntegerField(required=False, label="", widget=forms.NumberInput(attrs={'class': "form-control"}))
	vital_sign_bp = forms.IntegerField(required=False, label="", widget=forms.NumberInput(attrs={'class': "form-control"}))
	vital_sign_resp = forms.IntegerField(required=False, label="", widget=forms.NumberInput(attrs={'class': "form-control"}))
	vital_sign_spo2 = forms.IntegerField(required=False, label="", widget=forms.NumberInput(attrs={'class': "form-control"}))
	vital_sign_on_oxygen_therapy = forms.IntegerField(required=False, label="", widget=forms.NumberInput(attrs={'class': "form-control"}))
	vital_sign_hgt = forms.IntegerField(required=False, label="", widget=forms.NumberInput(attrs={'class': "form-control"}))
	allergy_drug = forms.CharField(required=False, label="Drug(s):", widget=forms.TextInput(attrs={'class': "form-control"}))
	allergy_food = forms.CharField(required=False, label="Food:", widget=forms.TextInput(attrs={'class': "form-control"}))
	allergy_others = forms.CharField(required=False, label="Others:", widget=forms.TextInput(attrs={'class': "form-control"}))
	biohazard_infectious_disease = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4, 'cols': 15}))
	invasive_line_insitu = forms.MultipleChoiceField(required=False, label="", widget=forms.CheckboxSelectMultiple(attrs={'class': "form-control"}), choices=INVASIVE_LINE_INSITU_CHOICES)
	medical_history = forms.MultipleChoiceField(required=False, label="", widget=forms.CheckboxSelectMultiple(attrs={'class': "form-control"}), choices=MEDICAL_HISTORY_CHOICES)
	surgical_history = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4, 'cols': 15}))
	date_diagnosis = forms.DateField(required=False, label="", initial=now, widget=forms.DateInput(attrs={'class': "form-control", 'type': "date"}))
	diagnosis = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4, 'cols': 15}))
	date_operation = forms.DateField(required=False, label="", initial=now, widget=forms.DateInput(attrs={'class': "form-control", 'type': "date"}))
	operation = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4, 'cols': 15}))
	own_medication = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=INVASIVE_LINE_INSITU_CHOICES)
	own_medication_drug_name = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4, 'cols': 15}))
	own_medication_dosage = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4, 'cols': 15}))
	own_medication_tablet_capsule = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4, 'cols': 15}))
	own_medication_frequency = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4, 'cols': 15}))
	adaptive_aids_with_patient = forms.MultipleChoiceField(required=False, label="", widget=forms.CheckboxSelectMultiple(attrs={'class': "form-control"}), choices=ADAPTIVE_AIDS_WITH_PATIENT_CHOICES)
	orientation = forms.MultipleChoiceField(required=False, label="", widget=forms.CheckboxSelectMultiple(attrs={'class': "form-control"}), choices=ORIENTATION_CHOICES)
	special_information = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	admission_by = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))


class ApplicationForHomeLeaveForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(ApplicationForHomeLeaveForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.fields['ic_number'].queryset = Admission.objects.none()
		self.fields['nric_number'].queryset = Admission.objects.none()

		if 'full_name' in self.data:
			try:
				full_name = int(self.data.get('full_name'))
				self.fields['ic_number'].queryset = Admission.objects.filter(full_name=full_name).order_by('full_name')
			except (ValueError, TypeError):
				pass

		if 'full_name' in self.data:
			try:
				full_name = int(self.data.get('full_name'))
				self.fields['nric_number'].queryset = Admission.objects.filter(full_name=full_name).order_by('full_name')
			except (ValueError, TypeError):
				pass

	class Meta:
		model = ApplicationForHomeLeave
		fields = ('full_name', 'ic_number', 'patient_family_name', 'nric_number', 'patient_family_relationship', 'patient_family_phone', 'designation', 'signature', 'date')

	full_name = make_ajax_field(Appointment, 'full_name', 'full_name', required=True, label='', show_help_text=False, help_text=u'*Type & choose a full name of Patient')
	ic_number = forms.CharField(required=True, label="", widget=forms.Select(attrs={'class': "form-control"}))
	patient_family_name = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	nric_number = forms.CharField(max_length=14, required=False, label="", initial='yymmdd-xx-zzzz', validators=[ic_number_validator], widget=forms.TextInput(attrs={'class': "form-control"}))
	patient_family_relationship = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	patient_family_phone = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	designation = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	signature = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
#    signature = JSignatureField()
	date = forms.DateField(required=False, label="", initial=now, widget=forms.DateInput(attrs={'class': "form-control", 'type': "date"}))


class AppointmentForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.fields['ic_number'].queryset = Admission.objects.none()

		if 'full_name' in self.data:
			try:
				full_name = int(self.data.get('full_name'))
				self.fields['ic_number'].queryset = Admission.objects.filter(full_name=full_name).order_by('full_name')
			except (ValueError, TypeError):
				pass

	class Meta:
		model = Appointment
		fields = ('full_name', 'ic_number', 'date', 'time', 'hospital_clinic_center', 'department', 'planning_investigation', 'treatment_order')

	full_name = make_ajax_field(Appointment, 'full_name', 'full_name', required=True, label='', show_help_text=False, help_text=u'*Type & choose a full name')
	ic_number = forms.CharField(required=True, label="", widget=forms.Select(attrs={'class': "form-control"}))
	date = forms.DateField(required=False, label="", initial=now, widget=forms.DateInput(attrs={'class': "form-control dateku", 'type': "date"}))
	time = forms.TimeField(required=False, label="", widget=forms.TimeInput(attrs={'class': "form-control"}))
	hospital_clinic_center = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4}))
	department = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4}))
	planning_investigation = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4}))
	treatment_order = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4}))


class CannulationForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.fields['ic_number'].queryset = Admission.objects.none()

		if 'full_name' in self.data:
			try:
				full_name = int(self.data.get('full_name'))
				self.fields['ic_number'].queryset = Admission.objects.filter(full_name=full_name).order_by('full_name')
			except (ValueError, TypeError):
				pass

	class Meta:
		model = Cannulation
		fields = ('full_name', 'ic_number', 'nasogastric_tube_date', 'nasogastric_tube_size', 'nasogastric_tube_type', 'nasogastric_tube_location', 'nasogastric_tube_due_date', 'urinary_catheter_inserted_by', 'urinary_catheter_date', 'urinary_catheter_size', 'urinary_catheter_type', 'urinary_catheter_location', 'urinary_catheter_due_date', 'urinary_catheter_inserted_by', 'urinary_catheter_date', 'urinary_catheter_size', 'urinary_catheter_type', 'urinary_catheter_location', 'urinary_catheter_due_date', 'urinary_catheter_inserted_by')

	full_name = make_ajax_field(Appointment, 'full_name', 'full_name', required=True, label='', show_help_text=False, help_text=u'*Type & choose a full name')
	ic_number = forms.CharField(required=True, label="", widget=forms.Select(attrs={'class': "form-control"}))
	nasogastric_tube_date = forms.DateField(required=False, label="", initial=now, widget=forms.DateInput(attrs={'class': "form-control", 'type': "date"}))
	nasogastric_tube_size = forms.IntegerField(required=False, label="", widget=forms.NumberInput(attrs={'class': "form-control"}))
	nasogastric_tube_type = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4}))
	nasogastric_tube_location = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4}))
	nasogastric_tube_due_date = forms.DateField(required=False, label="", initial=now, widget=forms.DateInput(attrs={'class': "form-control", 'type': "date"}))
	nasogastric_tube_inserted_by = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	urinary_catheter_date = forms.DateField(required=False, label="", initial=now, widget=forms.DateInput(attrs={'class': "form-control", 'type': "date"}))
	urinary_catheter_size = forms.IntegerField(required=False, label="", widget=forms.NumberInput(attrs={'class': "form-control"}))
	urinary_catheter_type = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4}))
	urinary_catheter_location = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4}))
	urinary_catheter_due_date = forms.DateField(required=False, label="", initial=now, widget=forms.DateInput(attrs={'class': "form-control", 'type': "date"}))
	urinary_catheter_inserted_by = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	urinary_catheter_date = forms.DateField(required=False, label="", initial=now, widget=forms.DateInput(attrs={'class': "form-control", 'type': "date"}))
	urinary_catheter_size = forms.IntegerField(required=False, label="", widget=forms.NumberInput(attrs={'class': "form-control"}))
	urinary_catheter_type = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4}))
	urinary_catheter_location = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4}))
	urinary_catheter_due_date = forms.DateField(required=False, label="", initial=now, widget=forms.DateInput(attrs={'class': "form-control", 'type': "date"}))
	urinary_catheter_inserted_by = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))


class ChargesForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.fields['ic_number'].queryset = Admission.objects.none()

		if 'full_name' in self.data:
			try:
				full_name = int(self.data.get('full_name'))
				self.fields['ic_number'].queryset = Admission.objects.filter(full_name=full_name).order_by('full_name')
			except (ValueError, TypeError):
				pass

	class Meta:
		model = Charges
		fields = '__all__'

	full_name = make_ajax_field(Appointment, 'full_name', 'full_name', required=True, label='', show_help_text=False, help_text=u'*Type & choose a full name')
	ic_number = forms.CharField(required=True, label="", widget=forms.Select(attrs={'class': "form-control"}))
	date = forms.DateField(required=False, label="", initial=now, widget=forms.DateInput(attrs={'class': "form-control", 'type': "date"}))
	items = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	amount_unit = forms.IntegerField(required=False, label="", widget=forms.NumberInput(attrs={'class': "form-control"}))
	given_by = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))


class DressingForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(DressingForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.fields['ic_number'].queryset = Admission.objects.none()

		if 'full_name' in self.data:
			try:
				full_name = int(self.data.get('full_name'))
				self.fields['ic_number'].queryset = Admission.objects.filter(full_name=full_name).order_by('full_name')
			except (ValueError, TypeError):
				pass

	class Meta:
		model = Dressing
		fields = '__all__'

	full_name = make_ajax_field(Appointment, 'full_name', 'full_name', required=True, label='', show_help_text=False, help_text=u'*Type & choose a full name')
	ic_number = forms.CharField(required=True, label="", widget=forms.Select(attrs={'class': "form-control"}))
	date = forms.DateField(required=False, label="", initial=now, widget=forms.DateInput(attrs={'class': "form-control", 'type': "date"}))
	time = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	frequency_dressing = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=WOUND_FREQUENCY_CHOICES)
	type_dressing = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	wound_location = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=WOUND_LOCATION_CHOICES)
#    wound_condition = forms.ModelChoiceField(required=False, label="", queryset=Dressing.objects, widget=forms.Select(attrs={'class': "form-control"}),)
	wound_condition = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=WOUND_CONDITION_CHOICES)
	images = forms.CharField(required=False, label="", widget=forms.FileInput(attrs={'class': "form-control"}))
	done_by = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))


class EnteralFeedingRegimeForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(EnteralFeedingRegimeForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.fields['ic_number'].queryset = Admission.objects.none()

		if 'full_name' in self.data:
			try:
				full_name = int(self.data.get('full_name'))
				self.fields['ic_number'].queryset = Admission.objects.filter(full_name=full_name).order_by('full_name')
			except (ValueError, TypeError):
				pass

	class Meta:
		model = EnteralFeedingRegime
		fields = '__all__'

	full_name = make_ajax_field(Appointment, 'full_name', 'full_name', required=True, label='', show_help_text=False, help_text=u'*Type & choose a full name')
	ic_number = forms.CharField(required=True, label="", widget=forms.Select(attrs={'class': "form-control"}))
	date = forms.DateField(required=False, label="", initial=now, widget=forms.DateInput(attrs={'class': "form-control", 'type': "date"}))
	time = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	type_of_milk = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	amount = forms.IntegerField(required=False, label="", widget=forms.NumberInput(attrs={'class': "form-control"}))
	warm_water_before = forms.IntegerField(required=False, label="", widget=forms.NumberInput(attrs={'class': "form-control"}))
	warm_water_after = forms.IntegerField(required=False, label="", widget=forms.NumberInput(attrs={'class': "form-control"}))


class HGTChartForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(HGTChartForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.fields['ic_number'].queryset = Admission.objects.none()

		if 'full_name' in self.data:
			try:
				full_name = int(self.data.get('full_name'))
				self.fields['ic_number'].queryset = Admission.objects.filter(full_name=full_name).order_by('full_name')
			except (ValueError, TypeError):
				pass

	class Meta:
		model = HGTChart
		fields = '__all__'

	full_name = make_ajax_field(Appointment, 'full_name', 'full_name', required=True, label='', show_help_text=False, help_text=u'*Type & choose a full name')
	ic_number = forms.CharField(required=True, label="", widget=forms.Select(attrs={'class': "form-control"}))
	date = forms.DateField(required=False, label="", initial=now, widget=forms.DateInput(attrs={'class': "form-control", 'type': "date"}))
	time = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	blood_glucose_reading = forms.IntegerField(required=False, label="", widget=forms.NumberInput(attrs={'class': "form-control"}))
	remark = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	done_by = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))


class IntakeOutputChartForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(IntakeOutputChartForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.fields['ic_number'].queryset = Admission.objects.none()

		if 'full_name' in self.data:
			try:
				full_name = int(self.data.get('full_name'))
				self.fields['ic_number'].queryset = Admission.objects.filter(full_name=full_name).order_by('full_name')
			except (ValueError, TypeError):
				pass

	class Meta:
		model = IntakeOutputChart
		fields = '__all__'

	full_name = make_ajax_field(Appointment, 'full_name', 'full_name', required=True, label='', show_help_text=False, help_text=u'*Type & choose a full name')
	ic_number = forms.CharField(required=True, label="", widget=forms.Select(attrs={'class': "form-control"}))
	date = forms.DateField(required=False, label="", initial=now, widget=forms.DateInput(attrs={'class': "form-control", 'type': "date"}))
	time = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	intake_oral_type = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	intake_oral_ml = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	intake_parenteral_type = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	intake_parenteral_ml = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	intake_other_type = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	intake_other_ml = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	urine_ml = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	urine_cumtotal = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	urine_gastric_ml = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	other_type = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	other_ml = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))


class MaintainanceForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(MaintainanceForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.fields['ic_number'].queryset = Admission.objects.none()

		if 'full_name' in self.data:
			try:
				full_name = int(self.data.get('full_name'))
				self.fields['ic_number'].queryset = Admission.objects.filter(full_name=full_name).order_by('full_name')
			except (ValueError, TypeError):
				pass

	class Meta:
		model = Maintainance
		fields = '__all__'

	full_name = make_ajax_field(Appointment, 'full_name', 'full_name', required=True, label='', show_help_text=False, help_text=u'*Type & choose a full name')
	ic_number = forms.CharField(required=True, label="", widget=forms.Select(attrs={'class': "form-control"}))
	date = forms.DateField(required=False, label="", initial=now, widget=forms.DateInput(attrs={'class': "form-control", 'type': "date"}))
	items = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control"}))
	location_room = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	reported_by = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	status = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=STATUS_CHOICES)


class MedicationAdministrationRecordForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(MedicationAdministrationRecordForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.fields['ic_number'].queryset = Admission.objects.none()

		if 'full_name' in self.data:
			try:
				full_name = int(self.data.get('full_name'))
				self.fields['ic_number'].queryset = Admission.objects.filter(full_name=full_name).order_by('full_name')
			except (ValueError, TypeError):
				pass

	class Meta:
		model = MedicationAdministrationRecord
		fields = '__all__'

	full_name = make_ajax_field(Appointment, 'full_name', 'full_name', required=True, label='', show_help_text=False, help_text=u'*Type & choose a full name')
	ic_number = forms.CharField(required=True, label="", widget=forms.Select(attrs={'class': "form-control"}))
	allergy = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	time = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	route = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	stat = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	date = forms.DateField(required=False, label="", initial=now, widget=forms.DateInput(attrs={'class': "form-control", 'type': "date"}))
	given_by = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))


class MedicationRecordForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(MedicationRecordForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.fields['ic_number'].queryset = Admission.objects.none()

		if 'full_name' in self.data:
			try:
				full_name = int(self.data.get('full_name'))
				self.fields['ic_number'].queryset = Admission.objects.filter(full_name=full_name).order_by('full_name')
			except (ValueError, TypeError):
				pass

	class Meta:
		model = MedicationRecord
		fields = '__all__'

	full_name = make_ajax_field(Appointment, 'full_name', 'full_name', required=True, label='', show_help_text=False, help_text=u'*Type & choose a full name')
	ic_number = forms.CharField(required=True, label="", widget=forms.Select(attrs={'class': "form-control"}))
	date = forms.DateField(required=False, label="", initial=now, widget=forms.DateInput(attrs={'class': "form-control", 'type': "date"}))
	time = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	medication = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	dosage = forms.IntegerField(required=False, label="", widget=forms.NumberInput(attrs={'class': "form-control"}))
	topup = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	balance = forms.IntegerField(required=False, label="", widget=forms.NumberInput(attrs={'class': "form-control"}))
	remark = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	staff = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))


class MiscellaneousChargesSlipForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(MiscellaneousChargesSlipForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.fields['ic_number'].queryset = Admission.objects.none()

		if 'full_name' in self.data:
			try:
				full_name = int(self.data.get('full_name'))
				self.fields['ic_number'].queryset = Admission.objects.filter(full_name=full_name).order_by('full_name')
			except (ValueError, TypeError):
				pass

	class Meta:
		model = MiscellaneousChargesSlip
		fields = '__all__'

	full_name = make_ajax_field(Appointment, 'full_name', 'full_name', required=True, label='', show_help_text=False, help_text=u'*Type & choose a full name')
	ic_number = forms.CharField(required=True, label="", widget=forms.Select(attrs={'class': "form-control"}))
	date = forms.DateField(required=False, label="", initial=now, widget=forms.DateInput(attrs={'class': "form-control", 'type': "date"}))
	items_procedures = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	amount_unit = forms.IntegerField(required=False, label="", widget=forms.NumberInput(attrs={'class': "form-control"}))
	given_by = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))


class NursingForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(NursingForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.fields['ic_number'].queryset = Admission.objects.none()

		if 'full_name' in self.data:
			try:
				full_name = int(self.data.get('full_name'))
				self.fields['ic_number'].queryset = Admission.objects.filter(full_name=full_name).order_by('full_name')
			except (ValueError, TypeError):
				pass

	class Meta:
		model = Nursing
		fields = '__all__'

	full_name = make_ajax_field(Appointment, 'full_name', 'full_name', required=True, label='', show_help_text=False, help_text=u'*Type & choose a full name')
	ic_number = forms.CharField(required=True, label="", widget=forms.Select(attrs={'class': "form-control"}))
	date_time = forms.DateField(required=False, label="", initial=now, widget=forms.DateInput(attrs={'class': "form-control", 'type': "date"}))
	report = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 6, 'cols': 15}))


class OvertimeClaimForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(OvertimeClaimForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.fields['ic_number'].queryset = Admission.objects.none()

		if 'full_name' in self.data:
			try:
				full_name = int(self.data.get('full_name'))
				self.fields['ic_number'].queryset = Admission.objects.filter(full_name=full_name).order_by('full_name')
			except (ValueError, TypeError):
				pass

	class Meta:
		model = Nursing
		fields = '__all__'

	full_name = make_ajax_field(Appointment, 'full_name', 'full_name', required=True, label='', show_help_text=False, help_text=u'*Type & choose a full name')
	ic_number = forms.CharField(required=True, label="", widget=forms.Select(attrs={'class': "form-control"}))
	date = forms.DateField(required=False, label="", initial=now, widget=forms.DateInput(attrs={'class': "form-control", 'type': "date"}))
	duration_time = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control", 'rows': 6, 'cols': 15}))
	hours = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control", 'rows': 6, 'cols': 15}))


class PhysioProgressNoteForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(PhysioProgressNoteForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.fields['ic_number'].queryset = Admission.objects.none()

		if 'full_name' in self.data:
			try:
				full_name = int(self.data.get('full_name'))
				self.fields['ic_number'].queryset = Admission.objects.filter(full_name=full_name).order_by('full_name')
			except (ValueError, TypeError):
				pass

	class Meta:
		model = PhysioProgressNote
		fields = '__all__'

	full_name = make_ajax_field(Appointment, 'full_name', 'full_name', required=True, label='', show_help_text=False, help_text=u'*Type & choose a full name')
	ic_number = forms.CharField(required=True, label="", widget=forms.Select(attrs={'class': "form-control"}))
	report = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 6, 'cols': 15}))


class PhysiotherapyGeneralAssessmentForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(PhysiotherapyGeneralAssessmentForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.fields['ic_number'].queryset = Admission.objects.none()

		if 'full_name' in self.data:
			try:
				full_name = int(self.data.get('full_name'))
				self.fields['ic_number'].queryset = Admission.objects.filter(full_name=full_name).order_by('full_name')
			except (ValueError, TypeError):
				pass

	class Meta:
		model = PhysiotherapyGeneralAssessment
		fields = '__all__'

	full_name = make_ajax_field(Appointment, 'full_name', 'full_name', required=True, label='', show_help_text=False, help_text=u'*Type & choose a full name')
	ic_number = forms.CharField(required=True, label="", widget=forms.Select(attrs={'class': "form-control"}))
	doctor_diagnosis = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
	doctor_management = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
	problem = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
	pain_scale = forms.MultipleChoiceField(required=False, label="", widget=forms.CheckboxSelectMultiple(attrs={'class': "form-control"}), choices=PAIN_SCALE_CHOICES)
	comments = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
	special_question = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
	general_health = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
	pmx_surgery = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
	ix_mri_x_ray = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
	medications_steroids = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
	occupation_recreation = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
	palpation = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
	pacemaker_hearing_aid = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
	splinting = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
	physical_examination_movement = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=PHYSICAL_EXAMINATION_MOVEMENT_CHOICES)
	muscle_power = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
	functional_activities = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
	special_test = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
	date_time = forms.DateField(required=False, label="", initial=now, widget=forms.DateInput(attrs={'class': "form-control", 'type': "date"}))
	attending_physiotherapist = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 5, 'cols': 10}))

	current_history = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
	past_history = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
	neurological = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=NEUROLOGICAL_CHOICES)
	clearing_test_other_joint = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
	physiotherapists_impression = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
	short_term_goals = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
	long_term_goals = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
	plan_treatment = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 5, 'cols': 10}))


class StaffRecordsForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(StaffRecordsForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.fields['ic_number'].queryset = Admission.objects.none()

		if 'full_name' in self.data:
			try:
				full_name = int(self.data.get('full_name'))
				self.fields['ic_number'].queryset = Admission.objects.filter(full_name=full_name).order_by('full_name')
			except (ValueError, TypeError):
				pass

	class Meta:
		model = StaffRecords
		fields = '__all__'

	full_name = make_ajax_field(Appointment, 'full_name', 'full_name', required=True, label='', show_help_text=False, help_text=u'*Type & choose a full name')
	ic_number = forms.CharField(required=True, label="", widget=forms.Select(attrs={'class': "form-control"}))
	annual_leave_days = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	public_holiday_days = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	replacement_public_holiday = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	medical_certificate = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	siri_no_diagnosis = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	emergency_leaves = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	emergency_leaves_reasons = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	unpaid_leaves = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	unpaid_leaves_reasons = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))


class StoolForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(StoolForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.fields['ic_number'].queryset = Admission.objects.none()

		if 'full_name' in self.data:
			try:
				full_name = int(self.data.get('full_name'))
				self.fields['ic_number'].queryset = Admission.objects.filter(full_name=full_name).order_by('full_name')
			except (ValueError, TypeError):
				pass

	class Meta:
		model = Stool
		fields = '__all__'

	full_name = make_ajax_field(Appointment, 'full_name', 'full_name', required=True, label='', show_help_text=False, help_text=u'*Type & choose a full name')
	ic_number = forms.CharField(required=True, label="", widget=forms.Select(attrs={'class': "form-control"}))
	date = forms.DateField(required=False, label="", initial=now, widget=forms.DateInput(attrs={'class': "form-control", 'type': "date"}))
	time = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	frequency = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=FREQUENCY_CHOICES)
	consistency = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=CONSISTENCY_CHOICES)
	amount = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=AMOUNT_CHOICES)
	remark = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	name = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))


class VisitingConsultantForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(VisitingConsultantForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.fields['ic_number'].queryset = Admission.objects.none()

		if 'full_name' in self.data:
			try:
				full_name = int(self.data.get('full_name'))
				self.fields['ic_number'].queryset = Admission.objects.filter(full_name=full_name).order_by('full_name')
			except (ValueError, TypeError):
				pass

	class Meta:
		model = VisitingConsultant
		fields = '__all__'

	full_name = make_ajax_field(Appointment, 'full_name', 'full_name', required=True, label='', show_help_text=False, help_text=u'*Type & choose a full name')
	ic_number = forms.CharField(required=True, label="", widget=forms.Select(attrs={'class': "form-control"}))
	date_time = forms.DateField(required=False, label="", initial=now, widget=forms.DateInput(attrs={'class': "form-control", 'type': "date"}))
	complaints = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	treatment_orders = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	consultant = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))


class VitalSignFlowForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(VitalSignFlowForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.fields['ic_number'].queryset = Admission.objects.none()

		if 'full_name' in self.data:
			try:
				full_name = int(self.data.get('full_name'))
				self.fields['ic_number'].queryset = Admission.objects.filter(full_name=full_name).order_by('full_name')
			except (ValueError, TypeError):
				pass

	class Meta:
		model = VitalSignFlow
		fields = '__all__'

	full_name = make_ajax_field(Appointment, 'full_name', 'full_name', required=True, label='', show_help_text=False, help_text=u'*Type & choose a full name')
	ic_number = forms.CharField(required=True, label="", widget=forms.Select(attrs={'class': "form-control"}))
	date = forms.DateField(required=False, label="", initial=now, widget=forms.DateInput(attrs={'class': "form-control", 'type': "date"}))
	time = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	temp = forms.IntegerField(required=False, label="", widget=forms.NumberInput(attrs={'class': "form-control"}))
	pulse = forms.IntegerField(required=False, label="", widget=forms.NumberInput(attrs={'class': "form-control"}))
	blood_pressure_systolic = forms.IntegerField(required=False, label="", widget=forms.NumberInput(attrs={'class': "form-control"}))
	blood_pressure_diastolic = forms.IntegerField(required=False, label="", widget=forms.NumberInput(attrs={'class': "form-control"}))
	respiration = forms.IntegerField(required=False, label="", widget=forms.NumberInput(attrs={'class': "form-control"}))
	spo2_percentage = forms.IntegerField(required=False, label="", widget=forms.NumberInput(attrs={'class': "form-control"}))
	spo2_o2 = forms.IntegerField(required=False, label="", widget=forms.NumberInput(attrs={'class': "form-control"}))
	hgt_liter = forms.IntegerField(required=False, label="", widget=forms.NumberInput(attrs={'class': "form-control"}))
	hgt_remarks = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
