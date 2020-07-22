from __future__ import unicode_literals
from django.db.models import Q

from selectable.base import ModelLookup
from selectable.registry import registry

#from ajax_select import register, LookupChannel

from .models import *
from accounts.models import *


class FullnameLookup(ModelLookup):
	model = UserProfile
	search_fields = ('full_name__icontains', )


registry.register(FullnameLookup)

#@register('full_name')
#class FullnameLookup(LookupChannel):
#	model = UserProfile
#	plugin_options = {
#		'render_in_input': True,
#	}
#	min_length = 4
#	disabled = True

#	def get_query(self, q, request):
#		return self.model.objects.filter(full_name__icontains=q)

#	def format_item_display(self, item):
#		#       return u"<span class='full_name'>%s</span>" % item.full_name
#		return "%s" % (item.full_name)
