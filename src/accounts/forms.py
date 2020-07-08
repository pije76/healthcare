from django import forms
from django.contrib.auth.models import *
from django.urls import reverse
from django.utils.translation import ugettext as _

from allauth.account.forms import LoginForm
from allauth.account.forms import SignupForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML

#from ajax_select.fields import AutoCompleteSelectField, AutoCompleteSelectMultipleField

from .models import *
from patient_form.models import *

ic_number_validator = RegexValidator("\d{6}\-\d{2}\-\d{4}", "IC Number format needs to be yymmdd-xx-zzzz.")

class MyLoginForm(LoginForm):
	def __init__(self, *args, **kwargs):
		super(MyLoginForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper(self)
		# Add magic stuff to redirect back.
		self.helper.layout.append(
			HTML(
				"{% if redirect_field_value %}"
				"<input type='hidden' name='{{ redirect_field_name }}'"
				" value='{{ redirect_field_value }}' />"
				"{% endif %}"
			)
		)
		# Add password reset link.
		self.helper.layout.append(
			HTML(
				"<p><a class='button secondaryAction' href={url}>{text}</a></p>".format(
					url=reverse('account_reset_password'),
					text=_('Forgot Password?')
				),
			)
		)
		# Add submit button like in original form.
		self.helper.layout.append(
			HTML(
				'<button class="btn btn-primary btn-block" type="submit">'
				'%s</button>' % _('Sign In')
			)
		)

		self.helper.form_class = 'form-horizontal'
		self.helper.label_class = 'col-xs-2 hide'
		self.helper.field_class = 'col-xs-8'


class MySignUpForm(SignupForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

	first_name = forms.CharField(max_length=100, required=True, label=_('First Name'))
	last_name = forms.CharField(max_length=100, required=False, label=_('Last Name (optional)'))

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

	first_name = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	last_name = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	email = forms.EmailField(required=False, label='', widget=forms.TextInput(attrs={'class': "form-control"}))
	ic_number = forms.CharField(max_length=14, required=False, label="", initial='yymmdd-xx-zzzz', validators=[ic_number_validator], widget=forms.TextInput(attrs={'class': "form-control"}))
	jkl = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))
	eth = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))

	class Meta:
		model = PatientProfile
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
