from django.db import models
from django.core.validators import RegexValidator
from django.utils.safestring import mark_safe

from jsignature.mixins import JSignatureFieldsMixin

from accounts.models import *

#from select2 import fields

#import select2

WOUND_FREQUENCY_CHOICES = (
	('od', 'OD'),
	('bd', 'BD'),
	('tds', 'TDS'),
	('stat', 'STAT'),
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
            ('serous', 'Seroous'),
        )),
        ('Amount', (
            ('exudate', 'Scant'),
            ('amount', 'Minimal'),
        )),
    )),
)

PHYSICAL_EXAMINATION_MOVEMENT_CHOICES = (
	('joint', 'Joint'),
	('active', 'Active'),
	('passive', 'Passive'),
)

NEUROLOGICAL_CHOICES = (
	('reflexes', 'Reflexes'),
	('motor', 'Motor'),
	('sensation', 'Sensation'),
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

ic_number_validator = RegexValidator("\d{6}\-\d{2}\-\d{4}", "IC Number format needs to be yymmdd-xx-zzzz.")


class Admission(models.Model):
	full_name = models.OneToOneField(PatientProfile, on_delete=models.CASCADE, null=True, blank=False)
	ic_number = models.CharField(max_length=14, validators=[ic_number_validator], unique=True, null=True, blank=True)
	date = models.DateTimeField(null=True, blank=True)
	time = models.TimeField("Time Admission", null=True, blank=True)
	admitted = models.CharField(max_length=255, null=True, blank=True)
	mode = models.CharField(max_length=255, null=True, blank=True)
	birth_date = models.DateTimeField(null=True, blank=True)
	age = models.IntegerField(null=True, blank=True)
	gender = models.CharField(max_length=255, null=True, blank=True)
	marital_status = models.CharField(max_length=255, null=True, blank=True)
	phone = models.CharField(max_length=255, null=True, blank=True)
	religion = models.CharField(max_length=255, null=True, blank=True)
	occupation = models.CharField(max_length=255, null=True, blank=True)
	communication_sight = models.CharField(max_length=255, null=True, blank=True)
	communication_hearing = models.CharField(max_length=255, null=True, blank=True)
	communication_others = models.CharField(max_length=255, null=True, blank=True)
	address = models.CharField(max_length=255, null=True, blank=True)
	ec_name = models.CharField('Name', max_length=255, null=True, blank=True)
	ec_ic_number = models.CharField('IC Number', max_length=14, null=True, blank=True)
	ec_relationship = models.CharField('Relationship', max_length=255, null=True, blank=True)
	ec_phone = models.CharField('Contact Number', max_length=255, null=True, blank=True)
	ec_address = models.CharField('Address', max_length=255, null=True, blank=True)

	general_condition = models.CharField(max_length=255, null=True, blank=True)
	vital_sign_temperature = models.CharField(max_length=255, null=True, blank=True)
	vital_sign_pulse = models.IntegerField(null=True, blank=True)
	vital_sign_bp = models.IntegerField(null=True, blank=True)
	vital_sign_resp = models.IntegerField(null=True, blank=True)
	vital_sign_spo2 = models.IntegerField(null=True, blank=True)
	vital_sign_on_oxygen_therapy = models.BooleanField(default=False, blank=True,)
	vital_sign_hgt = models.IntegerField(null=True, blank=True)
	allergy_drug = models.CharField(max_length=255, null=True, blank=True)
	allergy_food = models.CharField(max_length=255, null=True, blank=True)
	allergy_others = models.CharField(max_length=255, null=True, blank=True)
	biohazard_infectious_disease = models.CharField(max_length=255, null=True, blank=True)
	invasive_line_insitu = models.CharField(max_length=255, null=True, blank=True)
	medical_history = models.CharField(max_length=255, null=True, blank=True)
	surgical_history = models.CharField(max_length=255, null=True, blank=True)
	date_diagnosis = models.DateTimeField(null=True, blank=True)
	diagnosis = models.CharField(max_length=255, null=True, blank=True)
	date_operation = models.DateTimeField(null=True, blank=True)
	operation = models.CharField(max_length=255, null=True, blank=True)
	own_medication = models.BooleanField(default=False, blank=True,)
	own_medication_drug_name = models.CharField(max_length=255, null=True, blank=True)
	own_medication_dosage = models.CharField(max_length=255, null=True, blank=True)
	own_medication_tablet_capsule = models.CharField(max_length=255, null=True, blank=True)
	own_medication_frequency = models.CharField(max_length=255, null=True, blank=True)
	adaptive_aids_with_patient = models.CharField(max_length=255, null=True, blank=True)
	orientation = models.CharField(max_length=255, null=True, blank=True)
	special_information = models.CharField(max_length=255, null=True, blank=True)
	admission_by = models.CharField(max_length=255, null=True, blank=True)

	class Meta:
		verbose_name = 'Admission'
		verbose_name_plural = "Admission"

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		if self.mode:
			self.mode = eval(self.mode)
		if self.gender:
			self.gender = eval(self.gender)

	def __str__(self):
		return str(self.ic_number)

	@property
	def get_full_name(self):
		return str(self.full_name.full_name)

#    def get_ic_number(self):
#        return str(self.full_name.ic_number)

	class Meta:
		verbose_name = 'Admission'
		verbose_name_plural = "Admission"


class ApplicationForHomeLeave(models.Model):
	full_name = models.OneToOneField(PatientProfile, on_delete=models.CASCADE, null=True, blank=False)
	ic_number = models.OneToOneField(Admission, on_delete=models.CASCADE, null=True, blank=False)
	patient_family_name = models.CharField(max_length=255, blank=True)
	nric_number = models.CharField('NRIC Number', validators=[ic_number_validator], max_length=14, blank=False)
	patient_family_relationship = models.CharField(max_length=255, blank=True)
	patient_family_phone = models.CharField(max_length=255, blank=True)
	designation = models.CharField(max_length=255, blank=True)
	signature = models.CharField(max_length=255, blank=True)
	date = models.DateField()

	def __str__(self):
		return str(self.patient)

	class Meta:
		verbose_name = 'Application For Home Home Leave'
		verbose_name_plural = "Application For Home Home Leave"


class Appointment(models.Model):
	full_name = models.OneToOneField(PatientProfile, on_delete=models.CASCADE, null=True, blank=False)
	ic_number = models.OneToOneField(Admission, on_delete=models.CASCADE, null=True, blank=False)
	date = models.DateField()
	time = models.CharField(max_length=255, blank=True)
	hospital_clinic_center = models.CharField(max_length=255, blank=True)
	department = models.CharField(max_length=255, blank=True)
	planning_investigation = models.CharField(max_length=255, blank=True)
	treatment_order = models.CharField(max_length=255, blank=True)

	def __str__(self):
		return str(self.full_name)

	class Meta:
		verbose_name = 'Appointment'
		verbose_name_plural = "Appointment"


class Cannulation(models.Model):
	full_name = models.OneToOneField(PatientProfile, on_delete=models.CASCADE, null=True, blank=False)
	ic_number = models.OneToOneField(Admission, on_delete=models.CASCADE, null=True, blank=False)
	nasogastric_tube_date = models.DateField()
	nasogastric_tube_size = models.IntegerField(blank=True)
	nasogastric_tube_type = models.CharField(max_length=255, blank=True)
	nasogastric_tube_location = models.CharField(max_length=255, blank=True)
	nasogastric_tube_due_date = models.DateField()
	nasogastric_tube_inserted_by = models.CharField(max_length=255, blank=True)
	urinary_catheter_date = models.DateField()
	urinary_catheter_size = models.IntegerField(blank=True)
	urinary_catheter_type = models.CharField(max_length=255, blank=True)
	urinary_catheter_location = models.CharField(max_length=255, blank=True)
	urinary_catheter_due_date = models.DateField()
	urinary_catheter_inserted_by = models.CharField(max_length=255, blank=True)
	cannula_date = models.DateField()
	cannula_size = models.IntegerField(blank=True)
	cannula_type = models.CharField(max_length=255, blank=True)
	cannula_location = models.CharField(max_length=255, blank=True)
	cannula_due_date = models.DateField()
	cannula_inserted_by = models.CharField(max_length=255, blank=True)

	def __str__(self):
		return str(self.ic_number)

	class Meta:
		verbose_name = 'Catheterization And Cannulation'
		verbose_name_plural = "Catheterization And Cannulation"


class Charges(models.Model):
	full_name = models.OneToOneField(PatientProfile, on_delete=models.CASCADE, null=True, blank=False)
	ic_number = models.OneToOneField(Admission, on_delete=models.CASCADE, null=True, blank=False)
	date = models.DateField()
	items = models.CharField(max_length=255, blank=True)
	amount_unit = models.IntegerField(blank=False)
	given_by = models.CharField(max_length=255, blank=True)

	def __str__(self):
		return str(self.ic_number)

	class Meta:
		verbose_name = 'Charges'
		verbose_name_plural = "Charges"


def upload_path(instance, filename):
	return '{0}/{1}'.format('dressing_location', filename)


class WoundCondition(models.Model):
	name = models.CharField(max_length=255, blank=True, null=True)
	parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)

	def __str__(self):
		return self.name


