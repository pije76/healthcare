from django import forms
from django.core.validators import RegexValidator
from django.contrib.auth.models import *
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_list_or_404, get_object_or_404

from allauth.account.forms import LoginForm
from allauth.account.forms import SignupForm

import json

#from ajax_select.fields import AutoCompleteSelectField, AutoCompleteSelectMultipleField

ic_number_validator = RegexValidator("\d{6}\-\d{2}\-\d{4}", "IC Number format needs to be yymmdd-xx-zzzz.")


from .models import *
from patient_form.models import *

class MyLoginForm(LoginForm):
	def __init__(self, *args, **kwargs):
		super(MyLoginForm, self).__init__(*args, **kwargs)
		self.fields['login'].label = ""
		self.fields['login'].required = True
		self.fields['login'].widget = forms.TextInput()
		self.fields['password'].label = ""
		self.fields['password'].required = True
		self.fields['password'].widget = forms.PasswordInput()


class MySignUpForm(SignupForm):
	def __init__(self, *args, **kwargs):
		super(MySignUpForm, self).__init__(*args, **kwargs)

	first_name = forms.CharField(max_length=100, required=True, label='First Name')
	last_name = forms.CharField(max_length=100, required=False, label='Last Name (optional)')

	class Meta:
		model = PatientProfile
#		fields = '__all__'
		fields = ('first_name', 'last_name')

	def custom_signup(self, request, user):
		#	user = PatientProfile.objects.all()
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
#		user.ic_number = self.cleaned_data['ic_number']
		user.is_staff = True

		user.save()
		return user


class ChangePatientProfile(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

#	user = User.objects.get(username=request.user.username)

	first_name = forms.CharField(max_length=100, required=True, label='First Name')
	last_name = forms.CharField(max_length=100, required=False, label='Last Name (optional)')
	email = forms.CharField(max_length=100, required=False, label='Email (optional)')

	class Meta:
		model = PatientProfile
		fields = ('first_name', 'last_name', 'email')


class ChangeAdmission(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

	ic_number = forms.CharField(max_length=14, required=True, label='IC Number', validators=[ic_number_validator])

	class Meta:
		model = Admission
		fields = ('ic_number',)
