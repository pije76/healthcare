from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import loader
from django.dispatch import receiver
from django.db import connection
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.i18n import set_language

from allauth.account.signals import user_signed_up, user_logged_in
from allauth.account.views import LoginView, SignupView
from allauth.account.forms import LoginForm, SignupForm

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
    page_title = 'Account'

    context = {
        'patients': patients,
        'logos': logos,
        'titles': titles,
        'page_title': page_title,
    }
    return render(request, 'index.html', context)


@login_required
def change_profile(request):
    schema_name = connection.schema_name
    patients = PatientProfile.objects.filter(username=request.user.username)
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
    page_title = 'Account'
    icnumbers = Admission.objects.filter(full_name=request.user)
#    initial_icnumber = Admission.objects.filter(full_name=request.user).values_list('ic_number', flat=True).first()

    if request.method == 'POST':
        form = ChangePatientProfile(request.POST, instance=request.user)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.first_name = form.cleaned_data['first_name']
            profile.last_name = form.cleaned_data['last_name']
            profile.full_name = profile.first_name + ' ' + profile.last_name
            profile.save()
            messages.success(request, 'Your form has been save successfully.')
            return HttpResponseRedirect('/account/')
        else:
            messages.error(request, "Error")

    else:
        form = ChangePatientProfile(instance=request.user)

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


@login_required
def change_number(request):
    schema_name = connection.schema_name
    patients = PatientProfile.objects.filter(username=request.user.username)
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
    page_title = 'Account'
    icnumbers = Admission.objects.filter(full_name=request.user)
    initial_icnumber = Admission.objects.filter(full_name=request.user).values_list('ic_number', flat=True).first()

    if request.method == 'POST':
        form = ChangeAdmission(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.ic_number = form.cleaned_data['ic_number']
            profile.save()
            messages.success(request, 'Your form has been save successfully.')
            return HttpResponseRedirect('/account/')
        else:
            messages.error(request, "Error")

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


@login_required
def account(request):
    schema_name = connection.schema_name
    patients = PatientProfile.objects.filter(username=request.user.username)
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
    icnumbers = Admission.objects.filter(full_name=request.user)
    page_title = 'Account'

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


class CustomLoginView(LoginView):
    template_name = 'account/login.html'
#    form_class = MyLoginForm

#    def __init__(self, **kwargs):
#        super(CustomLoginView, self).__init__(*kwargs)

#    def dispatch(self, request, *args, **kwargs):
#        self.logo = request.session.get('logo')
#        return super(CustomLoginView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CustomLoginView, self).get_context_data(**kwargs)
        context['logos'] = self.client.logo
#        context.update({'signup_form': SignupForm})
        return context


login = CustomLoginView.as_view()


class MySignupView(SignupView):

    def dispatch(self, request, *args, **kwargs):
        self.company = request.session.get('company')
        return super(MySignupView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(MySignupView, self).get_context_data(**kwargs)
        context['logo'] = self.company.logo
        return context
