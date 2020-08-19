from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.db.models import F, Func, Value, CharField
from django.db.models import Value, CharField
from django.db.models.functions import Cast, Concat, ExtractYear, ExtractMonth, ExtractDay, ExtractHour, ExtractMinute
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.utils.translation import ugettext as _
from django.db.models import Sum

from patient.models import *
from patient.Forms.enteral_feeding_regime import *
from accounts.models import *
from customers.models import *

from bootstrap_modal_forms.generic import *

startdate = datetime.date.today()
enddate = startdate + datetime.timedelta(days=1)

start_time_day = datetime.datetime.strptime('00:00', '%H:%M').time()
end_time_day = datetime.datetime.strptime('12:00', '%H:%M').time()
start_time_night = datetime.datetime.strptime('12:01', '%H:%M').time()
end_time_night = datetime.datetime.strptime('23:59', '%H:%M').time()



@login_required
def enteral_feeding_regime_list(request, username):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
    page_title = _('Enteral Feeding Regime')
    patientid = UserProfile.objects.get(username=username).id
    patients = EnteralFeedingRegime.objects.filter(patient=patientid)
    profiles = UserProfile.objects.filter(pk=patientid)
    total = EnteralFeedingRegime.objects.aggregate(Sum('amount'))
    total_feeding = EnteralFeedingRegime.objects.filter(patient=patientid).aggregate(Sum('amount'))
    total_fluids = EnteralFeedingRegime.objects.filter(patient=patientid).values_list('total_fluids', flat=True).first()
    all_total_fluids = EnteralFeedingRegime.objects.filter(patient=patientid).aggregate(Sum('total_fluids'))

    context = {
        'logos': logos,
        'titles': titles,
        'page_title': page_title,
        'patients': patients,
        'profiles': profiles,
        'total': total,
        'total_feeding': total_feeding,
        'total_fluids': total_fluids,
        'all_total_fluids': all_total_fluids,
    }

    return render(request, 'patient/enteral_feeding_regime/enteral_feeding_regime_data.html', context)



@login_required
def enteral_feeding_regime_create(request, username):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
    page_title = _('Enteral Feeding Regime')
#   total_flush = EnteralFeedingRegime.objects.all().annotate(total_food=F('warm_water_before ') + F('warm_water_after'))
#    total = EnteralFeedingRegime.objects.aggregate(total_population=Sum('amount'))
    patients = get_object_or_404(UserProfile, username=username)
    profiles = UserProfile.objects.filter(username=username)
    icnumbers = UserProfile.objects.filter(username=username).values_list('ic_number', flat=True).first()

    initial = {
        'patient': patients,
        'ic_number': icnumbers,
    }

    if request.method == 'POST':
        form = EnteralFeedingRegimeForm(request.POST or None)
        if form.is_valid():
            profile = EnteralFeedingRegime()
            profile.patient = patients
            profile.date = form.cleaned_data['date']
            profile.time = form.cleaned_data['time']
            profile.type_of_milk = form.cleaned_data['type_of_milk']
            profile.amount = form.cleaned_data['amount']
            profile.warm_water_before = form.cleaned_data['warm_water_before']
            profile.warm_water_after = form.cleaned_data['warm_water_after']
            profile.save()

            messages.success(request, _(page_title + ' form was created.'))
            return redirect('patient:patientdata_detail', username=patients.username)
        else:
            messages.warning(request, form.errors)
    else:
        form = EnteralFeedingRegimeForm(initial=initial)

    context = {
        'logos': logos,
        'titles': titles,
        'page_title': page_title,
        'patients': patients,
        'profiles': profiles,
        'icnumbers': icnumbers,
        'form': form,
    }

    return render(request, 'patient/enteral_feeding_regime/enteral_feeding_regime_form.html', context)

class EnteralFeedingRegimeUpdateView(BSModalUpdateView):
    model = EnteralFeedingRegime
    template_name = 'patient/enteral_feeding_regime/partial_edit.html'
    form_class = EnteralFeedingRegimeForm
    page_title = _('EnteralFeedingRegime Form')
    success_message = _(page_title + ' form has been save successfully.')

    def get_success_url(self):
        username = self.kwargs['username']
        return reverse_lazy('patient:enteral_feeding_regime_data', kwargs={'username': username})


enteral_feeding_regime_edit = EnteralFeedingRegimeUpdateView.as_view()


class EnteralFeedingRegimeDeleteView(BSModalDeleteView):
    model = EnteralFeedingRegime
    template_name = 'patient/enteral_feeding_regime/partial_delete.html'
    page_title = _('EnteralFeedingRegime Form')
    success_message = _(page_title + ' form was deleted.')

    def get_success_url(self):
        username = self.kwargs['username']
        return reverse_lazy('patient:enteral_feeding_regime_data', kwargs={'username': username})


enteral_feeding_regime_delete = EnteralFeedingRegimeDeleteView.as_view()
