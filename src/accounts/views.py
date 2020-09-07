from django.shortcuts import render
from django.db import connection
from django.utils.translation import ugettext as _
from django.contrib.auth.decorators import login_required
from django.dispatch import receiver
from django.utils import translation
from django.contrib import messages
from django.http import HttpResponseRedirect

from customers.models import *
from .models import *
from .forms import *

from allauth.account.views import LoginView, SignupView
from allauth.account.signals import user_signed_up


# Create your views here.
def set_language_from_url(request, user_language):
	schema_name = connection.schema_name
	patients = UserProfile.objects.filter(username=request.user.username)
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Home')

	translation.activate(user_language)
	request.session[translation.LANGUAGE_SESSION_KEY] = user_language

	context = {
		'patients': patients,
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
	}

	return render(request, 'index.html', context)


def index(request):
	schema_name = connection.schema_name
	patients = UserProfile.objects.filter(username=request.user.username)
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Home')

	context = {
		'patients': patients,
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
	}
	return render(request, 'index.html', context)


@login_required
#@patient_required
def account(request):
	schema_name = connection.schema_name
	patients = UserProfile.objects.filter(username=request.user.username)
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	icnumbers = UserProfile.objects.filter(full_name=request.user)
	page_title = _('Account')

	context = {
		'patients': patients,
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'icnumbers': icnumbers,
		'navbar': 'account',
		'form': LoginForm(),
	}

	return render(request, 'account.html', context)


@login_required
#@method_decorator([login_required, patient_required], name='dispatch')
def change_profile(request):
	schema_name = connection.schema_name
	patients = UserProfile.objects.filter(username=request.user.username)
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Change Profile')
	icnumbers = UserProfile.objects.filter(full_name=request.user)
	initial_icnumber = UserProfile.objects.filter(full_name=request.user).values_list('ic_number', flat=True).first()

	aform = ChangeAdmission(prefix='admission', initial={'icnumbers': "icnumbers"})
	form = ChangeUserProfile(prefix='profile')

	if request.method == 'POST':
#        aform = ChangeAdmission(request.POST or None, initial={'ic_number': initial_icnumber})
#		form = ChangeUserProfile(request.POST or None, prefix='profile', instance=request.user)
		form = ChangeUserProfile(request.POST or None, instance=request.user)

#        if aform.is_valid() and form.is_valid():
		if form.is_valid():
#            admission = aform.save(commit=False)
#            admission.ic_number = aform.cleaned_data['ic_number']
#            admission.save()

			profile = form.save(commit=False)
#			profile.first_name = form.cleaned_data['first_name']
#			profile.last_name = form.cleaned_data['last_name']
#			profile.full_name = profile.first_name + ' ' + profile.last_name
			profile.full_name = form.cleaned_data['full_name']
			profile.email = form.cleaned_data['email']
			profile.ic_number = form.cleaned_data['ic_number']
			profile.save()

			messages.success(request, _('Your profile has been change successfully.'))
			return HttpResponseRedirect('/account/')
#            return HttpResponseRedirect(reverse('accounts'))
		else:
			messages.warning(request, form.errors)

	else:
#        aform = ChangeAdmission(initial={'ic_number': initial_icnumber})
#		form = ChangeUserProfile(prefix='profile', instance=request.user)
		form = ChangeUserProfile(instance=request.user)

	context = {
		'patients': patients,
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'navbar': 'account',
		'icnumbers': icnumbers,
		'form': form,
#        'aform': aform,
	}

	return render(request, 'account/change.html', context)


def signup_view(request):

	context = {
	}

	return render(request, 'account/signup.html', context)


class MyLoginView(LoginView):
	template_name = 'account/login.html'
	form_class = MyLoginForm

	def get_form_kwargs(self):
		kwargs = super().get_form_kwargs()
		kwargs['request'] = self.request
		return kwargs


login_view = MyLoginView.as_view()


class PatientSignUpView(SignupView):
	template_name = 'account/signup_patient.html'
	form_class = MySignUpForm

	def get_initial(self):
		initial_base = super().get_initial()
		initial_base['is_patient'] = True
		initial_base['is_staff'] = False
		return initial_base

#	def clean(self):
#		cleaned_data = super().clean()
#		username = cleaned_data.get("username")
#		if UserProfile.objects.filter(username=username):
#			raise forms.ValidationError('Username already exists.')
#		return self.cleaned_data


patient_signup = PatientSignUpView.as_view()


