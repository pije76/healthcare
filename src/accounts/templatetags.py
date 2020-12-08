from django import template
from django.template.defaultfilters import register
from django.urls import reverse, resolve, translate_url
from django.utils import translation


@register.simple_tag(takes_context=True)
def change_lang(context, lang=None, *args, **kwargs):
    path = context['request'].path
    return translate_url(path, lang)
