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
def enteral_feeding_regime_data(request, id):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
    page_title = _('Enteral Feeding Regime')
    patients = EnteralFeedingRegime.objects.filter(patient=id)
    total = EnteralFeedingRegime.objects.aggregate(Sum('amount'))
    profiles = PatientProfile.objects.filter(pk=id)
    total_feeding = EnteralFeedingRegime.objects.aggregate(Sum('amount'))
    total_fluids = EnteralFeedingRegime.objects.filter(patient=id).values_list('total_fluids', flat=True).first()
    all_total_fluids = EnteralFeedingRegime.objects.aggregate(Sum('total_fluids'))

    context = {
        'logos': logos,
        'titles': titles,
        'page_title': page_title,
        'patients': patients,
        'profiles': profiles,
        'total': total,
        'total_feeding': total_feeding,
        'total_fluids': total_fluids,
        'all_total_fluids': all_total_fluids,
    }

    return render(request, 'patient_data/enteral_feeding_regime_data.html', context)

