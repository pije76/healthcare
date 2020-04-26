from django.db.models import Q

from ajax_select import register, LookupChannel

from .models import *


@register('full_name')
class TagsLookup(LookupChannel):

    model = Admission

    def get_query(self, q, request):
        return self.model.objects.filter(full_name=q)

    def format_item_display(self, item):
        return u"<span class='full_name'>%s</span>" % item.full_name