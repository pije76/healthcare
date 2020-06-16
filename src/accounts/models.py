from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


# from tenant_users.tenants.models import UserProfile
USER_TYPE_CHOICES = (
	(1, 'patient'),
	(2, 'doctor'),
	(3, 'nurse'),
	(4, 'staff'),
)


class PatientProfile(AbstractUser):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	full_name = models.CharField(max_length=255, unique=True, null=True, blank=True)
	is_staff = models.BooleanField('staff status', default=True, help_text='Designates whether the user can log-in into admin page.')

	def __str__(self):
		return str(self.full_name)

	def patientprofile(self):
		return hasattr(self, 'patient_profile')

	def save(self, *args, **kwargs):
		self.full_name = '{0} {1}'.format(self.first_name, self.last_name)
		super().save(*args, **kwargs)

	class Meta:
		verbose_name = 'Patient Profile'
		verbose_name_plural = "Patient Profile"


#class PatientModel(PatientProfile):
#    class Meta:
#        proxy = True

#    def __str__(self):
#        return self.ic_number.upper()