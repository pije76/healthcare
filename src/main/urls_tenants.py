from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import RedirectView
from django.views.i18n import set_language
from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _

#from solid_i18n.urls import solid_i18n_patterns

from patient_form.views import *
from patient_data.views import *
from accounts.views import *

urlpatterns = [
	path('', index, name='index'),
#    path('', RedirectView.as_view(url='accounts/login/', permanent=False), name='index'),
	path('form/', include('patient_form.urls')),
	path('data/', include('patient_data.urls')),
#    path('grappelli/', include('grappelli.urls')),
	path('admin/', include('massadmin.urls')),
	path('admin/', admin.site.urls),
	path('accounts/', include('allauth.urls')),
	path(_('account/'), include('accounts.urls')),
#    path('avatar/', include('avatar.urls')),
#    path('ajax_select/', include('ajax_select.urls')),
	re_path(r'^selectable/', include('selectable.urls')),
#    path("select2/", include("django_select2.urls")),
#    path('profile/', include('userprofiles2.urls')),
#    path('i18n/', include('django.conf.urls.i18n')),
#    re_path(r'^i18n/', include('django.conf.urls.i18n')),
#    re_path(r'^i18n/$', set_language, name='set_language'),
#    re_path(r'^i18n/', lambda x: HttpResponse("Testing")),
	re_path(r'(?P<user_language>\w+)/$', set_language_from_url, name="set_language_from_url")

]

#urlpatterns += i18n_patterns(
#    path('', index, name='index'),
#    path(_('form/'), include('patient_form.urls')),
#    path(_('data/'), include('patient_data.urls')),
#    path(_('account/'), include('accounts.urls')),
#    prefix_default_language=False,
#)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
	import debug_toolbar
	urlpatterns = [
		path('__debug__/', include(debug_toolbar.urls)),

		# For django versions before 2.0:
		# url(r'^__debug__/', include(debug_toolbar.urls)),

	] + urlpatterns
