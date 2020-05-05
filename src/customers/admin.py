from django.db import models
from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django.utils.html import format_html

from django_tenants.admin import TenantAdminMixin

from .models import *


class ClientAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ('id', 'name', 'title', 'logo', 'image_img', 'created_on')
    list_filter = ['name']
    ModelAdmin.ordering = ('id',)

    class Meta:
        model = Client


admin.site.register(Client, ClientAdmin)
