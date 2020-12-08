from django import forms
from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django.contrib.admin.widgets import AutocompleteSelect
from django.db import models
from django.db.models import Count

from accounts.models import *
from patient.models import Medicine
from .models import *

from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin


class AllergyAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'patient',
        'allergy_drug',
        'allergy_food',
        'allergy_others',
    ]
    autocomplete_fields = ['patient', ]
    ModelAdmin.ordering = ('id',)


class MedicineAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'drug_name',
    ]
    ModelAdmin.ordering = ('id',)


# Register your models here.
admin.site.register(Allergy, AllergyAdmin)
admin.site.register(Medicine, MedicineAdmin)
admin.site.register(WoundCondition, MPTTModelAdmin)
