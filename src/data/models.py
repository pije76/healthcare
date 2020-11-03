from django.db import models
from django.utils.translation import ugettext_lazy as _

from accounts.models import UserProfile

from mptt.models import MPTTModel, TreeForeignKey


# Create your models here.
class Allergy(models.Model):
	patient = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=False, null=True)
	allergy_drug = models.CharField(max_length=255, blank=True, null=True)
	allergy_food = models.CharField(max_length=255, blank=True, null=True)
	allergy_others = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
#		return str(self.patient)
		return '%s (%s - %s)' % (self.allergy_drug, self.allergy_food, self.allergy_others)

	class Meta:
		verbose_name = _('Allergy')
		verbose_name_plural = _("Allergy")


class Medicine(models.Model):
	drug_name = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return str(self.drug_name)

	class Meta:
		verbose_name = _('Medicine')
		verbose_name_plural = _("Medicine")


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
