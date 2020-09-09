from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator
from django.db.models import F
from django.utils.safestring import mark_safe

from accounts.models import *
from staff.models import *

from mptt.models import MPTTModel, TreeForeignKey

import datetime

messageserror = _('IC Number format needs to be yymmdd-xx-zzzz.')

ic_number_validator = RegexValidator(regex='\d{6}\-\d{2}\-\d{4}', message=messageserror, code="invalid")


# Create your models here.
class Admission(models.Model):
	ADMITTED_CHOICES = (
		('Hospital', _('Hospital')),
		('Home', _('Home')),
		('Others', _('Others')),
	)

	MODE_CHOICES = (
		('Walked-in', _('Walked-in')),
		('Wheelchair', _('Wheelchair')),
		('Stretcher', _('Stretcher')),
	)

	GENDER_CHOICES = (
		('Male', _('Male')),
		('Female', _('Female')),
	)

	MARITAL_CHOICES = (
		('Single', _('Single')),
		('Married', _('Married')),
		('Others', _('Others')),
	)

	RELIGION_CHOICES = (
		('Buddhist', _('Buddhist')),
		('Christian', _('Christian')),
		('Hinduism', _('Hinduism')),
		('Islam', _('Islam')),
		('Others', _('Others')),
	)

	OCCUPATION_CHOICES = (
		('Retired', _('Retired')),
		('Housewife', _('Housewife')),
		('Others', _('Others')),
	)

	COMMUNICATION_SIGHT_CHOICES = (
		('Good', _('Good')),
		('Poor', _('Poor')),
		('Glasses', _('Glasses')),
		('Blind', _('Blind')),
	)

	COMMUNICATION_HEARING_CHOICES = (
		('Good', _('Good')),
		('Poor', _('Poor')),
		('Aid', _('Aid')),
		('Others', _('Others')),
	)

	GENERAL_CONDITION_CHOICES = (
		('Stable', _('Stable')),
		('Ill', _('Ill')),
		('Lethargic', _('Lethargic')),
		('Weak', _('Weak')),
		('Cachexic', _('Cachexic')),
		('Coma', _('Coma')),
		('Restless', _('Restless')),
		('Depress', _('Depress')),
		('Agitated', _('Agitated')),
	)

	INVASIVE_LINE_INSITU_CHOICES = (
		('ETT', _('ETT')),
		('Nasogastric tube', _('Nasogastric tube')),
		('Urinary catheter', _('Urinary catheter')),
		('Pacemaker', _('Pacemaker')),
		('Others', _('Others')),
	)

	MEDICAL_HISTORY_CHOICES = (
		('No Chronic Illness', _('No Chronic Illness')),
		('Asthma', _('Asthma')),
		('Diabetes Mellitus', _('Diabetes Mellitus')),
		('Hypertension', _('Hypertension')),
		('Heart Disease', _('Heart Disease')),
		('High Cholesterol', _('High Cholesterol')),
		('Dyslipidemia', _('Dyslipidemia')),
		('Others', _('Others')),
	)

	MEDICATION_ADMINISTRATION_FREQUENCY_CHOICES = (
		('OD', _('OD')),
		('OM', _('OM')),
		('PM', _('PM')),
		('ON', _('ON')),
		('BD', _('BD')),
		('TDS', _('TDS')),
		('QID', _('QID')),
		('EOD', _('EOD')),
		('PRN', _('PRN')),
		('OTHERS', _('OTHERS')),
	)

	ADAPTIVE_AIDS_WITH_PATIENT_CHOICES = (
		('Denture', _('Denture')),
		('Upper set', _('Upper set')),
		('Lower set', _('Lower set')),
		('Walking aid', _('Walking aid')),
		('Glasses', _('Glasses')),
		('Others', _('Others')),
		('Hearing aid', _('Hearing aid')),
	)

	ORIENTATION_CHOICES = (
		('Nurse call system', _('Nurse call system')),
		('Bed Mechanic', _('Bed Mechanic')),
		('Bathroom', _('Bathroom')),
		('Visiting', _('Visiting hours')),
		('Care of Valuables', _('Care of Valuables')),
		('Fire Exits', _('Fire Exits')),
		('No Smoking policy', _('No Smoking policy')),
		('Patient Right/ Responsibilities', _('Patient Right/ Responsibilities')),
		('Inform nurse if patient leaving the center', _(
			'Inform nurse if patient leaving the center')),
	)

	BOOLEAN_CHOICES = (
		(False, _('No')),
		(True, _('Yes')),
	)

	YES_NO_CHOICES = (
		('No', _('No')),
		('Yes', _('Yes')),
	)

	SURGICAL_CHOICES = (
		('None', _('None')),
	)

