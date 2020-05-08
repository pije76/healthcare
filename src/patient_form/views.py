from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.urls import reverse_lazy
from django.utils.translation import ugettext as _
from django.views.generic import ListView, CreateView, UpdateView
from django.core import serializers
from django.http import JsonResponse

from jsignature.utils import draw_signature

from .models import *
from .forms import *
#from accounts.models import *
from customers.models import *

# Create your views here.
def index(request):
    schema_name = connection.schema_name
    patients = PatientProfile.objects.filter(username=request.user.username)
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
    page_title = 'Homepage'

    context = {
        'patients': patients,
        'logos': logos,
        'titles': titles,
        'page_title': page_title,
    }
    return render(request, 'index.html', context)

@login_required
def admission(request):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
    page_title = 'Admission Form'

    if request.method == 'POST':
        form = AdmissionForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.full_name = request.user
            instance.save()
            messages.success(request, 'Your form has been sent successfully.')
            return HttpResponseRedirect('/data/appointment/')
        else:
            print(form.errors)
    else:
        form = AdmissionForm(initial={'full_name': request.user.full_name, 'time': '00:00'})

    context = {
        'logos': logos,
        'titles': titles,
        'page_title': page_title,
        'form': form,
    }

    return render(request, 'patient_form/admission.html', context)


@login_required
def homeleave(request):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
    page_title = 'Application For Home Leave'

    if request.method == 'POST':
        form = ApplicationForHomeLeaveForm(request.POST)
        if form.is_valid():
#            profile = form.save(commit=False)
#            profile.signature = form.cleaned_data.get('signature')
#            if profile.signature:
#                profile.signature = draw_signature(signature)
#                signature_file_path = draw_signature(signature, as_file=True)
#            profile.save()
            form.save()
            return HttpResponseRedirect('/data/homeleave/')
    else:
        form = ApplicationForHomeLeaveForm()

    context = {
        'logos': logos,
        'titles': titles,
        'page_title': page_title,
        'form': form,
    }

    return render(request, 'patient_form/homeleave.html', context)


def load_ic_number(request):
    query = request.GET.get('full_name')
    results = Admission.objects.filter(full_name=query)
    context = {
        'results': results,
    }
    return render(request, 'patient_form/dropdown_list.html', context)


@login_required
def appointment(request):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
    page_title = 'Appointment Form'
    appointments = Appointment.objects.all()

    if request.method == 'POST':
        form = AppointmentForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your form has been sent successfully.')
            return HttpResponseRedirect('/data/appointment/')
        else:
            print(form.errors)
    else:
        form = AppointmentForm()

    context = {
        'logos': logos,
        'titles': titles,
        'page_title': page_title,
        'appointments': appointments,
        'form': form,
    }

    return render(request, 'patient_form/appointment.html', context)


@login_required
def cannulation(request):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
    page_title = 'Cannulation Chart'

    if request.method == 'POST':
        form = CannulationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/data/cannulation/')
    else:
        form = CannulationForm()

    context = {
        'logos': logos,
        'titles': titles,
        'page_title': page_title,
        'form': form,
    }

    return render(request, 'patient_form/cannulation.html', context)


@login_required
def charges_sheet(request):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
    page_title = 'Charges Sheet'

    if request.method == 'POST':
        form = ChargesForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/data/charges/')
    else:
        form = ChargesForm()

    context = {
        'logos': logos,
        'titles': titles,
        'page_title': page_title,
        'form': form,
    }

    return render(request, 'patient_form/charges_sheet.html', context)


@login_required
def dressing(request):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
    page_title = 'Dressing Chart'

    if request.method == 'POST':
        form = DressingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/data/dressing/')
    else:
        form = DressingForm()

    context = {
        'logos': logos,
        'titles': titles,
        'page_title': page_title,
        'form': form,
    }

    return render(request, 'patient_form/dressing.html', context)


@login_required
def enteral_feeding_regime(request):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
    page_title = 'Enteral Feeding Regime'

    if request.method == 'POST':
        form = EnteralFeedingRegimeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/data/enteral-feeding-regime/')
    else:
        form = EnteralFeedingRegimeForm()

    context = {
        'logos': logos,
        'titles': titles,
        'page_title': page_title,
        'form': form,
    }

    return render(request, 'patient_form/enteral_feeding_regime.html', context)


