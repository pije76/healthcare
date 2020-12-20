from selectable.base import ModelLookup
from selectable.registry import registry

from .models import *


class FullnameLookup(ModelLookup):
    model = UserProfile
    search_fields = ('full_name__icontains', )


registry.register(FullnameLookup)
