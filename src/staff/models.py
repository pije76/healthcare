from django.db import models
from django.utils.translation import ugettext_lazy as _

from accounts.models import UserProfile

from mptt.models import MPTTModel, TreeForeignKey

from djangoyearlessdate.models import YearField

# Create your models here.

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


class WoundCondition(MPTTModel):
	name = models.CharField(max_length=255, blank=True, null=True)
	parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True, on_delete=models.CASCADE)

	class MPTTMeta:
		order_insertion_by = ['name']

	class Meta:
		verbose_name = _('Wound Condition')
		verbose_name_plural = _('Wound Condition')

#	def indented_title(self):
#		return ("-" * 4) * self.get_level() + self.name

	def __str__(self):
		return self.name
