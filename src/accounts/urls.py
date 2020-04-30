from django.urls import path, re_path
from django.views.generic import RedirectView

from . import views
from .forms import *

urlpatterns = [
    path('', views.account, name='account'),
    path('change-profile/', views.change_profile, name='change_profile'),
    path('change-icnumber/', views.change_number, name='change_number'),
#    path('login/', RedirectView.as_view(url='accounts/login/', permanent=False), name='index'),
    path('login/', views.index, name='index'),
#    path('login/', LoginView.as_view(), name="login" ),
]