@login_required
def hgt_chart(request):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
    page_title = 'HGT Chart'

    if request.method == 'POST':
        form = HGTChartForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/data/hgt/')
    else:
        form = HGTChartForm()

    context = {
        'logos': logos,
        'titles': titles,
        'page_title': page_title,
        'form': form,
    }

    return render(request, 'patient_form/hgt_chart.html', context)


@login_required
def intake_output(request):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
    page_title = 'Intake Output Chart'

    if request.method == 'POST':
        form = IntakeOutputChartForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/data/intake-output/')
    else:
        form = IntakeOutputChartForm()

    context = {
        'logos': logos,
        'titles': titles,
        'page_title': page_title,
        'form': form,
    }

    return render(request, 'patient_form/intake_output.html', context)


@login_required
def maintainance(request):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
    page_title = 'Maintainance Form'

    if request.method == 'POST':
        form = MaintainanceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/data/maintainance/')
    else:
        form = MaintainanceForm()

    context = {
        'logos': logos,
        'titles': titles,
        'page_title': page_title,
        'form': form,
    }

    return render(request, 'patient_form/maintainance.html', context)


@login_required
def medication_administration(request):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
    page_title = 'Medication Administration Record'

    if request.method == 'POST':
        form = MedicationAdministrationRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/data/medication-administration/')
    else:
        form = MedicationAdministrationRecordForm()

    context = {
        'logos': logos,
        'titles': titles,
        'page_title': page_title,
        'form': form,
    }

    return render(request, 'patient_form/medication_administration.html', context)


@login_required
def medication(request):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
    page_title = 'Medication Records'

    if request.method == 'POST':
        form = MedicationRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/data/medication/')
    else:
        form = MedicationRecordForm()

    context = {
        'logos': logos,
        'titles': titles,
        'page_title': page_title,
        'form': form,
    }

    return render(request, 'patient_form/medication.html', context)


@login_required
def nursing(request):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
    page_title = 'Nursing Report'

    if request.method == 'POST':
        form = NursingForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/data/nursing/')
    else:
        form = NursingForm()

    context = {
        'logos': logos,
        'titles': titles,
        'page_title': page_title,
        'form': form,
    }

    return render(request, 'patient_form/nursing.html', context)


@login_required
def physio_progress_note_back(request):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
    page_title = 'Physiotherapy Progress Note - Back'

    if request.method == 'POST':
        form = PhysioProgressNoteBackForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/data/physio-progress-note-back/')
    else:
        form = PhysioProgressNoteBackForm()

    context = {
        'logos': logos,
        'titles': titles,
        'page_title': page_title,
        'form': form,
    }

    return render(request, 'patient_form/physio_progress_note_back.html', context)


@login_required
def physio_progress_note_front(request):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
    page_title = 'Physiotherapy Progress Note - Front'

    if request.method == 'POST':
        form = PhysioProgressNoteFrontForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/data/physio-progress-note-front/')
    else:
        form = PhysioProgressNoteFrontForm()

    context = {
        'logos': logos,
        'titles': titles,
        'page_title': page_title,
        'form': form,
    }

    return render(request, 'patient_form/physio_progress_note_front.html', context)


@login_required
def physiotherapy_general_assessment(request):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
    page_title = 'Physiotherapy General Assessment Form'

    if request.method == 'POST':
        form = PhysiotherapyGeneralAssessmentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/data/physiotherapy-general-assessment/')
    else:
        form = PhysiotherapyGeneralAssessmentForm()

    context = {
        'logos': logos,
        'titles': titles,
        'page_title': page_title,
        'form': form,
    }

    return render(request, 'patient_form/physiotherapy_general_assessment.html', context)


@login_required
def stool(request):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
    page_title = 'Stool Chart'

    if request.method == 'POST':
        form = StoolForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/data/stool/')
    else:
        form = StoolForm()

    context = {
        'logos': logos,
        'titles': titles,
        'page_title': page_title,
        'form': form,
    }

    return render(request, 'patient_form/stool.html', context)


@login_required
def vital_sign_flow(request):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
    page_title = 'Vital Sign Flow Sheet'

    if request.method == 'POST':
        form = VitalSignFlowForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/data/vital-sign-flow/')
    else:
        form = VitalSignFlowForm()

    context = {
        'logos': logos,
        'titles': titles,
        'page_title': page_title,
        'form': form,
    }

    return render(request, 'patient_form/vital_sign_flow.html', context)
