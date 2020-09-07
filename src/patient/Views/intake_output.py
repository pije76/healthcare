from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.db.models import Sum, Count
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import ugettext as _
from django.urls import reverse, reverse_lazy

from patient.models import *
from patient.Forms.intake_output import *
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
def intake_output_list(request, username):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Intake Output Chart')
	patientid = UserProfile.objects.get(username=username).id
	patients = IntakeOutput.objects.filter(patient=patientid)
	profiles = UserProfile.objects.filter(pk=patientid)

	total_oral_day = IntakeOutput.objects.filter(patient=patientid, date__range=[startdate, enddate], time__range=(start_time_day, end_time_day)).aggregate(Sum('intake_oral_ml'))
	total_parental_day = IntakeOutput.objects.filter(patient=patientid, date__range=[startdate, enddate], time__range=(start_time_day, end_time_day)).aggregate(Sum('intake_parenteral_ml'))
	total_other_intake_day = IntakeOutput.objects.filter(patient=patientid, date__range=[startdate, enddate], time__range=(start_time_day, end_time_day)).aggregate(Sum('intake_other_ml'))
	total_cum_day = IntakeOutput.objects.filter(patient=patientid, date__range=[startdate, enddate], time__range=(start_time_day, end_time_day)).aggregate(Sum('output_urine_cum'))
	total_gastric_day = IntakeOutput.objects.filter(patient=patientid, date__range=[startdate, enddate], time__range=(start_time_day, end_time_day)).aggregate(Sum('output_gastric_ml'))
	total_other_output_day = IntakeOutput.objects.filter(patient=patientid, date__range=[startdate, enddate], time__range=(start_time_day, end_time_day)).aggregate(Sum('output_other_ml'))

	total_oral_night = IntakeOutput.objects.filter(patient=patientid, date__range=[startdate, enddate], time__range=(start_time_night, end_time_night)).aggregate(Sum('intake_oral_ml'))
	total_parental_night = IntakeOutput.objects.filter(patient=patientid, date__range=[startdate, enddate], time__range=(start_time_night, end_time_night)).aggregate(Sum('intake_parenteral_ml'))
	total_other_intake_night = IntakeOutput.objects.filter(patient=patientid, date__range=[startdate, enddate], time__range=(start_time_night, end_time_night)).aggregate(Sum('intake_other_ml'))
	total_cum_night = IntakeOutput.objects.filter(patient=patientid, date__range=[startdate, enddate], time__range=(start_time_night, end_time_night)).aggregate(Sum('output_urine_cum'))
	total_gastric_night = IntakeOutput.objects.filter(patient=patientid, date__range=[startdate, enddate], time__range=(start_time_night, end_time_night)).aggregate(Sum('output_gastric_ml'))
	total_other_output_night = IntakeOutput.objects.filter(patient=patientid, date__range=[startdate, enddate], time__range=(start_time_night, end_time_night)).aggregate(Sum('output_other_ml'))

	total_oral = IntakeOutput.objects.filter(patient=patientid).aggregate(Sum(F('intake_oral_ml')))
	total_parental = IntakeOutput.objects.filter(patient=patientid).aggregate(Sum(F('intake_parenteral_ml')))
	total_other_intake = IntakeOutput.objects.filter(patient=patientid,).aggregate(Sum(F('intake_other_ml')))

	agg_data = IntakeOutput.objects.aggregate(total_source1=Count('intake_oral_ml'), total_source2=Count('intake_parenteral_ml'), total_source3=Count('intake_other_ml'))
	total_count = sum(agg_data.values())
	res = IntakeOutput.objects.all().annotate(total_source1=Count('intake_oral_ml'), total_source2=Count('intake_parenteral_ml'), total_source3=Count('intake_other_ml')).annotate(total_count=F('total_source1') + F('total_source2') + F('total_source3')).order_by('-total_count')

#	total_intake = total_oral+total_parental+total_other_intake
	total_intake = sum(IntakeOutput.objects.filter(patient=patientid).order_by('date').aggregate(x=Sum('intake_oral_ml'), y=Sum('intake_parenteral_ml'), z=Sum('intake_other_ml')).values())

#	total_intake = IntakeOutput.objects.all().aggregate(latest=Sum(F('output_urine_cum') + F('output_gastric_ml') + F('output_other_ml')))

#	total_intake = IntakeOutput.objects.filter(patient=patientid).annotate(Count('output_urine_cum')).annotate(Count('output_gastric_ml')).annotate(Count('output_other_ml'))
#   total_output = total_cum+total_gastric+total_other_output
	total_output = sum(IntakeOutput.objects.filter(patient=patientid).order_by('date').aggregate(x=Sum('output_urine_cum'), y=Sum('output_gastric_ml'), z=Sum('output_other_ml')).values())

	total_balance = total_intake + total_output

	time_range_day = IntakeOutput.objects.filter(patient=patientid, time__range=(start_time_day, end_time_day))
	time_range_night = IntakeOutput.objects.filter(patient=patientid, time__range=(start_time_night, end_time_night))

	time_range = IntakeOutput.objects.filter(patient=patientid).order_by('date')

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,

		'total_oral_day': total_oral_day,
		'total_parental_day': total_parental_day,
		'total_other_intake_day': total_other_intake_day,
		'total_cum_day': total_cum_day,
		'total_gastric_day': total_gastric_day,
		'total_other_output_day': total_other_output_day,

		'total_oral_night': total_oral_night,
		'total_parental_night': total_parental_night,
		'total_other_intake_night': total_other_intake_night,
		'total_cum_night': total_cum_night,
		'total_gastric_night': total_gastric_night,
		'total_other_output_night': total_other_output_night,

		'total_intake': total_intake,
#       'total_parental': total_parental,

#       'total_intake': total_intake,
		'total_output': total_output,
		'total_balance': total_balance,

		'time_range_day': time_range_day,
		'time_range_night': time_range_night,
		'time_range': time_range,
	}

	return render(request, 'patient/intake_output/intake_output_data.html', context)


@login_required
def intake_output_create(request, username):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Intake Output Chart')
	profiles = UserProfile.objects.filter(username=username)
	patientid = UserProfile.objects.get(username=username).id
	patients = get_object_or_404(UserProfile, username=username)
	icnumbers = UserProfile.objects.filter(username=username).values_list('ic_number', flat=True).first()
	intakeoutput = IntakeOutput.objects.filter(patient=patientid)

	initial = [{
        'patient': item.full_name,
    }
    for item in profiles]

	initial_formset_factory = [
	{
		'patient': patients,
		'ic_number': icnumbers,
	}]

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
		formset = IntakeOutput_FormSet(request.POST or None)

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
				profile.output_urine_ml = item.cleaned_data['output_urine_ml']
				profile.output_urine_cum = item.cleaned_data['output_urine_cum']
				profile.output_gastric_ml = item.cleaned_data['output_gastric_ml']
				profile.output_other_type = item.cleaned_data['output_other_type']
				profile.output_other_ml = item.cleaned_data['output_other_ml']
				profile.save()

			messages.success(request, _(page_title + ' form was created.'))
			return redirect('patient:patientdata_detail', username=patients.username)
		else:
#           messages.warning(request, form.errors)
			messages.warning(request, formset.errors)
	else:
#       form = IntakeOutputForm(initial=initial)
		formset = IntakeOutput_FormSet(initial=initial_list)

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
		'icnumbers': icnumbers,
#       'form': form,
		'formset': formset,
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
#       return reverse_lazy('patient:patientdata_detail', kwargs={'username': self.object.username})

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
