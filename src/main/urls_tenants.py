from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import RedirectView
from django.views.i18n import set_language
from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _

from patient.views import *
from accounts.views import *

urlpatterns = [
	path('', index, name='index'),
#	path('', RedirectView.as_view(url='accounts/login/', permanent=False), name='index'),
	path('patient/', include('patient.urls')),
	path('staff/', include('staff.urls')),
	path('admin/', include('massadmin.urls')),
	path('admin/', admin.site.urls),
	path('accounts/', include('allauth.urls')),
	path(_('account/'), include('accounts.urls')),
	re_path(r'^selectable/', include('selectable.urls')),
	path('summernote/', include('django_summernote.urls')),
	path('load_ic_number', load_ic_number, name='load_ic_number'),

	re_path(r'(?P<user_language>\w+)/$', set_language_from_url, name="set_language_from_url")
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
