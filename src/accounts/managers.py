from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


PATIENT = 'PATIENT'
NURSE = 'NURSE'


class ProfileManager(models.Manager):
    def create_patient(self, *args, **kwargs):
        user = User.objects.create_user(*args, **kwargs)
        profile = self.create(user=user)
        student_group = Group.objects.get_or_create(name=NURSE)
        user.groups.add(student_group[0])
        user.save()
        return profile

    def create_nurse(self, *args, **kwargs):
        user = User.objects.create_user(*args, **kwargs)
        profile = self.create(user=user)
        student_group = Group.objects.get_or_create(name=PATIENT)
        user.groups.add(student_group[0])
        user.save()
        return profile


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError(_('The username must be set'))
        username = self.normalize_username(username)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(username, password, **extra_fields)