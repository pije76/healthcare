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
		'admitted_admission',
#		'admitted_others',
		'mode_admission',

		'ic_number',
#		'ic_upload',
		'image_img',
		'birth_date',
		'age',
		'gender',
		'marital_status',
		'religion',
		'occupation',
		'communication_sight',
		'communication_hearing',
		'address',

		'general_condition',
		'vital_sign_temperature',
		'vital_sign_pulse',
		'vital_sign_bp_upper',
		'vital_sign_bp_lower',
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
#		'surgical_history_none',
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
	autocomplete_fields = ['patient', ]
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
	autocomplete_fields = ['patient', ]
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


class CannulaAdmin(admin.ModelAdmin):
	list_display = [
		'id',
		'patient',
		'cannula_date',
		'cannula_size',
		'cannula_location',
		'cannula_due_date',
	]
	autocomplete_fields = ['patient', ]
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
#		'photos',
		'image_img',
		'done_by',
	]
	autocomplete_fields = ['patient', ]
	ModelAdmin.ordering = ('id',)


class DischargeCheckListAdmin(admin.ModelAdmin):
	list_display = [
		'id',
		'patient',
		'date_time',
		'discharge_status',
		'nasogastric_tube_date',
		'nasogastric_tube',
		'urinary_catheter_date',
		'nasogastric_tube',
		'urinary_catheter_date',
		'urinary_catheter',
		'surgical_dressing_intact',
		'spectacle_walking_aid_denture',
		'appointment_card_returned',
		'own_medication_return',
		'medication_reconcilation',
		'medication_reconcilation_patient',
		'given_by',
	]
	autocomplete_fields = ['patient', ]
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
	autocomplete_fields = ['patient', ]
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
	autocomplete_fields = ['patient', ]
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
		'output_urine_type',
		'output_urine_ml',
		'output_gastric_ml',
		'output_other_type',
		'output_other_ml',
	]
	autocomplete_fields = ['patient', ]
	ModelAdmin.ordering = ('id',)


class InvestigationReportAdmin(admin.ModelAdmin):
	list_display = [
		'id',
		'patient',
		'date',
#		'file_upload',
		'image_img',
	]
	autocomplete_fields = ['patient', ]
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
	autocomplete_fields = ['patient', ]
	ModelAdmin.ordering = ('id',)


class MedicationAdministrationRecordAdmin(admin.ModelAdmin):
	list_display = [
		'id',
		'patient',
#		'allergy',
		'allergy_drug',
		'allergy_food',
		'allergy_others',
		'medication_date',
		'medication_time',
		'medication_drug_name',
		'medication_dosage',
		'medication_unit',
		'medication_tablet_capsule',
		'medication_frequency',
		'medication_source',
		'medication_route',
		'medication_status',
		'medication_done',
	]
	autocomplete_fields = ['patient', ]
	ModelAdmin.ordering = ('id',)


class MedicationAdministrationRecordTemplateAdmin(admin.ModelAdmin):
	list_display = [
		'id',
		'patient',
		'own_medication',
		'medication_time',
		'medication_drug_name',
		'medication_dosage',
		'medication_unit',
		'medication_tablet_capsule',
		'medication_frequency',
	]
	autocomplete_fields = ['patient', ]
	ModelAdmin.ordering = ('id',)


class MedicationRecordAdmin(admin.ModelAdmin):
	list_display = [
		'id',
		'patient',
		'date',
		'time',
		'medication_drug_name',
		'dosage',
		'unit',
		'topup',
		'balance',
		'remark',
		'staff',
	]
	autocomplete_fields = ['patient', ]
	ModelAdmin.ordering = ('id',)


class MultipurposeAdmin(admin.ModelAdmin):
	list_display = [
		'id',
		'patient',
		'date_time',
		'symptom',
		'remark',
	]
	autocomplete_fields = ['patient', ]
	ModelAdmin.ordering = ('id',)


class MiscellaneousChargesSlipAdmin(admin.ModelAdmin):
	list_display = [
		'id',
		'patient',
		'date',
		'items_procedures',
		'unit',
		'amount',
		'given_by',
	]
	autocomplete_fields = ['patient', ]
	ModelAdmin.ordering = ('id',)


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
	autocomplete_fields = ['patient', ]
	ModelAdmin.ordering = ('id',)


class NursingAdmin(admin.ModelAdmin):
	list_display = [
		'id',
		'patient',
		'date_time',
		'report',
	]
	autocomplete_fields = ['patient', ]
	ModelAdmin.ordering = ('id',)


class PhysioProgressNoteSheetAdmin(admin.ModelAdmin):
	list_display = [
		'id',
		'patient',
		'date_time',
		'report',
	]
	autocomplete_fields = ['patient', ]
	ModelAdmin.ordering = ('id',)


class PhysiotherapyGeneralAssessmentAdmin(admin.ModelAdmin):
	list_display = [
		'id',
		'patient',
		'doctor_diagnosis',
		'doctor_management',
		'problem',
#		'front_body',
		'front_body_img',
#		'back_body',
		'back_body_img',
		'pain_scale',
	]
	autocomplete_fields = ['patient', ]
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
	autocomplete_fields = ['patient', ]
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
	autocomplete_fields = ['patient', ]
	ModelAdmin.ordering = ('id',)


class VitalSignFlowAdmin(admin.ModelAdmin):
	list_display = [
		'id',
		'patient',
		'date',
		'time',
		'temp',
		'pulse',
		'blood_pressure_systolic',
		'blood_pressure_diastolic',
		'respiration',
		'spo2_percentage',
		'spo2_o2',
	]
	autocomplete_fields = ['patient', ]
	ModelAdmin.ordering = ('id',)


class VisitingConsultantAdmin(admin.ModelAdmin):
	list_display = [
		'id',
		'patient',
		'date_time',
		'complaints',
		'treatment_orders',
		'consultant',
	]
	autocomplete_fields = ['patient', ]
	ModelAdmin.ordering = ('id',)


admin.site.register(Admission, AdmissionAdmin)
admin.site.register(ApplicationForHomeLeave, ApplicationForHomeLeaveAdmin)
admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Cannula, CannulaAdmin)
admin.site.register(DischargeCheckList, DischargeCheckListAdmin)
admin.site.register(Dressing, DressingAdmin)
admin.site.register(EnteralFeedingRegime, EnteralFeedingRegimeAdmin)
admin.site.register(HGT, HGTAdmin)
admin.site.register(IntakeOutput, IntakeOutputAdmin)
admin.site.register(InvestigationReport, InvestigationReportAdmin)
admin.site.register(Maintenance, MaintenanceAdmin)
admin.site.register(MedicationAdministrationRecord, MedicationAdministrationRecordAdmin)
admin.site.register(MedicationAdministrationRecordTemplate, MedicationAdministrationRecordTemplateAdmin)
admin.site.register(MedicationRecord, MedicationRecordAdmin)
admin.site.register(MiscellaneousChargesSlip, MiscellaneousChargesSlipAdmin)
admin.site.register(Multipurpose, MultipurposeAdmin)
admin.site.register(Nasogastric, NasogastricAdmin)
admin.site.register(Nursing, NursingAdmin)
admin.site.register(PhysioProgressNoteSheet, PhysioProgressNoteSheetAdmin)
admin.site.register(PhysiotherapyGeneralAssessment, PhysiotherapyGeneralAssessmentAdmin)
admin.site.register(Stool, StoolAdmin)
admin.site.register(Urinary, UrinaryAdmin)
admin.site.register(VisitingConsultant, VisitingConsultantAdmin)
admin.site.register(VitalSignFlow, VitalSignFlowAdmin)
