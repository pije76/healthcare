from django.urls import path, path

from .models import *
from .views import *

from patient.Views.admission import *
from patient.Views.appointment import *
from patient.Views.cannula import *
from patient.Views.dressing import *
from patient.Views.enteral_feeding_regime import *
from patient.Views.hgt import *
from patient.Views.application_home_leave import *
from patient.Views.intake_output import *
from patient.Views.investigationreport import *
from patient.Views.maintenance import *
from patient.Views.medication import *
from patient.Views.medication_administration import *
from patient.Views.miscellaneous_charges_slip import *
from patient.Views.multi_purpose import *
from patient.Views.nasogastric import *
from patient.Views.nursing import *
from patient.Views.overtime_claim import *
from patient.Views.physio_progress_note_back import *
from patient.Views.physio_progress_note_front import *
from patient.Views.physiotherapy_general_assessment import *
from patient.Views.stool import *
from patient.Views.urinary import *
from patient.Views.visiting_consultant_records import *
from patient.Views.vital_sign_flow import *


app_name = 'patient'

urlpatterns = [
    path('', patientdata_list, name='patientdata_list'),
#    path('', PatientListView.as_view(), name='patientdata_list'),
#    path('(?P<id>\d+)', patientdata_detail, name='patientdata_detail'),
    path('<username>/', patientdata_detail, name='patientdata_detail'),
#    path('patient/', patientdata_list, name='patientdata_list'),
#    path('patient/create', patientdata_create, name='patientdata_create'),
#    path('patient/<int:pk>/delete', patientdata_delete, name='patientdata_delete'),
    path('load_ic_number', load_ic_number, name='load_ic_number'),
    path('load_relationship', load_relationship, name='load_relationship'),
    path('load_phone', load_phone, name='load_phone'),
    path('load_signature', load_signature, name='load_signature'),

#    path('admission/<username>/', admission, name='admission_create'),
    path('<username>/admission/', admission_list, name='admission_list'),
    path('<username>/appointment/', appointment_list, name='appointment_list'),
    path('<username>/cannula/', cannula_list, name='cannula_list'),
    path('<username>/dressing/', dressing_list, name='dressing_list'),
    path('<username>/enteral-feeding-regime/', enteral_feeding_regime_list, name='enteral_feeding_regime_list'),
    path('<username>/hgt/', hgt_list, name='hgt_list'),
    path('<username>/application-home-leave/', application_home_leave_list, name='application_home_leave_list'),
    path('<username>/intake-output/', intake_output_list, name='intake_output_list'),
    path('<username>/investigationreport/', investigationreport_list, name='investigationreport_list'),
    path('<username>/maintenance/', maintenance_list, name='maintenance_list'),
    path('<username>/medication-administration/', medication_administration_list, name='medication_administration_list'),
    path('<username>/medication/', medication_list, name='medication_list'),
    path('<username>/miscellaneous-charges-slip/', miscellaneous_charges_slip_list, name='miscellaneous_charges_slip_list'),
    path('<username>/multi-purpose/', multi_purpose_list, name='multi_purpose_list'),
    path('<username>/nasogastric/', nasogastric_list, name='nasogastric_list'),
    path('<username>/nursing/', nursing_list, name='nursing_list'),
    path('<username>/overtime-claim/', overtime_claim_list, name='overtime_claim_list'),
    path('<username>/physio-progress-note-back/', physio_progress_note_back_list, name='physio_progress_note_back_list'),
    path('<username>/physio-progress-note-front/', physio_progress_note_front_list, name='physio_progress_note_front_list'),
    path('<username>/physiotherapy-general-assessment/', physiotherapy_general_assessment_list, name='physiotherapy_general_assessment_list'),
    path('<username>/stool/', stool_list, name='stool_list'),
    path('<username>/urinary/', urinary_list, name='urinary_list'),
    path('<username>/visiting-consultant-records/', visiting_consultant_records_list, name='visiting_consultant_records_list'),
    path('<username>/vital-sign-flow/', vital_sign_flow_list, name='vital_sign_flow_list'),


    path('admission/<username>/', admission_create, name='admission_create'),
    path('application-application-home-leave/<username>/', application_home_leave_create, name='application_home_leave_create'),
#   path('application-application-home-leave/<username>/autocomplete/', autocomplete.Select2QuerySetView.as_view()_create, name='autocomplete_application_home_leave_create'),
    path('appointment/<username>/', appointment_create, name='appointment_create'),
    path('cannula/<username>/', cannula_create, name='cannula_create'),
    path('dressing/<username>/', dressing_create, name='dressing_create'),
    path('enteral-feeding-regime/<username>/', enteral_feeding_regime_create, name='enteral_feeding_regime_create'),
    path('hgt/<username>/', hgt_create, name='hgt_create'),
    path('intake-output/<username>/', intake_output_create, name='intake_output_create'),
    path('investigationreport/<username>/', investigationreport_create, name='investigationreport_create'),
    path('maintenance/<username>/', maintenance_create, name='maintenance_create'),
    path('medication-administration/<username>/', medication_administration_create, name='medication_administration_create'),
    path('medication-record/<username>/', medication_record_create, name='medication_record_create'),
    path('miscellaneous-charges-slip/<username>/', miscellaneous_charges_slip_create, name='miscellaneous_charges_slip_create'),
    path('multi-purpose/<username>/', multi_purpose_create, name='multi_purpose_create'),
    path('nasogastric/<username>/', nasogastric_create, name='nasogastric_create'),
    path('nursing/<username>/', nursing_create, name='nursing_create'),
    path('overtime-claim/<username>/', overtime_claim_create, name='overtime_claim_create'),
    path('physio-progress-note-back/<username>/', physio_progress_note_back_create, name='physio_progress_note_back_create'),
    path('physio-progress-note-front/<username>/', physio_progress_note_front_create, name='physio_progress_note_front_create'),
    path('physiotherapy-general-assessment/<username>/', physiotherapy_general_assessment_create, name='physiotherapy_general_assessment_create'),
    path('stool/<username>/', stool_create, name='stool_create'),
    path('urinary/<username>/', urinary_create, name='urinary_create'),
    path('visiting-consultant-records/<username>/', visiting_consultant_records_create, name='visiting_consultant_records_create'),
    path('vital-sign-flow/<username>/', vital_sign_flow_create, name='vital_sign_flow_create'),


    path('<username>/admission/<int:pk>/edit', admission_edit, name='admission_edit'),
    path('<username>/appointment/<int:pk>/edit', appointment_edit, name='appointment_edit'),
    path('<username>/cannula/<int:pk>/edit', cannula_edit, name='cannula_edit'),
    path('<username>/dressing/<int:pk>/edit', dressing_edit, name='dressing_edit'),
    path('<username>/enteral-feeding-regime/<int:pk>/edit', enteral_feeding_regime_edit, name='enteral_feeding_regime_edit'),
    path('<username>/hgt/<int:pk>/edit', hgt_edit, name='hgt_edit'),
    path('<username>/application-home-leave/<int:pk>/edit', application_home_leave_edit, name='application_home_leave_edit'),
    path('<username>/intake-output/<int:pk>/edit', intake_output_edit, name='intake_output_edit'),
    path('<username>/investigationreport/<int:pk>/edit', investigationreport_edit, name='investigationreport_edit'),
    path('<username>/maintenance/<int:pk>/edit', maintenance_edit, name='maintenance_edit'),
    path('<username>/medication-administration/<int:pk>/edit', medication_administration_edit, name='medication_administration_edit'),
    path('<username>/medication/<int:pk>/edit', medication_edit, name='medication_edit'),
    path('<username>/miscellaneous-charges-slip/<int:pk>/edit', miscellaneous_charges_slip_edit, name='miscellaneous_charges_slip_edit'),
    path('<username>/multi-purpose/<int:pk>/edit', multi_purpose_edit, name='multi_purpose_edit'),
    path('<username>/nasogastric/<int:pk>/edit', nasogastric_edit, name='nasogastric_edit'),
    path('<username>/nursing/<int:pk>/edit', nursing_edit, name='nursing_edit'),
    path('<username>/overtime-claim/<int:pk>/edit', overtime_claim_edit, name='overtime_claim_edit'),
    path('<username>/physio-progress-note-back/<int:pk>/edit', physio_progress_note_back_edit, name='physio_progress_note_back_edit'),
    path('<username>/physio-progress-note-front/<int:pk>/edit', physio_progress_note_front_edit, name='physio_progress_note_front_edit'),
    path('<username>/physiotherapy-general-assessment/<int:pk>/edit', physiotherapy_general_assessment_edit, name='physiotherapy_general_assessment_edit'),
    path('<username>/stool/<int:pk>/edit', stool_edit, name='stool_edit'),
    path('<username>/urinary/<int:pk>/edit', urinary_edit, name='urinary_edit'),
    path('<username>/visiting-consultant-records/<int:pk>/edit', visiting_consultant_records_edit, name='visiting_consultant_records_edit'),
    path('<username>/vital-sign-flow/<int:pk>/edit', vital_sign_flow_edit, name='vital_sign_flow_edit'),


    path('<username>/admission/<int:pk>/delete', admission_delete, name='admission_delete'),
    path('<username>/appointment/<int:pk>/delete', appointment_delete, name='appointment_delete'),
    path('<username>/cannula/<int:pk>/delete', cannula_delete, name='cannula_delete'),
    path('<username>/dressing/<int:pk>/delete', dressing_delete, name='dressing_delete'),
    path('<username>/enteral-feeding-regime/<int:pk>/delete', enteral_feeding_regime_delete, name='enteral_feeding_regime_delete'),
    path('<username>/hgt/<int:pk>/delete', hgt_delete, name='hgt_delete'),
    path('<username>/application-home-leave/<int:pk>/delete', application_home_leave_delete, name='application_home_leave_delete'),
    path('<username>/intake-output/<int:pk>/delete', intake_output_delete, name='intake_output_delete'),
    path('<username>/investigationreport/<int:pk>/delete', investigationreport_delete, name='investigationreport_delete'),
    path('<username>/maintenance/<int:pk>/delete', maintenance_delete, name='maintenance_delete'),
    path('<username>/medication-administration/<int:pk>/delete', medication_administration_delete, name='medication_administration_delete'),
    path('<username>/medication/<int:pk>/delete', medication_delete, name='medication_delete'),
    path('<username>/miscellaneous-charges-slip/<int:pk>/delete', miscellaneous_charges_slip_delete, name='miscellaneous_charges_slip_delete'),
    path('<username>/multi-purpose/<int:pk>/delete', multi_purpose_delete, name='multi_purpose_delete'),
    path('<username>/nasogastric/<int:pk>/delete', nasogastric_delete, name='nasogastric_delete'),
    path('<username>/nursing/<int:pk>/delete', nursing_delete, name='nursing_delete'),
    path('<username>/overtime-claim/<int:pk>/delete', overtime_claim_delete, name='overtime_claim_delete'),
    path('<username>/physio-progress-note-back/<int:pk>/delete', physio_progress_note_back_delete, name='physio_progress_note_back_delete'),
    path('<username>/physio-progress-note-front/<int:pk>/delete', physio_progress_note_front_delete, name='physio_progress_note_front_delete'),
    path('<username>/physiotherapy-general-assessment/<int:pk>/delete', physiotherapy_general_assessment_delete, name='physiotherapy_general_assessment_delete'),
    path('<username>/stool/<int:pk>/delete', stool_delete, name='stool_delete'),
    path('<username>/urinary/<int:pk>/delete', urinary_delete, name='urinary_delete'),
    path('<username>/visiting-consultant-records/<int:pk>/delete', visiting_consultant_records_delete, name='visiting_consultant_records_delete'),
    path('<username>/vital-sign-flow/<int:pk>/delete', vital_sign_flow_delete, name='vital_sign_flow_delete'),

    path('<username>/application-home-leave/pdf', application_home_leave_pdf, name='application_home_leave_pdf'),
    path('<username>/overtime-claim/pdf', overtime_claim_pdf, name='overtime_claim_pdf'),

]
