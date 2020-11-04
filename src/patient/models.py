from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator
from django.db.models import F
from django.utils.safestring import mark_safe
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator

from accounts.models import *
from staff.models import *
from data.models import *
from .validators import *

from mptt.models import MPTTModel, TreeForeignKey
from decimal import Decimal

import datetime


def upload_path_admission(instance, filename):
	return 'admission/{0}/{1}'.format(instance.patient, filename)


def upload_path_dressing(instance, filename):
	return 'dressing/{0}/{1}'.format(instance.patient, filename)


def upload_path_investigation_report(instance, filename):
	return 'investigation_report/{0}/{1}'.format(instance.patient, filename)


def upload_path_physiotherapygeneralassessment(instance, filename):
	return 'physiotherapy_general_assessment/{0}/{1}'.format(instance.patient, filename)


# Create your models here.
class Admission(models.Model):
	patient = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=False, null=True)
	date_admission = models.DateField(blank=True, null=True)
	time_admission = models.TimeField(blank=True, null=True)
	admitted_admission = models.CharField(max_length=255, blank=True, null=True)
	admitted_others = models.CharField(max_length=255, blank=True, null=True)
	mode_admission = models.CharField(max_length=255, blank=True, null=True)

	ic_number = models.CharField(_('IC Number'), max_length=14, validators=[ic_number_validator], unique=True, blank=True, null=True)
	ic_upload = models.ImageField(_('IC Upload'), upload_to=upload_path_admission, blank=True, null=True)
	birth_date = models.DateField(blank=True, null=True)
	age = models.CharField(max_length=255, blank=True, null=True)
	gender = models.CharField(max_length=255, blank=True, null=True)
	marital_status = models.CharField(max_length=255, blank=True, null=True)
	marital_status_others = models.CharField(max_length=255, blank=True, null=True)
	religion = models.CharField(max_length=255, blank=True, null=True)
	religion_others = models.CharField(max_length=255, blank=True, null=True)
	occupation = models.CharField(max_length=255, blank=True, null=True)
	occupation_others = models.CharField(max_length=255, blank=True, null=True)
	communication_sight = models.CharField(max_length=255, blank=True, null=True)
	communication_hearing = models.CharField(max_length=255, blank=True, null=True)
	communication_hearing_others = models.CharField(max_length=255, blank=True, null=True)
	address = models.CharField(max_length=255, blank=True, null=True)

	general_condition = models.CharField(max_length=255, blank=True, null=True)
	vital_sign_temperature = models.PositiveIntegerField(blank=True, null=True)
	vital_sign_pulse = models.PositiveIntegerField(blank=True, null=True)
	vital_sign_bp = models.PositiveIntegerField(blank=True, null=True)
	vital_sign_resp = models.PositiveIntegerField(blank=True, null=True)
	vital_sign_spo2 = models.PositiveIntegerField(blank=True, null=True)
	vital_sign_on_oxygen_therapy = models.CharField(max_length=255, blank=True, null=True,)
	vital_sign_on_oxygen_therapy_flow_rate = models.PositiveIntegerField(blank=True, null=True)
	vital_sign_hgt = models.PositiveIntegerField(blank=True, null=True)

	biohazard_infectious_disease = models.CharField(max_length=255, blank=True, null=True)
	biohazard_infectious_disease_others = models.CharField(max_length=255, blank=True, null=True)
	invasive_line_insitu = models.CharField(max_length=255, blank=True, null=True)
	invasive_line_insitu_others = models.CharField(max_length=255, blank=True, null=True)
	medical_history = models.CharField(max_length=255, blank=True, null=True)
	medical_history_others = models.CharField(max_length=255, blank=True, null=True)
	surgical_history_none = models.CharField(max_length=255, blank=True, null=True)
	surgical_history = models.CharField(max_length=255, blank=True, null=True)

	date_diagnosis = models.DateField(blank=True, null=True)
	diagnosis = models.CharField(max_length=255, blank=True, null=True)

	date_operation = models.DateField(blank=True, null=True)
	operation = models.CharField(max_length=255, blank=True, null=True)

	adaptive_aids_with_patient = models.CharField(max_length=255, blank=True, null=True)
	adaptive_aids_with_patient_others = models.CharField(max_length=255, blank=True, null=True)
	orientation = models.CharField(max_length=255, blank=True, null=True)
	special_information = models.CharField(max_length=255, blank=True, null=True)
	admission_by = models.CharField(max_length=255, blank=True, null=True)

	own_medication = models.BooleanField(default=False)
	medication_date = models.DateField(blank=True, null=True)
	medication_time = models.TimeField(blank=True, null=True)
	medication_drug_name = models.ForeignKey(Medicine, on_delete=models.CASCADE, blank=True, null=True)
	medication_dosage = models.PositiveIntegerField(blank=True, null=True)
	medication_unit = models.CharField(max_length=255, blank=True, null=True)
	medication_tablet_capsule = models.PositiveIntegerField(blank=True, null=True)
	medication_frequency = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return str(self.patient)

	@property
	def get_ec_name(self):
		return self.ec_name

	def ic_upload_url(self):
		if self.ic_upload and hasattr(self.ic_upload, 'url'):
			return self.ic_upload.url

	def image_img(self):
		if self.ic_upload and hasattr(self.ic_upload, 'url'):
			return mark_safe('<img src="%s" style="width: 60px; height: 60px" />' % self.ic_upload.url)
		else:
			return _('No Thumbnail')

	image_img.short_description = _('IC Upload')

	class Meta:
		verbose_name = _('Admission')
		verbose_name_plural = _("Admission")