#	patient = models.OneToOneField(UserProfile, on_delete=models.CASCADE, blank=False, null=True)
	patient = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=False, null=True)
	date_admission = models.DateField(blank=True, null=True)
	time_admission = models.TimeField(blank=True, null=True)
	admitted = models.CharField(max_length=255, blank=True, null=True)
	admitted_others = models.CharField(max_length=255, blank=True, null=True)
	mode = models.CharField(max_length=255, blank=True, null=True)

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

	def __str__(self):
		return str(self.patient)

##	def save(self, *args, **kwargs):
#		if self.age:
##		today = datetime.date.today()
##		birth_date = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
##		self.age = birth_date
##		for field_name in ['admitted', 'biohazard_infectious_disease', 'invasive_line_insitu', 'medical_history', 'surgical_history', 'adaptive_aids_with_patient', 'special_information', 'diagnosis', 'operation']:
##			val = getattr(self, field_name, False)
##			if val:
##				setattr(self, field_name, val.capitalize())
##		super().save(*args, **kwargs)

##	@property
##	def get_age(self):
##		if self.birth_date:
##			today = datetime.date.today()
##			return today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
#		today = datetime.date.today()
#		sec = time.mktime(birth_date.timetuple())
#		bod = int(datetime.timedelta(self.birth_date))
#		convert_duration_year = int((sec / 3600) % 3600)
#		convert_duration_month = int((sec / 60) % 60)
#		convert_duration_day = int(self.birth_date)
#		delta_day = today - self.birth_date
#		total_age = str(delta_day/365.24219)
#		total_age = int((delta_day.days / 365.24219))
#		return int((datetime.now().date() - self.birth_date).days / 365.24219)
#		return int((datetime.datetime.now().date() - self.birth_date).days / 365.24219  )
#		return int((get_today - self.birth_date).days / 365.24219)
#		return total_age
##		return 0

#	def _get_mode_display(self, field):
#		value = getattr(self, field.attname)
#		return force_text(dict(field.flatchoices).get(value, value), strings_only=True)

#	def mode_display(self):
#		for c in MODE_CHOICES:
#			if c[0] == self.mode:
#				return c[1]

	@property
	def get_ec_name(self):
		return self.ec_name

	class Meta:
		verbose_name = _('Admission')
		verbose_name_plural = _("Admission")


class ApplicationForHomeLeave(models.Model):
	patient = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=False, null=True)
	ic_number = models.CharField(_('IC Number'), validators=[ic_number_validator], max_length=14, blank=True, null=True)

#	family_name = models.ForeignKey(Family, verbose_name="Family Name", on_delete=models.CASCADE, blank=False, null=True)
	family_name = models.CharField(verbose_name="Family Name", max_length=255, blank=True, null=True)
#	family_name = models.CharField(_('Family Name'), max_length=255, blank=True, null=True)
	family_ic_number = models.CharField(_('NRIC Number'), validators=[ic_number_validator], max_length=14, blank=True, null=True)
#	family_ic_number = ChainedForeignKey(Admission, chained_field="ec_name", chained_model_field="family_name", show_all=False, auto_choose=True, sort=True)
	family_relationship = models.CharField(_('Family Relationship'), max_length=255, blank=True, null=True)
