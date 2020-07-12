from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.db import connection
from django.db.models import Count, Sum, F, Q
from django.db.models.functions import Trunc
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.translation import ugettext as _
from django.views.generic import ListView
from django.http import JsonResponse

from patient_form.models import *
from accounts.models import *
from customers.models import *

#import datetime
from datetime import *

startdate = date.today()
enddate = startdate + timedelta(days=1)

start_time_day = datetime.strptime('00:00', '%H:%M').time()
end_time_day = datetime.strptime('12:00', '%H:%M').time()
start_time_night = datetime.strptime('12:01', '%H:%M').time()
end_time_night = datetime.strptime('23:59', '%H:%M').time()





@login_required
def staff_records(request, id):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
    page_title = _('Staff Records')
    patients = StaffRecords.objects.filter(patient=id)
    profiles = PatientProfile.objects.filter(pk=id)
    total_annual = StaffRecords.objects.filter(patient=id).aggregate(Sum('annual_leave_days'))
    total_public = StaffRecords.objects.filter(patient=id,).aggregate(Sum('public_holiday_days'))

    context = {
        'logos': logos,
        'titles': titles,
        'page_title': page_title,
        'patients': patients,
        'profiles': profiles,
        'total_annual': total_annual,
        'total_public': total_public,
    }

    return render(request, 'patient_data/staff_records_data.html', context)