class ApplicationForHomeLeave(models.Model):
	patient = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=False, null=True)
	ic_number = models.CharField(_('IC Number'), validators=[ic_number_validator], max_length=14, blank=True, null=True)

	family_name = models.CharField(verbose_name="Family Name", max_length=255, blank=True, null=True)
	family_ic_number = models.CharField(_('NRIC Number'), validators=[ic_number_validator], max_length=14, blank=True, null=True)
	family_relationship = models.CharField(_('Family Relationship'), max_length=255, blank=True, null=True)
	family_phone = models.CharField(_('Family Phone'), max_length=255, blank=True, null=True)

	signature_name = models.CharField(verbose_name="Witnessed Name", max_length=255, blank=True, null=True)
	signature_ic_number = models.CharField(_('NRIC Number'), validators=[ic_number_validator], max_length=14, blank=True, null=True)
	signature_relationship = models.CharField(_('Family Relationship'), max_length=255, blank=True, null=True)

	witnessed_name = models.CharField(verbose_name="Witnessed Name", max_length=255, blank=True, null=True)
	witnessed_designation = models.CharField(max_length=255, blank=True, null=True)
	witnessed_signature = models.CharField(max_length=255, blank=True, null=True)
	witnessed_date = models.DateField(blank=True, null=True)

	def __str__(self):
		return str(self.patient)

	def get_family(self):
		return self.ec_name.ec_name

	def get_ec_ic_number(self):
		return self.ec_name.ec_ic_number

	def get_relationship(self):
		return self.ec_name.ec_relationship

	def get_ec_phone(self):
		return self.ec_name.ec_phone

	class Meta:
		verbose_name = _('Application For Home Leave')
		verbose_name_plural = _("Application For Home Leave")


class Appointment(models.Model):
	patient = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=False, null=True)
	date_time = models.DateTimeField(blank=True, null=True)
	hospital_clinic_center = models.CharField(max_length=255, blank=True, null=True)
	department = models.CharField(max_length=255, blank=True, null=True)
	planning_investigation = models.CharField(max_length=255, blank=True, null=True)
	treatment_order = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return str(self.patient)

	@property
	def date_time_year(self):
		return self.date_time.strftime('%Y')

	def datetime_to_milliseconds(self):
		timetuple = self.date_time.timetuple()
		timestamp = datetime.time.mktime(timetuple)
		return timestamp * 1000.0

	@property
	def date_time_month(self):
		return self.date_time.month

	@property
	def date_time_day(self):
		return self.date_time.day

	@property
	def date_time_hour(self):
		return self.date_time.hour

	@property
	def date_time_minute(self):
		return self.date_time.minute

	class Meta:
		verbose_name = _('Appointment')
		verbose_name_plural = _("Appointment")


