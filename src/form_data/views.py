from django.shortcuts import render
from django.utils.translation import ugettext as _
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect

from io import BytesIO
from reportlab.pdfgen import canvas
from .pdf import get_template

from .models import *
from .forms import *
from accounts.models import *

# Create your views here.


def admission(request):
    #    item = Admission.objects.get(id=id)
    #    form = AdmissionForm(initial={'ic_number': item.ic_number})
    if request.method == 'POST':
        form = AdmissionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/admission/')
    else:
        form = AdmissionForm()

    context = {
        #        'item': 'item',
        'form': form,
    }

    return render(request, 'form_data/admission.html', context)


def homeleave(request):
    if request.method == 'POST':
        form = ApplicationForHomeLeaveForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/homeleave/')
    else:
        form = ApplicationForHomeLeaveForm()

    context = {
        #        'navbar': 'homeleave',
        'form': form,
    }

    return render(request, 'form_data/homeleave.html', context)


def viewpdf(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="homeleave.pdf"'

    buffer = BytesIO()

    # Create the PDF object, using the BytesIO object as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly.
    p.showPage()
    p.save()

    # Get the value of the BytesIO buffer and write it to the response.
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response


def appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            #            user = UserProfile.objects.get(id=user)
            #            user = details.save(commit = False)
            #            user.save()
            form.save()
            return HttpResponseRedirect('/appointment/')
    else:
        form = AppointmentForm()

    context = {
        #        'user': user,
        'form': form,
    }

    return render(request, 'form_data/appointment.html', context)


def cannulation(request):
    if request.method == 'POST':
        form = CannulationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/cannulation/')
    else:
        form = CannulationForm()

    context = {
        'navbar': 'cannulation',
        'form': form,
    }

    return render(request, 'form_data/cannulation.html', context)


def charges_sheet(request):
    if request.method == 'POST':
        form = ChargesForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/charges/')
    else:
        form = ChargesForm()

    context = {
        'navbar': 'charges_sheet',
        'form': form,
    }

    return render(request, 'form_data/charges_sheet.html', context)


def dressing(request):
    if request.method == 'POST':
        form = DressingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/dressing/')
    else:
        form = DressingForm()

    context = {
        'navbar': 'dressing',
        'form': form,
    }

    return render(request, 'form_data/dressing.html', context)


def enteral_feeding_regine(request):
    if request.method == 'POST':
        form = EnteralFeedingRegineForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/enteral-feeding-regine/')
    else:
        form = EnteralFeedingRegineForm()

    context = {
        'navbar': 'enteral_feeding_regine',
        'form': form,
    }

    return render(request, 'form_data/enteral_feeding_regine.html', context)


def hgt_chart(request):
    if request.method == 'POST':
        form = HGTChartForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/hgt/')
    else:
        form = HGTChartForm()

    context = {
        'navbar': 'hgt_chart',
        'form': form,
    }

    return render(request, 'form_data/hgt_chart.html', context)


def intake_output(request):
    if request.method == 'POST':
        form = IntakeOutputChartForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/intake-output/')
    else:
        form = IntakeOutputChartForm()

    context = {
        'navbar': 'intake_output',
        'form': form,
    }

    return render(request, 'form_data/intake_output.html', context)


def maintainance(request):
    if request.method == 'POST':
        form = MaintainanceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/maintainance/')
    else:
        form = MaintainanceForm()

    context = {
        'navbar': 'maintainance',
        'form': form,
    }

    return render(request, 'form_data/maintainance.html', context)


def medication_administration(request):
    if request.method == 'POST':
        form = MaintainanceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/medication-administration/')
    else:
        form = MaintainanceForm()

    context = {
        'navbar': 'medication_administration',
        'form': form,
    }

    return render(request, 'form_data/medication_administration.html', context)


def medication(request):
    if request.method == 'POST':
        form = MedicationRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/medication/')
    else:
        form = MedicationRecordForm()

    context = {
        'navbar': 'medication',
        'form': form,
    }

    return render(request, 'form_data/medication.html', context)


def nursing(request):
    if request.method == 'POST':
        form = NursingForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/nursing/')
    else:
        form = NursingForm()

    context = {
        'navbar': 'nursing',
        'form': form,
    }

    return render(request, 'form_data/nursing.html', context)


def physio_progress_note_back(request):
    if request.method == 'POST':
        form = PhysioProgressNoteBackForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/physio-progress-note-back/')
    else:
        form = PhysioProgressNoteBackForm()

    context = {
        'navbar': 'physio_progress_note_back',
        'form': form,
    }

    return render(request, 'form_data/physio_progress_note_back.html', context)


def physio_progress_note_front(request):
    if request.method == 'POST':
        form = PhysioProgressNoteFrontForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/physio-progress-note-front/')
    else:
        form = PhysioProgressNoteFrontForm()

    context = {
        'navbar': 'physio_progress_note_front',
        'form': form,
    }

    return render(request, 'form_data/physio_progress_note_front.html', context)


def physiotherapy_general_assessment(request):
    if request.method == 'POST':
        form = PhysiotherapyGeneralAssessmentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/physiotherapy-general-assessment/')
    else:
        form = PhysiotherapyGeneralAssessmentForm()

    context = {
        'navbar': 'physiotherapy_general_assessment',
        'form': form,
    }

    return render(request, 'form_data/physiotherapy_general_assessment.html', context)


def stool(request):
    if request.method == 'POST':
        form = StoolForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/stool/')
    else:
        form = StoolForm()

    context = {
        'navbar': 'stool',
        'form': form,
    }

    return render(request, 'form_data/stool.html', context)


def vital_sign_flow(request):
    if request.method == 'POST':
        form = VitalSignFlowForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/vital-sign-flow/')
    else:
        form = VitalSignFlowForm()

    context = {
        'navbar': 'vital_sign_flow',
        'form': form,
    }

    return render(request, 'form_data/vital_sign_flow.html', context)
