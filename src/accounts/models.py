from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe

from customers.models import *

from phonenumber_field.modelfields import PhoneNumberField
from phonenumber_field.phonenumber import to_python

ic_number_validator = RegexValidator("\d{6}\-\d{2}\-\d{4}", "IC Number format needs to be yymmdd-xx-zzzz.")


def validate_international_phonenumber(value):
    phone_number = to_python(value)
    if phone_number and not phone_number.is_valid():
        raise ValidationError(_("Please enter valid phone number with following format: +[countrycode][areacode][phonenumber]"), code="invalid_phone_number")


def upload_path_userprofile(instance, filename):
    schema_name = connection.schema_name
    name = Client.objects.filter(schema_name=schema_name).values_list('name', flat=True).first()

    return '{0}/{1}/user_profile/{2}'.format(name, instance.full_name, filename)


def upload_path_emergencycontact(instance, filename):
    schema_name = connection.schema_name
    name = Client.objects.filter(schema_name=schema_name).values_list('name', flat=True).first()

    return '{0}/{1}/emergency_contact/{2}'.format(name, instance.patient, filename)


# Create your models here.
class UserProfile(AbstractUser):
    full_name = models.CharField(_('Full Name'), max_length=255, blank=True, null=True)
    ic_number = models.CharField(_('IC Number'), max_length=14, validators=[ic_number_validator], unique=True, blank=True, null=True)
    ic_upload = models.ImageField(_('IC Upload'), upload_to=upload_path_userprofile, blank=True, null=True)
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

    is_patient = models.BooleanField('Patient', default=False)
    is_staff = models.BooleanField(_('Staff'), default=False)
    is_superuser = models.BooleanField('Admin', default=False)

    def __str__(self):
        return str(self.full_name)

    @property
    def get_ic_number(self):
        return self.ic_number

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
        verbose_name = _('User Profile')
        verbose_name_plural = _("User Profile")


class Family(models.Model):
    patient = models.ForeignKey(UserProfile, related_name='emergencycontact_profile', on_delete=models.CASCADE, blank=False, null=True)
    ec_name = models.CharField(_('Family Name'), max_length=255, blank=True, null=True)
    ec_ic_number = models.CharField(_('NRIC Number'), max_length=14, blank=True, null=True)
    ec_ic_upload = models.ImageField(_('IC Upload'), upload_to=upload_path_emergencycontact, blank=True, null=True)
    ec_relationship = models.CharField(_('Family Relationship'), max_length=255, blank=True, null=True)
    ec_phone = PhoneNumberField(_('Family Contact No'), validators=[validate_international_phonenumber], blank=True, null=True)
    ec_address = models.CharField(_('Family Address'), max_length=255, blank=True, null=True)

    def __str__(self):
        return str(self.ec_name)

    def ec_ic_upload_url(self):
        if self.ec_ic_upload and hasattr(self.ec_ic_upload, 'url'):
            return self.ec_ic_upload.url

    def image_img(self):
        if self.ec_ic_upload and hasattr(self.ec_ic_upload, 'url'):
            return mark_safe('<img src="%s" style="width: 60px; height: 60px" />' % self.ec_ic_upload.url)
        else:
            return _('No Thumbnail')

    image_img.short_description = _('EC IC Upload')

    class Meta:
        verbose_name = _('Family Contact')
        verbose_name_plural = _("Family Contact")