class Nasogastric(models.Model):
	patient = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=False, null=True)
	nasogastric_tube_date = models.DateField(blank=True, null=True)
	nasogastric_tube_size = models.PositiveIntegerField(blank=True, null=True)
	nasogastric_tube_type = models.CharField(max_length=255, blank=True, null=True)
	nasogastric_tube_location = models.CharField(max_length=255, blank=True, null=True)
	nasogastric_tube_due_date = models.DateField(blank=True, null=True)
	nasogastric_tube_inserted_by = models.CharField(max_length=255, blank=True, null=True)
	nasogastric_tube_remove_date = models.DateField(blank=True, null=True)
	nasogastric_tube_remove_by = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return str(self.patient)

	class Meta:
		verbose_name = _('Nasogastric')
		verbose_name_plural = _("Nasogastric")


class Urinary(models.Model):
	patient = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=False, null=True)
	urinary_catheter_date = models.DateField(blank=True, null=True)
	urinary_catheter_size = models.PositiveIntegerField(blank=True, null=True)
	urinary_catheter_type = models.CharField(max_length=255, blank=True, null=True)
	urinary_catheter_due_date = models.DateField(blank=True, null=True)
	urinary_catheter_inserted_by = models.CharField(max_length=255, blank=True, null=True)
	urinary_catheter_remove_date = models.DateField(blank=True, null=True)
	urinary_catheter_remove_by = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return str(self.patient)

	class Meta:
		verbose_name = _('Urinary')
		verbose_name_plural = _("Urinary")


class Cannula(models.Model):
	patient = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=False, null=True)
	cannula_date = models.DateField(blank=True, null=True)
	cannula_size = models.PositiveIntegerField(blank=True, null=True)
	cannula_location = models.CharField(max_length=255, blank=True, null=True)
	cannula_due_date = models.DateField(blank=True, null=True)
	cannula_remove_date = models.DateField(blank=True, null=True)
	cannula_remove_by = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return str(self.patient)

	class Meta:
		verbose_name = _('Cannula')
		verbose_name_plural = _("Cannula")


class DischargeCheckList(models.Model):
	patient = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=False, null=True)
	date_time = models.DateTimeField(blank=True, null=True)
	discharge_status = models.CharField(max_length=255, blank=True, null=True)
	nasogastric_tube_date = models.DateField(blank=True, null=True)
	nasogastric_tube = models.CharField(max_length=255, blank=True, null=True)
	urinary_catheter_date = models.DateField(blank=True, null=True)
	urinary_catheter = models.CharField(max_length=255, blank=True, null=True)
	surgical_dressing_intact = models.CharField(max_length=255, blank=True, null=True)
	spectacle_walking_aid_denture = models.CharField(max_length=255, blank=True, null=True)
	appointment_card_returned = models.CharField(max_length=255, blank=True, null=True)
	own_medication_return = models.CharField(max_length=255, blank=True, null=True)
	medication_reconcilation = models.CharField(max_length=255, blank=True, null=True)
	medication_reconcilation_patient = models.CharField(max_length=255, blank=True, null=True)
	given_by = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return str(self.patient)

	class Meta:
		verbose_name = _('Discharge CheckList')
		verbose_name_plural = _("Discharge CheckList")


class Dressing(models.Model):
	patient = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=False, null=True)
	date = models.DateField(blank=True, null=True)
	time = models.TimeField(blank=True, null=True)
	frequency_dressing = models.CharField(max_length=255, blank=True, null=True)
	type_dressing = models.CharField(max_length=255, blank=True, null=True)
	wound_location = models.CharField(max_length=255, blank=True, null=True)
	wound_condition = TreeForeignKey(WoundCondition, null=True, blank=True, on_delete=models.CASCADE)
	photos = models.ImageField(upload_to=upload_path_dressing, blank=True, null=True)
	note = models.CharField(max_length=255, blank=True, null=True)
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

	image_img.short_description = _('Photos')

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
	patient = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True, null=True)
	date = models.DateField(blank=True, null=True)
	time = models.TimeField(blank=True, null=True)
	type_of_milk = models.CharField(max_length=255, blank=True, null=True)
	amount = models.PositiveIntegerField(blank=True, null=True)
	warm_water_before = models.PositiveIntegerField(blank=True, null=True)
	warm_water_after = models.PositiveIntegerField(blank=True, null=True)
	_total_fluids = None

	objects = AnnotationManager(
		total_fluids=F('warm_water_before') + F('warm_water_after'),
	)

	def __str__(self):
		return str(self.patient)

	class Meta:
		verbose_name = _('Enteral Feeding Regime')
		verbose_name_plural = _("Enteral Feeding Regime")


