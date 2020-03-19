from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import *

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'is_student',
        'is_teacher',
        'class_of'
    ]
    list_filter = ['user__groups','classes__school_class']


    class Meta:
        model = UserProfile


admin.site.register(UserProfile, UserAdmin)
