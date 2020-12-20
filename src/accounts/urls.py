from django.urls import path

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
