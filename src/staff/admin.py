from django import forms
from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django.contrib.admin.widgets import AutocompleteSelect
from django.db import models
from django.db.models import Count

from accounts.models import *
from patient.models import Medicine
from .models import *
from .forms import *


# Register your models here.
class OvertimeClaimAdmin(admin.ModelAdmin):
	list_display = [
		'id',
		'staff',
		'date',
		'duration_time_from',
		'duration_time_to',
		'hours',
		'total_hours',
		'checked_sign_by',
		'verify_by',
	]
	ModelAdmin.ordering = ('id',)


class StaffRecordsAdmin(admin.ModelAdmin):
	list_display = [
		'id',
		'staff',
		'date',
		'annual_leave_days',
		'public_holiday_days',
		'replacement_public_holiday',
		'medical_certificate',
		'siri_no_diagnosis',
		'emergency_leaves',
		'emergency_leaves_reasons',
		'unpaid_leaves',
		'unpaid_leaves_reasons',
	]
#	autocomplete_fields = ['patient', ]
	ModelAdmin.ordering = ('id',)

admin.site.register(OvertimeClaim, OvertimeClaimAdmin)
admin.site.register(StaffRecords, StaffRecordsAdmin)