class HGT(models.Model):
	patient = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=False, null=True)
	date = models.DateField(blank=True, null=True)
	time = models.TimeField(blank=True, null=True)
	blood_glucose_reading = models.PositiveIntegerField(blank=True, null=True)
	remark = models.CharField(max_length=255, blank=True, null=True)
	done_by = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return str(self.patient)

	class Meta:
		verbose_name = _('HGT')
		verbose_name_plural = _("HGT")


class IntakeOutput(models.Model):
	patient = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=False, null=True)
	date = models.DateField(blank=True, null=True)
	time = models.TimeField(blank=True, null=True)
	intake_oral_type = models.CharField(max_length=255, blank=True, null=True)
	intake_oral_ml = models.PositiveIntegerField(blank=True, null=True)
	intake_parenteral_type = models.CharField(max_length=255, blank=True, null=True)
	intake_parenteral_ml = models.PositiveIntegerField(blank=True, null=True)
	intake_other_type = models.CharField(max_length=255, blank=True, null=True)
	intake_other_ml = models.PositiveIntegerField(blank=True, null=True)
	output_urine_type = models.CharField(max_length=255, blank=True, null=True)
	output_urine_ml = models.PositiveIntegerField(blank=True, null=True)
	output_gastric_ml = models.PositiveIntegerField(blank=True, null=True)
	output_other_type = models.CharField(max_length=255, blank=True, null=True)
	output_other_ml = models.PositiveIntegerField(blank=True, null=True)

	def __str__(self):
		return str(self.patient)

	class Meta:
		verbose_name = _('Intake Output')
		verbose_name_plural = _("Intake Output")


class InvestigationReport(models.Model):
	patient = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=False, null=True)
	date = models.DateField(blank=True, null=True)
	file_upload = models.ImageField(upload_to=upload_path_investigation_report, blank=True, null=True)

	def __str__(self):
		return str(self.patient)

	def file_upload_url(self):
		if self.file_upload and hasattr(self.file_upload, 'url'):
			return self.file_upload.url

	def image_img(self):
		if self.file_upload and hasattr(self.file_upload, 'url'):
			return mark_safe('<img src="%s" style="width: 60px; height: 60px" />' % self.file_upload.url)
		else:
			return _('No Thumbnail')

	image_img.short_description = _('File Upload')

	class Meta:
		verbose_name = _('Investigation Report')
		verbose_name_plural = _("Investigation Report")


class Maintenance(models.Model):
	patient = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=False, null=True)
	date = models.DateField(blank=True, null=True)
	items = models.CharField(max_length=255, blank=True, null=True)
	location_room = models.CharField(max_length=255, blank=True, null=True)
	reported_by = models.CharField(max_length=255, blank=True, null=True)
	status = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return str(self.patient)

	def get_absolute_url(self):
		return reverse('patient:maintenance', kwargs={'pk': self.pk})

	class Meta:
		verbose_name = _('Maintenance')
		verbose_name_plural = _("Maintenance")


class MedicationAdministrationRecordTemplate(models.Model):
	patient = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=False, null=True)
	own_medication = models.BooleanField(default=False)
	medication_date = models.DateField(blank=True, null=True)
	medication_time = models.TimeField(blank=True, null=True)
	medication_drug_name = models.ForeignKey(Medicine, on_delete=models.CASCADE, blank=True, null=True)
	medication_dosage = models.PositiveIntegerField(blank=True, null=True)
	medication_unit = models.CharField(max_length=255, blank=True, null=True)
	medication_tablet_capsule = models.PositiveIntegerField(blank=True, null=True)
	medication_frequency = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return str(self.patient)

	class Meta:
		verbose_name = _('Medication Administration Record (Template)')
		verbose_name_plural = _("Medication Administration Record (Template)")


