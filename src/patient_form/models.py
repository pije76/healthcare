from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models
from django.db.models import F
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _

#from jsignature.mixins import JSignatureFieldsMixin

from accounts.models import PatientProfile

#from select2 import fields
from mptt.models import MPTTModel, TreeForeignKey
from phonenumber_field.modelfields import PhoneNumber, PhoneNumberField
#from phonenumber_field.validators import validate_international_phonenumber
from phonenumber_field.phonenumber import to_python

messageserror = _('IC Number format needs to be yymmdd-xx-zzzz.')
ic_number_validator = RegexValidator(regex='\d{6}\-\d{2}\-\d{4}', message=messageserror, code="invalid")


#import select2

#from datetime import timedelta
import datetime
from datetime import *

now = date.today


def validate_international_phonenumber(value):
	phone_number = to_python(value)
	if phone_number and not phone_number.is_valid():
		raise ValidationError(
			_("Please enter valid phone number with following format: +[country code][area code][phone number]"), code="invalid_phone_number"
		)


WOUND_FREQUENCY_CHOICES = (
	('od', 'OD'),
	('bd', 'BD'),
	('tds', 'TDS'),
	('stat', 'STAT'),
)

ADMITTED_CHOICES = (
	('hospital', _('Hospital')),
	('home', _('Home')),
	('others', _('Others')),
)

MODE_CHOICES = (
	('walkedin', _('Walked-in')),
	('wheelchair', _('Wheelchair')),
	('stretcher', _('Stretcher')),
)

GENDER_CHOICES = (
	('male', _('Male')),
	('female', _('Female')),
)

MARITAL_CHOICES = (
	('single', _('Single')),
	('married', _('Married')),
	('others', _('Others')),
)

RELIGION_CHOICES = (
	('buddhist', _('Buddhist')),
	('christian', _('Christian')),
	('hinduism', _('Hinduism')),
	('islam', _('Islam')),
	('others', _('Others')),
)

OCCUPATION_CHOICES = (
	('retired', _('Retired')),
	('housewife', _('Housewife')),
	('others', _('Others')),
)

COMMUNICATION_SIGHT_CHOICES = (
	('good', _('Good')),
	('poor', _('Poor')),
	('glasses', _('Glasses')),
	('blind', _('Blind')),
)

COMMUNICATION_HEARING_CHOICES = (
	('good', _('Good')),
	('poor', _('Poor')),
	('aid', _('Aid')),
)

GENERAL_CONDITION_CHOICES = (
	('stable', _('Stable')),
	('ill', _('Ill')),
	('lethargic', _('Lethargic')),
	('weak', _('Weak')),
	('cachexic', _('Cachexic')),
	('coma', _('Coma')),
	('restless', _('Restless')),
	('depress', _('Depress')),
	('agitated', _('Agitated')),
)

INVASIVE_LINE_INSITU_CHOICES = (
	('-', _('None')),
	('ett', _('ETT')),
	('nasogastric_tube', _('Nasogastric tube')),
	('urinary_catheter', _('Urinary catheter')),
	('pacemaker', _('Pacemaker')),
	('others', _('Others')),
)

MEDICAL_HISTORY_CHOICES = (
	('nochronicillness', _('NO Chronic Illness')),
	('asthma', _('Asthma')),
	('diabetes_mellitus', _('Diabetes Mellitus')),
	('hypertension', _('Hypertension')),
	('heart_disease', _('Heart Disease')),
	('others', _('Others')),
)

ADAPTIVE_AIDS_WITH_PATIENT_CHOICES = (
	('denture', _('Denture')),
	('upperset', _('Upper set')),
	('lowerset', _('Lower set')),
	('walkingaid', _('Walking aid')),
	('hearingaid', _('Hearing aid')),
	('glasses', _('Glasses')),
	('others', _('Others')),
)

