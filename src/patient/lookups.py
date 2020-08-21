from __future__ import unicode_literals
from django.db.models import Q

from selectable.base import ModelLookup
from selectable.base import LookupBase
from selectable.registry import registry

#from ajax_select import register, LookupChannel

from accounts.models import UserProfile
from .models import Admission


class FullnameLookup(ModelLookup):
	model = UserProfile
	search_fields = (
		'full_name__icontains',
	)
	filters = {'is_patient': True, }


class StaffnameLookup(ModelLookup):
	model = UserProfile
	search_fields = (
		'full_name__icontains',
	)
	filters = {'is_staff': True, }


class FamilyNameLookup(ModelLookup):
	model = Admission
	search_fields = (
		'ec_name__icontains',
	)


class FamilyLookup(ModelLookup):
	model = Admission
	search_fields = (
#	full_name__icontains',
		'patient__icontains',
#		'patient__full_name__icontains',
#		'ic_number__icontains',
		'ec_name__icontains',
	)

	def get_query(self, request, term):
		results = super().get_query(request, term)
		patient = request.GET.get('patient', '')
		if patient:
			results = results.filter(patient=patient)
		return results

	def get_item_label(self, item):
		#		return "%s, %s" % (item.full_name, item.ec_ic_number)
		#		return "%s" % (item.full_name)
		return "%s" % (item.patient)
#		return item.ec_ic_number

	def get_item_value(self, item):
		#		return "%s" % (item.full_name)
		return "%s" % (item.patient)
#		return item.ec_ic_number


class ECNumberLookup(ModelLookup):
	model = Admission
	search_fields = (
		'patient__full_name__icontains',
		#		'full_name__icontains',
		'ec_name__icontains',
	)

#	def get_query(self, request, item):
#	def get_query(self, item):
#		data = ['Foo', 'Bar']
#		return [x for x in data if x.startswith(item)]

	def get_item_label(self, item):
		#		return u"%s" % (item.get_ec_name)
		return item.ec_name
#		return item.patient.full_name
#		return self.item.patient

#	def get_item_id(self, item):
#		return u"%s" % (item.get_ec_name)

	def get_item_value(self, item):
		return item.patient.full_name
#		return item.ec_name
#		return self.item.patient

#	def get_item(self, item):
#		return item.ec_name


registry.register(ECNumberLookup)
registry.register(FullnameLookup)
registry.register(FamilyNameLookup)


#@register('full_name')
# class FullnameLookup(LookupChannel):
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
