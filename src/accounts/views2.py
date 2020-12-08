from django import http
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.dispatch import receiver
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render, redirect
from django.utils import translation
from django.utils.http import is_safe_url
from django.utils.translation import get_language, ugettext as _

from customers.models import *
from .models import *
from .forms import *

from allauth.account.views import LoginView, SignupView
from allauth.account.signals import user_signed_up
from allauth.exceptions import ImmediateHttpResponse
from allauth.account import signals

import re


# Create your views here.
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


def set_theme(request):
#   next = request.POST.get('next', '')
    theme = request.GET.get('theme')
    request.session['theme'] = theme

#   if not is_safe_url(url=next, allowed_hosts=request.get_host()):
#       next = request.META.get('HTTP_REFERER')

#       if not is_safe_url(url=next, allowed_hosts=request.get_host()):
#           next = '/'

#   response = http.HttpResponseRedirect(next)

    if request.method == 'POST':
        theme = request.POST.get('theme')
#       theme = request.POST.get('theme', None)
#       theme = request.GET.get('update')
#       request.session['theme'] = theme
        print("theme:", theme)
        response = http.HttpResponseRedirect('/')

#       if theme:
#           if hasattr(request, 'session'):
#               request.session['DJANGO_BOOTSTRAP_UI_THEME'] = theme
#           else:
#               response.set_cookie('DJANGO_BOOTSTRAP_UI_THEME', theme)

#   return response
#   if request.method == 'POST':
#   request.session['theme'] = "bootstrap"
#   theme = request.POST.get('theme', None)
#   data = request.session['DJANGO_BOOTSTRAP_UI_THEME'] = theme
#   theme = request.session['DJANGO_BOOTSTRAP_UI_THEME'] = "bootstrap"
#   print("theme", theme)
#   data = request.POST.get('theme')
#       data = request.POST.get('next')
#       data = request.POST.get('theme', None)
#   data = request.GET.get('next')
#   data = request.POST.get('next')
#   data = request.GET.get(next, '')
#   data = request.POST.get(next, '')
#   data = request.REQUEST.get('next', '')
#   data = request.POST[theme]

#       print("data:", data)

    # set session data
#   request.session['theme'] = "bootstrap"
#   referer = "/"
#   if "HTTP_REFERER" in request.META:
#       referer = request.META["HTTP_REFERER"]
#       resp = HttpResponseRedirect(referer)
#       resp.set_cookie(theme, 0)
    else:
#       data = request.POST.get('next')
#       theme = request.session.get('next')
        theme = request.GET.get('theme')
#   theme = request.session['theme']
        print("theme:", theme)
        response = http.HttpResponseRedirect(next)

    # delete session data
#   del request.session['user_id']
    return response


def strip_lang(path):
    pattern = '^(/%s)/' % get_language()
    match = re.search(pattern, path)
    if match is None:
        return path
    return path[match.end(1):]


def set_language_from_url(request, user_language):
    schema_name = connection.schema_name
    patients = UserProfile.objects.filter(username=request.user.username)
    logos = Client.objects.filter(schema_name=schema_name)
    titles = Client.objects.filter(schema_name=schema_name).values_list('title', flat=True).first()
    page_title = _('Home')

#   redirect_page = request.GET.get('lang')
    next_path = request.POST.get('user_language')
#   next_path = strip_lang(request.path)

    valid = False
    for item in settings.LANGUAGES:
        if item[0] == user_language:
            valid = True
    if not valid:
        raise Http404(_('The language is not available!'))

#   if not user_language in [lang[0] for lang in settings.LANGUAGES]:
#       return HttpResponseRedirect('/')

#   try:
#       previous = request.META['HTTP_REFERER']
#       previous = request.META.get('HTTP_REFERER', '')
#       if user_language == translation.get_language():
#           return redirect(previous)

#   except KeyError:
#       next_url = '/' + user_language + '/'

    translation.activate(user_language)