class StaffSignUpView(SignupView):
	form_class = MySignUpForm
	template_name = 'account/signup_staff.html'

	@receiver(user_signed_up)
	def user_signed_up_handler(request, user, **kwargs):
		ct_admission = Permission.objects.filter(codename__contains='admission').values_list('id', flat=True)
		ct_appointment = Permission.objects.filter(codename__contains='appointment').values_list('id', flat=True)
		ct_cannula = Permission.objects.filter(codename__contains='cannula').values_list('id', flat=True)
		ct_dressing = Permission.objects.filter(codename__contains='dressing').values_list('id', flat=True)
		ct_enteral_feeding_regime = Permission.objects.filter(codename__contains='enteralfeedingregime').values_list('id', flat=True)
		ct_hgt = Permission.objects.filter(codename__contains='hgt').values_list('id', flat=True)
		ct_homeleave = Permission.objects.filter(codename__contains='applicationforhomeleave').values_list('id', flat=True)
		ct_intake_output = Permission.objects.filter(codename__contains='intakeoutput').values_list('id', flat=True)
		ct_investigationreport = Permission.objects.filter(codename__contains='investigationreport').values_list('id', flat=True)
		ct_maintenance = Permission.objects.filter(codename__contains='maintenance').values_list('id', flat=True)
		ct_medication = Permission.objects.filter(codename__contains='medication').values_list('id', flat=True)
		ct_medicationrecord = Permission.objects.filter(codename__contains='medicationrecord').values_list('id', flat=True)
		ct_medication_administration = Permission.objects.filter(codename__contains='medicationadministrationrecord').values_list('id', flat=True)
		ct_miscellaneous_charges_slip = Permission.objects.filter(codename__contains='miscellaneouschargesslip').values_list('id', flat=True)
		ct_multi_purpose = Permission.objects.filter(codename__contains='multipurpose').values_list('id', flat=True)
		ct_nasogastric = Permission.objects.filter(codename__contains='nasogastric').values_list('id', flat=True)
		ct_nursing = Permission.objects.filter(codename__contains='nursing').values_list('id', flat=True)
		ct_overtime_claim = Permission.objects.filter(codename__contains='overtimeclaim').values_list('id', flat=True)
		ct_physio_progress_note_back = Permission.objects.filter(codename__contains='physioprogressnoteback').values_list('id', flat=True)
		ct_physio_progress_note_front = Permission.objects.filter(codename__contains='physioprogressnotefront').values_list('id', flat=True)
		ct_physiotherapy_general_assessment = Permission.objects.filter(codename__contains='physiotherapygeneralassessment').values_list('id', flat=True)
		ct_stool = Permission.objects.filter(codename__contains='stool').values_list('id', flat=True)
		ct_urinary = Permission.objects.filter(codename__contains='urinary').values_list('id', flat=True)
		ct_visiting_consultant_records = Permission.objects.filter(codename__contains='visitingconsultant').values_list('id', flat=True)
		ct_vital_sign_flow = Permission.objects.filter(codename__contains='vitalsignflow').values_list('id', flat=True)

		for a in ct_admission:
			user.user_permissions.add(a)
		for b in ct_appointment:
			user.user_permissions.add(b)
		for c in ct_cannula:
			user.user_permissions.add(c)
		for d in ct_dressing:
			user.user_permissions.add(d)
		for e in ct_enteral_feeding_regime:
			user.user_permissions.add(e)
		for f in ct_hgt:
			user.user_permissions.add(f)
		for g in ct_homeleave:
			user.user_permissions.add(g)
		for h in ct_intake_output:
			user.user_permissions.add(h)
		for i in ct_maintenance:
			user.user_permissions.add(i)
		for j in ct_medication:
			user.user_permissions.add(j)
		for k in ct_medicationrecord:
			user.user_permissions.add(k)
		for ll in ct_medication_administration:
			user.user_permissions.add(ll)
		for m in ct_multi_purpose:
			user.user_permissions.add(m)
		for n in ct_miscellaneous_charges_slip:
			user.user_permissions.add(n)
		for o in ct_nasogastric:
			user.user_permissions.add(o)
		for p in ct_nursing:
			user.user_permissions.add(p)
		for q in ct_overtime_claim:
			user.user_permissions.add(q)
		for r in ct_physio_progress_note_back:
			user.user_permissions.add(r)
		for s in ct_physio_progress_note_front:
			user.user_permissions.add(s)
		for t in ct_physiotherapy_general_assessment:
			user.user_permissions.add(t)
		for u in ct_stool:
			user.user_permissions.add(u)
		for v in ct_urinary:
			user.user_permissions.add(v)
		for w in ct_visiting_consultant_records:
			user.user_permissions.add(w)
		for x in ct_vital_sign_flow:
			user.user_permissions.add(x)
		for y in ct_investigationreport:
			user.user_permissions.add(y)
		user.save()

	def get_initial(self):
		initial_base = super().get_initial()
		initial_base['is_patient'] = False
		initial_base['is_staff'] = True
		return initial_base


staff_signup = StaffSignUpView.as_view()

