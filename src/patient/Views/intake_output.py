from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.db.models import F, Sum, Count
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils.translation import ugettext as _

from patient.models import *
from patient.views import *
from patient.Forms.intake_output import *
from accounts.models import *
from customers.models import *

from bootstrap_modal_forms.generic import *


@login_required
def intake_output_list(request, username):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Intake Output Chart')
	patientid = UserProfile.objects.get(username=username).id
	patients = IntakeOutput.objects.filter(patient=patientid)
	profiles = UserProfile.objects.filter(pk=patientid)

	total_intake = IntakeOutput.objects.annotate(sum_abc=F('intake_oral_ml') + F('intake_parenteral_ml') + F('intake_other_ml')).aggregate(total=Sum('sum_abc'))['total'] or 0
	total_output = IntakeOutput.objects.annotate(sum_abc=F('output_urine_ml') + F('output_gastric_ml') + F('output_other_ml')).aggregate(total=Sum('sum_abc'))['total'] or 0
	total_balance = total_intake + total_output

	time_range_day = IntakeOutput.objects.filter(patient=patientid, time__range=[start_time_day, end_time_day])
	time_range_night = IntakeOutput.objects.filter(patient=patientid, time__range=[start_time_night, end_time_night])
	get_lastdate = IntakeOutput.objects.filter(patient=patientid).order_by('-date').exclude(time__isnull=True).values_list('date', flat=True).first()
	intakeoutput_data = IntakeOutput.objects.filter(patient=patientid).filter(date=get_lastdate).exclude(time__isnull=True)
	themes = request.session.get('theme')

	initial_list = {
		'date': get_lastdate,
	}

	if request.method == 'POST':
		form = IntakeOutputForm(request.POST or None)

		if form.is_valid():
#			profile = IntakeOutput()
#			profile.patient = patients
#			profile.date = form.cleaned_data['date']
#			profile.save()

			messages.success(request, _(page_title + ' form was created.'))
			return redirect('patient:patientdata_detail', username=patients.username)
		else:
			messages.warning(request, form.errors)
	else:
		form = IntakeOutputForm(initial=initial_list)

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,

		'total_intake': total_intake,
		'total_output': total_output,
		'total_balance': total_balance,

		'time_range_day': time_range_day,
		'time_range_night': time_range_night,
		'intakeoutput_data': intakeoutput_data,
		'form': form,
		"themes": themes,
	}

	return render(request, 'patient/intake_output/intake_output_data.html', context)


@login_required
def intake_output_create(request, username):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Intake Output Chart')
	profiles = UserProfile.objects.filter(username=username)
	patients = get_object_or_404(UserProfile, username=username)
	icnumbers = UserProfile.objects.filter(username=username).values_list('ic_number', flat=True).first()
	themes = request.session.get('theme')

	initial_form = {
		'patient': patients,
		'date': get_today,
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

	if request.method == 'POST':
		form = IntakeOutputForm(request.POST or None)
		formset = IntakeOutput_FormSet(request.POST or None)

		if form.is_valid():
			profile_form = IntakeOutput()
			profile_form.patient = patients
			profile_form.date = form.cleaned_data['date']
			profile_form.save()

		if formset.is_valid():
			for item in formset:
				profile = IntakeOutput()
				profile.patient = patients
				profile.date = item.cleaned_data['date']
				profile.time = item.cleaned_data['time']
				profile.intake_oral_type = item.cleaned_data['intake_oral_type']
				profile.intake_oral_ml = item.cleaned_data['intake_oral_ml']
				profile.intake_parenteral_type = item.cleaned_data['intake_parenteral_type']
				profile.intake_parenteral_ml = item.cleaned_data['intake_parenteral_ml']
				profile.intake_other_type = item.cleaned_data['intake_other_type']
				profile.intake_other_ml = item.cleaned_data['intake_other_ml']
				profile.output_urine_type = item.cleaned_data['output_urine_type']
				profile.output_urine_ml = item.cleaned_data['output_urine_ml']
				profile.output_gastric_ml = item.cleaned_data['output_gastric_ml']
				profile.output_other_type = item.cleaned_data['output_other_type']
				profile.output_other_ml = item.cleaned_data['output_other_ml']
				profile.save()

			messages.success(request, _(page_title + ' form was created.'))
			return redirect('patient:patientdata_detail', username=patients.username)
		else:
			messages.warning(request, form.errors)
			messages.warning(request, formset.errors)
	else:
		form = IntakeOutputForm(initial=initial_form)
		formset = IntakeOutput_FormSet(initial=initial_list)

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
		'icnumbers': icnumbers,
		'form': form,
		'formset': formset,
		"themes": themes,
	}

	return render(request, 'patient/intake_output/intake_output_form.html', context)


