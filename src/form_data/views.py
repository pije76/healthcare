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

    context = {
        'patients': patients,
        'logos': logos,
        'titles': titles,
    }
    return render(request, 'index.html', context)

@login_required
def admission(request):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()

    if request.method == 'POST':
        form = AdmissionForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.full_name = request.user
            instance.save()
            messages.success(request, 'Your form has been sent successfully.')
            return HttpResponseRedirect('/forms/index/')
        else:
            print(form.errors)
    else:
        form = AdmissionForm(initial={'full_name': request.user.full_name, 'time': '00:00'})

    context = {
        'logos': logos,
        'titles': titles,
        'form': form,
    }

    return render(request, 'form_data/admission.html', context)


@login_required
def homeleave(request):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
    if request.method == 'POST':
        form = ApplicationForHomeLeaveForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/homeleave/')
    else:
        form = ApplicationForHomeLeaveForm()

    context = {
        'logos': logos,
        'titles': titles,
        'form': form,
    }

    return render(request, 'form_data/homeleave.html', context)


def load_ic_number(request):
    query = request.GET.get('full_name')
    results = Admission.objects.filter(full_name=query)
    context = {
        'results': results,
    }
    return render(request, 'form_data/dropdown_list.html', context)


@login_required
def appointment(request):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()

    if request.method == 'POST':
        form = AppointmentForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your form has been sent successfully.')
            return HttpResponseRedirect('/forms/index/')
        else:
            print(form.errors)
    else:
        form = AppointmentForm()

    context = {
        'logos': logos,
        'titles': titles,
        'form': form,
    }

    return render(request, 'form_data/appointment.html', context)


@login_required
def cannulation(request):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
    if request.method == 'POST':
        form = CannulationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/cannulation/')
    else:
        form = CannulationForm()

    context = {
        'logos': logos,
        'titles': titles,
        'form': form,
    }

    return render(request, 'form_data/cannulation.html', context)


@login_required
def charges_sheet(request):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
    if request.method == 'POST':
        form = ChargesForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/charges/')
    else:
        form = ChargesForm()

    context = {
        'logos': logos,
        'titles': titles,
        'form': form,
    }

    return render(request, 'form_data/charges_sheet.html', context)


@login_required
def dressing(request):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
    if request.method == 'POST':
        form = DressingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/dressing/')
    else:
        form = DressingForm()

    context = {
        'logos': logos,
        'titles': titles,
        'form': form,
    }

    return render(request, 'form_data/dressing.html', context)


@login_required
def enteral_feeding_regine(request):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
    if request.method == 'POST':
        form = EnteralFeedingRegineForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/enteral-feeding-regine/')
    else:
        form = EnteralFeedingRegineForm()

    context = {
        'logos': logos,
        'titles': titles,
        'form': form,
    }

    return render(request, 'form_data/enteral_feeding_regine.html', context)


@login_required
def hgt_chart(request):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
    if request.method == 'POST':
        form = HGTChartForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/hgt/')
    else:
        form = HGTChartForm()

    context = {
        'logos': logos,
        'titles': titles,
        'form': form,
    }

    return render(request, 'form_data/hgt_chart.html', context)


@login_required
def intake_output(request):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
    if request.method == 'POST':
        form = IntakeOutputChartForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/intake-output/')
    else:
        form = IntakeOutputChartForm()

    context = {
        'logos': logos,
        'titles': titles,
        'form': form,
    }

    return render(request, 'form_data/intake_output.html', context)


@login_required
def maintainance(request):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
    if request.method == 'POST':
        form = MaintainanceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/maintainance/')
    else:
        form = MaintainanceForm()

    context = {
        'logos': logos,
        'titles': titles,
        'form': form,
    }

    return render(request, 'form_data/maintainance.html', context)


@login_required
def medication_administration(request):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
    if request.method == 'POST':
        form = MaintainanceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/medication-administration/')
    else:
        form = MaintainanceForm()

    context = {
        'logos': logos,
        'titles': titles,
        'form': form,
    }

    return render(request, 'form_data/medication_administration.html', context)


@login_required
def medication(request):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
    if request.method == 'POST':
        form = MedicationRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/medication/')
    else:
        form = MedicationRecordForm()

    context = {
        'logos': logos,
        'titles': titles,
        'form': form,
    }

    return render(request, 'form_data/medication.html', context)


@login_required
def nursing(request):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
    if request.method == 'POST':
        form = NursingForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/nursing/')
    else:
        form = NursingForm()

    context = {
        'logos': logos,
        'titles': titles,
        'form': form,
    }

    return render(request, 'form_data/nursing.html', context)


@login_required
def physio_progress_note_back(request):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
    if request.method == 'POST':
        form = PhysioProgressNoteBackForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/physio-progress-note-back/')
    else:
        form = PhysioProgressNoteBackForm()

    context = {
        'logos': logos,
        'titles': titles,
        'form': form,
    }

    return render(request, 'form_data/physio_progress_note_back.html', context)


@login_required
def physio_progress_note_front(request):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
    if request.method == 'POST':
        form = PhysioProgressNoteFrontForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/physio-progress-note-front/')
    else:
        form = PhysioProgressNoteFrontForm()

    context = {
        'logos': logos,
        'titles': titles,
        'form': form,
    }

    return render(request, 'form_data/physio_progress_note_front.html', context)


@login_required
def physiotherapy_general_assessment(request):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
    if request.method == 'POST':
        form = PhysiotherapyGeneralAssessmentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/physiotherapy-general-assessment/')
    else:
        form = PhysiotherapyGeneralAssessmentForm()

    context = {
        'logos': logos,
        'titles': titles,
        'form': form,
    }

    return render(request, 'form_data/physiotherapy_general_assessment.html', context)


@login_required
def stool(request):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
    if request.method == 'POST':
        form = StoolForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/stool/')
    else:
        form = StoolForm()

    context = {
        'logos': logos,
        'titles': titles,
        'form': form,
    }

    return render(request, 'form_data/stool.html', context)


@login_required
def vital_sign_flow(request):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
    if request.method == 'POST':
        form = VitalSignFlowForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/vital-sign-flow/')
    else:
        form = VitalSignFlowForm()

    context = {
        'logos': logos,
        'titles': titles,
        'form': form,
    }

    return render(request, 'form_data/vital_sign_flow.html', context)
