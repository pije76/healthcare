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

from accounts.models import UserProfile
from .models import *
from .forms import *


#class PatientDataAdmin(admin.StackedInline):
#	model = UserProfile
#    max_num = 1
#    extra = 1

#class AdmissionInline(admin.TabularInline):
#	model = UserProfile


#class PatientDataAdmin(admin.ModelAdmin):
#	inlines = [
#		AdmissionInline,
#	]


#@admin.register(Admission)
# class AdmissionAdmin(AjaxSelectAdmin):
#    form = AdmissionForm
class AdmissionAdmin(admin.ModelAdmin):
	list_display = [
		'id',
		'patient',
		'date_admission',
		'time_admission',
		'admitted',
#		'admitted_others',
		'mode',

		'general_condition',
		'vital_sign_temperature',
		'vital_sign_pulse',
		'vital_sign_bp',
		'vital_sign_resp',
		'vital_sign_spo2',
		'vital_sign_on_oxygen_therapy',
		'vital_sign_on_oxygen_therapy_flow_rate',
		'vital_sign_hgt',
		'biohazard_infectious_disease',
#		'biohazard_infectious_disease_others',
		'invasive_line_insitu',
#		'invasive_line_insitu_others',
		'medical_history',
#		'medical_history_others',
		'surgical_history_none',
		'surgical_history',

		'date_diagnosis',
		'diagnosis',
		'date_operation',
		'operation',

		'adaptive_aids_with_patient',
#		'adaptive_aids_with_patient_others',
		'orientation',
		'special_information',
		'admission_by',
	]
#	form = AdmissionForm
#    autocomplete_fields = ['patient', ]
	ModelAdmin.ordering = ('id',)
#	inlines = [
#		PatientDataAdmin,
#	]


class ApplicationForHomeLeaveAdmin(admin.ModelAdmin):
	list_display = [
		'id',
		'patient',
		'family_name',
		'family_ic_number',
		'family_relationship',
		'family_phone',
		'witnessed_designation',
		'witnessed_signature',
		'witnessed_date',
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


class EnteralFeedingRegimeAdmin(admin.ModelAdmin):
	list_display = [
		'id',
		'patient',
		'date',
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


class MedicationAdmin(admin.ModelAdmin):
	list_display = [
		'id',
		'patient',
		'medication',
		'medication_drug_name',
		'medication_dosage',
		'medication_tablet_capsule',
		'medication_frequency',
	]
	ModelAdmin.ordering = ('id',)


class MedicationAdministrationRecordAdmin(admin.ModelAdmin):
	list_display = [
		'id',
		'patient',
		'allergy',
		'medication',
#		'medication_name',
#		'medication_dosage',
#		'medication_tab_cap_mls',
#		'medication_frequency',
#		'medication_route',
		'medication_date',
		'medication_time',
		'status_nurse',
		'done',
		'stat',
		'medicationstat_date_time',
		'given_by',
	]
	ModelAdmin.ordering = ('id',)


class NursingAdmin(admin.ModelAdmin):
	list_display = [
		'id',
		'patient',
		'date_time',
		'report',
	]
	ModelAdmin.ordering = ('id',)


class IntakeOutputAdmin(admin.ModelAdmin):
	list_display = [
		'id',
		'patient',
		'date',
		'time',
		'intake_oral_type',
		'intake_oral_ml',
		'intake_parenteral_type',
		'intake_parenteral_ml',
		'intake_other_type',
		'intake_other_ml',
		'output_urine_ml',
		'output_urine_cum',
		'output_gastric_ml',
		'output_other_type',
		'output_other_ml',
	]
	ModelAdmin.ordering = ('id',)


class InvestigationReportAdmin(admin.ModelAdmin):
	list_display = [
		'id',
		'patient',
		'date',
		'file_upload',
		'image_img',
	]
	ModelAdmin.ordering = ('id',)



class OvertimeClaimAdmin(admin.ModelAdmin):
	list_display = [
		'id',
		'patient',
		'date',
		'duration_time_from',
		'duration_time_to',
		'hours',
		'total_hours',
		'checked_sign_by',
		'verify_by',
	]
	ModelAdmin.ordering = ('id',)


class PhysiotherapyGeneralAssessmentAdmin(admin.ModelAdmin):
	list_display = [
		'id',
		'patient',
		'doctor_diagnosis',
		'doctor_management',
		'problem',
		'front_body',
		'front_body_img',
		'back_body',
		'back_body_img',
		'pain_scale',
	]
	ModelAdmin.ordering = ('id',)


class PhysioProgressNoteBackAdmin(admin.ModelAdmin):
	list_display = [
		'id',
		'patient',
		'date_time',
		'report',
	]
	ModelAdmin.ordering = ('id',)


class StoolAdmin(admin.ModelAdmin):
	list_display = [
		'id',
		'patient',
		'time',
		'frequency',
		'consistency',
		'amount',
		'remark',
		'done_by',
	]
	ModelAdmin.ordering = ('id',)


class AllergyAdmin(admin.ModelAdmin):
	list_display = [
		'id',
		'patient',
		'allergy_drug',
		'allergy_food',
		'allergy_others',
	]
	ModelAdmin.ordering = ('id',)


admin.site.register(Admission, AdmissionAdmin)
admin.site.register(Allergy, AllergyAdmin)
admin.site.register(ApplicationForHomeLeave, ApplicationForHomeLeaveAdmin)
admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Cannula, CannulaAdmin)
admin.site.register(Dressing, DressingAdmin)
admin.site.register(EnteralFeedingRegime, EnteralFeedingRegimeAdmin)
admin.site.register(HGT, HGTAdmin)
admin.site.register(IntakeOutput, IntakeOutputAdmin)
admin.site.register(InvestigationReport, InvestigationReportAdmin)
admin.site.register(Maintenance, MaintenanceAdmin)
admin.site.register(Medication, MedicationAdmin)
admin.site.register(MedicationAdministrationRecord, MedicationAdministrationRecordAdmin)
admin.site.register(MedicationRecord)
admin.site.register(Multipurpose)
admin.site.register(MiscellaneousChargesSlip)
admin.site.register(Nasogastric, NasogastricAdmin)
admin.site.register(Nursing, NursingAdmin)
admin.site.register(OvertimeClaim, OvertimeClaimAdmin)
admin.site.register(PhysioProgressNoteBack, PhysioProgressNoteBackAdmin)
admin.site.register(PhysioProgressNoteFront)
admin.site.register(PhysiotherapyGeneralAssessment, PhysiotherapyGeneralAssessmentAdmin)
admin.site.register(Stool, StoolAdmin)
admin.site.register(Urinary, UrinaryAdmin)
admin.site.register(VitalSignFlow)
admin.site.register(VisitingConsultant)
