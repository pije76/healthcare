from django.db import models
from django.utils.translation import ugettext_lazy as _

from accounts.models import UserProfile

from mptt.models import MPTTModel, TreeForeignKey

from djangoyearlessdate.models import YearField


# Create your models here.
class OvertimeClaim(models.Model):
#	patient = models.ForeignKey(UserProfile, related_name='patient_overtimeclaim', on_delete=models.CASCADE, blank=False, null=True)
	staff = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=False, null=True)
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
		return str(self.staff)

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


class StaffRecords(models.Model):
	staff = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=False, null=True)
	date = YearField(null=True, blank=True)
	annual_leave_days = models.PositiveIntegerField(blank=True, null=True)
	public_holiday_days = models.PositiveIntegerField(blank=True, null=True)
	replacement_public_holiday = models.PositiveIntegerField(blank=True, null=True)
	medical_certificate = models.CharField(max_length=255, blank=True, null=True)
	siri_no_diagnosis = models.CharField(max_length=255, blank=True, null=True)
	emergency_leaves = models.CharField(max_length=255, blank=True, null=True)
	emergency_leaves_reasons = models.CharField(max_length=255, blank=True, null=True)
	unpaid_leaves = models.CharField(max_length=255, blank=True, null=True)
	unpaid_leaves_reasons = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return str(self.staff)

	class Meta:
		verbose_name = _('Staff Records')
		verbose_name_plural = _("Staff Records")
