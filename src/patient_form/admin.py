from django.db import models
from django import forms
from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django.contrib.admin.widgets import AutocompleteSelect

#from django_tenants.admin import TenantAdminMixin
# from ajax_select.admin import AjaxSelectAdmin
# from ajax_select import make_ajax_form
# from easy_select2 import select2_modelform

# import autocomplete_all

from .models import *
#from .forms import *


#@admin.register(Admission)
# class AdmissionAdmin(AjaxSelectAdmin):
#    form = AdmissionForm
class AdmissionAdmin(admin.ModelAdmin):
    list_display = [
        'id',
#       'patient',
        'full_name',
        'ic_number',
        'date',
        'time',
        'mode',
        'birth_date',
        'age',
        'gender',
        'marital_status',
        'address',
        'phone',
        'religion',
        'occupation',
    ]
    autocomplete_fields = ['full_name', ]
    ModelAdmin.ordering = ('id',)


class AppointmentAdmin(admin.ModelAdmin):
#   form = AppointmentForm
    list_display = [
        'id',
        'full_name',
        'ic_number',
        'date',
        'time',
        'hospital_clinic_center',
        'department',
        'planning_investigation',
        'treatment_order',
    ]

#   search_fields = ['full_name']
#    list_filter = ['patient']
#    readonly_fields = ('patient', 'appointment',)
#   autocomplete_except = []  # disable adding autocomplete_fields for listed fields
#   autocomplete_all = False  # disable automatic adding of autocomplete_fields at all
    autocomplete_fields = ['full_name', ]  # must be a foreign key or a many-to-many field.
    ModelAdmin.ordering = ('id',)

#    def save_model(self, request, obj, form, change):
#        if not obj.full_name.id:
#        if not change:
#            obj.full_name = request.user
#        obj.save()

#    def get_form(self, request, obj=None, **kwargs):
#        form = super(AppointmentAdmin, self).get_form(request, obj, **kwargs)
#        form.base_fields['patient'].label_from_instance = lambda obj: "{} {}".format(obj.id, obj.ic_number)
#        return form


class EnteralFeedingRegimeAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'full_name',
        'ic_number',
        'time',
        'type_of_milk',
        'amount',
    ]
    ModelAdmin.ordering = ('id',)


admin.site.register(Admission, AdmissionAdmin)
admin.site.register(ApplicationForHomeLeave)
admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Cannulation)
admin.site.register(Charges)
admin.site.register(WoundCondition)
admin.site.register(Dressing)
admin.site.register(EnteralFeedingRegime, EnteralFeedingRegimeAdmin)
admin.site.register(HGTChart)
admin.site.register(IntakeOutputChart)
admin.site.register(Maintainance)
admin.site.register(MedicationAdministrationRecord)
admin.site.register(MedicationRecord)
admin.site.register(MiscellaneousChargesSlip)
admin.site.register(Nursing)
admin.site.register(OvertimeClaim)
admin.site.register(PhysioProgressNote)
admin.site.register(PhysiotherapyGeneralAssessment)
admin.site.register(Stool)
admin.site.register(StaffRecords)
admin.site.register(VitalSignFlow)
admin.site.register(VisitingConsultant)
