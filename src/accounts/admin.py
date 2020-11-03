from django.contrib import admin
from django.contrib.admin import ModelAdmin, SimpleListFilter
from django.contrib.admin.filters import RelatedOnlyFieldListFilter
from django.contrib.admin.options import ModelAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

from patient.models import *
from .forms import *


# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
	list_display = [
		'id',
		'username',
		'email',
		'full_name',
		'ic_number',
		'image_img',
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
	ModelAdmin.ordering = ('id',)
	search_fields = ['full_name']

	def get_readonly_fields(self, request, obj=None):
		if obj is not None:
			return (
				'marital_status_others',
				'religion_others',
				'occupation_others',
				'communication_hearing_others',
			)
		else:
			return ()


class FamilyAdmin(admin.ModelAdmin):
	list_display = [
		'id',
		'patient',
		'ec_name',
		'ec_ic_number',
		'image_img',
		'ec_relationship',
		'ec_phone',
		'ec_address',
	]
	autocomplete_fields = ['patient', ]
	ModelAdmin.ordering = ('id',)


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Family, FamilyAdmin)
