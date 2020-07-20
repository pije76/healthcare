from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import connection
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
def save_overtime_claim_form(request, form, template_name):
    data = dict()

    if request.method == 'POST':
        if form.is_valid():
            patients = OvertimeClaim()
            patients = form.save(commit=False)
            patients.patient = request.user
            patients.save()
            data['form_is_valid'] = True
            patients = OvertimeClaim.objects.all()
            data['html_candidat_list'] = render_to_string('patient_data/patient_list.html', {'patients': patients})
        else:
            data['form_is_valid'] = False

    context = {
        'form': form,
    }
    data['html_form'] = render_to_string(template_name, context, request=request)

    return JsonResponse(data)


@login_required
def overtime_claim(request, username):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
    page_title = _('Overtime Claim Form')
    patientid = PatientProfile.objects.get(username=username).id
    patients = OvertimeClaim.objects.filter(patient=patientid)
    profiles = PatientProfile.objects.filter(pk=patientid)
#    experiments_per_hour = OvertimeClaim.objects.annotate(hour=TruncHour('date', output_field=TimeField()),).values('hours').annotate(experiments=Count('id'))
#   durations = OvertimeClaim.objects.filter(patient=id).order_by('duration_time').values_list('duration_time', flat=True).first()
#    tanggal = OvertimeClaim.objects.filter(patient=id).values_list('date', flat=True)
#    waktu = OvertimeClaim.objects.filter(patient=id).values_list('hours', flat=True)
#    durations = OvertimeClaim.objects.filter(patient=id).values_list('duration_time', flat=True)
#   durations = datetime.time(h, m, s)
#   model.time_field = t
#    delta = waktu - durations
#    hours = (delta.days * 24) + (delta.seconds // 3600)
#    profile = OvertimeClaim()
#    start_time = OvertimeClaim.objects.get(pk=id)
#    start = profile.hours
#    delta = profile.hours.strftime(profile.duration_time)
#    delta = profile.hours + profile.duration_time
#    print("delta:", delta)

#    profile.duration_time = form.cleaned_data['duration_time']
#    delta = datetime.time(profile.duration_time)
#    delta = datetime.time(profile.duration_time)
#    delta = datetime.strptime(profile.duration_time, '%H:%M:%S').time()
#    delta = profile.duration_time
#    delta = (datetime.combine(datetime.date(1, 1, 1), start_time) + timedelta(minutes=30)).time()
#    today = datetime.datetime.today()
#    delta = OvertimeClaim.objects.all()
#    delta = datetime.datetime(event_date.year, event_date.month, event_date.day, event_time.hour, event_time.minute, event_time.second)
#    print(type(delta))

#    profile.hours = form.cleaned_data['hours']
#    profile.hours = datetime.datetime.strptime(duration_time, '%H:%M').time()
#    profile.total_hours = form.cleaned_data['total_hours']
#    profile.total_hours = datetime.time(profile.duration_time)
#    profile.total_hours = datetime.datetime.strptime(profile.duration_time, '%H:%M').time()

    context = {
        'logos': logos,
        'titles': titles,
        'page_title': page_title,
        'patients': patients,
        'profiles': profiles,
#        'tanggal': tanggal,
#        'waktu': waktu,
#        'delta': delta,
    }

    return render(request, 'patient_data/overtime_claim_data/overtime_claim_data.html', context)


@login_required
def overtime_claim_data_edit(request, id):
    overtime_claims = get_object_or_404(timeClaim, pk=id)
    if request.method == 'POST':
        form = OvertimeClaimForm(request.POST or None, instance=overtime_claims)
    else:
        form = OvertimeClaimForm(instance=overtime_claims)
    return save_overtime_claim_form(request, form, 'patient_data/overtime_claim_data/partial_edit.html')


@login_required
def overtime_claim_data_delete(request, id):
    overtime_claims = get_object_or_404(timeClaim, pk=id)
    data = dict()

    if request.method == 'POST':
        overtime_claims.delete()
        data['form_is_valid'] = True
        patients = OvertimeClaim.objects.all()
        data['html_candidat_list'] = render_to_string('patient_data/patient_list.html', {'patients': patients})
        return JsonResponse(data)
    else:
        context = {'overtime_claims': overtime_claims}
        data['html_form'] = render_to_string('patient_data/overtime_claim_data/partial_delete.html', context, request=request)
        return JsonResponse(data)

    return JsonResponse(data)
