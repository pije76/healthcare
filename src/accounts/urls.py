from django.urls import include, path, path
from django.views.generic import RedirectView
from django.views.i18n import set_language

from .views import *

app_name = 'accounts'

urlpatterns = [
	path('', account, name='account'),
	path('change-profile/', change_profile, name='change_profile'),
	path('change-icnumber/', change_number, name='change_number'),
#    path('login/', RedirectView.as_view(url='accounts/login/', permanent=False), name='index'),
#    path('login/', index, name='index'),
	path('login/', login_view, name="login_view"),
	path('signup/', signup_view, name='signup_view'),
#	path('signup/', MySignUpForm.as_view(), name='signup_view'),
#	path('signup/', MySignUpForm.as_view(), name='signup_view'),
	path('signup/patient/', patient_signup, name='patient_signup'),
	path('signup/staff/', StaffSignUpView.as_view(), name='staff_signup'),

#    path('setlang/$', set_language, name='set_language'),
#    path('i18n/', include('django.conf.urls.i18n')),
#    path('i18n/$', set_language, name='set_language'),
]
