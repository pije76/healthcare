from django import forms
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _

from crispy_forms.bootstrap import *
from crispy_forms.helper import *
from crispy_forms.layout import *


from mptt.forms import TreeNodeChoiceField
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput
#from jsignature.forms import JSignatureField
from django_select2.forms import *
from durationwidget.widgets import TimeDurationWidget

from .models import *
from .lookups import *
from accounts.models import *

#import datetime
from datetime import *
messageserror = _("*IC Number format needs to be yymmdd-xx-zzzz.")
#ic_number_validator = RegexValidator("\d{6}\-\d{2}\-\d{4}", "IC Number format needs to be yymmdd-xx-zzzz.")
ic_number_validator = RegexValidator(regex='\d{6}\-\d{2}\-\d{4}', message=messageserror, code="invalid")

now = date.today


def get_now():
	return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


class AdmissionForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.fields['phone'].help_text = _('*Please enter valid phone number with following format: +[country code][area code][phone number]')
		self.fields['ec_phone'].help_text = _('*Please enter valid phone number with following format: +[country code][area code][phone number]')
		self.fields['ec_ic_number'].help_text = _('*IC Number format needs to be yymmdd-xx-zzzz.')

	date = forms.DateField(required=False, label=_("Date:"), initial=now, widget=DatePickerInput(attrs={'class': "form-control"}))
	time = forms.TimeField(required=False, label="Time", initial="00:00", widget=TimePickerInput(format="%H:%M", attrs={'class': "form-control"}))
	admitted = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=ADMITTED_CHOICES)
	mode = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=MODE_CHOICES)

	birth_date = forms.DateField(required=False, label="", initial=now, widget=DatePickerInput(attrs={'class': "form-control"}))
	age = forms.IntegerField(required=False, label="", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	gender = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(attrs={'class': "form-control col-4 tesr"}), choices=GENDER_CHOICES)
	marital_status = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=MARITAL_CHOICES)
	address = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4, 'cols': 15}))
	phone = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	religion = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=RELIGION_CHOICES)
	occupation = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=OCCUPATION_CHOICES)
	communication_sight = forms.ChoiceField(required=False, label=_("Sight:"), widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=COMMUNICATION_SIGHT_CHOICES)
	communication_hearing = forms.ChoiceField(required=False, label=_("Hearing:"), widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=COMMUNICATION_HEARING_CHOICES)
	communication_others = forms.CharField(required=False, label=_("Others:"), widget=forms.TextInput(attrs={'class': "form-control"}))
	ec_name = forms.CharField(required=False, label=_("Name:"), widget=forms.TextInput(attrs={'class': "form-control"}))
	ec_ic_number = forms.CharField(max_length=14, required=False, label=_("IC No:"), widget=forms.TextInput(attrs={'class': "form-control"}))
	ec_relationship = forms.CharField(required=False, label=_("Relationship:"), widget=forms.TextInput(attrs={'class': "form-control"}))
	ec_phone = forms.CharField(required=False, label=_("Contact No:"), widget=forms.TextInput(attrs={'class': "form-control"}))
	ec_address = forms.CharField(required=False, label=_("Address:"), widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4, 'cols': 15}))
	general_condition = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=GENERAL_CONDITION_CHOICES)
	vital_sign_temperature = forms.IntegerField(required=False, label="", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	vital_sign_pulse = forms.IntegerField(required=False, label="", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	vital_sign_bp = forms.IntegerField(required=False, label="", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	vital_sign_resp = forms.IntegerField(required=False, label="", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	vital_sign_spo2 = forms.IntegerField(required=False, label="", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	vital_sign_on_oxygen_therapy = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=BOOLEAN_CHOICES)
	vital_sign_on_oxygen_therapy_flow_rate = forms.IntegerField(required=False, label="", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	vital_sign_hgt = forms.IntegerField(required=False, label="", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	allergy_drug = forms.CharField(required=False, label=_("Drug(s):"), widget=forms.TextInput(attrs={'class': "form-control"}))
	allergy_food = forms.CharField(required=False, label=_("Food:"), widget=forms.TextInput(attrs={'class': "form-control"}))
	allergy_others = forms.CharField(required=False, label=_("Others:"), widget=forms.TextInput(attrs={'class': "form-control"}))
	biohazard_infectious_disease = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=BOOLEAN_CHOICES)
	invasive_line_insitu = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=INVASIVE_LINE_INSITU_CHOICES)
	medical_history = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=MEDICAL_HISTORY_CHOICES)
	surgical_history = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4, 'cols': 15}))
	date_diagnosis = forms.DateField(required=False, label="", initial=now, widget=DatePickerInput(attrs={'class': "form-control"}))
	diagnosis = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4, 'cols': 15}))
	date_operation = forms.DateField(required=False, label="", initial=now, widget=DatePickerInput(attrs={'class': "form-control"}))
	operation = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4, 'cols': 15}))
	own_medication = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=BOOLEAN_CHOICES)
	own_medication_drug_name = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4, 'cols': 15}))
	own_medication_dosage = forms.IntegerField(required=False, label="", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	own_medication_tablet_capsule = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4, 'cols': 15}))
	own_medication_frequency = forms.IntegerField(required=False, label="", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	adaptive_aids_with_patient = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=ADAPTIVE_AIDS_WITH_PATIENT_CHOICES)
	orientation = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(attrs={'class': "form-control"}), choices=ORIENTATION_CHOICES)
	special_information = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	admission_by = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))

	class Meta:
		model = Admission
		fields = '__all__'
		widgets = {
			'patient': forms.HiddenInput(),
		}


