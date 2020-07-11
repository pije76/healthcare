from django.db import models
from django import forms
from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django.contrib.admin.widgets import AutocompleteSelect
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin

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
        'patient',
        'date',
        'time',
        'admitted',
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
    autocomplete_fields = ['patient', ]
    ModelAdmin.ordering = ('id',)


class ApplicationForHomeLeaveAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'patient',
        'patient_family_name',
        'nric_number',
        'patient_family_relationship',
        'patient_family_phone',
        'designation',
        'signature',
        'date',
    ]
    autocomplete_fields = ['patient', ]
    ModelAdmin.ordering = ('id',)

class AppointmentAdmin(admin.ModelAdmin):
#   form = AppointmentForm
    list_display = [
        'id',
        'patient',
#        'ic_number',
        'date',
        'time',
        'hospital_clinic_center',
        'department',
        'planning_investigation',
        'treatment_order',
    ]

#   search_fields = ['patient']
#    list_filter = ['patient']
#    readonly_fields = ('patient', 'appointment',)
#   autocomplete_except = []  # disable adding autocomplete_fields for listed fields
#   autocomplete_all = False  # disable automatic adding of autocomplete_fields at all
    autocomplete_fields = ['patient', ]  # must be a foreign key or a many-to-many field.
    ModelAdmin.ordering = ('id',)

#    def save_model(self, request, obj, form, change):
#        if not obj.patient.id:
#        if not change:
#            obj.patient = request.user
#        obj.save()

#    def get_form(self, request, obj=None, **kwargs):
#        form = super(AppointmentAdmin, self).get_form(request, obj, **kwargs)
#        form.base_fields['patient'].label_from_instance = lambda obj: "{} {}".format(obj.id, obj.ic_number)
#        return form

class DressingAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'patient',
        'date',
        'time',
        'frequency_dressing',
        'wound_location',
        'type_dressing',
        'wound_location',
        'wound_condition',
        'photos',
        'image_img',
        'done_by',
    ]


class EnteralFeedingRegimeAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'patient',
        'time',
        'type_of_milk',
        'amount',
        'warm_water_before',
        'warm_water_after',
#        'total_fluids',
    ]


class MaintainanceAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'date',
        'items',
        'location_room',
        'reported_by',
        'status',
    ]
    ModelAdmin.ordering = ('id',)


class MedicationAdministrationRecordAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'patient',
        'allergy',
        'medication_name',
        'medication_dosage',
        'medication_tab',
        'medication_frequency',
        'medication_route',
        'medication_date',
        'medication_time',
        'signature_nurse',
        'stat',
        'date_time',
        'given_by',
    ]
    ModelAdmin.ordering = ('id',)


class IntakeOutputChartAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'patient',
        'date',
        'time_intake',
        'intake_oral_type',
        'intake_oral_ml',
        'intake_parenteral_type',
        'intake_parenteral_ml',
        'intake_other_type',
        'intake_other_ml',
        'time_output',
        'output_urine_ml',
        'output_urine_cum',
        'output_gastric_ml',
        'output_other_type',
        'output_other_ml',
    ]
    ModelAdmin.ordering = ('id',)


class OvertimeClaimAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'patient',
        'date',
        'duration_time',
        'hours',
        'checked_sign_by',
        'verify_by',
    ]
    autocomplete_fields = ['patient', ]
    ModelAdmin.ordering = ('id',)


admin.site.register(Admission, AdmissionAdmin)
admin.site.register(ApplicationForHomeLeave, ApplicationForHomeLeaveAdmin)
admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(CatheterizationCannulation)
admin.site.register(Charges)
admin.site.register(WoundCondition , MPTTModelAdmin)
#admin.site.register(WoundCondition, DraggableMPTTAdmin)
admin.site.register(Dressing, DressingAdmin)
admin.site.register(EnteralFeedingRegime, EnteralFeedingRegimeAdmin)
admin.site.register(HGTChart)
admin.site.register(IntakeOutputChart, IntakeOutputChartAdmin)
admin.site.register(Maintainance, MaintainanceAdmin)
admin.site.register(MedicationAdministrationRecord, MedicationAdministrationRecordAdmin)
admin.site.register(MedicationRecord)
admin.site.register(MiscellaneousChargesSlip)
admin.site.register(Nursing)
admin.site.register(OvertimeClaim, OvertimeClaimAdmin)
admin.site.register(PhysioProgressNote)
admin.site.register(PhysiotherapyGeneralAssessment)
admin.site.register(Stool)
admin.site.register(StaffRecords)
admin.site.register(VitalSignFlow)
admin.site.register(VisitingConsultant)
