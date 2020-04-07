from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.urls import include, path  # For django versions from 2.0 and up

from accounts.views import *
from patient.views import *

urlpatterns = [
    path('', RedirectView.as_view(url='accounts/login/', permanent=False), name='index'),
    path('admission/', admission, name='admission'),
    path('homeleave/', homeleave, name='homeleave'),
    path('appointment/', appointment, name='appointment'),
    path('cannulation/', cannulation, name='cannulation'),
    path('charges/', charges_sheet, name='charges_sheet'),
    path('dressing/', dressing, name='dressing'),
    path('enteral-feeding-regine/', enteral_feeding_regine, name='enteral_feeding_regine'),
    path('hgt/', hgt_chart, name='hgt_chart'),
    path('intake-output/', intake_output, name='intake_output'),
    path('maintainance/', maintainance, name='maintainance'),
    path('medication-administration/', medication_administration, name='medication_administration'),
    path('medication/', medication, name='medication'),
    path('nursing/', nursing, name='nursing'),
    path('physio-progress-note-back/', physio_progress_note_back, name='physio_progress_note_back'),
    path('physio-progress-note-front/', physio_progress_note_front, name='physio_progress_note_front'),
    path('physiotherapy-general-assessment/', physiotherapy_general_assessment, name='physiotherapy_general_assessment'),
    path('stool/', stool, name='stool'),
    path('vital-sign-flow/', vital_sign_flow, name='vital_sign_flow'),
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
