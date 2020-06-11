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