ORIENTATION_CHOICES = (
	('nursecallsystem', _('Nurse call system')),
	('bedmechanic', _('Bed Mechanic')),
	('bathroom', _('Bathroom')),
	('visiting_hours', _('Visiting hours')),
	('careofvaluables', _('Care of Valuables')),
	('fireexits', _('Fire Exits')),
	('nosmokingpolicy', _('No Smoking policy')),
	('patientrightresponsibilities', _('Patient Right/ Responsibilities')),
	('informnurseifpatientleavingthe_center', _('Inform nurse if patient leaving the center')),
)

WOUND_LOCATION_CHOICES = (
	('head', _('Head')),
	('face', _('Face')),
	('neck', _('Neck')),
	('chest', _('Chest')),
	('abdomen', _('Abdomen')),
	('back', _('Back')),
	('sacral', _('Sacral')),
	('buttock', _('Buttock')),
	('hand', _('Hand')),
	('leg', _('Leg')),
	('others', _('Others')),
)

WOUND_CONDITION_CHOICES = (
	('clean', _('Clean')),
	('slough', _('Slough')),
	('eschar', _('Eschar')),
	('Others', (
		('Exudate', (
			('sanguineous', _('Sanguineous')),
			('serous', _('Serous')),
			('haemoserous', _('Haemoserous')),
			('purulent', _('Purulent')),
		)),
		('Amount', (
			('scant', _('Scant')),
			('minimal', _('Minimal')),
			('moderate', _('Moderate')),
			('large', _('Large')),
		)),
	)),
)

PHYSICAL_EXAMINATION_MOVEMENT_CHOICES = (
	('joint', _('Joint')),
	('active', _('Active')),
	('passive', _('Passive')),
)

STATUS_CHOICES = (
	('-', '-'),
	('done', _('Done')),
	('pending', _('Pending')),
	('cancel', _('Cancel')),
)

NEUROLOGICAL_CHOICES = (
	('reflexes', _('Reflexes')),
	('motor', _('Motor')),
	('sensation', _('Sensation')),
)

STOOL_FREQUENCY_CHOICES = (
	('-', '-'),
	('bo', 'BO'),
	('bno', 'BNO'),
)

CONSISTENCY_CHOICES = (
	('-', '-'),
	('normal', _('Normal')),
	('hard', _('Hard')),
	('loose', _('Loose')),
	('watery', _('Watery')),
)

AMOUNT_CHOICES = (
	('-', '-'),
	('scanty', _('Scanty')),
	('minimal', _('Minimal')),
	('moderate', _('Moderate')),
	('large', _('Large')),
)

BOOLEAN_CHOICES = (
	(False, _('No')),
	(True, _('Yes')),
)

