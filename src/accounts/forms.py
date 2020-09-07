from django import forms
from django.contrib.auth.models import *
from django.utils.translation import ugettext as _

from .models import *
from patient.models import *

from allauth.account.forms import LoginForm, SignupForm

ic_number_validator = RegexValidator("\d{6}\-\d{2}\-\d{4}", "IC Number format needs to be yymmdd-xx-zzzz.")


class MyLoginForm(LoginForm):
	def __init__(self, *args, **kwargs):
		self.request = kwargs.pop('request')
		super().__init__(*args, **kwargs)

#	username = forms.CharField(max_length=100, required=True, label=_('Username'), widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': _("Username")}))
	password = forms.CharField(max_length=100, required=True, label=_('Password'), widget=forms.PasswordInput(attrs={'class': "form-control", 'placeholder': _("Password")}))


class MySignUpForm(SignupForm):

	username = forms.CharField(max_length=100, required=True, label=_('Username:'), widget=forms.TextInput(attrs={'class': "form-control"}))
	full_name = forms.CharField(max_length=100, required=False, label=_('Full Name:'), widget=forms.TextInput(attrs={'class': "form-control"}))
#	first_name = forms.CharField(max_length=100, required=True, label=_('First Name'), widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': _("First Name")}))
#	last_name = forms.CharField(max_length=100, required=False, label=_('Last Name'), widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': _("Last Name")}))
	is_patient = forms.BooleanField(required=False, label='', widget=forms.HiddenInput())
	is_staff = forms.BooleanField(required=False, label='', widget=forms.HiddenInput())

	def save(self, request):
		user = super().save(request)
		user.full_name = self.cleaned_data['full_name']
		user.username = self.cleaned_data['username']
#		user.first_name = self.cleaned_data['first_name']
#		user.last_name = self.cleaned_data['last_name']
		user.is_active = True
		user.is_admin = False
		user.is_staff = self.cleaned_data['is_staff']
		user.is_patient = self.cleaned_data['is_patient']
##		if user.is_staff is True and user.is_patient is False:
##			staff_profile = StaffProfile(staff_name=user)
##			staff_profile.save()
##		if user.is_staff is False and user.is_patient is True:
##			patient_profile = PatientProfile(patient_name=user)
##			patient_profile.save()
		user.save()
		return user

#	def clean_username(self):
#		cleaned_data = super().clean()
#		username = cleaned_data.get("username")
#		username = self.cleaned_data['username']
#		print("username: ", username)
#		try:
#			user = UserProfile.objects.get(username=username)
#			user = UserProfile.objects.filter(username=username)
#		except UserProfile.DoesNotExist:
#			return username
#		raise forms.ValidationError(u'Username "%s" is already in use.' % username)



class ChangeUserProfile(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

	full_name = forms.CharField(max_length=100, required=True, label='', widget=forms.TextInput(attrs={'class': "form-control"}))
	email = forms.EmailField(required=False, label='', widget=forms.TextInput(attrs={'class': "form-control"}))
	ic_number = forms.CharField(max_length=14, required=False, label="", initial='yymmdd-xx-zzzz', validators=[ic_number_validator], widget=forms.TextInput(attrs={'class': "form-control"}))

	class Meta:
		model = UserProfile
		fields = ('full_name', 'email', 'ic_number')


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
