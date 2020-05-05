from django.urls import path, re_path

from .models import *
from .views import *

app_name = 'form_data'

urlpatterns = [
    path('', index, name='index'),
    path('index/', index, name='index'),
    path('admission/', admission, name='admission'),
    path('homeleave/', homeleave, name='homeleave'),
    path('appointment/', appointment, name='appointment'),
    path('cannulation/', cannulation, name='cannulation'),
    path('charges/', charges_sheet, name='charges_sheet'),
    path('dressing/', dressing, name='dressing'),
    path('enteral-feeding-regine/', enteral_feeding_regine, name='enteral_feeding_regine'),
    path('hgt/', hgt_chart, name='hgt_chart'),
    path('intake-output/', intake_output, name='intake_output'),
    path('maintainance/', maintainance, name='maintainance'),
    path('medication-administration/', medication_administration, name='medication_administration'),
    path('medication/', medication, name='medication'),
    path('nursing/', nursing, name='nursing'),
    path('physio-progress-note-back/', physio_progress_note_back, name='physio_progress_note_back'),
    path('physio-progress-note-front/', physio_progress_note_front, name='physio_progress_note_front'),
    path('physiotherapy-general-assessment/', physiotherapy_general_assessment, name='physiotherapy_general_assessment'),
    path('stool/', stool, name='stool'),
    path('vital-sign-flow/', vital_sign_flow, name='vital_sign_flow'),
    path('load_ic_number/', load_ic_number, name='load_ic_number'),
]