#   response = HttpResponseRedirect(next_url)
#   return redirect(redirect_page)
#   return redirect('patient:patientdata_detail', username=patients.username)
#   return redirect(reverse(redirect_url_name))
#   request.session[translation.LANGUAGE_SESSION_KEY] = user_language
    request.session['user_language'] = user_language
#   response.set_cookie(settings.LANGUAGE_COOKIE_NAME, user_language)

    context = {
        'patients': patients,
        'logos': logos,
        'titles': titles,
        'page_title': page_title,
        'next_path': next_path,
    }

    return render(request, 'index.html', context)
#   return response


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


class StaffSignUpView(SignupView):
    form_class = MySignUpForm
    template_name = 'account/signup_staff.html'

    def form_valid(self, form):
        self.user = form.save(self.request)
        try:
            signals.user_signed_up.send(sender=self.user.__class__, request=self.request, user=self.user, **{})
            return redirect('staff:staffdata_list')
        except ImmediateHttpResponse as e:
            return e.response

    @receiver(user_signed_up)
    def user_signed_up_handler(request, user, **kwargs):
        ct_admission = Permission.objects.filter(codename__contains='admission').values_list('id', flat=True)
        ct_allergy = Permission.objects.filter(codename__contains='allergy').values_list('id', flat=True)
        ct_appointment = Permission.objects.filter(codename__contains='appointment').values_list('id', flat=True)
        ct_cannula = Permission.objects.filter(codename__contains='cannula').values_list('id', flat=True)
        ct_dischargechecklist = Permission.objects.filter(codename__contains='dischargechecklist').values_list('id', flat=True)
        ct_dressing = Permission.objects.filter(codename__contains='dressing').values_list('id', flat=True)
        ct_enteral_feeding_regime = Permission.objects.filter(codename__contains='enteralfeedingregime').values_list('id', flat=True)
        ct_family = Permission.objects.filter(codename__contains='family').values_list('id', flat=True)
        ct_hgt = Permission.objects.filter(codename__contains='hgt').values_list('id', flat=True)
        ct_homeleave = Permission.objects.filter(codename__contains='applicationforhomeleave').values_list('id', flat=True)
        ct_intake_output = Permission.objects.filter(codename__contains='intakeoutput').values_list('id', flat=True)
        ct_investigation_report = Permission.objects.filter(codename__contains='investigationreport').values_list('id', flat=True)
        ct_maintenance = Permission.objects.filter(codename__contains='maintenance').values_list('id', flat=True)
        ct_medication_administration = Permission.objects.filter(codename__contains='medicationadministrationrecord').values_list('id', flat=True)
        ct_medication_administration_template = Permission.objects.filter(codename__contains='medicationadministrationrecordtemplate').values_list('id', flat=True)
        ct_medicationrecord = Permission.objects.filter(codename__contains='medicationrecord').values_list('id', flat=True)
        ct_medicine = Permission.objects.filter(codename__contains='medicine').values_list('id', flat=True)
        ct_miscellaneous_charges_slip = Permission.objects.filter(codename__contains='miscellaneouschargesslip').values_list('id', flat=True)
        ct_multi_purpose = Permission.objects.filter(codename__contains='multipurpose').values_list('id', flat=True)
        ct_nasogastric = Permission.objects.filter(codename__contains='nasogastric').values_list('id', flat=True)
        ct_nursing = Permission.objects.filter(codename__contains='nursing').values_list('id', flat=True)
