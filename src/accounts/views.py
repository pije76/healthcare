from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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

from allauth.account.signals import user_signed_up, user_logged_in
from allauth.account.views import LoginView
from allauth.account.forms import LoginForm, SignupForm
from allauth.account.views import SignupView as signup_views

from accounts.models import *
from customers.models import *
from patient_form.models import *
from .models import *
from .forms import *
from .decorators import *


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
#	response = signup_views.signup(request)

	form = MySignUpForm()

	context = {
		'patients': patients,
		'form': form,
	}

	return render(request, 'account/signup.html', context)
#	return response

class SignUpView(TemplateView):
	template_name = 'account/signup.html'


class PatientSignUpView(CreateView):
	model = PatientProfile
	form_class = PatientSignUpForm
	template_name = 'account/signup.html'

	def get_context_data(self, **kwargs):
		kwargs['user_type'] = 'patient'
		return super().get_context_data(**kwargs)

	def form_valid(self, form):
		user = form.save()
		login(self.request, user)
		return redirect('accounts:index')


class FamilySignUpView(CreateView):
	model = FamilyProfile
	form_class = PatientSignUpForm
	template_name = 'account/signup.html'

	def get_context_data(self, **kwargs):
		kwargs['user_type'] = 'family'
		return super().get_context_data(**kwargs)

	def form_valid(self, form):
		user = form.save()
		login(self.request, user)
		return redirect('accounts:index')


class StaffSignUpView(CreateView):
	model = StaffProfile
	form_class = PatientSignUpForm
	template_name = 'account/signup.html'

	def get_context_data(self, **kwargs):
		kwargs['user_type'] = 'student'
		return super().get_context_data(**kwargs)

	def form_valid(self, form):
		user = form.save()
		login(self.request, user)
		return redirect('accounts:index')


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
	jl = UserProfile.objects.filter(full_name=request.user).values_list('jkl', flat=True).first()
	eth = UserProfile.objects.filter(full_name=request.user).values_list('eth', flat=True).first()

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
			profile.jkl = form.cleaned_data['jkl']
			profile.eth = form.cleaned_data['eth']
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
		form = ChangeAdmission(initial={'ic_number': initial_icnumber, 'jkl': jkl, 'ech': ech})

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

