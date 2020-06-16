from django.urls import path, re_path

from .models import *
from .views import *

app_name = 'patient_form'

urlpatterns = [
    path('', index, name='index'),
    path('index/', index, name='index'),
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
    path('miscellaneous-charges-slip/', miscellaneous_charges_slip, name='miscellaneous_charges_slip'),
    path('nursing/', nursing, name='nursing'),
    path('overtime-claim/', overtime_claim, name='overtime_claim'),
    path('physio-progress-note/', physio_progress_note, name='physio_progress_note'),
    path('physiotherapy-general-assessment/', physiotherapy_general_assessment, name='physiotherapy_general_assessment'),
    path('staff-records/', staff_records, name='staff_records'),
    path('stool/', stool, name='stool'),
    path('vital-sign-flow/', vital_sign_flow, name='vital_sign_flow'),
    path('visiting-consultant-records/', visiting_consultant_records, name='visiting_consultant_records'),
    path('load_ic_number/', load_ic_number, name='load_ic_number'),
]
