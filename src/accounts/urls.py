from django.urls import include, path, path
from django.views.generic import RedirectView
from django.views.i18n import set_language

from .views import *

app_name = 'accounts'

urlpatterns = [
    path('', account, name='account'),
    path('change-profile/', change_profile, name='change_profile'),
    path('login/', login_view, name="login_view"),
    path('signup/', signup_view, name='signup_view'),
    path('signup/patient/', patient_signup, name='patient_signup'),
    path('signup/staff/', staff_signup, name='staff_signup'),
]