#	family_phone = PhoneNumberField(_('Phone'), blank=True, validators=[validate_international_phonenumber])
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
#	date = models.DateField(blank=True, null=True)
#	time = models.TimeField(blank=True, null=True)
	date_time = models.DateTimeField(blank=True, null=True)
#	remind_date = models.DateTimeField(null=True)
#	is_notified = models.BooleanField(default=False)
	hospital_clinic_center = models.CharField(max_length=255, blank=True, null=True)
	department = models.CharField(max_length=255, blank=True, null=True)
	planning_investigation = models.CharField(max_length=255, blank=True, null=True)
	treatment_order = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return str(self.patient)

	@property
	def date_time_year(self):
		#		return self.date_time.year
		return self.date_time.strftime('%Y')
#		return unicode(self.date_time.strftime('%Y'))

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
	NASOGASTRIC_TUBE_TYPE_CHOICES = (
		('PVC', _('PVC')),
		('Silicone coated', _('Silicone coated')),
		('Silicone', _('Silicone')),
	)

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
	URINARY_CATHETER_TYPE_CHOICES = (
		('Latex', _('Latex')),
		('Silicone', _('Silicone')),
	)

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


def upload_path_dressing(instance, filename):
	return '{0}/{1}'.format('dressing', filename)


class Dressing(models.Model):
	WOUND_FREQUENCY_CHOICES = (
		('OD', 'OD'),
		('BD', 'BD'),
		('TDS', 'TDS'),
		('STAT', 'STAT'),
	)

	WOUND_LOCATION_CHOICES = (
		('Head', _('Head')),
		('Face', _('Face')),
		('Neck', _('Neck')),
		('Chest', _('Chest')),
		('Abdomen', _('Abdomen')),
		('Back', _('Back')),
		('Sacral', _('Sacral')),
		('Buttock', _('Buttock')),
		('Hand', _('Hand')),
		('Leg', _('Leg')),
		('Others', _('Others')),
	)

	WOUND_CONDITION_CHOICES = (
		('Clean', _('Clean')),
		('Slough', _('Slough')),
		('Eschar', _('Eschar')),
		('Others', (
			('Exudate', (
				('Sanguineous', _('Sanguineous')),
				('Serous', _('Serous')),
				('Haemoserous', _('Haemoserous')),
				('Purulent', _('Purulent')),
			)),
			('Amount', (
				('Scant', _('Scant')),
				('Minimal', _('Minimal')),
				('Moderate', _('Moderate')),
				('Large', _('Large')),
			)),
		)),
	)

	patient = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=False, null=True)
	date = models.DateField(blank=True, null=True)
	time = models.TimeField(blank=True, null=True)
	frequency_dressing = models.CharField(max_length=255, blank=True, null=True)
	type_dressing = models.CharField(max_length=255, blank=True, null=True)
	wound_location = models.CharField(max_length=255, blank=True, null=True)
	wound_condition = TreeForeignKey(WoundCondition, related_name='wound_conditions', null=True, blank=True, on_delete=models.CASCADE)
#	wound_condition = models.ForeignKey(WoundCondition, on_delete=models.CASCADE, blank=False, null=True)
#	wound_condition = models.CharField(max_length=255, blank=True, null=True)
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
	patient = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=False, null=True)
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
	frequency = models.CharField(max_length=255, blank=True, null=True)
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
	output_urine_ml = models.PositiveIntegerField(blank=True, null=True)
	output_urine_cum = models.PositiveIntegerField(blank=True, null=True)
	output_gastric_ml = models.PositiveIntegerField(blank=True, null=True)
	output_other_type = models.CharField(max_length=255, blank=True, null=True)
	output_other_ml = models.PositiveIntegerField(blank=True, null=True)

	def __str__(self):
		return str(self.patient)

	class Meta:
		verbose_name = _('Intake Output')
		verbose_name_plural = _("Intake Output")


def upload_path_investigationreport(instance, filename):
	return '{0}/{1}'.format('investigationreport', filename)


