from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import RedirectView

from . import views

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
from patient_data.Views.miscellaneous_charges_slip import *
from patient_data.Views.nursing_data import *
from patient_data.Views.overtime_claim import *
from patient_data.Views.physio_progress_note_data import *
from patient_data.Views.physiotherapy_general_assessment_data import *
from patient_data.Views.staff_records import *
from patient_data.Views.stool_data import *
from patient_data.Views.visiting_consultant_records import *
from patient_data.Views.vital_sign_flow_data import *



app_name = 'patient_data'

urlpatterns = [
    path('', patientdata_list, name='patientdata_list'),
    re_path(r'^(?P<id>\d+)', patientdata_detail, name='patientdata_detail'),
#    re_path(r'^patient_data/$', patientdata_list, name='patientdata_list'),
#    re_path(r'^patient_data/create', patientdata_create, name='patientdata_create'),
#    re_path(r'^patient_data/(?P<pk>\d+)/delete', patientdata_delete, name='patientdata_delete'),
    re_path(r'^admission/(?P<id>\d+)/$', admission_data, name='admission_data'),
    re_path(r'^homeleave/(?P<id>\d+)/$', homeleave_data, name='homeleave_data'),
    re_path(r'^appointment/(?P<id>\d+)/$', appointment_data, name='appointment_data'),
    re_path(r'^catheterization-cannulation/(?P<id>\d+)/$', cannulation_data, name='cannulation_data'),
    re_path(r'^charges/(?P<id>\d+)/$', charges_sheet_data, name='charges_sheet_data'),
    re_path(r'^dressing/(?P<id>\d+)/$', dressing_data, name='dressing_data'),
    re_path(r'^enteral-feeding-regime/(?P<id>\d+)/$', enteral_feeding_regime_data, name='enteral_feeding_regime_data'),
    re_path(r'^hgt-chart/(?P<id>\d+)/$', hgt_chart_data, name='hgt_chart_data'),
    re_path(r'^intake-output/(?P<id>\d+)/$', intake_output_data, name='intake_output_data'),
    re_path(r'^maintainance/(?P<id>\d+)/$', maintainance_data, name='maintainance_data'),
    re_path(r'^medication-administration/(?P<id>\d+)/$', medication_administration_data, name='medication_administration_data'),
    re_path(r'^medication/(?P<id>\d+)/$', medication_data, name='medication_data'),
    re_path(r'^miscellaneous-charges-slip/(?P<id>\d+)/$', miscellaneous_charges_slip, name='miscellaneous_charges_slip'),
    re_path(r'^nursing/(?P<id>\d+)/$', nursing_data, name='nursing_data'),
    re_path(r'^overtime-claim/(?P<id>\d+)/$', overtime_claim, name='overtime_claim'),
    re_path(r'^physio-progress-note/(?P<id>\d+)/$', physio_progress_note_data, name='physio_progress_note_data'),
    re_path(r'^physiotherapy-general-assessment/(?P<id>\d+)/$', physiotherapy_general_assessment_data, name='physiotherapy_general_assessment_data'),
    re_path(r'^staff-records/(?P<id>\d+)/$', staff_records, name='staff_records'),
    re_path(r'^stool/(?P<id>\d+)/$', stool_data, name='stool_data'),
    re_path(r'^visiting-consultant-records/(?P<id>\d+)/$', visiting_consultant_records, name='visiting_consultant_records'),
    re_path(r'^vital-sign-flow/(?P<id>\d+)/$', vital_sign_flow_data, name='vital_sign_flow_data'),

    re_path(r'^admission/(?P<id>\d+)/edit', admission_data_edit, name='admission_data_edit'),
    re_path(r'^admission/(?P<id>\d+)/delete', admission_data_delete, name='admission_data_delete'),

    re_path(r'^appointment/(?P<id>\d+)/edit', appointment_data_edit, name='appointment_data_edit'),
    re_path(r'^appointment/(?P<id>\d+)/delete', appointment_data_delete, name='appointment_data_delete'),

    re_path(r'^medication-administration/(?P<id>\d+)/edit', medication_administration_data_edit, name='medication_administration_data_edit'),
    re_path(r'^medication-administration/(?P<id>\d+)/delete', medication_administration_data_delete, name='medication_administration_data_delete'),

    re_path(r'^overtime-claim/(?P<id>\d+)/edit', overtime_claim_data_edit, name='overtime_claim_data_edit'),
    re_path(r'^overtime-claim/(?P<id>\d+)/delete', overtime_claim_data_delete, name='overtime_claim_data_delete'),

]