YES_NO_CHOICES = (
	('no', _('No')),
	('yes', _('Yes')),
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

ROUTE_CHOICES = (
	('oral', _('Oral')),
	('iv', 'IV'),
	('im', 'IM'),
	('s', 'S'),
	('c', 'C'),
	('sl', 'SL'),
	('rt', 'RT'),
	('pr', 'PR'),
	('la', 'LA'),
	('neb', 'Neb'),
)

MEDICATION_ADMINISTRATION_FREQUENCY_CHOICES = (
	('od', 'OD'),
	('om', 'OM'),
	('pm', 'PM'),
	('on', 'ON'),
	('bd', 'BD'),
	('tds', 'TDS'),
	('qid', 'QID'),
	('eod', 'EOD'),
	('prn', 'PRN'),
	('others', _('OTHERS')),
)

MEDICATION_ADMINISTRATION_STAT_CHOICES = (
	('n', 'N-NBM'),
	('o', 'O-Omit'),
	('r', 'R-Refused'),
	('ta', 'TA-Take Away'),
	('t', 'T-Taken'),
	('w', 'W-Withold'),
)

TAB_CHOICES = (
	('1', _('1/1 = 1 Tab')),
	('2', _('11/11 = 2 Tabs')),
	('3', _('111/111 = 3 Tabs')),
	('half', _('1/2 = Half Tab')),
	('others', _('1 1/2 = Others')),
	('4', _('4 Tabs')),
)

SIGNATURE_CHOICES = (
	('od', 'LSS'),
	('om', 'LPC'),
	('pm', 'SYA'),
)


messageserror = "IC Number format needs to be yymmdd-xx-zzzz."
ic_number_validator = RegexValidator(regex='\d{6}\-\d{2}\-\d{4}', message=messageserror, code="invalid")


def get_now():
	return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


class Admission(models.Model):
	patient = models.OneToOneField(PatientProfile, on_delete=models.CASCADE, blank=False, null=True)
	date = models.DateField(default=now, blank=True, null=True)
	time = models.TimeField(blank=True, null=True)
	admitted = models.CharField(choices=ADMITTED_CHOICES, max_length=255, blank=True, null=True)
	mode = models.CharField(choices=MODE_CHOICES, max_length=255, blank=True, null=True)
	birth_date = models.DateField(default=now, blank=True, null=True)
	age = models.PositiveIntegerField(default='0', blank=True, null=True)
	gender = models.CharField(choices=GENDER_CHOICES, max_length=255, blank=True, null=True)
	marital_status = models.CharField(choices=MARITAL_CHOICES, max_length=255, blank=True, null=True)
	phone = PhoneNumberField(blank=True, default="+600000000000", validators=[validate_international_phonenumber])
	religion = models.CharField(choices=RELIGION_CHOICES, max_length=255, blank=True, null=True)
	occupation = models.CharField(choices=OCCUPATION_CHOICES, max_length=255, blank=True, null=True)
	communication_sight = models.CharField(choices=COMMUNICATION_SIGHT_CHOICES, max_length=255, blank=True, null=True)
	communication_hearing = models.CharField(choices=COMMUNICATION_HEARING_CHOICES, max_length=255, blank=True, null=True)
	communication_others = models.CharField(max_length=255, blank=True, null=True)
	address = models.CharField(max_length=255, blank=True, null=True)
	ec_name = models.CharField(_('Name'), max_length=255, blank=True, null=True)
	ec_ic_number = models.CharField(max_length=14, validators=[ic_number_validator], unique=True, blank=True, null=True)
	ec_relationship = models.CharField(_('Relationship'), max_length=255, blank=True, null=True)
	ec_phone = models.CharField(_('Contact Number'), max_length=255, blank=True, null=True)
	ec_address = models.CharField(_('Address'), max_length=255, blank=True, null=True)

	general_condition = models.CharField(choices=GENERAL_CONDITION_CHOICES, max_length=255, blank=True, null=True)
	vital_sign_temperature = models.PositiveIntegerField(default='0', blank=True, null=True)
	vital_sign_pulse = models.PositiveIntegerField(default='0', blank=True, null=True)
	vital_sign_bp = models.PositiveIntegerField(default='0', blank=True, null=True)
	vital_sign_resp = models.PositiveIntegerField(default='0', blank=True, null=True)
	vital_sign_spo2 = models.PositiveIntegerField(default='0', blank=True, null=True)
	vital_sign_on_oxygen_therapy = models.BooleanField(choices=BOOLEAN_CHOICES, max_length=255, default=False, blank=True,)
	vital_sign_on_oxygen_therapy_flow_rate = models.PositiveIntegerField(default='0', blank=True, null=True)
	vital_sign_hgt = models.PositiveIntegerField(default='0', blank=True, null=True)
	allergy_drug = models.CharField(max_length=255, blank=True, null=True)
	allergy_food = models.CharField(max_length=255, blank=True, null=True)
	allergy_others = models.CharField(max_length=255, blank=True, null=True)
	biohazard_infectious_disease = models.BooleanField(choices=BOOLEAN_CHOICES, max_length=255, blank=True, null=True)
	invasive_line_insitu = models.CharField(choices=INVASIVE_LINE_INSITU_CHOICES, max_length=255, blank=True, null=True)
	medical_history = models.CharField(choices=MEDICAL_HISTORY_CHOICES, max_length=255, blank=True, null=True)
	surgical_history_none = models.BooleanField(choices=BOOLEAN_CHOICES, max_length=255, blank=True, null=True)
	surgical_history = models.CharField(max_length=255, blank=True, null=True)
	date_diagnosis = models.DateField(default=now, blank=True, null=True)
	diagnosis = models.CharField(max_length=255, blank=True, null=True)
	date_operation = models.DateField(default=now, blank=True, null=True)
	operation = models.CharField(max_length=255, blank=True, null=True)
	own_medication = models.BooleanField(choices=BOOLEAN_CHOICES, max_length=255, blank=True, null=True)
	own_medication_drug_name = models.CharField(max_length=255, blank=True, null=True)
	own_medication_dosage = models.PositiveIntegerField(default='0', blank=True, null=True)
	own_medication_tablet_capsule = models.CharField(max_length=255, blank=True, null=True)
	own_medication_frequency = models.PositiveIntegerField(default='0', blank=True, null=True)
	adaptive_aids_with_patient = models.CharField(choices=ADAPTIVE_AIDS_WITH_PATIENT_CHOICES, max_length=255, blank=True, null=True)
	orientation = models.CharField(choices=ORIENTATION_CHOICES, max_length=255, blank=True, null=True)
	special_information = models.CharField(max_length=255, blank=True, null=True)
	admission_by = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return str(self.patient)

	@property
	def age(self):
		return int((datetime.now().date() - self.birth_date).days / 365.25)

	class Meta:
		verbose_name = _('Admission')
		verbose_name_plural = _("Admission")


class ApplicationForHomeLeave(models.Model):
	patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE, blank=False, null=True)
	patient_family_name = models.CharField(_('Patient/Family Name'), max_length=255, blank=True, null=True)
	nric_number = models.CharField(_('NRIC Number'), validators=[ic_number_validator], max_length=14, blank=True, null=True)
	patient_family_relationship = models.CharField(_('Patient/Family Relationship'), max_length=255, blank=True, null=True)
	patient_family_phone = PhoneNumberField(_('Patient/Family Phone'), blank=True, default="", validators=[validate_international_phonenumber])
	designation = models.CharField(max_length=255, blank=True, null=True)
	signature = models.CharField(max_length=255, blank=True, null=True)
	date = models.DateField(default=now, blank=True, null=True)

	def __str__(self):
		return str(self.patient)

	class Meta:
		verbose_name = _('Application For Home Leave')
		verbose_name_plural = _("Application For Home Leave")


