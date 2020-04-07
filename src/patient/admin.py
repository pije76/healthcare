from django.db import models
from django.contrib import admin
from django_tenants.admin import TenantAdminMixin

from .models import *

admin.site.register(Patient)
admin.site.register(Admission)
admin.site.register(ApplicationForHomeCareHomeLeave)
admin.site.register(Appointment)
admin.site.register(Cannulation)
admin.site.register(Charges)
admin.site.register(Dressing)
admin.site.register(EnteralFeedingRegine)
admin.site.register(HGTChart)
admin.site.register(IntakeOutputChart)
admin.site.register(Maintainance)
admin.site.register(MedicationAdministrationRecord)
admin.site.register(Medication)
admin.site.register(Nursing)
admin.site.register(PhysioProgressNoteBack)
