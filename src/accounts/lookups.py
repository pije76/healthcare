from django.db.models import Q

#from ajax_select import register, LookupChannel
from selectable.base import ModelLookup
from selectable.registry import registry

from .models import *


#@register('full_name')
# class FullNameLookup(LookupChannel):
#    model = UserProfile

#    def get_query(self, q, request):
#        return self.model.objects.filter(full_name=q)

#    def format_item_display(self, item):
#        return u"<span class='full_name'>%s</span>" % item.full_name

class FullnameLookup(ModelLookup):
    model = UserProfile
    search_fields = ('full_name__icontains', )


registry.register(FullnameLookup)