class Appointment(models.Model):
	patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE, blank=False, null=True)
	date = models.DateField(default=now, blank=True, null=True)
	time = models.TimeField(blank=True, null=True)
	hospital_clinic_center = models.CharField(max_length=255, blank=True, null=True)
	department = models.CharField(max_length=255, blank=True, null=True)
	planning_investigation = models.CharField(max_length=255, blank=True, null=True)
	treatment_order = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return str(self.patient)

	class Meta:
		verbose_name = _('Appointment')
		verbose_name_plural = _("Appointment")


class CatheterizationCannulation(models.Model):
	patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE, blank=False, null=True)
	nasogastric_tube_date = models.DateField(default=now, blank=True, null=True)
	nasogastric_tube_size = models.PositiveIntegerField(default='0', blank=True, null=True)
	nasogastric_tube_type = models.CharField(max_length=255, blank=True, null=True)
	nasogastric_tube_location = models.CharField(max_length=255, blank=True, null=True)
	nasogastric_tube_due_date = models.DateField(default=now, blank=True, null=True)
	nasogastric_tube_inserted_by = models.CharField(max_length=255, blank=True, null=True)
	urinary_catheter_date = models.DateField(default=now, blank=True, null=True)
	urinary_catheter_size = models.PositiveIntegerField(default='0', blank=True, null=True)
	urinary_catheter_type = models.CharField(max_length=255, blank=True, null=True)
	urinary_catheter_location = models.CharField(max_length=255, blank=True, null=True)
	urinary_catheter_due_date = models.DateField(default=now, blank=True, null=True)
	urinary_catheter_inserted_by = models.CharField(max_length=255, blank=True, null=True)
	cannula_date = models.DateField(default=now, blank=True, null=True)
	cannula_size = models.PositiveIntegerField(default='0', blank=True, null=True)
	cannula_type = models.CharField(max_length=255, blank=True, null=True)
	cannula_location = models.CharField(max_length=255, blank=True, null=True)
	cannula_due_date = models.DateField(default=now, blank=True, null=True)
	cannula_inserted_by = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return str(self.patient)

	class Meta:
		verbose_name = _('Catheterization And Cannulation')
		verbose_name_plural = _("Catheterization And Cannulation")


