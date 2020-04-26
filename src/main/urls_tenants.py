from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.urls import include, path  # For django versions from 2.0 and up

from form_data.views import *
from accounts.views import *

urlpatterns = [
    path('', RedirectView.as_view(url='accounts/login/', permanent=False), name='index'),
    path('forms/', include('form_data.urls')),
    path('admin/', admin.site.urls),
    path(r'accounts/', include('allauth.urls')),
    path(r'account/', include('accounts.urls')),
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