class Dressing(models.Model):
	full_name = models.OneToOneField(PatientProfile, on_delete=models.CASCADE, null=True, blank=False)
	ic_number = models.OneToOneField(Admission, on_delete=models.CASCADE, null=True, blank=False)
	date = models.DateField()
	time = models.CharField(max_length=255, blank=True)
	frequency_dressing = models.CharField(max_length=255, choices=WOUND_FREQUENCY_CHOICES, blank=True)
	type_dressing = models.CharField(max_length=255, blank=True)
	wound_location = models.CharField(max_length=255, choices=WOUND_LOCATION_CHOICES, blank=True)
#	wound_condition = models.CharField(max_length=255, choices=WOUND_CONDITION_CHOICES, blank=True)
#	wound_condition = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
	wound_condition = models.ForeignKey(WoundCondition, null=True, blank=True, on_delete=models.CASCADE)
	images = models.FileField(upload_to="dressing_location", blank=True)
	done_by = models.CharField(max_length=255, blank=True)

	def __str__(self):
		return str(self.ic_number)

	class Meta:
		verbose_name = 'Dressing'
		verbose_name_plural = "Dressing"


class EnteralFeedingRegime(models.Model):
	full_name = models.OneToOneField(PatientProfile, on_delete=models.CASCADE, null=True, blank=False)
	ic_number = models.OneToOneField(Admission, on_delete=models.CASCADE, null=True, blank=False)
	time = models.CharField(max_length=255, blank=True)
	type_of_milk = models.CharField(max_length=255, blank=True)
	amount = models.IntegerField(blank=False)
	warm_water_before = models.IntegerField(blank=False)
	warm_water_after = models.IntegerField(blank=False)

	def __str__(self):
		return str(self.ic_number)

	class Meta:
		verbose_name = 'Enteral Feeding Regime'
		verbose_name_plural = "Enteral Feeding Regime"


