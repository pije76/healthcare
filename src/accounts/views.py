from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.db import connection
from django.dispatch import receiver
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.template import loader
from django.utils import translation
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext as _
from django.views.generic import TemplateView, CreateView, ListView, UpdateView
from django.views.i18n import set_language
from django.contrib.auth import views as auth_views

from allauth.account.signals import user_signed_up, user_logged_in
from allauth.account.forms import LoginForm, SignupForm
from allauth.account.views import LoginView, SignupView

from accounts.models import *
from customers.models import *
from patient.models import *
from .models import *
from .forms import *
#from .decorators import *


def set_language_from_url(request, user_language):
	schema_name = connection.schema_name
	patients = UserProfile.objects.filter(username=request.user.username)
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Home')

	translation.activate(user_language)
	request.session[translation.LANGUAGE_SESSION_KEY] = user_language
#	redirect_to = request.META.get('HTTP_REFERER', reverse('index'))
#	response = HttpResponse(redirect_to)
#	response = redirect('index')
#	response.set_cookie(settings.LANGUAGE_COOKIE_NAME, user_language)
#	return redirect('index')
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
#	user_language = 'en'
#	translation.activate(user_language)
#	request.session['django_language'] = user_language
#	request.session[translation.LANGUAGE_SESSION_KEY] = user_language
#	redirect_to = request.META.get('HTTP_REFERER', reverse('/account/'))
#	if translation.LANGUAGE_SESSION_KEY in request.session:
#		del request.session[translation.LANGUAGE_SESSION_KEY]
#		return HttpResponseRedirect(redirect_to)
#	response = HttpResponse(redirect_to)
#	response.set_cookie(settings.LANGUAGE_COOKIE_NAME, user_language)
#	print(translation.get_language())

#	if request.user.is_authenticated:
#		if request.user.is_patient:
#			return redirect('accounts:index')
#		else:
#			return redirect('accounts:index')

	context = {
		'patients': patients,
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
	}
	return render(request, 'index.html', context)


def signup_view(request):
#	tags = Tags()
	patients = UserProfile.objects.filter(full_name=request.user).values_list('full_name', flat=True).first()
#	parameters={}
#	all_tags = tags.get_tags()
#	parameters['all_tags'] = all_tags
#	response = SignupView.signup(request)

	form = MySignUpForm()

	context = {
		'patients': patients,
		'form': form,
	}

	return render(request, 'account/signup.html', context)
#	return response


class MyLoginView(LoginView):
	template_name = 'account/login.html'
	form_class = MyLoginForm

	def get_form_kwargs(self):
		kwargs = super().get_form_kwargs()
		kwargs['request'] = self.request
		return kwargs

#class SignUpView(TemplateView):
#	template_name = 'account/signup.html'


#class PatientSignUpView(CreateView):
#	model = PatientProfile
#	form_class = PatientSignUpForm
#	template_name = 'account/signup_patient.html'

#	def get_context_data(self, **kwargs):
#		kwargs['user_type'] = 'patient'
#		return super().get_context_data(**kwargs)

#	def form_valid(self, form):
#		user = form.save()
#		login(self.request, user)
#		return redirect('accounts:index')

login_view = MyLoginView.as_view()
#login_view = MyLoginView.as_view(redirect_authenticated_user=True)
#login_view = auth_views.LoginView.as_view(redirect_authenticated_user=True)

class PatientSignUpView(SignupView):
	template_name = 'account/signup_patient.html'
	form_class = MySignUpForm

	def get_initial(self):
		initial_base = super().get_initial()
		initial_base['is_patient'] = True
		initial_base['is_staff'] = False
		return initial_base

#	def get(self, request, *args, **kwargs):
#		self.initial = {"is_patient": True}
#		return super().get(self, request, *args, **kwargs)

#	def get_context_data(self, **kwargs):
#		kwargs['user_type'] = 'student'
#		context = super().get_context_data(**kwargs)
#		context['is_patient'] = self.is_patient
#		context['is_patient'] = True
#		context.update(self.kwargs)
#		return context

#	def get_form_kwargs(self, *args, **kwargs):
#		kwargs = super().get_form_kwargs()
#		kwargs['is_patient'] = True
#		kwargs.update({'is_patient': True})
#		profile = UserProfile.objects.create(is_patient=True)
#		kwargs.update({'instance': profile})
#		return kwargs

patient_signup = PatientSignUpView.as_view()

PERMISSIONS = ['add', 'change', 'delete', 'view', ]

#GROUPS_PERMISSIONS = {
#	'patient': {
#		models.Admission: ['add', 'change', 'delete', 'view'],
#	},
#}


class StaffSignUpView(SignupView):
#	model = StaffProfile
	form_class = MySignUpForm
	template_name = 'account/signup_staff.html'

	@receiver(user_signed_up)
