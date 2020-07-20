from django import template
from patient_form.models import *

register = template.Library()


@register.filter
def duration(td):
	total_seconds = int(td.total_seconds())
	hours = total_seconds // 3600
	minutes = (total_seconds % 3600) // 60

	return '{} hours {} min'.format(hours, minutes)


@register.simple_tag
def tag_get_display(obj):
	return MODE_CHOICES[obj][1]


@register.filter
def selected_choice(form, field_name):
	return dict(form.fields[field_name].choices)[form.data[field_name]]
#	return dict(form.fields[field_name].choices).get(form.initial.get(field_name, None), None)
#	return form.fields[field_name].queryset.get(pk=form[field_name].value())
