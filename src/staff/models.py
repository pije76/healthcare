from __future__ import unicode_literals

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models
from django.db.models import F
from django.utils.safestring import mark_safe
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.utils import six
from django.utils.functional import lazy
from django.utils.encoding import force_text
from django.db.models import signals

mark_safe_lazy = lazy(mark_safe, six.text_type)

#from jsignature.mixins import JSignatureFieldsMixin

from accounts.models import UserProfile, PatientProfile

from mptt.models import MPTTModel, TreeForeignKey
from phonenumber_field.modelfields import PhoneNumber, PhoneNumberField
#from phonenumber_field.validators import validate_international_phonenumber
from phonenumber_field.phonenumber import to_python
from djangoyearlessdate.models import YearField
#from smart_selects.db_fields import ChainedForeignKey

# Create your models here.

class StaffRecords(models.Model):
	patient = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=False, null=True)
#	date = models.DateField(blank=True, null=True)
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
	total = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return str(self.patient)

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
