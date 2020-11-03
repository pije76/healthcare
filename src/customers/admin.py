from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin.options import ModelAdmin
from django.contrib.admin.filters import RelatedOnlyFieldListFilter
from django.contrib.admin import ModelAdmin, SimpleListFilter
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

from .models import *

# Register your models here.
class ClientAdmin(admin.ModelAdmin):
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


admin.site.register(Client, ClientAdmin)
