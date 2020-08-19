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
		'admitted_others',
		'mode',

		'birth_date',
		'age',
		'gender',
		'marital_status',
		'marital_status_others',
		'religion',
		'religion_others',
		'occupation',
		'occupation_others',
		'communication_sight',
		'communication_hearing',
		'communication_hearing_others',
		'address',

		'ec_name',
		'ec_ic_number',
		'ec_relationship',
		'ec_phone',
		'ec_address',

		'general_condition',
		'vital_sign_temperature',
		'vital_sign_pulse',
		'vital_sign_bp',
		'vital_sign_resp',
		'vital_sign_spo2',
		'vital_sign_on_oxygen_therapy',
		'vital_sign_on_oxygen_therapy_flow_rate',
		'vital_sign_hgt',
		'allergy_drug',
		'allergy_food',
		'allergy_others',
		'biohazard_infectious_disease',
		'biohazard_infectious_disease_others',
		'invasive_line_insitu',
		'invasive_line_insitu_others',
		'medical_history',
		'medical_history_others',
		'surgical_history_none',
		'surgical_history',

		'date_diagnosis',
		'diagnosis',
		'date_operation',
		'operation',
		'own_medication',
		'own_medication_drug_name',
		'own_medication_dosage',
		'own_medication_tablet_capsule',
		'own_medication_frequency',

		'adaptive_aids_with_patient',
		'adaptive_aids_with_patient_others',
		'orientation',
		'special_information',
		'admission_by',
	]
#	form = AdmissionForm
#    autocomplete_fields = ['patient', ]
	ModelAdmin.ordering = ('id',)


class ApplicationForHomeLeaveAdmin(admin.ModelAdmin):
	list_display = [
		'id',
		'patient',
		'family_name',
		'family_ic_number',
		'family_relationship',
		'family_phone',
		'designation',
		'signature',
		'date',
	]
#    autocomplete_fields = ['patient', ]
	ModelAdmin.ordering = ('id',)

class AppointmentAdmin(admin.ModelAdmin):
#   form = AppointmentForm
	list_display = [
		'id',
		'patient',
#        'ic_number',
#		'date',
#		'time',
		'date_time',
		'hospital_clinic_center',
		'department',
		'planning_investigation',
		'treatment_order',
	]

#	list_filter = (
#		'patient',
#		'date_time',
#		'hospital_clinic_center',
#		'department',
#		'planning_investigation',
#		'treatment_order',
#	)

#   search_fields = ['patient']
#    list_filter = ['patient']
#    readonly_fields = ('patient', 'appointment',)
#   autocomplete_except = []  # disable adding autocomplete_fields for listed fields
#   autocomplete_all = False  # disable automatic adding of autocomplete_fields at all
#    autocomplete_fields = ['patient', ]  # must be a foreign key or a many-to-many field.
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
class NasogastricAdmin(admin.ModelAdmin):
	list_display = [
		'id',
		'patient',
		'nasogastric_tube_date',
		'nasogastric_tube_size',
		'nasogastric_tube_type',
		'nasogastric_tube_location',
		'nasogastric_tube_due_date',
		'nasogastric_tube_inserted_by',
	]
	ModelAdmin.ordering = ('id',)


class UrinaryAdmin(admin.ModelAdmin):
	list_display = [
		'id',
		'patient',
		'urinary_catheter_date',
		'urinary_catheter_size',
		'urinary_catheter_type',
		'urinary_catheter_due_date',
		'urinary_catheter_inserted_by',
	]
	ModelAdmin.ordering = ('id',)



class CannulaAdmin(admin.ModelAdmin):
	list_display = [
		'id',
		'patient',
		'cannula_date',
		'cannula_size',
		'cannula_location',
		'cannula_due_date',
	]
	ModelAdmin.ordering = ('id',)



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
	ModelAdmin.ordering = ('id',)
#	inlines = [
#        WoundConditionDataAdmin,
#    ]


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
	ModelAdmin.ordering = ('id',)


class HGTAdmin(admin.ModelAdmin):
	list_display = [
		'id',
		'patient',
		'date',
		'time',
		'blood_glucose_reading',
		'remark',
		'done_by',
	]
	ModelAdmin.ordering = ('id',)


class MaintenanceAdmin(admin.ModelAdmin):
	list_display = [
		'id',
		'patient',
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
		'medicationstat_date_time',
		'given_by',
	]
	ModelAdmin.ordering = ('id',)


class IntakeOutputAdmin(admin.ModelAdmin):
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
		'total_hours',
		'checked_sign_by',
		'verify_by',
	]
	ModelAdmin.ordering = ('id',)


admin.site.register(Admission, AdmissionAdmin)
admin.site.register(ApplicationForHomeLeave, ApplicationForHomeLeaveAdmin)
admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Nasogastric, NasogastricAdmin)
admin.site.register(Urinary, UrinaryAdmin)
admin.site.register(Cannula, CannulaAdmin)
admin.site.register(Dressing, DressingAdmin)
admin.site.register(EnteralFeedingRegime, EnteralFeedingRegimeAdmin)
admin.site.register(HGT, HGTAdmin)
admin.site.register(IntakeOutput, IntakeOutputAdmin)
admin.site.register(Maintenance, MaintenanceAdmin)
admin.site.register(MedicationAdministrationRecord, MedicationAdministrationRecordAdmin)
admin.site.register(MedicationRecord)
admin.site.register(Multipurpose)
admin.site.register(MiscellaneousChargesSlip)
admin.site.register(Nursing)
admin.site.register(OvertimeClaim, OvertimeClaimAdmin)
admin.site.register(PhysioProgressNoteBack)
admin.site.register(PhysioProgressNoteFront)
admin.site.register(PhysiotherapyGeneralAssessment)
admin.site.register(Stool)
admin.site.register(VitalSignFlow)
admin.site.register(VisitingConsultant)
