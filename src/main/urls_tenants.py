from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
from django.views.generic import RedirectView

from accounts.views import *

urlpatterns = [
	path('', RedirectView.as_view(url='accounts/login/', permanent=False), name='index'),
	#path('practise/', practise, name='practise'),
	#path('etext/', etext, name='etext'),
	#path('progress/', progress, name='progress'),
        path('admin/', admin.site.urls),
        path(r'accounts/', include('allauth.urls')),
	path(r'account/', include('accounts.urls')),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
