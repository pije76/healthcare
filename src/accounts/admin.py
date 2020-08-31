from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin.options import ModelAdmin
from django.contrib.admin.filters import RelatedOnlyFieldListFilter
from django.contrib.admin import ModelAdmin, SimpleListFilter
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

#from ajax_select.admin import AjaxSelectAdmin
#from ajax_select import make_ajax_form

from patient.models import *
from .forms import *


# Register your models here.
#class PatientDataAdmin(admin.StackedInline):
#    model = Admission
#    max_num = 1
#    extra = 1

class UserProfileAdmin(admin.ModelAdmin):
#    class FullNameModelChoiceField(forms.ModelChoiceField):
#        def label_from_instance(self, obj):
#            return "%s" % (obj.full_name)

#    class ICNumberModelChoiceField(forms.ModelChoiceField):
#        def label_from_instance(self, obj):
#            return "%s" % (obj.ic_number)

#    def formfield_for_foreignkey(self, db_field, request, **kwargs):
#        if db_field.name == 'full_name':
#            return self.FullNameModelChoiceField(queryset=UserProfile.objects)
#        elif db_field.name == 'ic_number':
#            return self.ICNumberModelChoiceField(queryset=UserProfile.objects)

#        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    list_display = [
        'id',
        'username',
        'email',
        'full_name',
        'ic_number',
        'date_joined',

        'birth_date',
        'age',
        'gender',
        'marital_status',
        'religion',
        'occupation',
        'communication_sight',
        'communication_hearing',
        'address',

        'is_active',
        'is_patient',
        'is_staff',
        'is_superuser',
    ]
#    list_filter = ['user']
    ModelAdmin.ordering = ('id',)
    search_fields = ['full_name']
#    form = UserProfileForm
#    form = make_ajax_form(UserProfile, {
#        'full_name': 'full_name'
#    })
#    inlines = [
#        PatientDataAdmin,
#    ]

#    class Meta:
#        model = UserProfile


class EmergencyContactAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'patient',
        'ec_name',
        'ec_ic_number',
        'ec_relationship',
        'ec_phone',
        'ec_address',
    ]
#    autocomplete_fields = ['patient', ]
    ModelAdmin.ordering = ('id',)


class PatientProfileAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(is_patient=True)

    ModelAdmin.ordering = ('id',)

    list_display = [
        'id',
        'username',
        'email',
        'full_name',
        'ic_number',
        'date_joined',

        'birth_date',
        'age',
        'gender',
        'marital_status',
        'religion',
        'occupation',
        'communication_sight',
        'communication_hearing',
        'address',

        'is_active',
    ]

    list_filter = ()


class StaffProfileAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(is_superuser=False, is_staff=True,)

    ModelAdmin.ordering = ('id',)

    list_display = [
        'id',
        'username',
        'email',
        'full_name',
        'ic_number',

        'birth_date',
        'age',
        'gender',
        'marital_status',
        'religion',
        'address',

        'is_active',
    ]

    readonly_fields = (
        'occupation',
        'occupation_others',
        'communication_sight',
        'communication_hearing',
        'communication_hearing_others',
    )

    list_filter = ()


class AdminProfileAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(is_superuser=True, is_staff=True,)

    ModelAdmin.ordering = ('id',)

    list_display = [
        'id',
        'username',
        'email',
        'full_name',
        'ic_number',

        'birth_date',
        'age',
        'gender',
        'marital_status',
        'religion',
        'address',

        'is_active',
    ]

    readonly_fields = (
        'occupation',
        'occupation_others',
        'communication_sight',
        'communication_hearing',
        'communication_hearing_others',
    )

    list_filter = ()


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(EmergencyContact, EmergencyContactAdmin)
#admin.site.register(PatientProfile, PatientProfileAdmin)
#admin.site.register(StaffProfile, StaffProfileAdmin)
#admin.site.register(AdminProfile, AdminProfileAdmin)
