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
def intake_output_data(request, id):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
    page_title = _('Intake Output Chart')
    patients = IntakeOutputChart.objects.filter(patient=id)
    profiles = PatientProfile.objects.filter(pk=id)

    total_oral_day = IntakeOutputChart.objects.filter(patient=id, date__range=[startdate, enddate], time_intake__range=(start_time_day, end_time_day)).aggregate(Sum('intake_oral_ml'))
    total_parental_day = IntakeOutputChart.objects.filter(patient=id, date__range=[startdate, enddate], time_intake__range=(start_time_day, end_time_day)).aggregate(Sum('intake_parenteral_ml'))
    total_other_intake_day = IntakeOutputChart.objects.filter(patient=id, date__range=[startdate, enddate], time_intake__range=(start_time_day, end_time_day)).aggregate(Sum('intake_other_ml'))
    total_cum_day = IntakeOutputChart.objects.filter(patient=id, date__range=[startdate, enddate], time_intake__range=(start_time_day, end_time_day)).aggregate(Sum('output_urine_cum'))
    total_gastric_day = IntakeOutputChart.objects.filter(patient=id, date__range=[startdate, enddate], time_intake__range=(start_time_day, end_time_day)).aggregate(Sum('output_gastric_ml'))
    total_other_output_day = IntakeOutputChart.objects.filter(patient=id, date__range=[startdate, enddate], time_intake__range=(start_time_day, end_time_day)).aggregate(Sum('output_other_ml'))

    total_oral_night = IntakeOutputChart.objects.filter(patient=id, date__range=[startdate, enddate], time_intake__range=(start_time_night, end_time_night)).aggregate(Sum('intake_oral_ml'))
    total_parental_night = IntakeOutputChart.objects.filter(patient=id, date__range=[startdate, enddate], time_intake__range=(start_time_night, end_time_night)).aggregate(Sum('intake_parenteral_ml'))
    total_other_intake_night = IntakeOutputChart.objects.filter(patient=id, date__range=[startdate, enddate], time_intake__range=(start_time_night, end_time_night)).aggregate(Sum('intake_other_ml'))
    total_cum_night = IntakeOutputChart.objects.filter(patient=id, date__range=[startdate, enddate], time_intake__range=(start_time_night, end_time_night)).aggregate(Sum('output_urine_cum'))
    total_gastric_night = IntakeOutputChart.objects.filter(patient=id, date__range=[startdate, enddate], time_intake__range=(start_time_night, end_time_night)).aggregate(Sum('output_gastric_ml'))
    total_other_output_night = IntakeOutputChart.objects.filter(patient=id, date__range=[startdate, enddate], time_intake__range=(start_time_night, end_time_night)).aggregate(Sum('output_other_ml'))

    total_oral = IntakeOutputChart.objects.filter(patient=id).aggregate(Sum('intake_oral_ml'))
    total_parental = IntakeOutputChart.objects.filter(patient=id).aggregate(Sum('intake_parenteral_ml'))
    total_other_intake = IntakeOutputChart.objects.filter(patient=id,).aggregate(Sum('intake_other_ml'))

    agg_data = IntakeOutputChart.objects.aggregate(total_source1=Count('intake_oral_ml'), total_source2=Count('intake_parenteral_ml'), total_source3=Count('intake_other_ml'))
    total_count = sum(agg_data.values())
    res = IntakeOutputChart.objects.all().annotate(total_source1=Count('intake_oral_ml'), total_source2=Count('intake_parenteral_ml'), total_source3=Count('intake_other_ml')).annotate(total_count=F('total_source1') + F('total_source2') + F('total_source3')).order_by('-total_count')

#   total_intake = total_oral+total_parental+total_other_intake

#   total_intake = IntakeOutputChart.objects.all().aggregate(Sum(F('output_urine_cum') + F('output_gastric_ml') + F('output_other_ml'))

    total_intake = IntakeOutputChart.objects.filter(patient=id).annotate(Count('output_urine_cum')).annotate(Count('output_gastric_ml')).annotate(Count('output_other_ml'))
#   total_output = total_cum+total_gastric+total_other_output

#   total_balance = total_intake + total_output

    time_range_day = IntakeOutputChart.objects.filter(patient=id, time_intake__range=(start_time_day, end_time_day))
    time_range_night = IntakeOutputChart.objects.filter(patient=id, time_intake__range=(start_time_night, end_time_night))

    context = {
        'logos': logos,
        'titles': titles,
        'page_title': page_title,
        'patients': patients,
        'profiles': profiles,

        'total_oral_day': total_oral_day,
        'total_parental_day': total_parental_day,
        'total_other_intake_day': total_other_intake_day,
        'total_cum_day': total_cum_day,
        'total_gastric_day': total_gastric_day,
        'total_other_output_day': total_other_output_day,

        'total_oral_night': total_oral_night,
        'total_parental_night': total_parental_night,
        'total_other_intake_night': total_other_intake_night,
        'total_cum_night': total_cum_night,
        'total_gastric_night': total_gastric_night,
        'total_other_output_night': total_other_output_night,

        'total_intake': total_intake,
#       'total_parental': total_parental,

#       'total_intake': total_intake,
#       'total_output': total_output,
#       'total_balance': total_balance,

        'time_range_day': time_range_day,
        'time_range_night': time_range_night,
    }

    return render(request, 'patient_data/intake_output_data.html', context)