class HGTChart(models.Model):
	full_name = models.OneToOneField(PatientProfile, on_delete=models.CASCADE, null=True, blank=False)
	ic_number = models.OneToOneField(Admission, on_delete=models.CASCADE, null=True, blank=False)
	date = models.DateField()
	time = models.CharField(max_length=255, blank=True)
	blood_glucose_reading = models.IntegerField(blank=False)
	remark = models.CharField(max_length=255, blank=True)
	done_by = models.CharField(max_length=255, blank=True)

	def __str__(self):
		return str(self.ic_number)

	class Meta:
		verbose_name = 'HGT Chart'
		verbose_name_plural = "HGT Chart"


class IntakeOutputChart(models.Model):
	full_name = models.OneToOneField(PatientProfile, on_delete=models.CASCADE, null=True, blank=False)
	ic_number = models.OneToOneField(Admission, on_delete=models.CASCADE, null=True, blank=False)
	date = models.DateField()
	time = models.CharField(max_length=255, blank=True)
	intake_oral_type = models.CharField(max_length=255, blank=True)
	intake_oral_ml = models.CharField(max_length=255, blank=True)
	intake_parenteral_type = models.CharField(max_length=255, blank=True)
	intake_parenteral_ml = models.CharField(max_length=255, blank=True)
	intake_other_type = models.CharField(max_length=255, blank=True)
	intake_other_ml = models.CharField(max_length=255, blank=True)
	urine_ml = models.CharField(max_length=255, blank=True)
	urine_cumtotal = models.CharField(max_length=255, blank=True)
	urine_gastric_ml = models.CharField(max_length=255, blank=True)
	other_type = models.CharField(max_length=255, blank=True)
	other_ml = models.CharField(max_length=255, blank=True)

	def __str__(self):
		return str(self.ic_number)

	class Meta:
		verbose_name = 'Intake Output Chart'
		verbose_name_plural = "Intake Output Chart"


