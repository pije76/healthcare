from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.db import connection
from django.db.models import F, Func, Value, CharField, Sum, Value, CharField
from django.db.models.functions import Cast, Concat, ExtractYear, ExtractMonth, ExtractDay, ExtractHour, ExtractMinute
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.template.loader import render_to_string, get_template
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.utils.translation import ugettext as _

from patient.models import *
from patient.Forms.enteral_feeding_regime import *
from accounts.models import *
from customers.models import *
from ..views import *

from bootstrap_modal_forms.generic import *

import datetime
#import json


@login_required
def enteral_feeding_regime_list(request, username):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Enteral Feeding Regime')
	user_name = UserProfile.objects.get(username=username).username
	patients = get_object_or_404(UserProfile, username=username)
	patientid = UserProfile.objects.get(username=username).id
	enteralfeedingregime_data = EnteralFeedingRegime.objects.filter(patient=patientid).exclude(amount__isnull=True)
	profiles = UserProfile.objects.filter(pk=patientid)

	get_lastdate = EnteralFeedingRegime.objects.filter(patient=patientid).order_by('-date').exclude(amount__isnull=True).values_list('date', flat=True).first()
	get_warm_water_before = EnteralFeedingRegime.objects.filter(patient=patientid).filter(date=get_lastdate).values_list('warm_water_before', flat=True).first()
	get_warm_water_after = EnteralFeedingRegime.objects.filter(patient=patientid).filter(date=get_lastdate).values_list('warm_water_after', flat=True).first()

	initial = {
		'patient': patients,
		'date': get_lastdate,
		'warm_water_before': get_warm_water_before,
		'warm_water_after': get_warm_water_after,
	}

	data = dict()

	if request.method == "GET":
		form = EnteralFeedingRegime_Water_ModelForm(initial=initial)

		get_newdate = request.GET.get('get_newdate', None)
		if get_newdate is not None:
			set_newdate = datetime.datetime.strptime(get_newdate, '%d-%m-%Y')
		else:
			set_newdate = get_lastdate

		warm_water_before = EnteralFeedingRegime.objects.filter(patient=patientid, date=set_newdate).values_list('warm_water_before', flat=True).first()
		warm_water_after = EnteralFeedingRegime.objects.filter(patient=patientid, date=set_newdate).values_list('warm_water_after', flat=True).first()
		total_feeding = EnteralFeedingRegime.objects.filter(patient=patientid).filter(date=set_newdate).aggregate(Sum('amount'))
		get_total_feeding = total_feeding['amount__sum']
		get_total_fluids = warm_water_before + warm_water_after + get_total_feeding

		if warm_water_before and warm_water_after is not None:
			total_warm_water = warm_water_before + warm_water_after
		else:
			pass

		context1 = {
			'logos': logos,
			'titles': titles,
			'page_title': page_title,
			'profiles': profiles,
			'user_name': user_name,
			'total_feeding': get_total_feeding,
			'total_fluids': get_total_fluids,
			'enteralfeedingregime_data': enteralfeedingregime_data,
			'warm_water_before': get_warm_water_before,
			'warm_water_after': get_warm_water_after,
			'form': form,
		}

		return render(request, 'patient/enteral_feeding_regime/enteral_feeding_regime_data.html', context1)

	if request.method == "POST" and request.is_ajax:
		form = EnteralFeedingRegime_Water_ModelForm(request.POST or None)

		get_newdate = request.POST.get('get_newdate', None)
		if get_newdate is not None:
			set_newdate = datetime.datetime.strptime(get_newdate, '%d-%m-%Y')
		else:
			set_newdate = get_lastdate

		warm_water_before = EnteralFeedingRegime.objects.filter(patient=patientid, date=set_newdate).values_list('warm_water_before', flat=True).first()
		warm_water_after = EnteralFeedingRegime.objects.filter(patient=patientid, date=set_newdate).values_list('warm_water_after', flat=True).first()
		total_feeding = EnteralFeedingRegime.objects.filter(patient=patientid).filter(date=set_newdate).aggregate(Sum('amount'))
		get_total_feeding = total_feeding['amount__sum']
		get_total_fluids = warm_water_before + warm_water_after + get_total_feeding

		if form.is_valid():
#			form.save()

			if warm_water_before and warm_water_after is not None:
				total_warm_water = warm_water_before + warm_water_after
			else:
				pass

			data['warm_water_before'] = warm_water_before
			data['warm_water_after'] = warm_water_after
			data['total_warm_water'] = total_warm_water
			data['total_feeding'] = get_total_feeding
			data['total_fluids'] = get_total_fluids

			return JsonResponse(data)
		else:
#			messages.warning(request, form.errors)
			return JsonResponse({"response error": form.errors}, status=400)

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
	]

	if request.method == 'POST':
		form = EnteralFeedingRegime_Form(request.POST or None)
		formset = EnteralFeedingRegime_FormSet(request.POST or None)

		if form.is_valid():

			profile_form = EnteralFeedingRegime()
			profile_form.patient = patients
			profile_form.date = form.cleaned_data['date']
			profile_form.warm_water_before = form.cleaned_data['warm_water_before']
			profile_form.warm_water_after = form.cleaned_data['warm_water_after']
			profile_form.save()

		if formset.is_valid():
			for item in formset:
#				get_date = EnteralFeedingRegime.objects.filter(patient=patients).values_list("date", flat=True).first()
				profile = EnteralFeedingRegime()
				profile.patient = patients
				profile.date = item.cleaned_data['date']
#				profile.date = get_date
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

	def get_form(self, form_class=None):
		form = super().get_form(form_class=None)
		form.fields['date'].label = _("Date")
		form.fields['time'].label = _("Time")
		form.fields['type_of_milk'].label = _("Type of Milk")
		form.fields['amount'].label = _("Amount")
		return form

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
