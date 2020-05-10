from __future__ import unicode_literals
from django.db.models import Q

from selectable.base import ModelLookup
from selectable.registry import registry

from ajax_select import register, LookupChannel

from .models import *
from accounts.models import *


@register('full_name')
class FullnameLookup(LookupChannel):
    model = PatientProfile

    def get_query(self, q, request):
        return self.model.objects.filter(full_name__icontains=q)

    def format_item_display(self, item):
#       return u"<span class='full_name'>%s</span>" % item.full_name
        return "%s" % (item.full_name)

