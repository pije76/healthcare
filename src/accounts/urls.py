from django.urls import include, path, re_path
from django.views.generic import RedirectView
from django.views.i18n import set_language

from .views import *

urlpatterns = [
    path('', account, name='account'),
    re_path(r'^change-profile/$', change_profile, name='change_profile'),
    path('change-icnumber/', change_number, name='change_number'),
#    path('login/', RedirectView.as_view(url='accounts/login/', permanent=False), name='index'),
    path('login/', index, name='index'),
    re_path(r'^signup/$', signup_view, name='signup_view'),
#    re_path(r'^setlang/$', set_language, name='set_language'),
#    re_path(r'^i18n/', include('django.conf.urls.i18n')),
#    re_path(r'^i18n/$', set_language, name='set_language'),
#    path('login/', LoginView.as_view(), name="login" ),
]
