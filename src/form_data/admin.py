from django.db import models
from django.contrib import admin
from django.contrib.admin.options import ModelAdmin

from django_tenants.admin import TenantAdminMixin
from ajax_select.admin import AjaxSelectAdmin
from ajax_select import make_ajax_form

from .models import *
from .forms import *

admin.site.register(Admission)
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
admin.site.register(PhysioProgressNoteFront)
admin.site.register(PhysiotherapyGeneralAssessment)
admin.site.register(Stool)
admin.site.register(VitalSignFlow)