class Maintainance(models.Model):
	full_name = models.OneToOneField(PatientProfile, on_delete=models.CASCADE, null=True, blank=False)
	ic_number = models.OneToOneField(Admission, on_delete=models.CASCADE, null=True, blank=False)
	date = models.DateField()
	items = models.CharField(max_length=255, blank=True)
	location_room = models.CharField(max_length=255, blank=True)
	reported_by = models.CharField(max_length=255, blank=True)
	status = models.CharField(max_length=255, blank=True)

	def __str__(self):
		return str(self.ic_number)

	class Meta:
		verbose_name = 'Maintainance'
		verbose_name_plural = "Maintainance"


class MedicationAdministrationRecord(models.Model):
	full_name = models.OneToOneField(PatientProfile, on_delete=models.CASCADE, null=True, blank=False)
	ic_number = models.OneToOneField(Admission, on_delete=models.CASCADE, null=True, blank=False)
	allergy = models.CharField(max_length=255, blank=True)
	time = models.CharField(max_length=255, blank=True)
	route = models.CharField(max_length=255, blank=True)
	stat = models.CharField(max_length=255, blank=True)
	date = models.DateField()
	given_by = models.CharField(max_length=255, blank=True)

	def __str__(self):
		return str(self.ic_number)

	class Meta:
		verbose_name = 'Medication Administration Record'
		verbose_name_plural = "Medication Administration Record"


class MedicationRecord(models.Model):
	full_name = models.OneToOneField(PatientProfile, on_delete=models.CASCADE, null=True, blank=False)
	ic_number = models.OneToOneField(Admission, on_delete=models.CASCADE, null=True, blank=False)
	date = models.DateField()
	time = models.CharField(max_length=255, blank=True)
	medication = models.CharField(max_length=255, blank=True)
	dosage = models.IntegerField(blank=True)
	topup = models.CharField(max_length=255, blank=True)
	balance = models.IntegerField(blank=False)
	remark = models.CharField(max_length=255, blank=True)
	staff = models.CharField(max_length=255, blank=True)

	def __str__(self):
		return str(self.ic_number)

	class Meta:
		verbose_name = 'Medication'
		verbose_name_plural = "Medication"


