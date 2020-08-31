from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy


from allauth.account.adapter import DefaultAccountAdapter

from patient import urls
#from patient.urls impport *

class AccountAdapter(DefaultAccountAdapter):
	def get_login_redirect_url(self, request):
#		path = super().get_login_redirect_url(request)
		user = request.user

		if user.is_superuser:
#			path = "/staff/"
			path = reverse('staff:staffdata_list')
			return path

		if user.is_staff:
#			path = "/patient/"
			path = reverse('patient:patientdata_list')
			return path

		if user.is_patient:
			path = "/patient/{username}/"
#			path = reverse_lazy('patient:patientdata_detail', username=user.username)
#			path = reverse('patient:patientdata_detail', username=user.username).format(username=user.username)
#			path = reverse_lazy('patient:patientdata_detail', username=user.username)
			return path.format(username=user.username)
#			return path


#	def save_user(self, request, user, form, commit=False):
#		data = form.cleaned_data
#		user.first_name = data['first_name']
#		user.last_name = data['last_name']
#		user.ic_number = data['ic_number']
#		if 'password1' in data:
#			user.set_password(data['password1'])
#		else:
#			user.set_unusable_password()
#		self.populate_username(request, user)
#		user.save()
#		return user
