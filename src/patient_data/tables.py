import django_tables2 as tables

from accounts.models import *


class PatientProfileTable(tables.Table):
	class Meta:
		model = PatientProfile