class Charges(models.Model):
	patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE, blank=False, null=True)
	date = models.DateField(default=now, blank=True, null=True)
	items = models.CharField(max_length=255, blank=True, null=True)
	amount_unit = models.PositiveIntegerField(default='0', blank=True, null=True)
	given_by = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return str(self.patient)

	class Meta:
		verbose_name = _('Charges')
		verbose_name_plural = _("Charges")


class WoundCondition(MPTTModel):
	name = models.CharField(max_length=255, blank=True, null=True)
	parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True, on_delete=models.CASCADE)

	class MPTTMeta:
		order_insertion_by = ['name']

	class Meta:
		verbose_name = _('Wound Condition')
		verbose_name_plural = _('Wound Condition')

	def indented_title(self):
		return ("-" * 4) * self.get_level() + self.name

	def __str__(self):
		return self.name


def upload_path(instance, filename):
	return '{0}/{1}'.format('dressing_location', filename)


class Dressing(models.Model):
	patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE, blank=False, null=True)
	date = models.DateField(default=now, blank=True, null=True)
	time = models.TimeField(blank=True, null=True)
	frequency_dressing = models.CharField(choices=WOUND_FREQUENCY_CHOICES, max_length=255, blank=True, null=True)
	type_dressing = models.CharField(max_length=255, blank=True, null=True)
	wound_location = models.CharField(choices=WOUND_LOCATION_CHOICES, max_length=255, blank=True, null=True)
	wound_condition = TreeForeignKey(WoundCondition, related_name='wound_conditions', null=True, blank=True, on_delete=models.CASCADE)
	photos = models.FileField(upload_to=upload_path, blank=True, null=True)
	done_by = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return str(self.patient)

	def photos_url(self):
		if self.photos and hasattr(self.photos, 'url'):
			return self.photos.url

	def image_img(self):
		if self.photos and hasattr(self.photos, 'url'):
			return mark_safe('<img src="%s" style="width: 60px; height: 60px" />' % self.photos.url)
		else:
			return _('No Thumbnail')

	image_img.short_description = _('Thumbnail')

	class Meta:
		verbose_name = _('Dressing')
		verbose_name_plural = _("Dressing")


class AnnotationManager(models.Manager):
	def __init__(self, **kwargs):
		super().__init__()
		self.annotations = kwargs

	def get_queryset(self):
		return super().get_queryset().annotate(**self.annotations)


class EnteralFeedingRegime(models.Model):
	patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE, blank=False, null=True)
	time = models.TimeField(blank=True, null=True)
	type_of_milk = models.CharField(max_length=255, blank=True, null=True)
	amount = models.PositiveIntegerField(default='0', blank=True, null=True)
	warm_water_before = models.PositiveIntegerField(default='0', blank=True, null=True)
	warm_water_after = models.PositiveIntegerField(default='0', blank=True, null=True)
	_total_fluids = None

	objects = AnnotationManager(
			total_fluids=F('warm_water_before') + F('warm_water_after'),
	)

	def __str__(self):
		return str(self.patient)

	class Meta:
		verbose_name = _('Enteral Feeding Regime')
		verbose_name_plural = _("Enteral Feeding Regime")


class HGTChart(models.Model):
	patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE, blank=False, null=True)
	date = models.DateField(default=now, blank=True, null=True)
	time = models.TimeField(blank=True, null=True)
	blood_glucose_reading = models.PositiveIntegerField(default='0', blank=True, null=True)
	remark = models.CharField(max_length=255, blank=True, null=True)
	done_by = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return str(self.patient)

	class Meta:
		verbose_name = _('HGT Chart')
		verbose_name_plural = _("HGT Chart")


