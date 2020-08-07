from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.db.models import Sum, Count
from django.shortcuts import render, get_object_or_404
from django.utils.translation import ugettext as _
from django.http import JsonResponse

from patient_form.models import *
from patient_form.forms import *
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
def save_intake_output_data_form(request, form, template_name):
    data = dict()

    if request.method == 'POST':
        if form.is_valid():
            patients = IntakeOutputChart()
            patients = form.save(commit=False)
            patients.patient = request.user
            patients.save()
            data['form_is_valid'] = True
            patients = IntakeOutputChart.objects.all()
            data['html_intake_output_list'] = render_to_string('patient_data/intake_output_data/intake_output_data.html', {'patients': patients})
        else:
            data['form_is_valid'] = False

    context = {
        'form': form,
    }
    data['html_form'] = render_to_string(template_name, context, request=request)

    return JsonResponse(data)



@login_required
def intake_output_data(request, username):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
    page_title = _('Intake Output Chart')
    patientid = UserProfile.objects.get(username=username).id
    patients = IntakeOutputChart.objects.filter(patient=patientid)
    profiles = UserProfile.objects.filter(pk=patientid)

    total_oral_day = IntakeOutputChart.objects.filter(patient=patientid, date__range=[startdate, enddate], time_intake__range=(start_time_day, end_time_day)).aggregate(Sum('intake_oral_ml'))
    total_parental_day = IntakeOutputChart.objects.filter(patient=patientid, date__range=[startdate, enddate], time_intake__range=(start_time_day, end_time_day)).aggregate(Sum('intake_parenteral_ml'))
    total_other_intake_day = IntakeOutputChart.objects.filter(patient=patientid, date__range=[startdate, enddate], time_intake__range=(start_time_day, end_time_day)).aggregate(Sum('intake_other_ml'))
    total_cum_day = IntakeOutputChart.objects.filter(patient=patientid, date__range=[startdate, enddate], time_intake__range=(start_time_day, end_time_day)).aggregate(Sum('output_urine_cum'))
    total_gastric_day = IntakeOutputChart.objects.filter(patient=patientid, date__range=[startdate, enddate], time_intake__range=(start_time_day, end_time_day)).aggregate(Sum('output_gastric_ml'))
    total_other_output_day = IntakeOutputChart.objects.filter(patient=patientid, date__range=[startdate, enddate], time_intake__range=(start_time_day, end_time_day)).aggregate(Sum('output_other_ml'))

    total_oral_night = IntakeOutputChart.objects.filter(patient=patientid, date__range=[startdate, enddate], time_intake__range=(start_time_night, end_time_night)).aggregate(Sum('intake_oral_ml'))
    total_parental_night = IntakeOutputChart.objects.filter(patient=patientid, date__range=[startdate, enddate], time_intake__range=(start_time_night, end_time_night)).aggregate(Sum('intake_parenteral_ml'))
    total_other_intake_night = IntakeOutputChart.objects.filter(patient=patientid, date__range=[startdate, enddate], time_intake__range=(start_time_night, end_time_night)).aggregate(Sum('intake_other_ml'))
    total_cum_night = IntakeOutputChart.objects.filter(patient=patientid, date__range=[startdate, enddate], time_intake__range=(start_time_night, end_time_night)).aggregate(Sum('output_urine_cum'))
    total_gastric_night = IntakeOutputChart.objects.filter(patient=patientid, date__range=[startdate, enddate], time_intake__range=(start_time_night, end_time_night)).aggregate(Sum('output_gastric_ml'))
    total_other_output_night = IntakeOutputChart.objects.filter(patient=patientid, date__range=[startdate, enddate], time_intake__range=(start_time_night, end_time_night)).aggregate(Sum('output_other_ml'))

    total_oral = IntakeOutputChart.objects.filter(patient=patientid).aggregate(Sum('intake_oral_ml'))
    total_parental = IntakeOutputChart.objects.filter(patient=patientid).aggregate(Sum('intake_parenteral_ml'))
    total_other_intake = IntakeOutputChart.objects.filter(patient=patientid,).aggregate(Sum('intake_other_ml'))

    agg_data = IntakeOutputChart.objects.aggregate(total_source1=Count('intake_oral_ml'), total_source2=Count('intake_parenteral_ml'), total_source3=Count('intake_other_ml'))
    total_count = sum(agg_data.values())
    res = IntakeOutputChart.objects.all().annotate(total_source1=Count('intake_oral_ml'), total_source2=Count('intake_parenteral_ml'), total_source3=Count('intake_other_ml')).annotate(total_count=F('total_source1') + F('total_source2') + F('total_source3')).order_by('-total_count')

#   total_intake = total_oral+total_parental+total_other_intake

#   total_intake = IntakeOutputChart.objects.all().aggregate(Sum(F('output_urine_cum') + F('output_gastric_ml') + F('output_other_ml'))

    total_intake = IntakeOutputChart.objects.filter(patient=patientid).annotate(Count('output_urine_cum')).annotate(Count('output_gastric_ml')).annotate(Count('output_other_ml'))
#   total_output = total_cum+total_gastric+total_other_output

#   total_balance = total_intake + total_output

    time_range_day = IntakeOutputChart.objects.filter(patient=patientid, time_intake__range=(start_time_day, end_time_day))
    time_range_night = IntakeOutputChart.objects.filter(patient=patientid, time_intake__range=(start_time_night, end_time_night))

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

    return render(request, 'patient_data/intake_output_data/intake_output_data.html', context)


@login_required
def intake_output_data_edit(request, id):
    intake_outputs = get_object_or_404(IntakeOutputChart, pk=id)
    if request.method == 'POST':
        form = IntakeOutputChartForm(request.POST or None, instance=intake_outputs)
    else:
        form = IntakeOutputChartForm(instance=intake_outputs)
    return save_intake_output_data_form(request, form, 'patient_data/intake_output_data/partial_edit.html')


@login_required
def intake_output_data_delete(request, id):
    intake_outputs = get_object_or_404(IntakeOutputChart, pk=id)
    data = dict()

    if request.method == 'POST':
        intake_outputs.delete()
        data['form_is_valid'] = True
        patients = IntakeOutputChart.objects.all()
        data['html_intake_output_list'] = render_to_string('patient_data/intake_output_data/intake_output_data.html', {'patients': patients})
        return JsonResponse(data)
    else:
        context = {'intake_outputs': intake_outputs}
        data['html_form'] = render_to_string('patient_data/intake_output_data/partial_delete.html', context, request=request)
        return JsonResponse(data)

    return JsonResponse(data)