class IntakeOutputCreateView(BSModalCreateView):
	form_class = IntakeOutput_ModelForm
	template_name = 'patient/_formintake_output_form.html'
	page_title = _('Intake Output Chart')
	success_message = _(page_title + ' form was created.')

	def get_success_url(self):
		username = self.kwargs['username']
		return reverse_lazy('patient:patientdata_detail', kwargs={'username': username})

	def get_context_data(self, **kwargs):
		data = super().get_context_data(**kwargs)

		if self.request.POST:
			data['formset'] = IntakeOutput_ModelFormSet(self.request.POST, instance=self.object, form_kwargs={'request': self.request})
		else:
			data['formset'] = IntakeOutput_ModelFormSet(instance=self.object, form_kwargs={'request': self.request})
		return data

	def form_valid(self, form):
		form.instance.date_created = timezone.now()

		context = self.get_context_data()
		formset = context['formset']

		with transaction.atomic():
			self.object = form.save()

			if formset.is_valid():
				formset.instance = self.object
				formset.save()

		return super().form_valid(form)


intake_output_new = IntakeOutputCreateView.as_view()


class IntakeOutputUpdateView(BSModalUpdateView):
	model = IntakeOutput
	template_name = 'patient/intake_output/partial_edit.html'
	form_class = IntakeOutput_ModelForm
	page_title = _('IntakeOutput Form')
	success_message = _(page_title + ' form has been save successfully.')

	def get_form(self, form_class=None):
		form = super().get_form(form_class=None)
		form.fields['date'].label = _("Date")
		form.fields['time'].label = _("Time")
		form.fields['intake_oral_type'].label = _("Intake Oral Type")
		form.fields['intake_oral_ml'].label = _("Intake Oral ML")
		form.fields['intake_parenteral_type'].label = _("Intake Parenteral Type")
		form.fields['intake_parenteral_ml'].label = _("Intake Parenteral ML")
		form.fields['intake_other_type'].label = _("Intake Other Type")
		form.fields['intake_other_ml'].label = _("Intake Other ML")
		form.fields['output_urine_type'].label = _("Output Urine Type")
		form.fields['output_urine_ml'].label = _("Output Urine ML")
		form.fields['output_gastric_ml'].label = _("Output Gastric ML")
		form.fields['output_other_type'].label = _("Output Other Type")
		form.fields['output_other_ml'].label = _("Output Other ML")
		return form

	def get_success_url(self):
		username = self.kwargs['username']
		return reverse_lazy('patient:intake_output_list', kwargs={'username': username})


intake_output_edit = IntakeOutputUpdateView.as_view()


class IntakeOutputDeleteView(BSModalDeleteView):
	model = IntakeOutput
	template_name = 'patient/intake_output/partial_delete.html'
	page_title = _('IntakeOutput Form')
	success_message = _(page_title + ' form was deleted.')

	def get_success_url(self):
		username = self.kwargs['username']
		return reverse_lazy('patient:intake_output_list', kwargs={'username': username})


intake_output_delete = IntakeOutputDeleteView.as_view()