class MedicationAdministrationRecord(models.Model):
	patient = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=False, null=True)
	allergy_drug = models.CharField(max_length=255, blank=True, null=True)
	allergy_food = models.CharField(max_length=255, blank=True, null=True)
	allergy_others = models.CharField(max_length=255, blank=True, null=True)
	medication_date = models.DateField(blank=True, null=True)
	medication_time = models.TimeField(blank=True, null=True)
	medication_drug_name = models.ForeignKey(Medicine, on_delete=models.CASCADE, blank=True, null=True)
	medication_dosage = models.PositiveIntegerField(blank=True, null=True)
	medication_unit = models.CharField(max_length=255, blank=True, null=True)
	medication_tablet_capsule = models.PositiveIntegerField(blank=True, null=True)
	medication_frequency = models.CharField(max_length=255, blank=True, null=True)
	medication_source = models.CharField(max_length=255, blank=True, null=True)
	medication_route = models.CharField(max_length=255, blank=True, null=True)
	medication_status = models.CharField(max_length=255, blank=True, null=True)
	medication_done = models.BooleanField(default=False)

	def __str__(self):
		return str(self.patient)

	class Meta:
		verbose_name = _('Medication Administration Record')
		verbose_name_plural = _("Medication Administration Record")


class MedicationRecord(models.Model):
	patient = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=False, null=True)
	date = models.DateField(blank=True, null=True)
	time = models.TimeField(blank=True, null=True)
	medication = models.CharField(max_length=255, blank=True, null=True)
	dosage = models.PositiveIntegerField(blank=True, null=True)
	unit = models.CharField(max_length=255, blank=True, null=True)
	topup = models.CharField(max_length=255, blank=True, null=True)
	balance = models.PositiveIntegerField(blank=True, null=True)
	remark = models.CharField(max_length=255, blank=True, null=True)
	staff = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return str(self.patient)

	class Meta:
		verbose_name = _('Medication Record')
		verbose_name_plural = _("Medication Record")


class MiscellaneousChargesSlip(models.Model):
	patient = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=False, null=True)
	date = models.DateField(blank=True, null=True)
	items_procedures = models.CharField(max_length=255, blank=True, null=True)
	unit = models.CharField(max_length=255, blank=True, null=True)
	amount = models.PositiveIntegerField(blank=True, null=True)
	given_by = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return str(self.patient)

	class Meta:
		verbose_name = _('Miscellaneous Charges Slip')
		verbose_name_plural = _("Miscellaneous Charges Slip")


class Multipurpose(models.Model):
	patient = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=False, null=True)
	date_time = models.DateTimeField(blank=True, null=True)
	symptom = models.CharField(max_length=255, blank=True, null=True)
	remark = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return str(self.patient)

	class Meta:
		verbose_name = _('Multipurpose Chart')
		verbose_name_plural = _("Multipurpose Chart")


class Nursing(models.Model):
	patient = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=False, null=True)
	date_time = models.DateTimeField(blank=True, null=True)
	report = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return str(self.patient)

	class Meta:
		verbose_name = _('Nursing')
		verbose_name_plural = _("Nursing")


class PhysioProgressNoteSheet(models.Model):
	patient = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=False, null=True)
	date_time = models.DateTimeField(blank=True, null=True)
	report = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return str(self.patient)

	class Meta:
		verbose_name = _('Physio Progress Note Sheet')
		verbose_name_plural = _("Physio Progress Note Sheet")