#	@permission_required('patient.add_admission')
	def user_signed_up_handler(request, user, **kwargs):
		ct_admission = Permission.objects.filter(codename__contains='admission').values_list('id', flat=True)
		ct_appointment = Permission.objects.filter(codename__contains='appointment').values_list('id', flat=True)
		ct_cannula = Permission.objects.filter(codename__contains='cannula').values_list('id', flat=True)
		ct_dressing = Permission.objects.filter(codename__contains='dressing').values_list('id', flat=True)
		ct_enteral_feeding_regime = Permission.objects.filter(codename__contains='enteralfeedingregime').values_list('id', flat=True)
		ct_hgt = Permission.objects.filter(codename__contains='hgt').values_list('id', flat=True)
		ct_homeleave = Permission.objects.filter(codename__contains='applicationforhomeleave').values_list('id', flat=True)
		ct_intake_output = Permission.objects.filter(codename__contains='intakeoutput').values_list('id', flat=True)
		ct_maintenance = Permission.objects.filter(codename__contains='maintenance').values_list('id', flat=True)
		ct_medication = Permission.objects.filter(codename__contains='medicationrecord').values_list('id', flat=True)
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
		for k in ct_medication_administration:
			user.user_permissions.add(k)
		for ll in ct_multi_purpose:
			user.user_permissions.add(ll)
		for m in ct_miscellaneous_charges_slip:
			user.user_permissions.add(m)
		for n in ct_nasogastric:
			user.user_permissions.add(n)
		for o in ct_nursing:
			user.user_permissions.add(o)
		for p in ct_overtime_claim:
			user.user_permissions.add(p)
		for q in ct_physio_progress_note_back:
			user.user_permissions.add(q)
		for r in ct_physio_progress_note_front:
			user.user_permissions.add(r)
		for s in ct_physiotherapy_general_assessment:
			user.user_permissions.add(s)
		for t in ct_stool:
			user.user_permissions.add(t)
		for u in ct_urinary:
			user.user_permissions.add(u)
		for v in ct_visiting_consultant_records:
			user.user_permissions.add(v)
		for w in ct_vital_sign_flow:
			user.user_permissions.add(w)
		user.save()

#	permission_required = ('patien_form.can_add_admission',)
#	permission = Permission.objects.get(name='can add a new data')
#	permission = Permission.objects.get(content_type=content_type, codename='is_member')


#	@permission_required('patient.add_admission')
#	@permission_required('patient.add_admission', fn=objectgetter(Admission, 'post_id'))
#	@permission_required('patient.add_admission')
#	@receiver(user_signed_up)
	def get_initial(self):
		initial_base = super().get_initial()
		initial_base['is_patient'] = False
		initial_base['is_staff'] = True
		return initial_base

#	def get_context_data(self, **kwargs):
#		kwargs['user_type'] = 'student'
#		ret = super().get_context_data(**kwargs)
#		ret.update(self.kwargs)
#		return super().get_context_data(**kwargs)
#		return ret

#	def form_valid(self, form):
#		user = form.save()
#		login(self.request, user)
#		return redirect('accounts:index')

#class StaffSignUpView(SignupView):
#	template_name = 'account/signup_staff.html'
#	form_class = StaffSignUpForm


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
			profile.first_name = form.cleaned_data['first_name']
			profile.last_name = form.cleaned_data['last_name']
			profile.full_name = profile.first_name + ' ' + profile.last_name
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


@login_required
def change_number(request):
	schema_name = connection.schema_name
	patients = UserProfile.objects.filter(username=request.user.username)
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Change Number')
	icnumbers = Admission.objects.filter(full_name=request.user)
	initial_icnumber = Admission.objects.filter(full_name=request.user).values_list('ic_number', flat=True).first()

	if request.method == 'POST':
		form = ChangeAdmission(request.POST)
		if form.is_valid():
			profile = form.save(commit=False)
			profile.ic_number = form.cleaned_data['ic_number']
			profile.save()

			messages.success(request, _('Your form has been save successfully.'))
			return HttpResponseRedirect('/account/')
		else:
			messages.warning(request, form.errors)

	else:
		form = ChangeAdmission(initial={'ic_number': initial_icnumber})

	context = {
		'patients': patients,
		'logos': logos,
		'titles': titles,
		'page_title': page_title,
		'navbar': 'account',
		'icnumbers': icnumbers,
		'form': form,
	}
	return render(request, 'account/change.html', context)


# def login(request):
#    schema_name = connection.schema_name
#    patients = UserProfile.objects.filter(username=request.user.username)
#    logos = Client.objects.filter(schema_name=schema_name)
#    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()

#    context = {
#        'patients': patients,
#        'logos': logos,
#        'titles': titles,
#        'navbar': 'account',
#    }
#    return render(request, 'account.html', context)