class InvestigationReport(models.Model):
	patient = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=False, null=True)
	date = models.DateField(blank=True, null=True)
	file_upload = models.ImageField(upload_to=upload_path_investigationreport, blank=True, null=True)

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

	image_img.short_description = _('Thumbnail')

	class Meta:
		verbose_name = _('Investigation Report')
		verbose_name_plural = _("Investigation Report")


class Maintenance(models.Model):
	STATUS_CHOICES = (
		('Done', _('Done')),
		('Pending', _('Pending')),
		('Cancel', _('Cancel')),
	)

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


class MedicationRecord(models.Model):
	patient = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=False, null=True)
	date = models.DateField(blank=True, null=True)
	time = models.TimeField(blank=True, null=True)
	medication = models.CharField(max_length=255, blank=True, null=True)
	dosage = models.PositiveIntegerField(blank=True, null=True)
	topup = models.CharField(max_length=255, blank=True, null=True)
	balance = models.PositiveIntegerField(blank=True, null=True)
	remark = models.CharField(max_length=255, blank=True, null=True)
	staff = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return str(self.patient)

	class Meta:
		verbose_name = _('Medication Record')
		verbose_name_plural = _("Medication Record")


class Allergy(models.Model):
	patient = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=False, null=True)
	allergy_drug = models.CharField(max_length=255, blank=True, null=True)
	allergy_food = models.CharField(max_length=255, blank=True, null=True)
	allergy_others = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return '%s (%s - %s)' % (self.allergy_drug, self.allergy_food, self.allergy_others)

	class Meta:
		verbose_name = _('Allergy')
		verbose_name_plural = _("Allergy")


class Medication(models.Model):
	patient = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=False, null=True)
#	medication = models.CharField(max_length=255, blank=True, null=True)
	medication = models.BooleanField(default=False)
	medication_drug_name = models.CharField(max_length=255, blank=True, null=True)
	medication_dosage = models.PositiveIntegerField(blank=True, null=True)
	medication_tablet_capsule = models.PositiveIntegerField(blank=True, null=True)
	medication_frequency = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
#		return str(self.patient)
		return '%s (%s - %s - %s)' % (self.medication_drug_name, self.medication_dosage, self.medication_tablet_capsule, self.medication_frequency)

	class Meta:
		verbose_name = _('Medication Template')
		verbose_name_plural = _("Medication Template")


class MedicationAdministrationRecord(models.Model):
	TAB_CHOICES = (
		('1', _('1/1 = 1 Tab')),
		('2', _('11/11 = 2 Tabs')),
		('3', _('111/111 = 3 Tabs')),
		('Half', _('1/2 = Half Tab')),
		('Others', _('1 1/2 = Others')),
		('4', _('4 Tabs')),
	)

	MEDICATION_ADMINISTRATION_FREQUENCY_CHOICES = (
		('OD', _('OD')),
		('OM', _('OM')),
		('PM', _('PM')),
		('ON', _('ON')),
		('BD', _('BD')),
		('TDS', _('TDS')),
		('QID', _('QID')),
		('EOD', _('EOD')),
		('PRN', _('PRN')),
		('OTHERS', _('OTHERS')),
	)

	ROUTE_CHOICES = (
		('Oral', _('Oral')),
		('IV', 'IV'),
		('IM', 'IM'),
		('SC', 'SC'),
		('SL', 'SL'),
		('RT', 'RT'),
		('PR', 'PR'),
		('LA', 'LA'),
		('Neb', 'Neb'),
	)

	SIGNATURE_CHOICES = (
		('LSS', 'LSS'),
		('LPC', 'LPC'),
		('SYA', 'SYA'),
	)

	STAT_CHOICES = (
		('NBM', 'N-NBM'),
		('Omit', 'O-Omit'),
		('Refused', 'R-Refused'),
		('Take Away', 'TA-Take Away'),
		('Taken', 'T-Taken'),
		('Withold', 'W-Withold'),
	)

	BOOLEAN_CHOICES = (
		(False, _('No')),
		(True, _('Yes')),
	)

	patient = models.ForeignKey(UserProfile, related_name="patient_medicationadministrationrecord", on_delete=models.CASCADE, blank=False, null=True)
