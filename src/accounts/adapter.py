from django import forms
from django.conf import settings
from django.conf import settings
from django.core.exceptions import ValidationError
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.utils.translation import ugettext as _

from allauth.account.adapter import DefaultAccountAdapter
from .views import *
from patient import urls


class AccountAdapter(DefaultAccountAdapter):
	def get_login_redirect_url(self, request):
		user = request.user

		if user.is_superuser:
			path = reverse('staff:staffdata_list')
			return path

		if user.is_staff:
			path = reverse('patient:patientdata_list')
			return path

		if user.is_patient:
			path = "/patient/{username}/"
			return path.format(username=user.username)

	def clean_password(self, password, user=None):
		min_length = settings.PASSWORD_MIN_LENGTH
		if len(password) < min_length:
			raise forms.ValidationError(_("Password must be a minimum of {0} characters.").format(min_length))
			validate_password(password, user)
		return password
