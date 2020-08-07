from django import forms
from django.contrib.auth.models import *
from django.urls import reverse
from django.utils.translation import ugettext as _
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from allauth.account.forms import LoginForm
from allauth.account.forms import SignupForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML

#from ajax_select.fields import AutoCompleteSelectField, AutoCompleteSelectMultipleField

from .models import *
from patient_form.models import *

ic_number_validator = RegexValidator("\d{6}\-\d{2}\-\d{4}", "IC Number format needs to be yymmdd-xx-zzzz.")

class MyLoginForm(LoginForm):
#	class Meta:
#		model = UserProfile
#		fields = ('username', 'password')

#	def __init__(self, *args, **kwargs):
#		super().__init__(*args, **kwargs)
#		self.helper = FormHelper(self)

#	username = forms.CharField(max_length=100, required=True, label=_('Username:'))
	password = forms.CharField(max_length=100, required=True, label=_('Password'), widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': _("Password")}))

class MySignUpForm(SignupForm):

	first_name = forms.CharField(max_length=100, required=True, label=_('First Name'), widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': _("First Name")}))
	last_name = forms.CharField(max_length=100, required=False, label=_('Last Name'), widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': _("Last Name")}))
#	ic_number = forms.CharField(max_length=14, required=True, label=_('IC Number'), initial='yymmdd-xx-zzzz')
	is_patient = forms.BooleanField(required=False ,label='', widget=forms.HiddenInput())
	is_staff = forms.BooleanField(required=False ,label='', widget=forms.HiddenInput())

#	def custom_signup(self, request, user):
#	def signup(self, request, user):
	def save(self, request):
		user = super().save(request)
#		profile = UserProfile(full_name=user)
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
#		user.ic_number = self.cleaned_data['ic_number']
		user.is_active = True
#		user.is_patient = True
		user.is_patient = self.cleaned_data['is_patient']
		user.is_staff = self.cleaned_data['is_staff']
		user.is_admin = False
		user.save()
		return user


#class PatientSignUpForm(UserCreationForm):
#    interests = forms.ModelMultipleChoiceField(queryset=Subject.objects.all(),widget=forms.CheckboxSelectMultiple,required=True    )

#	class Meta(UserCreationForm.Meta):
#		model = UserProfile

#	@transaction.atomic
#	def save(self):
#		user = super().save(commit=False)
#        user.is_patient = True
#		user.save()
#		patient = PatientProfile.objects.create(user=user)
#        patient.interests.add(*self.cleaned_data.get('interests'))
#		return user

class ChangeUserProfile(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

#	user = User.objects.get(username=request.user.username)

	first_name = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	last_name = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	email = forms.EmailField(required=False, label='', widget=forms.TextInput(attrs={'class': "form-control"}))
	ic_number = forms.CharField(max_length=14, required=False, label="", initial='yymmdd-xx-zzzz', validators=[ic_number_validator], widget=forms.TextInput(attrs={'class': "form-control"}))
	jkl = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	eth = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))

	class Meta:
		model = UserProfile
		fields = ('first_name', 'last_name', 'email', 'ic_number', 'jkl', 'eth')


class ChangeAdmission(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

	def clean_ic_number(self):
		ic_number = self.cleaned_data['ic_number']
		try:
			ic_number = Admission.objects.get(ic_number=ic_number)
		except Admission.DoesNotExist:
			return ic_number
		raise forms.ValidationError('%s already exists' % ic_number)

	ic_number = forms.CharField(max_length=14, required=False, label="", initial='yymmdd-xx-zzzz', validators=[ic_number_validator], widget=forms.TextInput(attrs={'class': "form-control"}))

	class Meta:
		model = Admission
		fields = ('ic_number',)
