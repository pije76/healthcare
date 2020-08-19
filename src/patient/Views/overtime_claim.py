from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import ugettext as _
from django.http import JsonResponse

from patient.models import *
from patient.Forms.overtime_claim import *
from accounts.models import *
from customers.models import *

from bootstrap_modal_forms.generic import *

import datetime

startdate = datetime.date.today()
enddate = startdate + datetime.timedelta(days=1)

start_time_day = datetime.datetime.strptime('00:00', '%H:%M').time()
end_time_day = datetime.datetime.strptime('12:00', '%H:%M').time()
start_time_night = datetime.datetime.strptime('12:01', '%H:%M').time()
end_time_night = datetime.datetime.strptime('23:59', '%H:%M').time()



@login_required
def overtime_claim_list(request, username):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
    page_title = _('Overtime Claim Form')
    patientid = UserProfile.objects.get(username=username).id
    patients = OvertimeClaim.objects.filter(patient=patientid)
    profiles = UserProfile.objects.filter(pk=patientid)
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

    return render(request, 'patient/overtime_claim/overtime_claim_data.html', context)



@login_required
def overtime_claim_create(request, username):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
    page_title = _('Overtime Claim Form')
    patients = get_object_or_404(UserProfile, username=username)
    staffs = get_object_or_404(UserProfile, full_name=request.user)
    profiles = UserProfile.objects.filter(username=username)
    icnumbers = UserProfile.objects.filter(username=username).values_list('ic_number', flat=True).first()
#   durations = OvertimeClaim.objects.filter(patient=id).values_list('duration_time', flat=True).
#   d = dict()
#   d['duration_time'] = a.duration_time
#   total = OvertimeClaim.objects.annotate(duration = Func(F('end_date'), F('start_date'), function='age'))

#   t = datetime.time(convert_duration_hour, convert_duration_minute)

    initial = {
        'patient': patients,
        'ic_number': icnumbers,
        'checked_sign_by': staffs,
        'verify_by': None,
    }

    if request.method == 'POST':
        form = OvertimeClaimForm(request.POST or None)
        if form.is_valid():

            duration_time = form.cleaned_data['duration_time']
            hours = form.cleaned_data['hours']
            sec = duration_time.total_seconds()
            convert_duration_hour = int((sec / 3600) % 3600)
            convert_duration_minute = int((sec / 60) % 60)
            convert_duration_second = int(sec)
            delta = datetime.timedelta(hours=convert_duration_hour, minutes=convert_duration_minute)
            total_delta = (datetime.datetime.combine(datetime.date(1, 1, 1), hours) + delta).time()

            profile = OvertimeClaim()
            profile.patient = patients
            profile.date = form.cleaned_data['date']
            profile.duration_time = form.cleaned_data['duration_time']
            profile.hours = form.cleaned_data['hours']
            profile.total_hours = total_delta
            profile.checked_sign_by = staffs
            profile.verify_by = form.cleaned_data['verify_by']
            profile.save()

            messages.success(request, _(page_title + ' form was created.'))
            return redirect('patient:patientdata_detail', username=patients.username)
        else:
            messages.warning(request, form.errors)
    else:
        form = OvertimeClaimForm(initial=initial)

    print("staffs: ", staffs)
    context = {
        'logos': logos,
        'titles': titles,
        'page_title': page_title,
        'patients': patients,
        'profiles': profiles,
        'icnumbers': icnumbers,
        'form': form,
    }

    return render(request, 'patient/overtime_claim/overtime_claim_form.html', context)

class OvertimeClaimUpdateView(BSModalUpdateView):
    model = OvertimeClaim
    template_name = 'patient/overtime_claim/partial_edit.html'
    form_class = OvertimeClaimForm
    page_title = _('OvertimeClaim Form')
    success_message = _(page_title + ' form has been save successfully.')

    def get_success_url(self):
        username = self.kwargs['username']
        return reverse_lazy('patient:overtime_claim_data', kwargs={'username': username})


overtime_claim_edit = OvertimeClaimUpdateView.as_view()


class OvertimeClaimDeleteView(BSModalDeleteView):
    model = OvertimeClaim
    template_name = 'patient/overtime_claim/partial_delete.html'
    page_title = _('OvertimeClaim Form')
    success_message = _(page_title + ' form was deleted.')

    def get_success_url(self):
        username = self.kwargs['username']
        return reverse_lazy('patient:overtime_claim_data', kwargs={'username': username})


overtime_claim_delete = OvertimeClaimDeleteView.as_view()

