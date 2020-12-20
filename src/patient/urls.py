from django.urls import path, path

from .models import *
from .views import *

from patient.Views.admission import *
from patient.Views.appointment import *
from patient.Views.cannula import *
from patient.Views.dressing import *
from patient.Views.discharge_checklist import *
from patient.Views.enteral_feeding_regime import *
from patient.Views.hgt import *
from patient.Views.application_home_leave import *
from patient.Views.intake_output import *
from patient.Views.investigation_report import *
from patient.Views.maintenance import *
from patient.Views.medication_administration import *
from patient.Views.medication_administration_template import *
from patient.Views.medication_record import *
from patient.Views.miscellaneous_charges_slip import *
from patient.Views.multi_purpose import *
from patient.Views.nasogastric import *
from patient.Views.nursing import *
from patient.Views.physio_progress_note_sheet import *
from patient.Views.physiotherapy_general_assessment import *
from patient.Views.stool import *
from patient.Views.urinary import *
from patient.Views.visiting_consultant import *
from patient.Views.vital_sign_flow import *


app_name = 'patient'

urlpatterns = [
    path('', patientdata_list, name='patientdata_list'),
    #    path('', PatientListView.as_view(), name='patientdata_list'),
    #    path('(?P<id>\d+)', patientdata_detail, name='patientdata_detail'),
    path('<str:username>/', patientdata_detail, name='patientdata_detail'),
    #    path('patient/', patientdata_list, name='patientdata_list'),
    #    path('patient/create', patientdata_create, name='patientdata_create'),
    #    path('patient/<int:pk>/delete', patientdata_delete, name='patientdata_delete'),
    path('load_ic_number', load_ic_number, name='load_ic_number'),
    path('load_relationship', load_relationship, name='load_relationship'),
    path('load_phone', load_phone, name='load_phone'),
    path('load_signature', load_signature, name='load_signature'),

    #    path('admission/<username>/', admission, name='admission_create'),
    path('<str:username>/admission/view', admission_list, name='admission_list'),
    path('<str:username>/appointment/view', appointment_list, name='appointment_list'),
    path('<str:username>/cannula/view', cannula_list, name='cannula_list'),
    path('<str:username>/discharge-checklist/view', discharge_checklist_list, name='discharge_checklist_list'),
    path('<str:username>/dressing/view', dressing_list, name='dressing_list'),
    path('<str:username>/enteral-feeding-regime/view', enteral_feeding_regime_list, name='enteral_feeding_regime_list'),
    path('<str:username>/hgt/view', hgt_list, name='hgt_list'),
    path('<str:username>/application-home-leave/view', application_home_leave_list, name='application_home_leave_list'),
    path('<str:username>/intake-output/view', intake_output_list, name='intake_output_list'),
    path('<str:username>/investigation-report/view', investigation_report_list, name='investigation_report_list'),
    path('<str:username>/maintenance/view', maintenance_list, name='maintenance_list'),
    path('<str:username>/medication-administration/view', medication_administration_list, name='medication_administration_list'),
    path('<str:username>/medication-administration-template/view', medication_administration_template_list, name='medication_administration_template_list'),
    path('<str:username>/medication-record/view', medication_record_list, name='medication_record_list'),
    path('<str:username>/miscellaneous-charges-slip/view', miscellaneous_charges_slip_list, name='miscellaneous_charges_slip_list'),
    path('<str:username>/multi-purpose/view', multi_purpose_list, name='multi_purpose_list'),
    path('<str:username>/nasogastric/view', nasogastric_list, name='nasogastric_list'),
    path('<str:username>/nursing/view', nursing_list, name='nursing_list'),
    path('<str:username>/physio-progress-note-sheet/view', physio_progress_note_sheet_list, name='physio_progress_note_sheet_list'),
    path('<str:username>/physiotherapy-general-assessment/view', physiotherapy_general_assessment_list, name='physiotherapy_general_assessment_list'),
    path('<str:username>/stool/view', stool_list, name='stool_list'),
    path('<str:username>/urinary/view', urinary_list, name='urinary_list'),
    path('<str:username>/visiting-consultant/view', visiting_consultant_list, name='visiting_consultant_list'),
    path('<str:username>/vital-sign-flow/view', vital_sign_flow_list, name='vital_sign_flow_list'),


    path('<str:username>/admission/create', admission_create, name='admission_create'),
    path('<str:username>/application-application-home-leave/create', application_home_leave_create, name='application_home_leave_create'),
    #   path('<str:username>/application-application-home-leave/<username>/autocomplete/', autocomplete.Select2QuerySetView.as_view()_create, name='autocomplete_application_home_leave_create'),
    path('<str:username>/appointment/create', appointment_create, name='appointment_create'),
    path('<str:username>/cannula/create', cannula_create, name='cannula_create'),
    path('<str:username>/discharge-checklist/create', discharge_checklist_create, name='discharge_checklist_create'),
    path('<str:username>/dressing/create', dressing_create, name='dressing_create'),
    path('<str:username>/enteral-feeding-regime/create', enteral_feeding_regime_create, name='enteral_feeding_regime_create'),
    path('<str:username>/hgt/create', hgt_create, name='hgt_create'),
    path('<str:username>/intake-output/create', intake_output_create, name='intake_output_create'),
    path('<str:username>/investigation-report/create', investigation_report_create, name='investigation_report_create'),
    path('<str:username>/maintenance/create', maintenance_create, name='maintenance_create'),
    path('<str:username>/medication-administration/create', medication_administration_create, name='medication_administration_create'),
    path('<str:username>/medication-administration-template/create', medication_administration_template_create, name='medication_administration_template_create'),
    path('<str:username>/medication-record/create', medication_record_create, name='medication_record_create'),
    path('<str:username>/miscellaneous-charges-slip/create', miscellaneous_charges_slip_create, name='miscellaneous_charges_slip_create'),
    path('<str:username>/multi-purpose/create', multi_purpose_create, name='multi_purpose_create'),
    path('<str:username>/nasogastric/create', nasogastric_create, name='nasogastric_create'),
    path('<str:username>/nursing/create', nursing_create, name='nursing_create'),
    path('<str:username>/physio-progress-note-sheet/create', physio_progress_note_sheet_create, name='physio_progress_note_sheet_create'),
    path('<str:username>/physiotherapy-general-assessment/create', physiotherapy_general_assessment_create, name='physiotherapy_general_assessment_create'),
    path('<str:username>/stool/create', stool_create, name='stool_create'),
    path('<str:username>/urinary/create', urinary_create, name='urinary_create'),
    path('<str:username>/visiting-consultant/create', visiting_consultant_create, name='visiting_consultant_create'),
    path('<str:username>/vital-sign-flow/create', vital_sign_flow_create, name='vital_sign_flow_create'),


    path('<str:username>/admission/<int:pk>/edit', admission_edit, name='admission_edit'),
    path('<str:username>/appointment/<int:pk>/edit', appointment_edit, name='appointment_edit'),
    path('<str:username>/cannula/<int:pk>/edit', cannula_edit, name='cannula_edit'),
    path('<str:username>/discharge-checklist/<int:pk>/edit', discharge_checklist_edit, name='discharge_checklist_edit'),
    path('<str:username>/dressing/<int:pk>/edit', dressing_edit, name='dressing_edit'),
    path('<str:username>/enteral-feeding-regime/<int:pk>/edit', enteral_feeding_regime_edit, name='enteral_feeding_regime_edit'),
    path('<str:username>/hgt/<int:pk>/edit', hgt_edit, name='hgt_edit'),
    path('<str:username>/application-home-leave/<int:pk>/edit', application_home_leave_edit, name='application_home_leave_edit'),
    path('<str:username>/intake-output/<int:pk>/edit', intake_output_edit, name='intake_output_edit'),
    path('<str:username>/investigation-report/<int:pk>/edit', investigation_report_edit, name='investigation_report_edit'),
    path('<str:username>/maintenance/<int:pk>/edit', maintenance_edit, name='maintenance_edit'),
    path('<str:username>/medication-administration/<int:pk>/edit', medication_administration_edit, name='medication_administration_edit'),
#    path('<str:username>/medication-administration-template/<int:pk>/edit', medication_administration_template_edit, name='medication_administration_template_edit'),
    path('<str:username>/medication-administration-template/<int:pk>/edit', medication_administration_template_edit_popup, name='medication_administration_template_edit'),
#    path('<str:username>/medication-administration-template/<int:pk>/edit', medication_administration_template_edit_formset, name='medication_administration_template_edit_formset'),
    path('<str:username>/medication-record/<int:pk>/edit', medication_record_edit, name='medication_record_edit'),
    path('<str:username>/miscellaneous-charges-slip/<int:pk>/edit', miscellaneous_charges_slip_edit, name='miscellaneous_charges_slip_edit'),
    path('<str:username>/multi-purpose/<int:pk>/edit', multi_purpose_edit, name='multi_purpose_edit'),
    path('<str:username>/nasogastric/<int:pk>/edit', nasogastric_edit, name='nasogastric_edit'),
    path('<str:username>/nursing/<int:pk>/edit', nursing_edit, name='nursing_edit'),
    path('<str:username>/physio-progress-note-sheet/<int:pk>/edit', physio_progress_note_sheet_edit, name='physio_progress_note_sheet_edit'),
    path('<str:username>/physiotherapy-general-assessment/<int:pk>/edit', physiotherapy_general_assessment_edit, name='physiotherapy_general_assessment_edit'),
    path('<str:username>/stool/<int:pk>/edit', stool_edit, name='stool_edit'),
    path('<str:username>/urinary/<int:pk>/edit', urinary_edit, name='urinary_edit'),
    path('<str:username>/visiting-consultant/<int:pk>/edit', visiting_consultant_edit, name='visiting_consultant_edit'),
    path('<str:username>/vital-sign-flow/<int:pk>/edit', vital_sign_flow_edit, name='vital_sign_flow_edit'),


    path('<str:username>/admission/<int:pk>/delete', admission_delete, name='admission_delete'),
    path('<str:username>/appointment/<int:pk>/delete', appointment_delete, name='appointment_delete'),
    path('<str:username>/cannula/<int:pk>/delete', cannula_delete, name='cannula_delete'),
    path('<str:username>/discharge-checklist/<int:pk>/delete', discharge_checklist_delete, name='discharge_checklist_delete'),
    path('<str:username>/dressing/<int:pk>/delete', dressing_delete, name='dressing_delete'),
    path('<str:username>/enteral-feeding-regime/<int:pk>/delete', enteral_feeding_regime_delete, name='enteral_feeding_regime_delete'),
    path('<str:username>/hgt/<int:pk>/delete', hgt_delete, name='hgt_delete'),
    path('<str:username>/application-home-leave/<int:pk>/delete', application_home_leave_delete, name='application_home_leave_delete'),
    path('<str:username>/intake-output/<int:pk>/delete', intake_output_delete, name='intake_output_delete'),
    path('<str:username>/investigation-report/<int:pk>/delete', investigation_report_delete, name='investigation_report_delete'),
    path('<str:username>/maintenance/<int:pk>/delete', maintenance_delete, name='maintenance_delete'),
    path('<str:username>/medication-administration/<int:pk>/delete', medication_administration_delete, name='medication_administration_delete'),
    path('<str:username>/medication-administration-template/<int:pk>/delete', medication_administration_template_delete, name='medication_administration_template_delete'),
    path('<str:username>/medication-record/<int:pk>/delete', medication_record_delete, name='medication_record_delete'),
    path('<str:username>/miscellaneous-charges-slip/<int:pk>/delete', miscellaneous_charges_slip_delete, name='miscellaneous_charges_slip_delete'),
    path('<str:username>/multi-purpose/<int:pk>/delete', multi_purpose_delete, name='multi_purpose_delete'),
    path('<str:username>/nasogastric/<int:pk>/delete', nasogastric_delete, name='nasogastric_delete'),
    path('<str:username>/nursing/<int:pk>/delete', nursing_delete, name='nursing_delete'),
    path('<str:username>/physio-progress-note-sheet/<int:pk>/delete', physio_progress_note_sheet_delete, name='physio_progress_note_sheet_delete'),
    path('<str:username>/physiotherapy-general-assessment/<int:pk>/delete', physiotherapy_general_assessment_delete, name='physiotherapy_general_assessment_delete'),
    path('<str:username>/stool/<int:pk>/delete', stool_delete, name='stool_delete'),
    path('<str:username>/urinary/<int:pk>/delete', urinary_delete, name='urinary_delete'),
    path('<str:username>/visiting-consultant/<int:pk>/delete', visiting_consultant_delete, name='visiting_consultant_delete'),
    path('<str:username>/vital-sign-flow/<int:pk>/delete', vital_sign_flow_delete, name='vital_sign_flow_delete'),

    path('<str:username>/application-home-leave/pdf', application_home_leave_pdf, name='application_home_leave_pdf'),
]
