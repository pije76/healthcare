from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _

#from patient_form.models import Admission

# from tenant_users.tenants.models import UserProfile
USER_TYPE_CHOICES = (
	(1, _('Patient')),
	(2, _('Doctor')),
	(3, _('Nurse')),
	(4, _('Staff')),
)

ic_number_validator = RegexValidator("\d{6}\-\d{2}\-\d{4}", "IC Number format needs to be yymmdd-xx-zzzz.")


class PatientProfile(AbstractUser):
	first_name = models.CharField(default="First", max_length=255, blank=False, null=True)
	last_name = models.CharField(default="Last", max_length=255, blank=True, null=True)
	full_name = models.CharField(max_length=255, unique=True, blank=True, null=True)
	ic_number = models.CharField(default="000000-00-0000", max_length=14, validators=[ic_number_validator], unique=True, blank=True, null=True)
	jkl = models.CharField(max_length=255, blank=True, null=True)
	eth = models.CharField(max_length=255, blank=True, null=True)
	is_staff = models.BooleanField(_('staff status'), default=True, help_text=_('Designates whether the user can log-in into admin page.'))

	def __str__(self):
		return str(self.full_name)
#		return str(self.pk)
#		return self.pk

#	def patientprofile(self):
#		return hasattr(self, 'patient_profile')

	def save(self, *args, **kwargs):
		self.full_name = '{0} {1}'.format(self.first_name, self.last_name)
		super().save(*args, **kwargs)

	class Meta:
		verbose_name = _('Profile')
		verbose_name_plural = _("Profile")


#class PatientModel(PatientProfile):
#    class Meta:
#        proxy = True

#    def __str__(self):
#        return self.ic_number.upper()