class IntakeOutputChart(models.Model):
	patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE, blank=False, null=True)
	date = models.DateField(default=now, blank=True, null=True)
	time_intake = models.TimeField(blank=True, null=True)
	intake_oral_type = models.CharField(max_length=255, blank=True, null=True)
	intake_oral_ml = models.PositiveIntegerField(default='0', blank=True, null=True)
	intake_parenteral_type = models.CharField(max_length=255, blank=True, null=True)
	intake_parenteral_ml = models.PositiveIntegerField(default='0', blank=True, null=True)
	intake_other_type = models.CharField(max_length=255, blank=True, null=True)
	intake_other_ml = models.PositiveIntegerField(default='0', blank=True, null=True)
	time_output = models.TimeField(blank=True, null=True)
	output_urine_ml = models.PositiveIntegerField(default='0', blank=True, null=True)
	output_urine_cum = models.PositiveIntegerField(default='0', blank=True, null=True)
	output_gastric_ml = models.PositiveIntegerField(default='0', blank=True, null=True)
	output_other_type = models.CharField(max_length=255, blank=True, null=True)
	output_other_ml = models.PositiveIntegerField(default='0', blank=True, null=True)

	def __str__(self):
		return str(self.patient)

	class Meta:
		verbose_name = _('Intake Output Chart')
		verbose_name_plural = _("Intake Output Chart")


class Maintainance(models.Model):
	patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE, blank=False, null=True)
	date = models.DateField(default=now, blank=True, null=True)
	items = models.CharField(max_length=255, blank=True, null=True)
	location_room = models.CharField(max_length=255, blank=True, null=True)
	reported_by = models.CharField(max_length=255, blank=True, null=True)
	status = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return str(self.patient)

	def get_absolute_url(self):
		return reverse('patient_form:maintainance', kwargs={'pk': self.pk})

	class Meta:
		verbose_name = _('Maintainance')
		verbose_name_plural = _("Maintainance")


class MedicationRecord(models.Model):
	patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE, blank=False, null=True)
	date = models.DateField(default=now, blank=True, null=True)
	time = models.TimeField(blank=True, null=True)
	medication = models.CharField(max_length=255, blank=True, null=True)
	dosage = models.PositiveIntegerField(default='0', blank=True, null=True)
	topup = models.CharField(max_length=255, blank=True, null=True)
	balance = models.PositiveIntegerField(default='0', blank=True, null=True)
	remark = models.CharField(max_length=255, blank=True, null=True)
	staff = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return str(self.patient)

	class Meta:
		verbose_name = _('Medication Record')
		verbose_name_plural = _("Medication Record")


class MedicationAdministrationRecord(models.Model):
	patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE, blank=False, null=True)
	allergy = models.CharField(max_length=255, blank=True, null=True)
	medication_name = models.CharField(max_length=255, blank=True, null=True)
	medication_dosage = models.PositiveIntegerField(default='0', blank=True, null=True)
	medication_tab = models.CharField(choices=TAB_CHOICES, max_length=255, blank=True, null=True)
	medication_frequency = models.CharField(choices=MEDICATION_ADMINISTRATION_FREQUENCY_CHOICES, max_length=255, blank=True, null=True)
	medication_route = models.CharField(choices=ROUTE_CHOICES, max_length=255, blank=True, null=True)
	medication_date_time = models.DateTimeField(default=get_now, blank=True, null=True)
	signature_nurse = models.CharField(choices=SIGNATURE_CHOICES, max_length=255, blank=True, null=True)
	stat = models.CharField(choices=MEDICATION_ADMINISTRATION_STAT_CHOICES, max_length=255, blank=True, null=True)
	date_time = models.DateTimeField(default=get_now, blank=True, null=True)
	given_by = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return str(self.patient)

	class Meta:
		verbose_name = _('Medication Administration Record')
		verbose_name_plural = _("Medication Administration Record")


