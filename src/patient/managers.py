from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

TEACHER = 'TEACHER'
STUDENT = 'STUDENT'

class ProfileManager(models.Manager):
    def create_student(self, *args, **kwargs):
        user = User.objects.create_user(*args, **kwargs)
        profile = self.create(user=user)
        student_group = Group.objects.get_or_create(name=STUDENT)
        user.groups.add(student_group[0])
        user.save()
        return profile

    def create_teacher(self, *args, **kwargs):
        user = User.objects.create_user(*args, **kwargs)
        profile = self.create(user=user)
        student_group = Group.objects.get_or_create(name=TEACHER)
        user.groups.add(student_group[0])
        user.save()
        return profile
