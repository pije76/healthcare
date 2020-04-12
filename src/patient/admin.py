from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import *

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = [
#        'ic_number',
        'user',
#        'full_name',
    ]
    list_filter = ['user']


    class Meta:
        model = UserProfile


admin.site.register(UserProfile, UserAdmin)
