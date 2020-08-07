from django.urls import path, re_path

from .models import *
from .views import *

from patient_data.Views.admission_data import *
from patient_data.Views.homeleave_data import *
from patient_data.Views.appointment_data import *
from patient_data.Views.cannulation_data import *
from patient_data.Views.charges_sheet_data import *
from patient_data.Views.dressing_data import *
from patient_data.Views.enteral_feeding_regime_data import *
from patient_data.Views.hgt_chart_data import *
from patient_data.Views.intake_output_data import *
from patient_data.Views.maintainance_data import *
from patient_data.Views.medication_administration_data import *
from patient_data.Views.medication_data import *
from patient_data.Views.miscellaneous_charges_slip_data import *
from patient_data.Views.nursing_data import *
from patient_data.Views.overtime_claim_data import *
from patient_data.Views.physio_progress_note_data import *
from patient_data.Views.physiotherapy_general_assessment_data import *
from patient_data.Views.staff_records_data import *
from patient_data.Views.stool_data import *
from patient_data.Views.visiting_consultant_records_data import *
from patient_data.Views.vital_sign_flow_data import *



app_name = 'patient_data'

urlpatterns = [
    path('', patientdata_list, name='patientdata_list'),
#    path('', PatientListView.as_view(), name='patientdata_list'),
#    re_path(r'^(?P<id>\d+)', patientdata_detail, name='patientdata_detail'),
    re_path(r'^(?P<username>\w+)/$', patientdata_detail, name='patientdata_detail'),
#    re_path(r'^patient_data/$', patientdata_list, name='patientdata_list'),
#    re_path(r'^patient_data/create', patientdata_create, name='patientdata_create'),
#    re_path(r'^patient_data/(?P<pk>\d+)/delete', patientdata_delete, name='patientdata_delete'),
    re_path(r'^(?P<username>\w+)/admission/$', admission_data, name='admission_data'),
    re_path(r'^(?P<username>\w+)/homeleave/$', homeleave_data, name='homeleave_data'),
    re_path(r'^(?P<username>\w+)/appointment/$', appointment_data, name='appointment_data'),
    re_path(r'^(?P<username>\w+)/catheterization-cannulation/$', cannulation_data, name='cannulation_data'),
    re_path(r'^(?P<username>\w+)/charges/$', charges_sheet_data, name='charges_sheet_data'),
    re_path(r'^(?P<username>\w+)/dressing/$', dressing_data, name='dressing_data'),
    re_path(r'^(?P<username>\w+)/enteral-feeding-regime/$', enteral_feeding_regime_data, name='enteral_feeding_regime_data'),
    re_path(r'^(?P<username>\w+)/hgt-chart/$', hgt_chart_data, name='hgt_chart_data'),
    re_path(r'^(?P<username>\w+)/intake-output/$', intake_output_data, name='intake_output_data'),
    re_path(r'^(?P<username>\w+)/maintainance/$', maintainance_data, name='maintainance_data'),
    re_path(r'^(?P<username>\w+)/medication-administration/$', medication_administration_data, name='medication_administration_data'),
    re_path(r'^(?P<username>\w+)/medication/$', medication_data, name='medication_data'),
    re_path(r'^(?P<username>\w+)/miscellaneous-charges-slip/$', miscellaneous_charges_slip, name='miscellaneous_charges_slip'),
    re_path(r'^(?P<username>\w+)/nursing/$', nursing_data, name='nursing_data'),
    re_path(r'^(?P<username>\w+)/overtime-claim/$', overtime_claim, name='overtime_claim'),
    re_path(r'^(?P<username>\w+)/physio-progress-note/$', physio_progress_note_data, name='physio_progress_note_data'),
    re_path(r'^(?P<username>\w+)/physiotherapy-general-assessment/$', physiotherapy_general_assessment_data, name='physiotherapy_general_assessment_data'),
    re_path(r'^(?P<username>\w+)/staff-records/$', staff_records, name='staff_records'),
    re_path(r'^(?P<username>\w+)/stool/$', stool_data, name='stool_data'),
    re_path(r'^(?P<username>\w+)/visiting-consultant-records/$', visiting_consultant_records, name='visiting_consultant_records'),
    re_path(r'^(?P<username>\w+)/vital-sign-flow/$', vital_sign_flow_data, name='vital_sign_flow_data'),


#    re_path(r'^(?P<username>\w+)/admission/(?P<id>\d+)/edit', admission_data_edit, name='admission_data_edit'),
    re_path(r'^(?P<username>\w+)/admission/(?P<pk>\d+)/edit', AdmissionUpdateView.as_view(), name='admission_data_edit'),
#    re_path(r'^admission/(?P<id>\d+)/delete', admission_data_delete, name='admission_data_delete'),
    re_path(r'^(?P<username>\w+)/admission/(?P<pk>\d+)/delete', AdmissionDeleteView.as_view(), name='admission_data_delete'),

    re_path(r'^(?P<username>\w+)/homeleave/(?P<id>\d+)/edit', homeleave_data_edit, name='homeleave_data_edit'),
    re_path(r'^homeleave/(?P<id>\d+)/delete', homeleave_data_delete, name='homeleave_data_delete'),

#    re_path(r'^(?P<username>\w+)/appointment/(?P<id>\d+)/edit', appointment_data_edit, name='appointment_data_edit'),
    re_path(r'^(?P<username>\w+)/appointment/(?P<pk>\d+)/edit', AppointmentUpdateView.as_view(), name='appointment_data_edit'),
#    re_path(r'^(?P<username>\w+)/appointment/(?P<id>\d+)/delete', appointment_data_delete, name='appointment_data_delete'),
    re_path(r'^(?P<username>\w+)/appointment/(?P<pk>\d+)/delete', AppointmentDeleteView.as_view(), name='appointment_data_delete'),

    re_path(r'^(?P<username>\w+)/catheterization-cannulation/(?P<id>\d+)/edit', cannulation_data_edit, name='cannulation_data_edit'),
    re_path(r'^catheterization-cannulation/(?P<id>\d+)/delete', cannulation_data_delete, name='cannulation_data_delete'),

    re_path(r'^(?P<username>\w+)/charges/(?P<id>\d+)/edit', charges_sheet_data_edit, name='charges_sheet_data_edit'),
    re_path(r'^charges/(?P<id>\d+)/delete', charges_sheet_data_delete, name='charges_sheet_data_delete'),

    re_path(r'^(?P<username>\w+)/dressing/(?P<id>\d+)/edit', dressing_data_edit, name='dressing_data_edit'),
    re_path(r'^dressing/(?P<id>\d+)/delete', dressing_data_delete, name='dressing_data_delete'),

    re_path(r'^(?P<username>\w+)/enteral-feeding-regime/(?P<id>\d+)/edit', enteral_feeding_regime_data_edit, name='enteral_feeding_regime_data_edit'),
    re_path(r'^enteral-feeding-regime/(?P<id>\d+)/delete', enteral_feeding_regime_data_delete, name='enteral_feeding_regime_data_delete'),

    re_path(r'^(?P<username>\w+)/hgt-chart/(?P<id>\d+)/edit', hgt_chart_data_edit, name='hgt_chart_data_edit'),
    re_path(r'^hgt-chart/(?P<id>\d+)/delete', hgt_chart_data_delete, name='hgt_chart_data_delete'),

    re_path(r'^(?P<username>\w+)/intake-output/(?P<id>\d+)/edit', intake_output_data_edit, name='intake_output_data_edit'),
    re_path(r'^intake-output/(?P<id>\d+)/delete', intake_output_data_delete, name='intake_output_data_delete'),

    re_path(r'^(?P<username>\w+)/maintainance/(?P<id>\d+)/edit', maintainance_data_edit, name='maintainance_data_edit'),
    re_path(r'^maintainance/(?P<id>\d+)/delete', maintainance_data_delete, name='maintainance_data_delete'),

    re_path(r'^(?P<username>\w+)/medication-administration/(?P<id>\d+)/edit', medication_administration_data_edit, name='medication_administration_data_edit'),
    re_path(r'^medication-administration/(?P<id>\d+)/delete', medication_administration_data_delete, name='medication_administration_data_delete'),

    re_path(r'^(?P<username>\w+)/medication/(?P<id>\d+)/edit', medication_data_edit, name='medication_data_edit'),
    re_path(r'^medication/(?P<id>\d+)/delete', medication_data_delete, name='medication_data_delete'),

    re_path(r'^(?P<username>\w+)/miscellaneous-charges-slip/(?P<id>\d+)/edit', miscellaneous_charges_slip_data_edit, name='miscellaneous_charges_slip_data_edit'),
    re_path(r'^miscellaneous-charges-slip/(?P<id>\d+)/delete', miscellaneous_charges_slip_data_delete, name='miscellaneous_charges_slip_data_delete'),

    re_path(r'^(?P<username>\w+)/nursing/(?P<id>\d+)/edit', nursing_data_edit, name='nursing_data_edit'),
    re_path(r'^nursing/(?P<id>\d+)/delete', nursing_data_delete, name='nursing_data_delete'),

    re_path(r'^(?P<username>\w+)/overtime-claim/(?P<id>\d+)/edit', overtime_claim_data_edit, name='overtime_claim_data_edit'),
    re_path(r'^overtime-claim/(?P<id>\d+)/delete', overtime_claim_data_delete, name='overtime_claim_data_delete'),

    re_path(r'^(?P<username>\w+)/physio-progress-note/(?P<id>\d+)/edit', physio_progress_note_data_edit, name='physio_progress_note_data_edit'),
    re_path(r'^physio-progress-note/(?P<id>\d+)/delete', physio_progress_note_data_delete, name='physio_progress_note_data_delete'),

    re_path(r'^(?P<username>\w+)/physiotherapy-general-assessment/(?P<id>\d+)/edit', physiotherapy_general_assessment_data_edit, name='physiotherapy_general_assessment_data_edit'),
    re_path(r'^physiotherapy-general-assessment/(?P<id>\d+)/delete', physiotherapy_general_assessment_data_delete, name='physiotherapy_general_assessment_data_delete'),

    re_path(r'^(?P<username>\w+)/staff-records/(?P<id>\d+)/edit', staff_records_data_edit, name='staff_records_data_edit'),
    re_path(r'^staff-records/(?P<id>\d+)/delete', staff_records_data_delete, name='staff_records_data_delete'),

    re_path(r'^(?P<username>\w+)/stool/(?P<id>\d+)/edit', stool_data_edit, name='stool_data_edit'),
    re_path(r'^stool/(?P<id>\d+)/delete', stool_data_delete, name='stool_data_delete'),

    re_path(r'^(?P<username>\w+)/visiting-consultant-records/(?P<id>\d+)/edit', visiting_consultant_records_data_edit, name='visiting_consultant_records_data_edit'),
    re_path(r'^visiting-consultant-records/(?P<id>\d+)/delete', visiting_consultant_records_data_delete, name='visiting_consultant_records_data_delete'),

    re_path(r'^(?P<username>\w+)/vital-sign-flow/(?P<id>\d+)/edit', vital_sign_flow_data_edit, name='vital_sign_flow_data_edit'),
    re_path(r'^vital-sign-flow/(?P<id>\d+)/delete', vital_sign_flow_data_delete, name='vital_sign_flow_data_delete'),
]
