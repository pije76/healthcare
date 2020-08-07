import django_tables2 as tables

from accounts.models import *


class UserProfileTable(tables.Table):
	class Meta:
		model = UserProfile
