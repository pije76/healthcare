from django.db import models
from django.contrib import admin
from django_tenants.admin import TenantAdminMixin

from .models import *

admin.site.register(Patient)
admin.site.register(Admission)
admin.site.register(ApplicationForHomeCareHomeLeave)
admin.site.register(Appointment)
admin.site.register(Cannulation)
admin.site.register(ChargesSheet)
admin.site.register(DressingChart)

