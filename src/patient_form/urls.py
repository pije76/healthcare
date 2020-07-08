from django.urls import path, re_path

from .models import *
from .views import *

app_name = 'patient_form'

urlpatterns = [
    path('', index, name='index'),
    path('index/', index, name='index'),
    re_path(r'^admission/(?P<id>\d+)/$', admission, name='admission'),
    re_path(r'^application-homeleave/(?P<id>\d+)/$', application_homeleave, name='application_homeleave'),
    re_path(r'^appointment/(?P<id>\d+)/$', appointment, name='appointment'),
    re_path(r'^catheterization-cannulation/(?P<id>\d+)/$', catheterization_cannulation, name='catheterization_cannulation'),
    re_path(r'^charges/(?P<id>\d+)/$', charges_sheet, name='charges_sheet'),
    re_path(r'^dressing/(?P<id>\d+)/$', dressing, name='dressing'),
    re_path(r'^enteral-feeding-regime/(?P<id>\d+)/$', enteral_feeding_regime, name='enteral_feeding_regime'),
    re_path(r'^hgt-chart/(?P<id>\d+)/$', hgt_chart, name='hgt_chart'),
    re_path(r'^intake-output/(?P<id>\d+)/$', intake_output, name='intake_output'),
    re_path(r'^maintainance/(?P<id>\d+)/$', maintainance, name='maintainance'),
    re_path(r'^medication-record/(?P<id>\d+)/$', medication_record, name='medication_record'),
    re_path(r'^medication-administration/(?P<id>\d+)/$', medication_administration, name='medication_administration'),
    re_path(r'^miscellaneous-charges-slip/(?P<id>\d+)/$', miscellaneous_charges_slip, name='miscellaneous_charges_slip'),
    re_path(r'^nursing/(?P<id>\d+)/$', nursing, name='nursing'),
    re_path(r'^overtime-claim/(?P<id>\d+)/$', overtime_claim, name='overtime_claim'),
    re_path(r'^physio-progress-note/(?P<id>\d+)/$', physio_progress_note, name='physio_progress_note'),
    re_path(r'^physiotherapy-general-assessment/(?P<id>\d+)/$', physiotherapy_general_assessment, name='physiotherapy_general_assessment'),
    re_path(r'^staff-records/(?P<id>\d+)/$', staff_records, name='staff_records'),
    re_path(r'^stool/(?P<id>\d+)/$', stool, name='stool'),
    re_path(r'^visiting-consultant-records/(?P<id>\d+)/$', visiting_consultant_records, name='visiting_consultant_records'),
    re_path(r'^vital-sign-flow/(?P<id>\d+)/$', vital_sign_flow, name='vital_sign_flow'),
    path('load_ic_number/', load_ic_number, name='load_ic_number'),
]