class ApplicationForHomeLeaveForm(forms.ModelForm):

	patient = forms.CharField(required=False, label="", initial="patient", widget=forms.TextInput(attrs={'class': "form-control"}))
	patient_family_name = forms.CharField(required=False, label="", initial="name", widget=forms.TextInput(attrs={'class': "form-control"}))
	nric_number = forms.CharField(max_length=14, required=False, label="", initial='yymmdd-xx-zzzz', validators=[ic_number_validator], widget=forms.TextInput(attrs={'class': "form-control"}))
	patient_family_relationship = forms.CharField(required=False, label="", initial="myself/relationship", widget=forms.TextInput(attrs={'class': "form-control"}))
	patient_family_phone = forms.CharField(required=False, label="", initial="+60xxxxxxxx", widget=forms.TextInput(attrs={'class': "form-control"}))
	designation = forms.CharField(required=False, label="", initial="designation", widget=forms.TextInput(attrs={'class': "form-control"}))
	signature = forms.CharField(required=False, label="", initial="signature", widget=forms.TextInput(attrs={'class': "form-control"}))
#    signature = JSignatureField()
	date = forms.DateField(required=False, label="", initial=now, widget=DatePickerInput(attrs={'class': "form-control"}))

	class Meta:
		model = ApplicationForHomeLeave
		fields = '__all__'
		widgets = {
			'patient': forms.HiddenInput(),
		}


class AppointmentForm(forms.ModelForm):

	date = forms.DateField(required=False, label="", initial=now, widget=DatePickerInput(attrs={'class': "form-control"}))
	time = forms.TimeField(required=False, label="", initial="00:00", widget=TimePickerInput(format="%H:%M", attrs={'class': "form-control"}))
	hospital_clinic_center = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4}))
	department = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4}))
	planning_investigation = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4}))
	treatment_order = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4}))

	class Meta:
		model = Appointment
		fields = '__all__'
#		exclude = ['patient']
		widgets = {
			'patient': forms.HiddenInput(),
		}

class CannulationForm(forms.ModelForm):

	nasogastric_tube_date = forms.DateField(required=False, label="", initial=now, widget=DatePickerInput(attrs={'class': "form-control"}))
	nasogastric_tube_size = forms.IntegerField(required=False, label="", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	nasogastric_tube_type = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4}))
	nasogastric_tube_location = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4}))
	nasogastric_tube_due_date = forms.DateField(required=False, label="", initial=now, widget=DatePickerInput(attrs={'class': "form-control"}))
	nasogastric_tube_inserted_by = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	urinary_catheter_date = forms.DateField(required=False, label="", initial=now, widget=DatePickerInput(attrs={'class': "form-control"}))
	urinary_catheter_size = forms.IntegerField(required=False, label="", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	urinary_catheter_type = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4}))
	urinary_catheter_location = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4}))
	urinary_catheter_due_date = forms.DateField(required=False, label="", initial=now, widget=DatePickerInput(attrs={'class': "form-control"}))
	urinary_catheter_inserted_by = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	cannula_date = forms.DateField(required=False, label="", initial=now, widget=DatePickerInput(attrs={'class': "form-control"}))
	cannula_size = forms.IntegerField(required=False, label="", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	cannula_type = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4}))
	cannula_location = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 4}))
	cannula_due_date = forms.DateField(required=False, label="", initial=now, widget=DatePickerInput(attrs={'class': "form-control"}))
	cannula_inserted_by = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))

	class Meta:
		model = CatheterizationCannulation
		fields = '__all__'
		widgets = {
			'patient': forms.HiddenInput(),
		}


