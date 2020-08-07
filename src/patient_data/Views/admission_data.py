from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.shortcuts import render, get_object_or_404
from django.utils.translation import ugettext as _
from django.http import JsonResponse
from django.urls import reverse, reverse_lazy

from patient_form.models import *
from patient_form.forms import *
from accounts.models import *
from customers.models import *

from bootstrap_modal_forms.generic import (
  BSModalCreateView,
  BSModalUpdateView,
  BSModalReadView,
  BSModalDeleteView
)

#import datetime
from datetime import *

startdate = date.today()
enddate = startdate + timedelta(days=1)

start_time_day = datetime.strptime('00:00', '%H:%M').time()
end_time_day = datetime.strptime('12:00', '%H:%M').time()
start_time_night = datetime.strptime('12:01', '%H:%M').time()
end_time_night = datetime.strptime('23:59', '%H:%M').time()


@login_required
def save_admission_data_form(request, form, template_name):
	data = dict()

	if request.method == 'POST':
		if form.is_valid():
			patients = Admission()
			patients = form.save(commit=False)
			patients.patient = request.user
			patients.save()
			data['form_is_valid'] = True
			patients = Admission.objects.all()
			data['html_admission_list'] = render_to_string('patient_data/admission_data/admission_data.html', {'patients': patients})
		else:
			data['form_is_valid'] = False

	context = {
		'form': form,
	}
	data['html_form'] = render_to_string(template_name, context, request=request)

	return JsonResponse(data)


@login_required
def admission_data(request, username):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Admission Form')
	patientid = UserProfile.objects.get(username=username).id
	patients = Admission.objects.filter(patient=patientid)
	profiles = UserProfile.objects.filter(pk=patientid)

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
	}

	return render(request, 'patient_data/admission_data/admission_data.html', context)


@login_required
def admission_data_edit(request, id):
	admissions = get_object_or_404(Admission, pk=id)
	if request.method == 'POST':
		form = AdmissionForm(request.POST or None, instance=admissions)
	else:
		form = AdmissionForm(instance=admissions)
	return save_admission_data_form(request, form, 'patient_data/admission_data/partial_edit.html')


class AdmissionUpdateView(BSModalUpdateView):
	model = Admission
#	initial = {
#		'patient': 'foo',
#		'value2': 'bar'
#	}
	template_name = 'patient_data/admission_data/partial_edit.html'
	form_class = AdmissionForm
	page_title = _('Admission Form')
	success_message = _(page_title + ' form has been save successfully.')
#	success_url = reverse_lazy('patient_data:admission_data')

	def get_success_url(self):
		username=self.kwargs['username']
		return reverse_lazy('patient_data:admission_data', kwargs={'username': username})

	def get_initial(self):		
		return {'patient': 'foo', 'value2': 'bar'}

#	def get_context_data(self, **kwargs):
#		data = super(AdmissionUpdateView, self).get_context_data(**kwargs)
#		if self.request.POST:
#			data['patient'] = AdmissionFormSet(self.request.POST, instance=self.object, form_kwargs={'request': self.request})
#		else:
#			data['patient'] = AdmissionFormSet(instance=self.object, form_kwargs={'request': self.request})
#		return data
	
	def form_valid(self, form):
		form.instance.date_created = timezone.now()
		context = self.get_context_data()
		objects = context['patient']
		with transaction.atomic():
			self.object = form.save()

			if objects.is_valid():
				objects.instance = self.object
				objects.save()

		return super(AdmissionUpdateView, self).form_valid(form)


@login_required
def admission_data_delete(request, id):
	admissions = get_object_or_404(Admission, pk=id)
	data = dict()

	if request.method == 'POST':
		admissions.delete()
		data['form_is_valid'] = True
		patients = Admission.objects.all()
		data['html_admission_list'] = render_to_string('patient_data/admission_data/admission_data.html', {'patients': patients})
		return JsonResponse(data)
	else:
		context = {'admissions': admissions}
		data['html_form'] = render_to_string('patient_data/admission_data/partial_delete.html', context, request=request)
		return JsonResponse(data)

	return JsonResponse(data)

class AdmissionDeleteView(BSModalDeleteView):
	model = Admission
	template_name = 'patient_data/admission_data/partial_delete.html'
	page_title = _('Admission Form')
	success_message = _(page_title + ' form was deleted.')

	def get_success_url(self):
		username=self.kwargs['username']
		return reverse_lazy('patient_data:admission_data', kwargs={'username': username})
