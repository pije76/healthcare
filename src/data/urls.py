from django.urls import path, re_path

from .models import *
from .views import *

app_name = 'data'

urlpatterns = [
#    path('', index, name='index'),
#    path('index/', index, name='index'),
#    re_path(r'^admission/(?P<username>\w+)/$', admission, name='admission_create'),

    path('', data_list, name='data_list'),
#    path('', PatientListView.as_view(), name='staffdata_list'),
#    re_path(r'^(?P<id>\d+)', staffdata_detail, name='staffdata_detail'),
    re_path(r'^drug/$', drug_list, name='drug_list'),
    re_path(r'^drug/create', drug_create, name='drug_create'),
    re_path(r'^drug/edit', drug_edit, name='drug_edit'),
    re_path(r'^drug/delete', drug_delete, name='drug_delete'),

    re_path(r'^wound-condition/$', wound_condition_list, name='wound_condition_list'),
    re_path(r'^wound-condition/create', wound_condition_create, name='wound_condition_create'),
    re_path(r'^wound-condition/edit', wound_condition_edit, name='wound_condition_edit'),
    re_path(r'^wound-condition/delete', wound_condition_delete, name='wound_condition_delete'),

]
