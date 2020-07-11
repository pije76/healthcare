"""edapt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns 
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import RedirectView
from django.views.i18n import set_language
from django.http import HttpResponse


from accounts.views import *

urlpatterns = [
    path('', index, name='index'),
#    path('', RedirectView.as_view(url='accounts/login/', permanent=False), name='index'),
    path('admin/', include('massadmin.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('account/', include('accounts.urls')),
#    path('i18n/', include('django.conf.urls.i18n')),
#    re_path(r'^i18n/', include('django.conf.urls.i18n')),
#    re_path(r'^i18n/$', set_language, name='set_language'),
#    re_path(r'^i18n/', lambda x: HttpResponse("Test")),

]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns
