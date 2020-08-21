from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.utils.translation import ugettext as _
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.db.models import Sum, Count

from .models import *
from .forms import *
from accounts.models import *
from customers.models import *

from bootstrap_modal_forms.generic import *

# Create your views here.
@login_required
def staffdata_list(request):
	schema_name = connection.schema_name
	staffs = UserProfile.objects.filter(username=request.user.username)
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Staff List')

	if request.user.is_superuser:
#		datastaff = UserProfile.objects.all()
		datastaff = UserProfile.objects.filter(is_staff=True).exclude(is_superuser=True).order_by("id")
		print("datastaff1: ", datastaff)
#		q = Q()
#		for item in city_list:
#			q = q | Q(address__city__icontains=city)
#		fullname_data = datastaff.values_list('id', flat=True)
#		datastaffs = Admission.objects.filter(staff__in=fullname_data).order_by('staff')
#		datastaffs = UserProfile.objects.filter(username=request.user.username)
#		datastaffs = Admission.objects.all()
#		results = chain(datastaffs, datastaff)
	else:
		pass
		print("datastaff2: ", datastaff)
#		datastaff = UserProfile.objects.filter(full_name=request.user, is_staff=True).order_by("id")
#		datastaffs = Admission.objects.filter(staff__in=datastaff)
#		print("datastaff2: ", datastaff)

	context = {
		'staffs': staffs,
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		"datastaff": datastaff,
	}

	return render(request, 'staff/staff_list.html', context)


@login_required
def staffdata_detail(request, username):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	staffs = UserProfile.objects.filter(username=username)
#	staffs = UserProfile.objects.filter(staff=id)
#	staffs = UserProfile.objects.filter(pk=id).values_list('staff', flat=True).first()
	page_title = _('Staff Detail')
#	icnumbers = Admission.objects.filter(staff=request.user)

	context = {
		'titles': titles,
		'logos': logos,
		'page_title': page_title,
		"staffs": staffs,
#		"icnumbers": icnumbers,
	}

	return render(request, 'staff/staff_detail.html', context)


def load_ic_number(request):
	fullname_data = request.GET.get('full_name')
	staff_data = request.GET.get('staff')
	family_data = request.GET.get('ec_name')
	fullname_results = UserProfile.objects.filter(full_name=fullname_data).order_by('full_name')
#	fullname_results = UserProfile.objects.filter(full_name=request.user)
#	staff_results = Admission.objects.filter(staff=staff_data)
	context = {
		'fullname_results': fullname_results,
#		'staff_results': staff_results,
	}
	return render(request, 'staff/dropdown_list.html', context)


@login_required
def staff_records_list(request, username):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Staff Records')
	patientid = UserProfile.objects.get(username=username).id
	patients = StaffRecords.objects.filter(patient=patientid)
	profiles = UserProfile.objects.filter(pk=patientid)
	total_annual = StaffRecords.objects.filter(patient=patientid).aggregate(Sum('annual_leave_days'))
	total_public = StaffRecords.objects.filter(patient=patientid,).aggregate(Sum('public_holiday_days'))

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
		'total_annual': total_annual,
		'total_public': total_public,
	}

	return render(request, 'staff/staff_records/staff_records_data.html', context)



@login_required
def staff_records_create(request, username):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Staff Records')
	patients = get_object_or_404(UserProfile, username=username)
	profiles = UserProfile.objects.filter(username=username)
	icnumbers = UserProfile.objects.filter(username=username).values_list('ic_number', flat=True).first()

	initial = {
		'patient': patients,
		'ic_number': icnumbers,
	}

	if request.method == 'POST':
		form = StaffRecordsForm(request.POST or None)
		if form.is_valid():
			profile = StaffRecords()
			profile.patient = patients
			profile.date = form.cleaned_data['date']
			profile.annual_leave_days = form.cleaned_data['annual_leave_days']
			profile.public_holiday_days = form.cleaned_data['public_holiday_days']
			profile.replacement_public_holiday = form.cleaned_data['replacement_public_holiday']
			profile.medical_certificate = form.cleaned_data['medical_certificate']
			profile.siri_no_diagnosis = form.cleaned_data['siri_no_diagnosis']
			profile.emergency_leaves = form.cleaned_data['emergency_leaves']
			profile.emergency_leaves_reasons = form.cleaned_data['emergency_leaves_reasons']
			profile.unpaid_leaves = form.cleaned_data['unpaid_leaves']
			profile.unpaid_leaves_reasons = form.cleaned_data['unpaid_leaves_reasons']
			profile.total = form.cleaned_data['total']
			profile.save()

			messages.success(request, _(page_title + ' form was created.'))
			return redirect('patient:patientdata_detail', username=patients.username)
		else:
			messages.warning(request, form.errors)
	else:
		form = StaffRecordsForm(initial=initial)

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
		'icnumbers': icnumbers,
		'form': form,
	}

	return render(request, 'staff/staff_records/staff_records_form.html', context)


class StaffRecordsUpdateView(BSModalUpdateView):
	model = StaffRecords
	template_name = 'staff/staff_records/partial_edit.html'
	form_class = StaffRecordsForm
	page_title = _('StaffRecords Form')
	success_message = _(page_title + ' form has been save successfully.')

	def get_success_url(self):
		username = self.kwargs['username']
		return reverse_lazy('patient:staff_records_data', kwargs={'username': username})


staff_records_edit = StaffRecordsUpdateView.as_view()


class StaffRecordsDeleteView(BSModalDeleteView):
	model = StaffRecords
	template_name = 'staff/staff_records/partial_delete.html'
	page_title = _('StaffRecords Form')
	success_message = _(page_title + ' form was deleted.')

	def get_success_url(self):
		username = self.kwargs['username']
		return reverse_lazy('patient:staff_records_data', kwargs={'username': username})


staff_records_delete = StaffRecordsDeleteView.as_view()
