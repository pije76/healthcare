from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import ugettext as _
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse

from patient.models import *
from patient.Forms.overtime_claim import *
from accounts.models import *
from customers.models import *
from ..utils import *

from bootstrap_modal_forms.generic import *
from reportlab.pdfgen import canvas

from io import BytesIO
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

#    profile.duration_time = form.cleaned_data['duration_time']
#    delta = datetime.time(profile.duration_time)
#    delta = datetime.time(profile.duration_time)
#    delta = datetime.strptime(profile.duration_time, '%H:%M:%S').time()
#    delta = profile.duration_time
#    delta = (datetime.combine(datetime.date(1, 1, 1), start_time) + timedelta(minutes=30)).time()
#    today = datetime.datetime.today()
#    delta = OvertimeClaim.objects.all()
#    delta = datetime.datetime(event_date.year, event_date.month, event_date.day, event_time.hour, event_time.minute, event_time.second)

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

#    pdf_full_path = settings.BASE_DIR + obj.pdf.url

    initial = {
        'patient': patients,
        'ic_number': icnumbers,
        'checked_sign_by': staffs,
        'verify_by': None,
    }

    if request.method == 'POST':
        form = OvertimeClaim_Form(request.POST or None)
        if form.is_valid():

            duration_time_from = form.cleaned_data['duration_time_from']
            duration_time_to = form.cleaned_data['duration_time_to']
#            hours = form.cleaned_data['hours']
#            sec_from = duration_time_from.timedelta.total_seconds()
            sec_from = duration_time_from.hour * 60 + duration_time_from.minute
#            convert_duration_hour_from = int((sec_from / 3600) % 3600)
#            convert_duration_minute_from = int((sec_from / 60) % 60)

#            sec_to = duration_time_to.total_seconds()
            sec_to = duration_time_to.hour * 60 + duration_time_to.minute
#            convert_duration_hour_to = int((sec_to / 3600) % 3600)
#            convert_duration_minute_to = int((sec_to / 60) % 60)

#            delta_from = datetime.timedelta(hours=convert_duration_hour_from, minutes=convert_duration_minute_from)
#            total_delta_from = (datetime.datetime.combine(datetime.date(1, 1, 1), hours) + delta_from).time()

#            delta_to = datetime.timedelta(hours=convert_duration_hour_to, minutes=convert_duration_minute_to)
#            total_delta_to = (datetime.datetime.combine(datetime.date(1, 1, 1), hours) + delta_to).time()

#            total_delta = (delta_to - delta_from)
            total_delta = (sec_to - sec_from) / 60


            profile = OvertimeClaim()
            profile.patient = patients
            profile.date = form.cleaned_data['date']
            profile.duration_time_from = form.cleaned_data['duration_time_from']
            profile.duration_time_to = form.cleaned_data['duration_time_to']
#            total = int(total_delta_to - total_delta_from)
#            print("total_delta_from: ", total_delta)
            profile.hours = form.cleaned_data['hours']
            profile.total_hours = total_delta
            profile.checked_sign_by = staffs
            if profile.verify_by is None:
                pass
            else:
                profile.verify_by = form.cleaned_data['verify_by']
            profile.save()

            messages.success(request, _(page_title + ' form was created.'))
            return redirect('patient:patientdata_detail', username=patients.username)
        else:
            messages.warning(request, form.errors)
    else:
        form = OvertimeClaim_Form(initial=initial)

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


def overtime_claim_pdf(response, username):
    schema_name = connection.schema_name
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
    page_title = _('Application For Home Leave')
    patientid = UserProfile.objects.get(username=username).id
    patients = OvertimeClaim.objects.filter(patient=patientid)
    profiles = UserProfile.objects.filter(pk=patientid)

    pdfname = _('Overtime Claim')
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename=pdfname'
#   response['Content-Disposition'] = 'attachment; filename="{}"'.format(pdfname)
    application_data = OvertimeClaim.objects.all()
#   application_data = ApplicationForHomeLeave.objects.all[0].name
    detail_application_data = u", ".join(str(obj) for obj in application_data)

    buffer = BytesIO()
    p = canvas.Canvas(buffer)
    p.setTitle(pdfname)
    p.drawString(100, 100, detail_application_data)
    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)


    context = {
        'titles': titles,
        'page_title': page_title,
        'pdfname': pdfname,
        'patients': patients,
        'profiles': profiles,
        'application_data': application_data
    }

    result = generate_pdf('patient/overtime_claim/overtime_claim_pdf.html', file_object=response, context=context)
    return result
#   return response

class OvertimeClaimUpdateView(BSModalUpdateView):
    model = OvertimeClaim
    template_name = 'patient/overtime_claim/partial_edit.html'
    form_class = OvertimeClaim_ModelForm
    page_title = _('OvertimeClaim Form')
    success_message = _(page_title + ' form has been save successfully.')

    def get_success_url(self):
        username = self.kwargs['username']
        return reverse_lazy('patient:overtime_claim_list', kwargs={'username': username})


overtime_claim_edit = OvertimeClaimUpdateView.as_view()


class OvertimeClaimDeleteView(BSModalDeleteView):
    model = OvertimeClaim
    template_name = 'patient/overtime_claim/partial_delete.html'
    page_title = _('OvertimeClaim Form')
    success_message = _(page_title + ' form was deleted.')

    def get_success_url(self):
        username = self.kwargs['username']
        return reverse_lazy('patient:overtime_claim_list', kwargs={'username': username})


overtime_claim_delete = OvertimeClaimDeleteView.as_view()