class ChargesForm(forms.ModelForm):

	date = forms.DateField(required=False, label="", initial=now, widget=DatePickerInput(attrs={'class': "form-control"}))
	items = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	amount_unit = forms.IntegerField(required=False, label="", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	given_by = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))

	class Meta:
		model = Charges
		fields = '__all__'
		widgets = {
			'patient': forms.HiddenInput(),
		}


class DressingForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.fields['photos'].label = ''

	date = forms.DateField(required=False, label="", initial=now, widget=DatePickerInput(attrs={'class': "form-control"}))
	time = forms.TimeField(required=False, label="", initial="00:00", widget=TimePickerInput(format="%H:%M", attrs={'class': "form-control"}))
	frequency_dressing = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=WOUND_FREQUENCY_CHOICES)
	type_dressing = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	wound_location = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=WOUND_LOCATION_CHOICES)
	wound_condition = TreeNodeChoiceField(required=False, label="", queryset=WoundCondition.objects, widget=forms.Select(attrs={'class': "form-control"}),)
	photos = forms.FileInput()
	done_by = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))

	class Meta:
		model = Dressing
		fields = '__all__'
		widgets = {
			'patient': forms.HiddenInput(),
		}


class EnteralFeedingRegimeForm(forms.ModelForm):

	date = forms.DateField(required=False, label="", initial=now, widget=DatePickerInput(attrs={'class': "form-control"}))
	time = forms.TimeField(required=False, label="", initial="00:00", widget=TimePickerInput(format="%H:%M", attrs={'class': "form-control"}))
	type_of_milk = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	amount = forms.IntegerField(required=False, label="", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	warm_water_before = forms.IntegerField(required=False, label="", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control calc"}))
	warm_water_after = forms.IntegerField(required=False, label="", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control calc"}))

	class Meta:
		model = EnteralFeedingRegime
		fields = '__all__'
		widgets = {
			'patient': forms.HiddenInput(),
		}


class HGTChartForm(forms.ModelForm):

	date = forms.DateField(required=False, label="", initial=now, widget=DatePickerInput(attrs={'class': "form-control"}))
	time = forms.TimeField(required=False, label="", initial="00:00", widget=TimePickerInput(format="%H:%M", attrs={'class': "form-control"}))
	blood_glucose_reading = forms.IntegerField(required=False, label="", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	remark = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	done_by = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))

	class Meta:
		model = HGTChart
		fields = '__all__'
		widgets = {
			'patient': forms.HiddenInput(),
		}


class IntakeOutputChartForm(forms.ModelForm):

	date = forms.DateField(required=False, label="", initial=now, widget=DatePickerInput(attrs={'class': "form-control"}))
	time_intake = forms.TimeField(required=False, label="", initial="00:00", widget=TimePickerInput(format="%H:%M", attrs={'class': "form-control"}))
	intake_oral_type = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	intake_oral_ml = forms.IntegerField(required=False, label="", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	intake_parenteral_type = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	intake_parenteral_ml = forms.IntegerField(required=False, label="", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	intake_other_type = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	intake_other_ml = forms.IntegerField(required=False, label="", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	time_output = forms.TimeField(required=False, label="", initial="00:00", widget=TimePickerInput(format="%H:%M", attrs={'class': "form-control"}))
	output_urine_ml = forms.IntegerField(required=False, label="", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	output_urine_cum = forms.IntegerField(required=False, label="", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	output_gastric_ml = forms.IntegerField(required=False, label="", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	output_other_type = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	output_other_ml = forms.IntegerField(required=False, label="", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))

	class Meta:
		model = IntakeOutputChart
		fields = '__all__'
		widgets = {
			'patient': forms.HiddenInput(),
		}


class MaintainanceForm(forms.ModelForm):

	date = forms.DateField(required=False, label="", initial=now, widget=DatePickerInput(attrs={'class': "form-control"}))
	items = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	location_room = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	reported_by = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	status = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=STATUS_CHOICES)

	class Meta:
		model = Maintainance
		fields = '__all__'
		widgets = {
			'patient': forms.HiddenInput(),
		}


class MedicationAdministrationRecordForm(forms.ModelForm):

	allergy = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	medication_name = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	medication_dosage = forms.IntegerField(required=False, label="", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	medication_tab = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=TAB_CHOICES)
	medication_frequency = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=MEDICATION_ADMINISTRATION_FREQUENCY_CHOICES)
	medication_route = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=ROUTE_CHOICES)
	medication_date = forms.DateField(required=False, label="", initial=now, widget=DatePickerInput(attrs={'class': "form-control"}))
	medication_time = forms.TimeField(required=False, label="", initial="00:00", widget=TimePickerInput(format="%H:%M", attrs={'class': "form-control"}))
	medication_date_time = forms.DateTimeField(required=False, label="", initial=get_now, input_formats=['%d-%m-%Y %H:%M'], widget=DatePickerInput(format="%d-%m-%Y %H:%M", attrs={'class': 'form-control'}))
	signature_nurse = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=SIGNATURE_CHOICES)
	stat = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=MEDICATION_ADMINISTRATION_STAT_CHOICES)
	date_time = forms.DateTimeField(required=False, label="", initial=get_now, input_formats=['%d-%m-%Y %H:%M'], widget=DatePickerInput(format="%d-%m-%Y %H:%M", attrs={'class': 'form-control'}))
	given_by = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))

	class Meta:
		model = MedicationAdministrationRecord
		fields = '__all__'
		widgets = {
			'patient': forms.HiddenInput(),
		}


