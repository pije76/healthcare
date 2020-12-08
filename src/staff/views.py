from django.contrib.auth.decorators import login_required
from django.db import connection
from django.db.models import Sum, Count
from django.http import HttpResponse
from django.shortcuts import render, redirect, HttpResponseRedirect, Http404, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext as _


from accounts.models import *
from accounts.decorators import *
from customers.models import *
from .models import *
from .forms import *
from patient.utils import *

from reportlab.pdfgen import canvas
from bootstrap_modal_forms.generic import *


# Create your views here.
@login_required
@admin_required
def staffdata_list(request):
    schema_name = connection.schema_name
    staffs = UserProfile.objects.filter(username=request.user.username)
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(
        schema_name=schema_name).values_list('title', flat=True).first()
    page_title = _('Staff List')
    themes = request.session.get('theme')

#	if request.user.is_superuser:
#		datastaff = UserProfile.objects.all()
    datastaff = UserProfile.objects.filter(
        is_staff=True).exclude(is_superuser=True).order_by("id")
#		q = Q()
#		for item in city_list:
#			q = q | Q(address__city__icontains=city)
#		fullname_data = datastaff.values_list('id', flat=True)
#		datastaffs = Admission.objects.filter(staff__in=fullname_data).order_by('staff')
#		datastaffs = UserProfile.objects.filter(username=request.user.username)
#		datastaffs = Admission.objects.all()
#		results = chain(datastaffs, datastaff)

#		context = {
#			'staffs': staffs,
#			'logos': logos,
#			'titles': titles,
#			'page_title': page_title,
#			"datastaff": datastaff,
#		}

#	else:
#		pass
#		datastaff = UserProfile.objects.filter(full_name=request.user, is_staff=True).order_by("id")
#		datastaffs = Admission.objects.filter(staff__in=datastaff)

    context = {
        'staffs': staffs,
        'logos': logos,
        'titles': titles,
        'page_title': page_title,
        "datastaff": datastaff,
        "themes": themes,
    }

    return render(request, 'staff/staff_list.html', context)


@login_required
def staffdata_detail(request, username):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(
        schema_name=schema_name).values_list('title', flat=True).first()
    staffs = UserProfile.objects.filter(username=username)
    staffid = UserProfile.objects.filter(
        username=username).values_list('id', flat=True).first()
    overtimeclaim = OvertimeClaim.objects.filter(staff=staffid)
    staffrecords = StaffRecords.objects.filter(staff=staffid)
#	staffs = UserProfile.objects.filter(staff=id)
#	staffs = UserProfile.objects.filter(pk=id).values_list('staff', flat=True).first()
    page_title = _('Staff Detail')
    themes = request.session.get('theme')
#	icnumbers = Admission.objects.filter(staff=request.user)

    context = {
        'titles': titles,
        'logos': logos,
        'page_title': page_title,
        "staffs": staffs,
        'overtimeclaim': overtimeclaim,
        'staffrecords': staffrecords,
        "themes": themes,
        #		"icnumbers": icnumbers,
    }

    return render(request, 'staff/staff_detail.html', context)


@login_required
def overtime_claim_list(request, username):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(
        schema_name=schema_name).values_list('title', flat=True).first()
    page_title = _('Overtime Claim Form')
    staffid = UserProfile.objects.filter(
        username=username).values_list('id', flat=True).first()
    staffs = OvertimeClaim.objects.filter(staff=staffid)
    profiles = UserProfile.objects.filter(pk=staffid)
    themes = request.session.get('theme')

    context = {
        'logos': logos,
        'titles': titles,
        'page_title': page_title,
        'staffs': staffs,
        'profiles': profiles,
        "themes": themes,
    }

    return render(request, 'staff/overtime_claim/overtime_claim_data.html', context)


