from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import ugettext as _

from io import BytesIO
from reportlab.pdfgen import canvas
from .pdf import get_template

from .models import *
from .forms import *

# Create your views here.


def admission(request):
    if request.method == 'POST':
        form = AdmissionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = AdmissionForm()

    context = {
        'navbar': 'admission',
        'form': form,
    }

    return render(request, 'admission.html', context)


def homeleave(request):
    if request.method == 'POST':
        form = AdmissionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = AdmissionForm()

    context = {
        'navbar': 'homeleave',
        'form': form,
    }

    return render(request, 'homeleave.html', context)


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
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = AppointmentForm()

    context = {
        'navbar': 'appointment',
        'form': form,
    }

    return render(request, 'appointment.html', context)


def cannulation(request):
    if request.method == 'POST':
        form = CannulationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = CannulationForm()

    context = {
        'navbar': 'cannulation',
        'form': form,
    }

    return render(request, 'cannulation.html', context)


def charges_sheet(request):
    if request.method == 'POST':
        form = ChargesSheetForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = ChargesSheetForm()

    context = {
        'navbar': 'charges_sheet',
        'form': form,
    }

    return render(request, 'charges_sheet.html', context)


def dressing(request):
    if request.method == 'POST':
        form = DressingChartForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = DressingChartForm()

    context = {
        'navbar': 'dressing',
        'form': form,
    }

    return render(request, 'dressing.html', context)


def enteral_feeding_regine(request):
    if request.method == 'POST':
        form = EnteralFeedingRegineForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = EnteralFeedingRegineForm()

    context = {
        'navbar': 'enteral_feeding_regine',
        'form': form,
    }

    return render(request, 'enteral_feeding_regine.html', context)

def hgt_chart(request):
    if request.method == 'POST':
        form = HGTChartForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = HGTChartForm()

    context = {
        'navbar': 'hgt_chart',
        'form': form,
    }

    return render(request, 'hgt_chart.html', context)

def intake_output(request):
    if request.method == 'POST':
        form = DressingChartForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = DressingChartForm()

    context = {
        'navbar': 'intake_output',
        'form': form,
    }

    return render(request, 'intake_output.html', context)

def maintainance(request):
    if request.method == 'POST':
        form = MaintainanceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = MaintainanceForm()

    context = {
        'navbar': 'maintainance',
        'form': form,
    }

    return render(request, 'maintainance.html', context)
