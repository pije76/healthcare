from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext as _
from django.db import connection

from accounts.models import *
from customers.models import *
from .models import *
from .forms import *

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
#		datastaff = UserProfile.objects.filter(full_name=request.user, is_staff=True).order_by("id")
#		datastaffs = Admission.objects.filter(staff__in=datastaff)

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


@login_required
def staff_records_list(request, username):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Staff Records')
	staffid = UserProfile.objects.get(username=username).id
	staffs = StaffRecords.objects.filter(staff=staffid)
	profiles = UserProfile.objects.filter(pk=staffid)
	total_annual = StaffRecords.objects.filter(staff=staffid).aggregate(Sum('annual_leave_days'))
	total_public = StaffRecords.objects.filter(staff=staffid,).aggregate(Sum('public_holiday_days'))
	total_replacement = StaffRecords.objects.filter(staff=staffid,).aggregate(Sum('replacement_public_holiday'))

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'staffs': staffs,
		'profiles': profiles,
		'total_annual': total_annual,
		'total_public': total_public,
		'total_replacement': total_replacement,
	}

	return render(request, 'staff/staff_records/staff_records_data.html', context)


@login_required
def staff_records_create(request, username):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Staff Records')
	staffs = get_object_or_404(UserProfile, username=username)
	profiles = UserProfile.objects.filter(username=username)
	icnumbers = UserProfile.objects.filter(username=username).values_list('ic_number', flat=True).first()

	thisyear = datetime.datetime.now().year

	initial = {
		'staff': staffs,
		'ic_number': icnumbers,
#		'date': thisyear,
	}

	if request.method == 'POST':
		form = StaffRecords_Form(request.POST or None)

		if form.is_valid():
			profile = StaffRecords()
			profile.staff = staffs
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
			profile.save()

			messages.success(request, _(page_title + ' form was created.'))
			return redirect('staff:staffdata_detail', username=staffs.username)
		else:
			messages.warning(request, form.errors)
	else:
		form = StaffRecords_Form(initial=initial)

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'staffs': staffs,
		'profiles': profiles,
		'icnumbers': icnumbers,
		'form': form,
	}

	return render(request, 'staff/staff_records/staff_records_form.html', context)


class StaffRecordsUpdateView(BSModalUpdateView):
	model = StaffRecords
	template_name = 'staff/staff_records/partial_edit.html'
	form_class = StaffRecord_ModelForm
	page_title = _('StaffRecords Form')
	success_message = _(page_title + ' form has been save successfully.')

	def get_success_url(self):
		username = self.kwargs['username']
		return reverse_lazy('staff:staffdata_detail', kwargs={'username': username})


staff_records_edit = StaffRecordsUpdateView.as_view()


class StaffRecordsDeleteView(BSModalDeleteView):
	model = StaffRecords
	template_name = 'staff/staff_records/partial_delete.html'
	page_title = _('StaffRecords Form')
	success_message = _(page_title + ' form was deleted.')

	def get_success_url(self):
		username = self.kwargs['username']
		return reverse_lazy('staff:staffdata_detail', kwargs={'username': username})


staff_records_delete = StaffRecordsDeleteView.as_view()