class MiscellaneousChargesSlip(models.Model):
	full_name = models.OneToOneField(PatientProfile, on_delete=models.CASCADE, null=True, blank=False)
	ic_number = models.OneToOneField(Admission, on_delete=models.CASCADE, null=True, blank=False)
	date = models.DateField()
	items_procedures = models.CharField(max_length=255, blank=True)
	amount_unit = models.IntegerField(blank=True)
	given_by = models.CharField(max_length=255, blank=True)

	def __str__(self):
		return str(self.ic_number)

	class Meta:
		verbose_name = 'Miscellaneous Charges Slip'
		verbose_name_plural = "Miscellaneous Charges Slip"


class Nursing(models.Model):
	full_name = models.OneToOneField(PatientProfile, on_delete=models.CASCADE, null=True, blank=False)
	ic_number = models.OneToOneField(Admission, on_delete=models.CASCADE, null=True, blank=False)
	date_time = models.DateTimeField()
	report = models.CharField(max_length=255, blank=True)

	def __str__(self):
		return str(self.ic_number)

	class Meta:
		verbose_name = 'Nursing'
		verbose_name_plural = "Nursing"


class OvertimeClaim(models.Model):
	full_name = models.OneToOneField(PatientProfile, on_delete=models.CASCADE, null=True, blank=False)
	ic_number = models.OneToOneField(Admission, on_delete=models.CASCADE, null=True, blank=False)
	date = models.DateField()
	duration_time = models.CharField(max_length=255, blank=True)
	hours = models.CharField(max_length=255, blank=True)

	def __str__(self):
		return str(self.ic_number)

	class Meta:
		verbose_name = 'Overtime Claim'
		verbose_name_plural = "Overtime Claim"


class PhysioProgressNote(models.Model):
	full_name = models.OneToOneField(PatientProfile, on_delete=models.CASCADE, null=True, blank=False)
	ic_number = models.OneToOneField(Admission, on_delete=models.CASCADE, null=True, blank=False)
	report = models.CharField(max_length=255, blank=True)

	def __str__(self):
		return str(self.ic_number)

	class Meta:
		verbose_name = 'Physio Progress Note'
		verbose_name_plural = "Physio Progress Note"


class PhysiotherapyGeneralAssessment(models.Model):
	full_name = models.OneToOneField(PatientProfile, on_delete=models.CASCADE, null=True, blank=False)
	ic_number = models.OneToOneField(Admission, on_delete=models.CASCADE, null=True, blank=False)
	doctor_diagnosis = models.CharField(max_length=255, blank=True)
	doctor_management = models.CharField(max_length=255, blank=True)
	problem = models.CharField(max_length=255, blank=True)
	pain_scale = models.CharField(max_length=255, choices=PAIN_SCALE_CHOICES, blank=True)
	comments = models.CharField(max_length=255, blank=True)
	current_history = models.CharField(max_length=255, blank=True)
	special_question = models.CharField(max_length=255, blank=True)
	general_health = models.CharField(max_length=255, blank=True)
	pmx_surgery = models.CharField(max_length=255, blank=True)
	ix_mri_x_ray = models.CharField(max_length=255, blank=True)
	medications_steroids = models.CharField(max_length=255, blank=True)
	occupation_recreation = models.CharField(max_length=255, blank=True)
	pacemaker_hearing_aid = models.CharField(max_length=255, blank=True)
	splinting = models.CharField(max_length=255, blank=True)

	physical_examination_movement = models.CharField(max_length=255, choices=PHYSICAL_EXAMINATION_MOVEMENT_CHOICES, blank=True)
	neurological = models.CharField(max_length=255, choices=NEUROLOGICAL_CHOICES, blank=True)

	muscle_power = models.CharField(max_length=255, blank=True)
	clearing_test_other_joint = models.CharField(max_length=255, blank=True)
	physiotherapists_impression = models.CharField(max_length=255, blank=True)

	functional_activities = models.CharField(max_length=255, blank=True)
	short_term_goals = models.CharField(max_length=255, blank=True)
	long_term_goals = models.CharField(max_length=255, blank=True)
	special_test = models.CharField(max_length=255, blank=True)
	plan_treatment = models.CharField(max_length=255, blank=True)
	date_time = models.DateTimeField()
	attending_physiotherapist = models.CharField(max_length=255, blank=True)

	def __str__(self):
		return str(self.ic_number)

	class Meta:
		verbose_name = 'Physiotherapy General Assessment'
		verbose_name_plural = "Physiotherapy General Assessment"