class PhysiotherapyGeneralAssessment(models.Model):
	patient = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=False, null=True)
	doctor_diagnosis = models.CharField(max_length=255, blank=True, null=True)
	doctor_management = models.CharField(max_length=255, blank=True, null=True)
	problem = models.CharField(max_length=255, blank=True, null=True)
	front_body = models.ImageField(upload_to=upload_path_physiotherapygeneralassessment, blank=True, null=True)
	back_body = models.ImageField(upload_to=upload_path_physiotherapygeneralassessment, blank=True, null=True)
	pain_scale = models.CharField(max_length=255, blank=True, null=True)
	comments = models.CharField(max_length=255, blank=True, null=True)
	current_history = models.CharField(max_length=255, blank=True, null=True)
	past_history = models.CharField(max_length=255, blank=True, null=True)
	special_question = models.CharField(max_length=255, blank=True, null=True)
	general_health = models.CharField(max_length=255, blank=True, null=True)
	pmx_surgery = models.CharField(max_length=255, blank=True, null=True)
	ix_mri_x_ray = models.CharField(max_length=255, blank=True, null=True)
	medications_steroids = models.CharField(max_length=255, blank=True, null=True)
	occupation_recreation = models.CharField(max_length=255, blank=True, null=True)
	palpation = models.CharField(max_length=255, blank=True, null=True)
	pacemaker_hearing_aid = models.CharField(max_length=255, blank=True, null=True)
	splinting = models.CharField(max_length=255, blank=True, null=True)

	physical_examination_movement = models.CharField(max_length=255, blank=True, null=True)
	neurological_reflexes = models.CharField(max_length=255, blank=True, null=True)
	neurological_motor = models.CharField(max_length=255, blank=True, null=True)
	neurological_sensation = models.CharField(max_length=255, blank=True, null=True)

	muscle_power = models.CharField(max_length=255, blank=True, null=True)
	clearing_test_other_joint = models.CharField(max_length=255, blank=True, null=True)
	physiotherapists_impression = models.CharField(max_length=255, blank=True, null=True)

	functional_activities = models.CharField(max_length=255, blank=True, null=True)
	short_term_goals = models.CharField(max_length=255, blank=True, null=True)
	long_term_goals = models.CharField(max_length=255, blank=True, null=True)
	special_test = models.CharField(max_length=255, blank=True, null=True)
	plan_treatment = models.CharField(max_length=255, blank=True, null=True)
	date_time = models.DateTimeField(blank=True, null=True)
	attending_physiotherapist = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return str(self.patient)

	def front_body_url(self):
		if self.front_body and hasattr(self.front_body, 'url'):
			return self.front_body.url

	def back_body_url(self):
		if self.back_body and hasattr(self.back_body, 'url'):
			return self.back_body.url

	def front_body_img(self):
		if self.front_body and hasattr(self.front_body, 'url'):
			return mark_safe('<img src="%s" style="width: 60px; height: 60px" />' % self.front_body.url)
		else:
			return _('No Front Body Thumbnail')

	front_body_img.short_description = _('Front Body')

	def back_body_img(self):
		if self.back_body and hasattr(self.back_body, 'url'):
			return mark_safe('<img src="%s" style="width: 60px; height: 60px" />' % self.back_body.url)
		else:
			return _('No Back Body Thumbnail')

	back_body_img.short_description = _('Back Body')

	class Meta:
		verbose_name = _('Physiotherapy General Assessment')
		verbose_name_plural = _("Physiotherapy General Assessment")


class Stool(models.Model):
	patient = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=False, null=True)
	date = models.DateField(blank=True, null=True)
	time = models.TimeField(blank=True, null=True)
	frequency = models.CharField(max_length=255, blank=True, null=True)
	consistency = models.CharField(max_length=255, blank=True, null=True)
	amount = models.CharField(max_length=255, blank=True, null=True)
	remark = models.CharField(max_length=255, blank=True, null=True)
	done_by = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return str(self.patient)

	class Meta:
		verbose_name = _('Stool')
		verbose_name_plural = _("Stool")


class VisitingConsultant(models.Model):
	patient = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=False, null=True)
	date_time = models.DateTimeField(blank=True, null=True)
	complaints = models.CharField(max_length=255, blank=True, null=True)
	treatment_orders = models.CharField(max_length=255, blank=True, null=True)
	consultant = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return str(self.patient)

	class Meta:
		verbose_name = _('Visiting Consultant')
		verbose_name_plural = _("Visiting Consultant")


class VitalSignFlow(models.Model):
	patient = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=False, null=True)
	date = models.DateField(blank=True, null=True)
	time = models.TimeField(blank=True, null=True)
	temp = models.DecimalField(validators=[MinValueValidator(Decimal('0.01'))], max_digits=5, decimal_places=2, blank=True, null=True)
	pulse = models.PositiveIntegerField(blank=True, null=True)
	blood_pressure_systolic = models.PositiveIntegerField(blank=True, null=True)
	blood_pressure_diastolic = models.PositiveIntegerField(blank=True, null=True)
	respiration = models.PositiveIntegerField(blank=True, null=True)
	spo2_percentage = models.PositiveIntegerField(blank=True, null=True)
	spo2_o2 = models.PositiveIntegerField(blank=True, null=True)

	def __str__(self):
		return str(self.patient)

	class Meta:
		verbose_name = _('Vital Sign Chart')
		verbose_name_plural = _("Vital Sign Chart")