#       ct_overtime_claim = Permission.objects.filter(codename__contains='overtimeclaim').values_list('id', flat=True)
        ct_physio_progress_note_sheet = Permission.objects.filter(codename__contains='physioprogressnotesheet').values_list('id', flat=True)
        ct_physiotherapy_general_assessment = Permission.objects.filter(codename__contains='physiotherapygeneralassessment').values_list('id', flat=True)
        ct_stool = Permission.objects.filter(codename__contains='stool').values_list('id', flat=True)
        ct_urinary = Permission.objects.filter(codename__contains='urinary').values_list('id', flat=True)
        ct_visiting_consultant = Permission.objects.filter(codename__contains='visitingconsultant').values_list('id', flat=True)
        ct_vital_sign_flow = Permission.objects.filter(codename__contains='vitalsignflow').values_list('id', flat=True)
        ct_wound_condition = Permission.objects.filter(codename__contains='woundcondition').values_list('id', flat=True)

        for a in ct_admission:
            user.user_permissions.add(a)
        for b in ct_appointment:
            user.user_permissions.add(b)
        for c in ct_cannula:
            user.user_permissions.add(c)
        for d in ct_medicine:
            user.user_permissions.add(d)
        for e in ct_dressing:
            user.user_permissions.add(e)
        for f in ct_enteral_feeding_regime:
            user.user_permissions.add(f)
        for g in ct_hgt:
            user.user_permissions.add(g)
        for h in ct_homeleave:
            user.user_permissions.add(h)
        for i in ct_intake_output:
            user.user_permissions.add(i)
        for j in ct_maintenance:
            user.user_permissions.add(j)
        for k in ct_medication_administration_template:
            user.user_permissions.add(k)
        for ll in ct_medicationrecord:
            user.user_permissions.add(ll)
        for m in ct_medication_administration:
            user.user_permissions.add(m)
        for n in ct_multi_purpose:
            user.user_permissions.add(n)
        for o in ct_miscellaneous_charges_slip:
            user.user_permissions.add(o)
        for p in ct_nasogastric:
            user.user_permissions.add(p)
        for q in ct_nursing:
            user.user_permissions.add(q)
        for r in ct_physio_progress_note_sheet:
            user.user_permissions.add(r)
        for s in ct_physiotherapy_general_assessment:
            user.user_permissions.add(s)
        for t in ct_stool:
            user.user_permissions.add(t)
        for u in ct_urinary:
            user.user_permissions.add(u)
        for v in ct_visiting_consultant:
            user.user_permissions.add(v)
        for w in ct_vital_sign_flow:
            user.user_permissions.add(w)
        for x in ct_investigation_report:
            user.user_permissions.add(x)
        for y in ct_wound_condition:
            user.user_permissions.add(y)
        for z in ct_allergy:
            user.user_permissions.add(z)
        for aa in ct_family:
            user.user_permissions.add(aa)
        for ab in ct_dischargechecklist:
            user.user_permissions.add(ab)
        user.save()

    def get_initial(self):
        initial_base = super().get_initial()
        initial_base['is_patient'] = False
        initial_base['is_staff'] = True
        return initial_base


staff_signup = StaffSignUpView.as_view()


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
#       form = ChangeUserProfile(request.POST or None, prefix='profile', instance=request.user)
        form = ChangeUserProfile(request.POST or None, instance=request.user)

#        if aform.is_valid() and form.is_valid():
        if form.is_valid():
#            admission = aform.save(commit=False)
#            admission.ic_number = aform.cleaned_data['ic_number']
#            admission.save()

            profile = form.save(commit=False)
#           profile.first_name = form.cleaned_data['first_name']
#           profile.last_name = form.cleaned_data['last_name']
#           profile.full_name = profile.first_name + ' ' + profile.last_name
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
#       form = ChangeUserProfile(prefix='profile', instance=request.user)
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

    def form_valid(self, form):
        self.user = form.save(self.request)
        try:
            signals.user_signed_up.send(sender=self.user.__class__, request=self.request, user=self.user, **{})
            return redirect('patient:patientdata_list')
        except ImmediateHttpResponse as e:
            return e.response


#   def clean(self):
#       cleaned_data = super().clean()
#       username = cleaned_data.get("username")
#       if UserProfile.objects.filter(username=username):
#           raise forms.ValidationError('Username already exists.')
#       return self.cleaned_data


patient_signup = PatientSignUpView.as_view()
