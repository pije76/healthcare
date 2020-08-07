from django.urls import path, re_path

from .models import *
from .views import *

from dal import autocomplete

app_name = 'patient_form'

urlpatterns = [
    path('', index, name='index'),
    path('index/', index, name='index'),
#    re_path(r'^admission/(?P<username>\w+)/$', admission, name='admission'),
    re_path(r'^admission/(?P<username>\w+)/$', admission, name='admission'),
    re_path(r'^application-homeleave/(?P<username>\w+)/$', application_homeleave, name='application_homeleave'),
#    re_path(r'^application-homeleave/(?P<username>\w+)/autocomplete/$', autocomplete.Select2QuerySetView.as_view(), name='autocomplete_application_homeleave'),
    re_path(r'^appointment/(?P<username>\w+)/$', appointment, name='appointment'),
    re_path(r'^catheterization-cannulation/(?P<username>\w+)/$', catheterization_cannulation, name='catheterization_cannulation'),
    re_path(r'^charges/(?P<username>\w+)/$', charges_sheet, name='charges_sheet'),
    re_path(r'^dressing/(?P<username>\w+)/$', dressing, name='dressing'),
    re_path(r'^enteral-feeding-regime/(?P<username>\w+)/$', enteral_feeding_regime, name='enteral_feeding_regime'),
    re_path(r'^hgt-chart/(?P<username>\w+)/$', hgt_chart, name='hgt_chart'),
    re_path(r'^intake-output/(?P<username>\w+)/$', intake_output, name='intake_output'),
    re_path(r'^maintainance/(?P<username>\w+)/$', maintainance, name='maintainance'),
    re_path(r'^medication-record/(?P<username>\w+)/$', medication_record, name='medication_record'),
    re_path(r'^medication-administration/(?P<username>\w+)/$', medication_administration, name='medication_administration'),
    re_path(r'^miscellaneous-charges-slip/(?P<username>\w+)/$', miscellaneous_charges_slip, name='miscellaneous_charges_slip'),
    re_path(r'^nursing/(?P<username>\w+)/$', nursing, name='nursing'),
    re_path(r'^overtime-claim/(?P<username>\w+)/$', overtime_claim, name='overtime_claim'),
    re_path(r'^physio-progress-note/(?P<username>\w+)/$', physio_progress_note, name='physio_progress_note'),
    re_path(r'^physiotherapy-general-assessment/(?P<username>\w+)/$', physiotherapy_general_assessment, name='physiotherapy_general_assessment'),
    re_path(r'^staff-records/(?P<username>\w+)/$', staff_records, name='staff_records'),
    re_path(r'^stool/(?P<username>\w+)/$', stool, name='stool'),
    re_path(r'^visiting-consultant-records/(?P<username>\w+)/$', visiting_consultant_records, name='visiting_consultant_records'),
    re_path(r'^vital-sign-flow/(?P<username>\w+)/$', vital_sign_flow, name='vital_sign_flow'),
    re_path(r'^load_ic_number/$', load_ic_number, name='load_ic_number'),
]

