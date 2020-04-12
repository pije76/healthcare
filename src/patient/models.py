from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class UserProfile(models.Model):
    user = models.OneToOneField(User, models.OneToOneField, related_name='profile')

    def __str__(self):
        return str(self.user)
#        return str(self.ic_number)

    class Meta:
        verbose_name = 'Patient Profile'
        verbose_name_plural = "Patient Profile"