#	allergy = models.CharField(max_length=255, blank=True, null=True)
#	allergy = models.ForeignKey(Allergy, related_name="medication_allergy", on_delete=models.CASCADE, blank=False, null=True)
	allergy = models.OneToOneField(Allergy, related_name="medication_allergy", on_delete=models.CASCADE, blank=False, null=True)
#	medication_name = models.CharField(max_length=255, blank=True, null=True)
#	medication_dosage = models.PositiveIntegerField(blank=True, null=True)
#	medication_tab_cap_mls = models.CharField(max_length=255, blank=True, null=True)
#	medication_frequency = models.CharField(max_length=255, blank=True, null=True)
#	medication_route = models.CharField(max_length=255, blank=True, null=True)
	medication_date = models.DateField(blank=True, null=True)
	medication_time = models.TimeField(blank=True, null=True)
	medication = models.ForeignKey(Medication, related_name="medication_admission", on_delete=models.CASCADE, blank=False, null=True)
	status_nurse = models.CharField(max_length=255, blank=True, null=True)
	stat = models.CharField(max_length=255, blank=True, null=True)
	medicationstat_date_time = models.DateTimeField(blank=True, null=True)
	given_by = models.CharField(max_length=255, blank=True, null=True)
	done = models.BooleanField(default=False)

	def __str__(self):
		return str(self.patient)

	def get_fields(self):
		return [(field.verbose_name, field.value_from_object(self)) for field in self.__class__._meta.fields]

	def get_all_fields(self):
		fields = []
		for f in self._meta.fields:

			fname = f.name
			# resolve picklists/choices, with get_xyz_display() function
			get_choice = 'get_' + fname + '_display'
			if hasattr(self, get_choice):
				value = getattr(self, get_choice)()
			else:
				try:
					value = getattr(self, fname)
				except AttributeError:
					value = None

			# only display fields with values and skip some fields entirely
			if f.editable and value and f.name not in ('id', 'status', 'workshop', 'user', 'complete'):
				fields.append(
					{
						'label': f.verbose_name,
						'name': f.name,
						'value': value,
					}
				)
		return fields

	class Meta:
		verbose_name = _('Medication Administration Record')
		verbose_name_plural = _("Medication Administration Record")


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


class OvertimeClaim(models.Model):
	patient = models.ForeignKey(UserProfile, related_name='patient_overtimeclaim', on_delete=models.CASCADE, blank=False, null=True)
	date = models.DateField(blank=True, null=True)
#	date = models.DateTimeField(blank=True, null=True)
#	duration_time_from = models.DurationField(blank=True, null=True)
	duration_time_from = models.TimeField(blank=True, null=True)
#	duration_time_to = models.DurationField(blank=True, null=True)
	duration_time_to = models.TimeField(blank=True, null=True)
	hours = models.TimeField(blank=True, null=True)
	total_hours = models.CharField(max_length=255, blank=True, null=True)
	checked_sign_by = models.ForeignKey(UserProfile, related_name='checked_sign_by_overtimeclaim', on_delete=models.CASCADE, blank=True, null=True)
	verify_by = models.ForeignKey(UserProfile, related_name='verify_by_overtimeclaim', default=None, on_delete=models.CASCADE, blank=True, null=True)

	def __str__(self):
		return str(self.patient)

	def save(self, *args, **kwargs):
		if self.verify_by is None:
			self.verify_by = None
		super().save(*args, **kwargs)

	@property
	def convert_duration_time(self):
		sec = self.duration_time.datetime.total_seconds()
		return '%02d:%02d' % (int((sec / 3600) % 3600), int((sec / 60) % 60))

	@property
	def convert_duration_hour(self):
		sec = self.duration_time.total_seconds()
		return '%02d' % (int((sec / 3600) % 3600))

	@property
	def convert_duration_minute(self):
		sec = self.duration_time.total_seconds()
		return '%02d' % (int((sec / 60) % 60))

	@property
	def convert_duration_second(self):
		sec = self.duration_time.total_seconds()
		return '%02d' % (int(sec))