class MiscellaneousChargesSlip(models.Model):
	patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE, blank=False, null=True)
	date = models.DateField(default=now, blank=True, null=True)
	items_procedures = models.CharField(max_length=255, blank=True, null=True)
	amount_unit = models.PositiveIntegerField(default='0', blank=True, null=True)
	given_by = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return str(self.patient)

	class Meta:
		verbose_name = _('Miscellaneous Charges Slip')
		verbose_name_plural = _("Miscellaneous Charges Slip")


class Nursing(models.Model):
	patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE, blank=False, null=True)
	date_time = models.DateTimeField(default=get_now, blank=False, null=True)
	report = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return str(self.patient)

	class Meta:
		verbose_name = _('Nursing')
		verbose_name_plural = _("Nursing")


class OvertimeClaim(models.Model):
	patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE, blank=False, null=True)
	date = models.DateField(default=now, blank=True, null=True)
	duration_time = models.DurationField(default='00:05:00', blank=True, null=True)
	hours = models.TimeField(blank=True, null=True)
	checked_sign_by = models.CharField(max_length=255, blank=True, null=True)
	verify_by = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return str(self.patient)

	def convert_duration_time(self):
		sec = self.duration_time.total_seconds()
		return '%02d:%02d' % (int((sec / 3600) % 3600), int((sec / 60) % 60))

	def to_timedelta(self, value):
		if not value or value == '0':
			return TimeDelta(microseconds=0)

		pairs = []
		for b in value.lower().split():
			for index, char in enumerate(b):
				if not char.isdigit():
					pairs.append((b[:index], b[index:])) #digits, letters
					break
		if not pairs:
			raise ValidationError(self.error_messages['invalid'])

		microseconds = 0
		for digits, chars in pairs:
			if not digits or not chars:
				raise ValidationError(self.error_messages['invalid'])
			microseconds += int(digits) * TimeDelta.values_in_microseconds[chars]

		return TimeDelta(microseconds=microseconds)

#	def get_duration(self):
#		return self.datetime.time(convert_duration_time)
#		return self.datetime.date(date)

	class Meta:
		verbose_name = _('Overtime Claim')
		verbose_name_plural = _("Overtime Claim")


class PhysioProgressNote(models.Model):
	patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE, blank=False, null=True)
	report = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return str(self.patient)

	class Meta:
		verbose_name = _('Physio Progress Note')
		verbose_name_plural = _("Physio Progress Note")


class PhysiotherapyGeneralAssessment(models.Model):
	patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE, blank=False, null=True)
	doctor_diagnosis = models.CharField(max_length=255, blank=True, null=True)
	doctor_management = models.CharField(max_length=255, blank=True, null=True)
	problem = models.CharField(max_length=255, blank=True, null=True)
	pain_scale = models.CharField(choices=PAIN_SCALE_CHOICES, max_length=255, blank=True, null=True)
	comments = models.CharField(max_length=255, blank=True, null=True)
	current_history = models.CharField(max_length=255, blank=True, null=True)
	past_history = models.CharField(max_length=255, blank=True, null=True)
	special_question = models.CharField(max_length=255, blank=True, null=True)
	general_health = models.CharField(max_length=255, blank=True, null=True)
	pmx_surgery = models.CharField(max_length=255, blank=True, null=True)
	ix_mri_x_ray = models.CharField(max_length=255, blank=True, null=True)
	medications_steroids = models.CharField(max_length=255, blank=True, null=True)
	occupation_recreation = models.CharField(max_length=255, blank=True, null=True)
	pacemaker_hearing_aid = models.CharField(max_length=255, blank=True, null=True)
	splinting = models.CharField(max_length=255, blank=True, null=True)

	physical_examination_movement = models.CharField(choices=PHYSICAL_EXAMINATION_MOVEMENT_CHOICES, max_length=255, blank=True, null=True)
	neurological = models.CharField(choices=NEUROLOGICAL_CHOICES, max_length=255, blank=True, null=True)

	muscle_power = models.CharField(max_length=255, blank=True, null=True)
	clearing_test_other_joint = models.CharField(max_length=255, blank=True, null=True)
	physiotherapists_impression = models.CharField(max_length=255, blank=True, null=True)

	functional_activities = models.CharField(max_length=255, blank=True, null=True)
	short_term_goals = models.CharField(max_length=255, blank=True, null=True)
	long_term_goals = models.CharField(max_length=255, blank=True, null=True)
	special_test = models.CharField(max_length=255, blank=True, null=True)
	plan_treatment = models.CharField(max_length=255, blank=True, null=True)
	date_time = models.DateTimeField(default=get_now, blank=False, null=True)
	attending_physiotherapist = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return str(self.patient)

	class Meta:
		verbose_name = _('Physiotherapy General Assessment')
		verbose_name_plural = _("Physiotherapy General Assessment")


