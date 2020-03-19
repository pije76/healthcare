from django.db import models
from django.contrib.auth.models import User
from .managers import ProfileManager, TEACHER, STUDENT


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, models.OneToOneField, related_name='profile')
    objects = ProfileManager()

    def is_student(self):
        return self.user.groups.filter(name=STUDENT).exists()

    def is_teacher(self):
        return self.user.groups.filter(name=TEACHER).exists()

    def class_of(self):
        return self.classes.all().first().school_class.name


class Class(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(UserProfile, through='ClassMembers')

    def __str__(self):
        return self.name


class ClassMembers(models.Model):
    school_class = models.ForeignKey(
        Class, on_delete=models.CASCADE)
    member = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name='classes')