class Stool(models.Model):
	full_name = models.OneToOneField(PatientProfile, on_delete=models.CASCADE, null=True, blank=False)
	ic_number = models.OneToOneField(Admission, on_delete=models.CASCADE, null=True, blank=False)
	date_time = models.DateField()
	complaints = models.CharField(max_length=255, blank=True)
	treatment_orders = models.CharField(max_length=255, blank=True)
	consultant = models.CharField(max_length=255, blank=True)

	def __str__(self):
		return str(self.ic_number)

	class Meta:
		verbose_name = 'Stool'
		verbose_name_plural = "Stool"


class StaffRecords(models.Model):
	full_name = models.OneToOneField(PatientProfile, on_delete=models.CASCADE, null=True, blank=False)
	ic_number = models.OneToOneField(Admission, on_delete=models.CASCADE, null=True, blank=False)
	annual_leave_days = models.CharField(max_length=255, blank=True)
	public_holiday_days = models.CharField(max_length=255, blank=True)
	replacement_public_holiday = models.CharField(max_length=255, blank=True)
	medical_certificate = models.CharField(max_length=255, blank=True)
	siri_no_diagnosis = models.CharField(max_length=255, blank=True)
	emergency_leaves = models.CharField(max_length=255, blank=True)
	emergency_leaves_reasons = models.CharField(max_length=255, blank=True)
	unpaid_leaves = models.CharField(max_length=255, blank=True)
	unpaid_leaves_reasons = models.CharField(max_length=255, blank=True)

	def __str__(self):
		return str(self.ic_number)

	class Meta:
		verbose_name = 'Staff Records'
		verbose_name_plural = "Staff Records"


class VisitingConsultant(models.Model):
	full_name = models.OneToOneField(PatientProfile, on_delete=models.CASCADE, null=True, blank=False)
	ic_number = models.OneToOneField(Admission, on_delete=models.CASCADE, null=True, blank=False)
	date = models.DateField()
	time = models.CharField(max_length=255, blank=True)
	frequency = models.CharField(max_length=255, blank=True)
	consistency = models.CharField(max_length=255, blank=True)
	amount = models.CharField(max_length=255, blank=True)
	remark = models.CharField(max_length=255, blank=True)
	name = models.CharField(max_length=255, blank=True)

	def __str__(self):
		return str(self.ic_number)

	class Meta:
		verbose_name = 'Visiting Consultant'
		verbose_name_plural = "Visiting Consultant"


class VitalSignFlow(models.Model):
	full_name = models.OneToOneField(PatientProfile, on_delete=models.CASCADE, null=True, blank=False)
	ic_number = models.OneToOneField(Admission, on_delete=models.CASCADE, null=True, blank=False)
	date = models.DateField()
	time = models.CharField(max_length=255, blank=True)
	temp = models.IntegerField(blank=False)
	pulse = models.IntegerField(blank=False)
	blood_pressure_systolic = models.IntegerField(blank=False)
	blood_pressure_diastolic = models.IntegerField(blank=False)
	respiration = models.IntegerField(blank=False)
	spo2_percentage = models.IntegerField(blank=False)
	spo2_o2 = models.IntegerField(blank=False)
	hgt_liter = models.IntegerField(blank=False)
	hgt_remarks = models.IntegerField(blank=False)

	def __str__(self):
		return str(self.ic_number)

	class Meta:
		verbose_name = 'Vital Sign Flow'
		verbose_name_plural = "Vital Sign Flow"