class MedicationRecordForm(forms.ModelForm):

	date = forms.DateField(required=False, label="", initial=now, widget=DatePickerInput(attrs={'class': "form-control"}))
	time = forms.TimeField(required=False, label="", initial="00:00", widget=TimePickerInput(format="%H:%M", attrs={'class': "form-control"}))
	medication = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	dosage = forms.IntegerField(required=False, label="", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	topup = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	balance = forms.IntegerField(required=False, label="", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	remark = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	staff = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))

	class Meta:
		model = MedicationRecord
		fields = '__all__'
		widgets = {
			'patient': forms.HiddenInput(),
		}


class MiscellaneousChargesSlipForm(forms.ModelForm):

	date = forms.DateField(required=False, label="", initial=now, widget=DatePickerInput(attrs={'class': "form-control"}))
	items_procedures = forms.CharField(required=False, label="", initial="I'm still confused about this", widget=forms.TextInput(attrs={'class': "form-control"}))
	amount_unit = forms.IntegerField(required=False, label="", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	given_by = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))

	class Meta:
		model = MiscellaneousChargesSlip
		fields = '__all__'
		widgets = {
			'patient': forms.HiddenInput(),
		}


class NursingForm(forms.ModelForm):

	date_time = forms.DateTimeField(required=False, label="", initial=get_now, input_formats=['%d-%m-%Y %H:%M'], widget=DatePickerInput(format="%d-%m-%Y %H:%M", attrs={'class': 'form-control'}))
	report = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 6, 'cols': 15}))

	class Meta:
		model = Nursing
		fields = '__all__'
		widgets = {
			'patient': forms.HiddenInput(),
		}


class OvertimeClaimForm(forms.ModelForm):

	date = forms.DateField(required=False, label="", initial=now, widget=DatePickerInput(attrs={'class': "form-control"}))
	duration_time = forms.DurationField(required=False, label="", initial="00:00:00", widget=TimeDurationWidget(show_days=False, show_hours=True, show_minutes=True, show_seconds=False))
	hours = forms.TimeField(required=False, label="", initial="00:00", widget=TimePickerInput(format="%H:%M", attrs={'class': "form-control"}))
	checked_sign_by = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	verify_by = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'class': "form-control"}))

	class Meta:
		model = OvertimeClaim
		fields = '__all__'
		widgets = {
			'patient': forms.HiddenInput(),
		}