#	def count_hours(self):
#		t = datetime.time(convert_duration_hour, convert_duration_minute, convert_duration_second)
#		return t
#		OvertimeClaim().hours = t

#	def to_timedelta(self, value):
#		if not value or value == '0':
#			return TimeDelta(microseconds=0)

#		pairs = []
#		for b in value.lower().split():
#			for index, char in enumerate(b):
#				if not char.isdigit():
#					pairs.append((b[:index], b[index:])) #digits, letters
#					break
#		if not pairs:
#			raise ValidationError(self.error_messages['invalid'])

#		microseconds = 0
#		for digits, chars in pairs:
#			if not digits or not chars:
#				raise ValidationError(self.error_messages['invalid'])
#			microseconds += int(digits) * TimeDelta.values_in_microseconds[chars]

#		return TimeDelta(microseconds=microseconds)

#	def get_duration(self):
#		return self.datetime.time(convert_duration_time)
#		return self.datetime.date(date)

	class Meta:
		verbose_name = _('Overtime Claim')
		verbose_name_plural = _("Overtime Claim")


class PhysioProgressNoteFront(models.Model):
	patient = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=False, null=True)
	date_time = models.DateTimeField(blank=True, null=True)
	report = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return str(self.patient)

	class Meta:
		verbose_name = _('Physio Progress Note Front')
		verbose_name_plural = _("Physio Progress Note Front")


class PhysioProgressNoteBack(models.Model):
	patient = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=False, null=True)
	date_time = models.DateTimeField(blank=True, null=True)
	report = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return str(self.patient)

	class Meta:
		verbose_name = _('Physio Progress Note Back')
		verbose_name_plural = _("Physio Progress Note Back")



def upload_path_physiotherapygeneralassessment(instance, filename):
	return '{0}/{1}'.format('physiotherapygeneralassessment', filename)


class PhysiotherapyGeneralAssessment(models.Model):

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

	PHYSICAL_EXAMINATION_MOVEMENT_CHOICES = (
		('Joint', _('Joint')),
		('Active', _('Active')),
		('Passive', _('Passive')),
	)

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

	front_body_img.short_description = _('Front Body Thumbnail')

	def back_body_img(self):
		if self.back_body and hasattr(self.back_body, 'url'):
			return mark_safe('<img src="%s" style="width: 60px; height: 60px" />' % self.back_body.url)
		else:
			return _('No Back Body Thumbnail')

	back_body_img.short_description = _('Back Body Thumbnail')


	class Meta:
		verbose_name = _('Physiotherapy General Assessment')
		verbose_name_plural = _("Physiotherapy General Assessment")


class Stool(models.Model):
	STOOL_FREQUENCY_CHOICES = (
		('BO', 'BO'),
		('BNO', 'BNO'),
	)
	CONSISTENCY_CHOICES = (
		('Normal', _('Normal')),
		('Hard', _('Hard')),
		('Loose', _('Loose')),
		('Watery', _('Watery')),
	)

	AMOUNT_CHOICES = (
		('Scanty', _('Scanty')),
		('Minimal', _('Minimal')),
		('Moderate', _('Moderate')),
		('Large', _('Large')),
	)

	patient = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=False, null=True)
#	patient = models.OneToOneField(UserProfile, on_delete=models.CASCADE, blank=False, null=True)
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
	temp = models.PositiveIntegerField(blank=True, null=True)
	pulse = models.PositiveIntegerField(blank=True, null=True)
	blood_pressure_systolic = models.PositiveIntegerField(blank=True, null=True)
	blood_pressure_diastolic = models.PositiveIntegerField(blank=True, null=True)
	respiration = models.PositiveIntegerField(blank=True, null=True)
	spo2_percentage = models.PositiveIntegerField(blank=True, null=True)
	spo2_o2 = models.PositiveIntegerField(blank=True, null=True)

	def __str__(self):
		return str(self.patient)

	class Meta:
		verbose_name = _('Vital Sign Flow')
		verbose_name_plural = _("Vital Sign Flow")
