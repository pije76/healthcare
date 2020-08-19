from django import forms
from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django.contrib.admin.widgets import AutocompleteSelect
from django.db import models
from django.db.models import Count

from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin

#from django_tenants.admin import TenantAdminMixin
# from ajax_select.admin import AjaxSelectAdmin
# from ajax_select import make_ajax_form
# from easy_select2 import select2_modelform

# import autocomplete_all

from .models import *
from .forms import *
# Register your models here.

class WoundConditionDataAdmin(admin.StackedInline):
	model = WoundCondition
#    max_num = 1
#    extra = 1

admin.site.register(StaffRecords)
admin.site.register(WoundCondition, MPTTModelAdmin)
#admin.site.register(WoundCondition, DraggableMPTTAdmin)
