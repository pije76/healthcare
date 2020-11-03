from django import template

import json

register = template.Library()


@register.filter(name='convert_list_to_string')
def convert_list_to_string(value):
#	data = json.loads(value)
	return ''.join([str(e) for e in value])


@register.filter(name='join_with_commas')
def join_with_commas(value):
	if not value:
		return ""
#	for item in value:
#		k = len(item)
	k = len(value)
#	print("j: ", j)
	if k == 1:
		return u"%s" % value[0]
	else:
		return ", ".join(str(obj) for obj in value[:k - 1]) + " and " + str(value[k - 1])


@register.filter(name='index_value')
def index_value(value, index):
	try:
		return value[index]
	except IndexError:
		return None


@register.filter(name='get_fields')
def get_fields(value):
	return [field for field in value]
