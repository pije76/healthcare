from django.db import models
from django.contrib import admin
from django.contrib.admin.options import ModelAdmin

from django_tenants.admin import TenantAdminMixin

from .models import *


class AdmissionAdmin(admin.ModelAdmin):
    list_display = [
        'date',
        'time',
        'mode',
        'full_name',
        'ic_number',
        'birth_date',
        'age',
        'gender',
        'marital_status',
        'address',
        'phone',
        'religion',
        'occupation',
        'ec_name',
        'ec_ic_number',
        'ec_relationship',
        'ec_phone',
        'ec_address',
        'general_condition',
        'temperature',
        'pulse',
        'BP',
        'resp',
        'spo2',
        'medication',
        'food',
        'others',
        'biohazard_infectious_disease',
        'medical_history',
        'surgical_history',
        'diagnosis',
        'own_medication',
        'denture',
        'admission_by',
        'date_discharge',
    ]
    list_filter = ['full_name']


    class Meta:
        model = Admission


admin.site.register(Admission, AdmissionAdmin)
admin.site.register(ApplicationForHomeLeave)
admin.site.register(Appointment)
admin.site.register(Cannulation)
admin.site.register(Charges)
admin.site.register(Dressing)
admin.site.register(EnteralFeedingRegine)
admin.site.register(HGTChart)
admin.site.register(IntakeOutputChart)
admin.site.register(Maintainance)
admin.site.register(MedicationAdministrationRecord)
admin.site.register(MedicationRecord)
admin.site.register(Nursing)
admin.site.register(PhysioProgressNoteBack)