@login_required
def overtime_claim_create(request, username):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(
        schema_name=schema_name).values_list('title', flat=True).first()
    page_title = _('Overtime Claim Form')
    staffs = get_object_or_404(UserProfile, username=username)
    staffchecked = get_object_or_404(UserProfile, full_name=request.user)
    profiles = UserProfile.objects.filter(username=username)
    icnumbers = UserProfile.objects.filter(
        username=username).values_list('ic_number', flat=True).first()
    themes = request.session.get('theme')

    initial = {
        'staff': staffs,
        'ic_number': icnumbers,
        'checked_sign_by': staffchecked,
        'verify_by': None,
    }

    if request.method == 'POST':
        form = OvertimeClaim_Form(request.POST or None)
        if form.is_valid():

            duration_time_from = form.cleaned_data['duration_time_from']
            duration_time_to = form.cleaned_data['duration_time_to']
            sec_from = duration_time_from.hour * 60 + duration_time_from.minute
            sec_to = duration_time_to.hour * 60 + duration_time_to.minute
            total_delta = (sec_to - sec_from) / 60

            profile = OvertimeClaim()
            profile.staff = staffs
            profile.date = form.cleaned_data['date']
            profile.duration_time_from = form.cleaned_data['duration_time_from']
            profile.duration_time_to = form.cleaned_data['duration_time_to']
            profile.hours = form.cleaned_data['hours']
            profile.total_hours = total_delta
            profile.checked_sign_by = staffchecked
            verify_by_data = form.cleaned_data['verify_by'] or None
            staffverify = get_object_or_404(
                UserProfile, full_name=verify_by_data)

            if verify_by_data is not None:
                profile.verify_by = staffverify
#				profile.verify_by = verify_by_data
#				profile.verify_by = form.cleaned_data['verify_by']
            else:
                profile.verify_by = None

            profile.save()

            messages.success(request, _(page_title + ' form was created.'))
            return redirect('staff:staffdata_detail', username=staffs.username)
        else:
            messages.warning(request, form.errors)
    else:
        form = OvertimeClaim_Form(initial=initial)

    context = {
        'logos': logos,
        'titles': titles,
        'page_title': page_title,
        'staffs': staffs,
        'profiles': profiles,
        'icnumbers': icnumbers,
        'form': form,
        "themes": themes,
    }

    return render(request, 'staff/overtime_claim/overtime_claim_form.html', context)


def overtime_claim_pdf(response, username):
    schema_name = connection.schema_name
    titles = Client.objects.filter(
        schema_name=schema_name).values_list('title', flat=True).first()
    page_title = _('Application For Home Leave')
    staffid = UserProfile.objects.filter(
        username=username).values_list('id', flat=True).first()
    staffs = get_object_or_404(UserProfile, username=username)
    icnumbers = UserProfile.objects.filter(
        username=username).values_list('ic_number', flat=True).first()
    profiles = UserProfile.objects.filter(pk=staffid)

    pdfname = _('Overtime Claim')
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename=pdfname'
#   response['Content-Disposition'] = 'attachment; filename="{}"'.format(pdfname)
    application_data = OvertimeClaim.objects.all()
#   application_data = ApplicationForHomeLeave.objects.all[0].name
    detail_application_data = u", ".join(str(obj) for obj in application_data)

    buffer = BytesIO()
    p = canvas.Canvas(buffer)
    p.setTitle(pdfname)
    p.drawString(100, 100, detail_application_data)
    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    context = {
        'titles': titles,
        'page_title': page_title,
        'pdfname': pdfname,
        'staffs': staffs,
        'icnumbers': icnumbers,
        'profiles': profiles,
        'application_data': application_data,
    }

    result = generate_pdf('staff/overtime_claim/overtime_claim_pdf.html',
                          file_object=response, context=context)
    return result
#   return response


