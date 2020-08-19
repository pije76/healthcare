from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _
from django.dispatch import receiver

#from patient_form.models import Admission
from allauth.account.signals import email_confirmed
from allauth.account.signals import user_signed_up

#from smart_selects.db_fields import ChainedForeignKey

# from tenant_users.tenants.models import UserProfile

ic_number_validator = RegexValidator("\d{6}\-\d{2}\-\d{4}", "IC Number format needs to be yymmdd-xx-zzzz.")

class Role(models.Model):
	PATIENT = 1
	STAFF = 2
	ADMIN = 3

	USER_TYPE_CHOICES = (
		(PATIENT, _('Patient')),
		(STAFF, _('Staff')),
		(ADMIN, _('Admin')),
	)

	is_patient = models.BooleanField('Patient', default=False)
	is_admin = models.BooleanField('Admin', default=False)
	is_staff = models.BooleanField('Staff', default=False)
#	id = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, primary_key=True)
#	name = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)
#	user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)
#	user_type = models.PositiveSmallIntegerField("User Type", default="patient", choices=USER_TYPE_CHOICES)
#	user_type = models.CharField("User Type", default="is_patient", max_length=255, blank=True, null=True, choices=USER_TYPE_CHOICES)

	def __str__(self):
#		return self.get_id_display()
		return str(self.name)

	class Meta:
		verbose_name = _('User Role')
		verbose_name_plural = _("User Role")


class UserProfile(AbstractUser):
#	username = models.CharField(max_length=255, unique=True, blank=False, null=True)
#	slug = models.SlugField(max_length=255, unique=True)
	first_name = models.CharField(max_length=255, blank=False, null=True)
	last_name = models.CharField(max_length=255, blank=True, null=True)
	full_name = models.CharField(_('Full Name'), max_length=255, blank=True, null=True)
	ic_number = models.CharField(_('IC Number'), max_length=14, validators=[ic_number_validator], unique=True, blank=True, null=True)
	is_patient = models.BooleanField('Patient', default=False)
	is_staff = models.BooleanField(_('Staff'), default=False)
	is_superuser = models.BooleanField('Admin', default=False)
#	roles = models.ManyToManyField(Role, blank=True)

	def __str__(self):
		return str(self.full_name)
#		return str(self.username)
#		return str(self.pk)
#		return self.pk

#	def patientprofile(self):
#		return hasattr(self, 'patient_profile')

	@property
	def get_ic_number(self):
		return self.ic_number

	def save(self, *args, **kwargs):
#		self.slug = slugify(self.username)
		self.full_name = '{0} {1}'.format(self.first_name, self.last_name)
		super().save(*args, **kwargs)

#	@receiver(user_signed_up)
#	def user_signed_up_data(request, user, **kwargs):
#		profile = UserProfile(user=user)
#		data = UserProfile.objects.filter(user=user, is_patient=False)
#		if data:
#			picture = data[0].get_avatar_url()
#			if picture:
#				save_image_from_url(model=profile, url=picture)
#			profile.save()
#		user.first_name = self.cleaned_data['first_name']
#		user.last_name = self.cleaned_data['last_name']
#		user.ic_number = self.cleaned_data['ic_number']
#		user.is_active = True
#		user.is_patient = True
#		user.is_staff = False
#		user.is_admin = False
#		user.save()
#		full_name = kwargs['full_name']
#		user = UserProfile.objects.get(full_name=full_name)
#		user = kwargs['user']
		# Do your stuff with the user
#		user.save()

#	@receiver(email_confirmed)
#	def email_confirmed_(request, email_address, **kwargs):
#		user = User.objects.get(email=email_address.email)
#		user.is_active = True
#		user.save()

	class Meta:
		verbose_name = _('User Profile')
		verbose_name_plural = _("User Profile")
#		permissions = (
#            ('patient_form.add_admission', 'Assign task'),
#        )


#class PatientModel(UserProfile):
#    class Meta:
#        proxy = True

#    def __str__(self):
#        return self.ic_number.upper()

class PatientProfile(UserProfile):
	user = models.OneToOneField(UserProfile, parent_link=True, related_name='patient_profile', on_delete=models.CASCADE, blank=False, null=False)

	class Meta:
		verbose_name = _('Patient')
		verbose_name_plural = _("Patient")

class StaffProfile(UserProfile):
	user = models.OneToOneField(UserProfile, parent_link=True, related_name='staff_profile', on_delete=models.CASCADE, blank=False, null=False)

	class Meta:
		verbose_name = _('Staff')
		verbose_name_plural = _("Staff")

class AdminProfile(UserProfile):
	user = models.OneToOneField(UserProfile, parent_link=True, related_name='admin_profile', on_delete=models.CASCADE, blank=False, null=False)

	class Meta:
		verbose_name = _('Admin')
		verbose_name_plural = _("Admin")