class StaffRecords(models.Model):
	patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE, blank=False, null=True)
	annual_leave_days = models.PositiveIntegerField(default='0', blank=True, null=True)
	public_holiday_days = models.PositiveIntegerField(default='0', blank=True, null=True)
	replacement_public_holiday = models.CharField(max_length=255, blank=True, null=True)
	medical_certificate = models.CharField(max_length=255, blank=True, null=True)
	siri_no_diagnosis = models.CharField(max_length=255, blank=True, null=True)
	emergency_leaves = models.CharField(max_length=255, blank=True, null=True)
	emergency_leaves_reasons = models.CharField(max_length=255, blank=True, null=True)
	unpaid_leaves = models.CharField(max_length=255, blank=True, null=True)
	unpaid_leaves_reasons = models.CharField(max_length=255, blank=True, null=True)
	total = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return str(self.patient)

	class Meta:
		verbose_name = _('Staff Records')
		verbose_name_plural = _("Staff Records")


class Stool(models.Model):
	patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE, blank=False, null=True)
	date = models.DateField(default=now, blank=True, null=True)
	time = models.TimeField(blank=True, null=True)
	frequency = models.CharField(choices=STOOL_FREQUENCY_CHOICES, max_length=255, blank=True, null=True)
	consistency = models.CharField(choices=CONSISTENCY_CHOICES, max_length=255, blank=True, null=True)
	amount = models.CharField(choices=AMOUNT_CHOICES, max_length=255, blank=True, null=True)
	remark = models.CharField(max_length=255, blank=True, null=True)
	name = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return str(self.patient)

	class Meta:
		verbose_name = _('Stool')
		verbose_name_plural = _("Stool")


class VisitingConsultant(models.Model):
	patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE, blank=False, null=True)
	date_time = models.DateTimeField(default=get_now, blank=False, null=True)
	complaints = models.CharField(max_length=255, blank=True, null=True)
	treatment_orders = models.CharField(max_length=255, blank=True, null=True)
	consultant = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return str(self.patient)

	class Meta:
		verbose_name = _('Visiting Consultant')
		verbose_name_plural = _("Visiting Consultant")


class VitalSignFlow(models.Model):
	patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE, blank=False, null=True)
	date = models.DateField(default=now, blank=True, null=True)
	time = models.TimeField(blank=True, null=True)
	temp = models.PositiveIntegerField(default='0', blank=True, null=True)
	pulse = models.PositiveIntegerField(default='0', blank=True, null=True)
	blood_pressure_systolic = models.PositiveIntegerField(default='0', blank=True, null=True)
	blood_pressure_diastolic = models.PositiveIntegerField(default='0', blank=True, null=True)
	respiration = models.PositiveIntegerField(default='0', blank=True, null=True)
	spo2_percentage = models.PositiveIntegerField(default='0', blank=True, null=True)
	spo2_o2 = models.PositiveIntegerField(default='0', blank=True, null=True)
	hgt_liter = models.PositiveIntegerField(default='0', blank=True, null=True)
	hgt_remarks = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return str(self.patient)

	class Meta:
		verbose_name = _('Vital Sign Flow')
		verbose_name_plural = _("Vital Sign Flow")
