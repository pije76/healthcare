from django.contrib import admin
from django.contrib.admin import ModelAdmin, SimpleListFilter
from django.contrib.admin.filters import RelatedOnlyFieldListFilter
from django.contrib.admin.options import ModelAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from django_tenants.admin import TenantAdminMixin

from .models import *

# Register your models here.


#class ClientAdmin(admin.ModelAdmin):
class ClientAdmin(TenantAdminMixin, admin.ModelAdmin):
    ModelAdmin.ordering = ('id',)

    list_display = [
        'id',
        'name',
        'title',
        'logo',
        'created_on',
    ]

    readonly_fields = (
        #        'occupation',
        #        'occupation_others',
        #        'communication_sight',
        #        'communication_hearing',
        #        'communication_hearing_others',
    )

    list_filter = ()

    def has_change_permission(self, request):
        if request.user.is_superuser:
            return False
        return True

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(full_name=request.user)

#    fields = ('name',)

#    def formfield_for_foreignkey(self, db_field, request, **kwargs):
#        if db_field.name == 'name':
#            kwargs['queryset'] = User.objects.filter(is_superuser=True)

#        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Client, ClientAdmin)
