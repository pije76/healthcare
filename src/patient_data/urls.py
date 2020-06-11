from django.urls import path, re_path

from . import views

from .models import *
from .views import *

app_name = 'patient_data'

urlpatterns = [
    path('', patientdata_list, name='patientdata_list'),
    re_path(r'^(?P<pk>\d+)', patientdata_detail, name='patientdata_detail'),
#    re_path(r'^patient_data/$', patientdata_list, name='patientdata_list'),
#    re_path(r'^patient_data/create', patientdata_create, name='patientdata_create'),
#    re_path(r'^patient_data/(?P<pk>\d+)/delete', patientdata_delete, name='patientdata_delete'),
    path('admission/', admission, name='admission'),
    path('homeleave/', homeleave, name='homeleave'),
    path('appointment/', appointment, name='appointment'),
    path('cannulation/', cannulation, name='cannulation'),
    path('charges/', charges_sheet, name='charges_sheet'),
    path('dressing/', dressing, name='dressing'),
    path('enteral-feeding-regime/', enteral_feeding_regime, name='enteral_feeding_regime'),
    path('hgt/', hgt_chart, name='hgt_chart'),
    path('intake-output/', intake_output, name='intake_output'),
    path('maintainance/', maintainance, name='maintainance'),
    path('medication-administration/', medication_administration, name='medication_administration'),
    path('medication/', medication, name='medication'),
    path('nursing/', nursing, name='nursing'),
    path('physio-progress-note/', physio_progress_note, name='physio_progress_note'),
    path('physiotherapy-general-assessment/', physiotherapy_general_assessment, name='physiotherapy_general_assessment'),
    path('stool/', stool, name='stool'),
    path('vital-sign-flow/', vital_sign_flow, name='vital_sign_flow'),
]