class PhysioProgressNoteForm(forms.ModelForm):

	report = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 6, 'cols': 15}))

	class Meta:
		model = PhysioProgressNote
		fields = '__all__'
		widgets = {
			'patient': forms.HiddenInput(),
		}


class PhysiotherapyGeneralAssessmentForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		helper = FormHelper()
		helper.layout = Layout(
			InlineRadios('pain_scale')
		)

	doctor_diagnosis = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
	doctor_management = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
	problem = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
	pain_scale = forms.ChoiceField(required=False, label="", widget=forms.RadioSelect(), choices=PAIN_SCALE_CHOICES)
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
	date_time = forms.DateTimeField(required=False, label="", initial=get_now, input_formats=['%d-%m-%Y %H:%M'], widget=DatePickerInput(format="%d-%m-%Y %H:%M", attrs={'class': 'form-control'}))
	attending_physiotherapist = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
	current_history = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
	past_history = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
	neurological = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=NEUROLOGICAL_CHOICES)
	clearing_test_other_joint = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
	physiotherapists_impression = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
	short_term_goals = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
	long_term_goals = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 5, 'cols': 10}))
	plan_treatment = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control", 'rows': 5, 'cols': 10}))

	class Meta:
		model = PhysiotherapyGeneralAssessment
		fields = '__all__'
		widgets = {
			'patient': forms.HiddenInput(),
		}


class StaffRecordsForm(forms.ModelForm):

	annual_leave_days = forms.IntegerField(required=False, label="", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	public_holiday_days = forms.IntegerField(required=False, label="", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	replacement_public_holiday = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	medical_certificate = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	siri_no_diagnosis = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	emergency_leaves = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	emergency_leaves_reasons = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	unpaid_leaves = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	unpaid_leaves_reasons = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))

	class Meta:
		model = StaffRecords
		fields = '__all__'
		widgets = {
			'patient': forms.HiddenInput(),
		}


class StoolForm(forms.ModelForm):

	date = forms.DateField(required=False, label="", initial=now, widget=DatePickerInput(attrs={'class': "form-control"}))
	time = forms.TimeField(required=False, label="", initial="00:00", widget=TimePickerInput(format="%H:%M", attrs={'class': "form-control"}))
	frequency = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=STOOL_FREQUENCY_CHOICES)
	consistency = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=CONSISTENCY_CHOICES)
	amount = forms.ChoiceField(required=False, label="", widget=forms.Select(attrs={'class': "form-control"}), choices=AMOUNT_CHOICES)
	remark = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	name = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))

	class Meta:
		model = Stool
		fields = '__all__'
		widgets = {
			'patient': forms.HiddenInput(),
		}


class VisitingConsultantForm(forms.ModelForm):

	date_time = forms.DateTimeField(required=False, label="", initial=get_now, input_formats=['%d-%m-%Y %H:%M'], widget=DatePickerInput(format="%d-%m-%Y %H:%M", attrs={'class': 'form-control'}))
	complaints = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	treatment_orders = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	consultant = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))

	class Meta:
		model = VisitingConsultant
		fields = '__all__'
		widgets = {
			'patient': forms.HiddenInput(),
		}


class VitalSignFlowForm(forms.ModelForm):

	date = forms.DateField(required=False, label="", initial=now, widget=DatePickerInput(attrs={'class': "form-control"}))
	time = forms.TimeField(required=False, label="", initial="00:00", widget=TimePickerInput(format="%H:%M", attrs={'class': "form-control"}))
	temp = forms.IntegerField(required=False, label="", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	pulse = forms.IntegerField(required=False, label="", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	blood_pressure_systolic = forms.IntegerField(required=False, label="", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	blood_pressure_diastolic = forms.IntegerField(required=False, label="", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	respiration = forms.IntegerField(required=False, label="", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	spo2_percentage = forms.IntegerField(required=False, label="", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	spo2_o2 = forms.IntegerField(required=False, label="", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	hgt_liter = forms.IntegerField(required=False, label="", min_value=0, widget=forms.NumberInput(attrs={'class': "form-control"}))
	hgt_remarks = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))

	class Meta:
		model = VitalSignFlow
		fields = '__all__'
		widgets = {
			'patient': forms.HiddenInput(),
		}
