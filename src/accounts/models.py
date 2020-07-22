from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _
from django.dispatch import receiver

#from patient_form.models import Admission
from allauth.account.signals import email_confirmed

# from tenant_users.tenants.models import UserProfile

ic_number_validator = RegexValidator("\d{6}\-\d{2}\-\d{4}", "IC Number format needs to be yymmdd-xx-zzzz.")

class Role(models.Model):
	PATIENT = 1
	FAMILY = 2
	STAFF = 3

	USER_TYPE_CHOICES = (
		(PATIENT, _('patient')),
		(FAMILY, _('family')),
		(STAFF, _('staff')),
	)

#	is_patient = models.BooleanField('Patient', default=False)
#	is_family = models.BooleanField('Family', default=False)
#	is_staff = models.BooleanField('Staff', default=False)
	id = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, primary_key=True)
#	user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)
#	user_type = models.PositiveSmallIntegerField("User Type", default="patient", choices=USER_TYPE_CHOICES)
#	user_type = models.CharField("User Type", default="is_patient", max_length=255, blank=True, null=True, choices=USER_TYPE_CHOICES)

	def __str__(self):
		return self.get_id_display()

	class Meta:
		verbose_name = _('User Role')
		verbose_name_plural = _("User Role")


class UserProfile(AbstractUser):
	first_name = models.CharField(default="First", max_length=255, blank=False, null=True)
	last_name = models.CharField(default="Last", max_length=255, blank=True, null=True)
	full_name = models.CharField(max_length=255, unique=True, blank=True, null=True)
	ic_number = models.CharField(max_length=14, validators=[ic_number_validator], unique=True, blank=True, null=True)
	jkl = models.CharField(max_length=255, blank=True, null=True)
	eth = models.CharField(max_length=255, blank=True, null=True)
#	is_staff = models.BooleanField(_('staff status'), default=True, help_text=_('Designates whether the user can log-in into admin page.'))
	roles = models.ManyToManyField(Role)

	def __str__(self):
		return str(self.full_name)
#		return str(self.pk)
#		return self.pk

#	def patientprofile(self):
#		return hasattr(self, 'patient_profile')

	def save(self, *args, **kwargs):
		self.full_name = '{0} {1}'.format(self.first_name, self.last_name)
		super().save(*args, **kwargs)


	@receiver(email_confirmed)
	def email_confirmed_(request, email_address, **kwargs):
		user = User.objects.get(email=email_address.email)
		user.is_active = True
		user.save()

	class Meta:
		verbose_name = _('User Profile')
		verbose_name_plural = _("User Profile")


#class PatientModel(UserProfile):
#    class Meta:
#        proxy = True

#    def __str__(self):
#        return self.ic_number.upper()

class PatientProfile(models.Model):
	user = models.OneToOneField(UserProfile, related_name='patient_profile', on_delete=models.CASCADE, blank=False, null=True)

	class Meta:
		verbose_name = _('Patient')
		verbose_name_plural = _("Patient")

class FamilyProfile(models.Model):
	user = models.OneToOneField(UserProfile, related_name='family_profile', on_delete=models.CASCADE, blank=False, null=True)

	class Meta:
		verbose_name = _('Family')
		verbose_name_plural = _("Family")


class StaffProfile(models.Model):
	user = models.OneToOneField(UserProfile, related_name='staff_profile', on_delete=models.CASCADE, blank=False, null=True)

	class Meta:
		verbose_name = _('Staff')
		verbose_name_plural = _("Staff")