class OvertimeClaimUpdateView(BSModalUpdateView):
    model = OvertimeClaim
    template_name = 'staff/overtime_claim/partial_edit.html'
    form_class = OvertimeClaim_ModelForm
    page_title = _('OvertimeClaim Form')
    success_message = _(page_title + ' form has been save successfully.')

    def get_form(self, form_class=None):
        form = super().get_form(form_class=None)
        form.fields['date'].label = _("Date")
        form.fields['duration_time_from'].label = _("Duration-Time From")
        form.fields['duration_time_to'].label = _("Duration-Time To")
        form.fields['total_hours'].label = _("Total Hours")
        form.fields['checked_sign_by'].label = _("Checked Sign by")
        form.fields['verify_by'].label = _("Verify by")
#		if form.fields['verify_by'] is None:
#			pass
        return form

    def get_success_url(self):
        username = self.kwargs['username']
        return reverse_lazy('staff:overtime_claim_list', kwargs={'username': username})


overtime_claim_edit = OvertimeClaimUpdateView.as_view()


class OvertimeClaimDeleteView(BSModalDeleteView):
    model = OvertimeClaim
    template_name = 'staff/overtime_claim/partial_delete.html'
    page_title = _('OvertimeClaim Form')
    success_message = _(page_title + ' form was deleted.')

    def get_success_url(self):
        username = self.kwargs['username']
        return reverse_lazy('staff:overtime_claim_list', kwargs={'username': username})


overtime_claim_delete = OvertimeClaimDeleteView.as_view()


@login_required
def staff_records_list(request, username):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(
        schema_name=schema_name).values_list('title', flat=True).first()
    page_title = _('Staff Records')
    staffid = UserProfile.objects.filter(
        username=username).values_list('id', flat=True).first()
    staffs = StaffRecords.objects.filter(staff=staffid)
    profiles = UserProfile.objects.filter(pk=staffid)
    total_annual = StaffRecords.objects.filter(
        staff=staffid).aggregate(Sum('annual_leave_days'))
    total_public = StaffRecords.objects.filter(
        staff=staffid,).aggregate(Sum('public_holiday_days'))
    total_replacement = StaffRecords.objects.filter(
        staff=staffid,).aggregate(Sum('replacement_public_holiday'))
    themes = request.session.get('theme')

    context = {
        'logos': logos,
        'titles': titles,
        'page_title': page_title,
        'staffs': staffs,
        'profiles': profiles,
        'total_annual': total_annual,
        'total_public': total_public,
        'total_replacement': total_replacement,
        "themes": themes,
    }

    return render(request, 'staff/staff_records/staff_records_data.html', context)


@login_required
def staff_records_create(request, username):
    schema_name = connection.schema_name
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(
        schema_name=schema_name).values_list('title', flat=True).first()
    page_title = _('Staff Records')
    staffs = get_object_or_404(UserProfile, username=username)
    profiles = UserProfile.objects.filter(username=username)
    icnumbers = UserProfile.objects.filter(
        username=username).values_list('ic_number', flat=True).first()
    themes = request.session.get('theme')

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
        "themes": themes,
    }

    return render(request, 'staff/staff_records/staff_records_form.html', context)


class StaffRecordsUpdateView(BSModalUpdateView):
    model = StaffRecords
    template_name = 'staff/staff_records/partial_edit.html'
    form_class = StaffRecord_ModelForm
    page_title = _('StaffRecords Form')
    success_message = _(page_title + ' form has been save successfully.')

    def get_form(self, form_class=None):
        form = super().get_form(form_class=None)
        form.fields['date'].label = _("Date")
        form.fields['annual_leave_days'].label = _("Annual Leave Days")
        form.fields['public_holiday_days'].label = _("Public Holiday Days")
        form.fields['replacement_public_holiday'].label = _(
            "Replacement Public Holiday")
        form.fields['medical_certificate'].label = _("Medical Certificate")
        form.fields['siri_no_diagnosis'].label = _("Siri No Diagnosis")
        form.fields['emergency_leaves'].label = _("Emergency Leaves")
        form.fields['emergency_leaves_reasons'].label = _(
            "Emergency Leaves Reasons")
        form.fields['unpaid_leaves'].label = _("Unpaid Leaves")
        form.fields['unpaid_leaves_reasons'].label = _("Unpaid Leaves Reasons")
        return form

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
