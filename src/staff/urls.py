from django.urls import path, re_path

from .models import *
from .views import *

app_name = 'staff'

urlpatterns = [
    #    path('', index, name='index'),
    #    path('index/', index, name='index'),
    #    re_path(r'^admission/(?P<username>\w+)/$', admission, name='admission_create'),

    path('', staffdata_list, name='staffdata_list'),
    #    path('', PatientListView.as_view(), name='staffdata_list'),
    #    re_path(r'^(?P<id>\d+)', staffdata_detail, name='staffdata_detail'),
    #   re_path(r'^(?P<username>\w+)/$', staffdata_detail, name='staffdata_detail'),
    path('<str:username>/', staffdata_detail, name='staffdata_detail'),
    #    re_path(r'^staff/$', staffdata_list, name='staffdata_list'),
    #    re_path(r'^staff/create', staffdata_create, name='staffdata_create'),
    #    re_path(r'^staff/(?P<pk>\d+)/delete', staffdata_delete, name='staffdata_delete'),
    #    re_path(r'^load_ic_number/$', load_ic_number, name='load_ic_number'),

    path('<str:username>/overtime-claim/', overtime_claim_list, name='overtime_claim_list'),
    path('overtime-claim/<username>/', overtime_claim_create, name='overtime_claim_create'),
    path('<str:username>/overtime-claim/<int:pk>/edit', overtime_claim_edit, name='overtime_claim_edit'),
    path('<str:username>/overtime-claim/<int:pk>/delete', overtime_claim_delete, name='overtime_claim_delete'),
    path('<str:username>/overtime-claim/pdf', overtime_claim_pdf, name='overtime_claim_pdf'),

    re_path(r'^(?P<username>\w+)/staff-records/$', staff_records_list, name='staff_records_list'),
    re_path(r'^staff-records/(?P<username>\w+)/$', staff_records_create, name='staff_records_create'),
    re_path(r'^(?P<username>\w+)/staff-records/(?P<pk>\d+)/edit', staff_records_edit, name='staff_records_edit'),
    re_path(r'^(?P<username>\w+)/staff-records/(?P<pk>\d+)/delete', staff_records_delete, name='staff_records_delete'),
]
