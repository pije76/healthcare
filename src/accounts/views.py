from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import loader
from django.dispatch import receiver
from django.db import connection
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.i18n import set_language
from django.utils.translation import ugettext as _

from allauth.account.signals import user_signed_up, user_logged_in
from allauth.account.views import LoginView
from allauth.account.forms import LoginForm, SignupForm
from allauth.account.views import SignupView as signup_views

from accounts.models import *
from customers.models import *
from patient_form.models import *
from .models import *
from .forms import *


def index(request):
	schema_name = connection.schema_name
	patients = PatientProfile.objects.filter(username=request.user.username)
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

def signup_view(request):
#	tags = Tags()
	patients = PatientProfile.objects.filter(full_name=request.user).values_list('full_name', flat=True).first()
#	parameters={}
#	all_tags = tags.get_tags()
#	parameters['all_tags'] = all_tags
#	response = signup_views.signup(request)

	form = MySignUpForm()

	context = {
		'patients': patients,
		'form': form,
	}

	return render(request, 'account/change.html', context)
#	return response

@login_required
def account(request):
	schema_name = connection.schema_name
	patients = PatientProfile.objects.filter(username=request.user.username)
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	icnumbers = PatientProfile.objects.filter(full_name=request.user)
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
def change_profile(request):
	schema_name = connection.schema_name
	patients = PatientProfile.objects.filter(username=request.user.username)
	logos = Client.objects.filter(schema_name=schema_name)
	titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
	page_title = _('Change Profile')
	icnumbers = PatientProfile.objects.filter(full_name=request.user)
	initial_icnumber = PatientProfile.objects.filter(full_name=request.user).values_list('ic_number', flat=True).first()
	jl = PatientProfile.objects.filter(full_name=request.user).values_list('jkl', flat=True).first()
	eth = PatientProfile.objects.filter(full_name=request.user).values_list('eth', flat=True).first()

	aform = ChangeAdmission(prefix='admission', initial={'icnumbers': "icnumbers"})
	form = ChangePatientProfile(prefix='profile')

	if request.method == 'POST':
#        aform = ChangeAdmission(request.POST or None, initial={'ic_number': initial_icnumber})
#		form = ChangePatientProfile(request.POST or None, prefix='profile', instance=request.user)
		form = ChangePatientProfile(request.POST or None, instance=request.user)

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
#		form = ChangePatientProfile(prefix='profile', instance=request.user)
		form = ChangePatientProfile(instance=request.user)

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
	patients = PatientProfile.objects.filter(username=request.user.username)
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
#    patients = PatientProfile.objects.filter(username=request.user.username)
#    logos = Client.objects.filter(schema_name=schema_name)
#    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()

#    context = {
#        'patients': patients,
#        'logos': logos,
#        'titles': titles,
#        'navbar': 'account',
#    }
#    return render(request, 'account.html', context)

