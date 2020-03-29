from django.shortcuts import render

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

