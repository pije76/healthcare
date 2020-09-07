from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.db.models import F, Func, Value, CharField
from django.db.models import Value, CharField
from django.db.models.functions import Cast, Concat, ExtractYear, ExtractMonth, ExtractDay, ExtractHour, ExtractMinute
from django.urls import reverse, reverse_lazy
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

import datetime

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
	warm_water_before = EnteralFeedingRegime.objects.filter(patient=patientid).values_list('warm_water_before', flat=True).first()
	warm_water_after = EnteralFeedingRegime.objects.filter(patient=patientid).values_list('warm_water_after', flat=True).first()

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
		'warm_water_before': warm_water_before,
		'warm_water_after': warm_water_after,
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
#	EnteralFeedingRegime_FormSet = formset_factory(EnteralFeedingRegime_Form, extra=24, formset=TestBaseFormSet)

	initial = {
		'patient': patients,
		'done_by': request.user,
	}

	initial_list = [
		{'time': '00:00'},
		{'time': '01:00'},
		{'time': '02:00'},
		{'time': '03:00'},
		{'time': '04:00'},
		{'time': '05:00'},
		{'time': '06:00'},
		{'time': '07:00'},
		{'time': '08:00'},
		{'time': '09:00'},
		{'time': '10:00'},
		{'time': '11:00'},
		{'time': '12:00'},
		{'time': '13:00'},
		{'time': '14:00'},
		{'time': '15:00'},
		{'time': '16:00'},
		{'time': '17:00'},
		{'time': '18:00'},
		{'time': '19:00'},
		{'time': '20:00'},
		{'time': '21:00'},
		{'time': '22:00'},
		{'time': '23:00'},
	]

	initial_formset = [{
		'patient': item.full_name,
		'done_by': request.user,
	}
	for item in profiles]

	queryset = request.user.username

	if request.method == 'POST':
		form = EnteralFeedingRegime_Form(request.POST or None)
		formset = EnteralFeedingRegime_FormSet(request.POST or None)

		if form.is_valid() and formset.is_valid():

			profile_form = EnteralFeedingRegime()
			profile_form.patient = patients
			profile_form.date = form.cleaned_data['date']
			profile_form.warm_water_before = form.cleaned_data['warm_water_before']
			profile_form.warm_water_after = form.cleaned_data['warm_water_after']
			profile_form.save()

			for item in formset:
				profile = EnteralFeedingRegime()
				profile.patient = patients
				profile.date = item.cleaned_data['date']
				profile.time = item.cleaned_data['time']
				profile.type_of_milk = item.cleaned_data['type_of_milk']
				profile.amount = item.cleaned_data['amount']
				profile.save()

			messages.success(request, _(page_title + ' form was created.'))
			return redirect('patient:patientdata_detail', username=patients.username)
		else:
			messages.warning(request, formset.errors)
	else:
#		EnteralFeedingRegime_FormSet = formset_factory(EnteralFeedingRegime_Form, extra=24, formset=TestBaseFormSet)
		form = EnteralFeedingRegime_Form(initial=initial)
#		formset = EnteralFeedingRegime_FormSet(get_username=username)
		formset = EnteralFeedingRegime_FormSet(initial=initial_list)
#		formset = EnteralFeedingRegime_FormSet()
#		formset = EnteralFeedingRegime_FormSet(form_kwargs={'time': custom_kwarg})

#    data = ['01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00']
#    for item in data:
#        ls.append(item)

#        print("delta: ", item)
#    print("data: ", data)
#    delta = datetime.datetime.now() + datetime.timedelta(hours=1)
#    data = list(delta)

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
		'icnumbers': icnumbers,
		'form': form,
		'formset': formset,
	}

	return render(request, 'patient/enteral_feeding_regime/enteral_feeding_regime_form.html', context)

class EnteralFeedingRegimeUpdateView(BSModalUpdateView):
	model = EnteralFeedingRegime
	template_name = 'patient/enteral_feeding_regime/partial_edit.html'
	form_class = EnteralFeedingRegime_ModelForm
	page_title = _('EnteralFeedingRegime Form')
	success_message = _(page_title + ' form has been save successfully.')

	def get_success_url(self):
		username = self.kwargs['username']
		return reverse_lazy('patient:enteral_feeding_regime_list', kwargs={'username': username})


enteral_feeding_regime_edit = EnteralFeedingRegimeUpdateView.as_view()


class EnteralFeedingRegimeDeleteView(BSModalDeleteView):
	model = EnteralFeedingRegime
	template_name = 'patient/enteral_feeding_regime/partial_delete.html'
	page_title = _('EnteralFeedingRegime Form')
	success_message = _(page_title + ' form was deleted.')

	def get_success_url(self):
		username = self.kwargs['username']
		return reverse_lazy('patient:enteral_feeding_regime_list', kwargs={'username': username})


enteral_feeding_regime_delete = EnteralFeedingRegimeDeleteView.as_view()
