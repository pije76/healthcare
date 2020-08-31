from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.db.models import F, Func, Value, CharField
from django.db.models import Value, CharField
from django.db.models.functions import Cast, Concat, ExtractYear, ExtractMonth, ExtractDay, ExtractHour, ExtractMinute
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.utils.translation import ugettext as _
from django.views.generic import View
from django.views.generic.detail import DetailView


from patient.models import *
from patient.Forms.application_home_leave import *
from accounts.models import *
from customers.models import *
from ..utils import *

from bootstrap_modal_forms.generic import *
from reportlab.pdfgen import canvas

from io import BytesIO

startdate = datetime.date.today()
enddate = startdate + datetime.timedelta(days=1)

start_time_day = datetime.datetime.strptime('00:00', '%H:%M').time()
end_time_day = datetime.datetime.strptime('12:00', '%H:%M').time()
start_time_night = datetime.datetime.strptime('12:01', '%H:%M').time()
end_time_night = datetime.datetime.strptime('23:59', '%H:%M').time()


@login_required
def application_home_leave_list(request, username):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Application For Home Leave')
	patientid = UserProfile.objects.get(username=username).id
	patients = ApplicationForHomeLeave.objects.filter(patient=patientid)
	profiles = UserProfile.objects.filter(pk=patientid)

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
	}

	return render(request, 'patient/application_home_leave/application_home_leave_data.html', context)


@login_required
def application_home_leave_create(request, username):
	schema_name = connection.schema_name
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Application For Home Leave')
	patients = get_object_or_404(UserProfile, username=username)
	profiles = UserProfile.objects.filter(username=username)
	icnumbers = UserProfile.objects.filter(username=username).values_list('ic_number', flat=True).first()

	initial = {
#       'patient': patients,
#       'ic_number': icnumbers,
	}

	if request.method == 'POST':
#		form = ApplicationForHomeLeave_ModelForm(request.POST or None, instance=request.user)
		form = ApplicationForHomeLeave_Form(request.POST or None)

		if form.is_valid():
#			profile = form.save(commit=False)
			profile = ApplicationForHomeLeave()
			profile.patient = form.cleaned_data['patient']
			profile.family_name = form.cleaned_data['family_name']
			profile.family_ic_number = form.cleaned_data['family_ic_number']
			profile.family_relationship = form.cleaned_data['family_relationship']
			profile.family_phone = form.cleaned_data['family_phone']
			profile.designation = form.cleaned_data['designation']
			profile.signature = form.cleaned_data['signature']
			profile.date = form.cleaned_data['date']
			profile.save()

			messages.success(request, _(page_title + ' form was created.'))
			return redirect('patient:patientdata_detail', username=patients.username)
		else:
			messages.warning(request, form.errors)
	else:
		form = ApplicationForHomeLeave_Form()
#       form = ApplicationForHomeLeaveForm(initial=initial)
#       form = ApplicationForHomeLeaveForm(instance=request.user)
#       form = ApplicationForHomeLeaveForm(initial=initial, instance=request.user)
#       form = ApplicationForHomeLeaveForm()

	context = {
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'patients': patients,
		'profiles': profiles,
		'icnumbers': icnumbers,
		'form': form,
	}

	return render(request, 'patient/application_home_leave/application_home_leave_form.html', context)

class PdfMixin(object):
    content_type = "application/pdf"
    response_class = PdfResponse

def application_home_leave_pdf(response, username):
	schema_name = connection.schema_name
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Application For Home Leave')
	patientid = UserProfile.objects.get(username=username).id
	patients = ApplicationForHomeLeave.objects.filter(patient=patientid)
	profiles = UserProfile.objects.filter(pk=patientid)

	pdfname = _('Application For Home Leave')
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'inline; filename=pdfname'
#	response['Content-Disposition'] = 'attachment; filename="{}"'.format(pdfname)
	application_data = ApplicationForHomeLeave.objects.all()
#	application_data = ApplicationForHomeLeave.objects.all[0].name
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
		'patients': patients,
		'profiles': profiles,
		'application_data': application_data
	}

	result = generate_pdf('patient/application_home_leave/application_home_leave_pdf.html', file_object=response, context=context)
	return result
#	return response


def ticket(request, id):
	application_id = get_object_or_404(ApplicationForHomeLeave, id=id)
	pdf_ticket = ticket_to_pdf(application_id.visitor, application_id.event)
	response = HttpResponse(pdf_ticket['content'], content_type=pdf_ticket['mimetype'])
	response['Content-Disposition'] = ('inline; filename=' + pdf_ticket['filename'])
	return response


def ticket_to_pdf(visitor, event):
	filename = 'ticket.pdf'
	current_site = ApplicationForHomeLeave.objects.get_current().domain
	site = '{scheme}://{host}'.format(scheme=config.SCHEME, host=current_site)
	url = pyqrcode.create(current_site + visitor.get_absolute_url())
	qr_code = url.png_as_base64_str(scale=5)
	context = {
		'visitor': visitor,
		'qr_code': qr_code,
		'event': event,
		'config': config
	}
	ticket = render('patient/application_home_leave/application_home_leave_pdf.html', context)

	html = HTML(string=ticket, base_url=site)
	pdf = html.write_pdf()

	return {
		'filename': filename,
		'content': pdf,
		'mimetype': 'application/pdf',
	}


class ApplicationForHomeLeaveUpdateView(BSModalUpdateView):
	model = ApplicationForHomeLeave
	template_name = 'patient/application_home_leave/partial_edit.html'
	form_class = ApplicationForHomeLeave_ModelForm
	page_title = _('ApplicationForHomeLeave Form')
	success_message = _(page_title + ' form has been save successfully.')

	def get_success_url(self):
		username = self.kwargs['username']
		return reverse_lazy('patient:application_home_leave_list', kwargs={'username': username})


application_home_leave_edit = ApplicationForHomeLeaveUpdateView.as_view()


class ApplicationForHomeLeaveDeleteView(BSModalDeleteView):
	model = ApplicationForHomeLeave
	template_name = 'patient/application_home_leave/partial_delete.html'
	page_title = _('ApplicationForHomeLeave Form')
	success_message = _(page_title + ' form was deleted.')

	def get_success_url(self):
		username = self.kwargs['username']
		return reverse_lazy('patient:application_home_leave_list', kwargs={'username': username})


application_home_leave_delete = ApplicationForHomeLeaveDeleteView.as_view()
