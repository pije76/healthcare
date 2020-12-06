from django import template
from django.conf import settings
from django.template import Library

register = template.Library()


@register.simple_tag(takes_context=True)
def get_current_url_for_lang(context, lang_code):
    request = context.get('request', False)
    if not request:
        return None

    request = context['request']
    curr_url = request.path
    if len(curr_url) < 4 or curr_url[0] != '/' or curr_url[3] != '/':
        return curr_url

    if context.get('LANGUAGES', False):
        codes = []
        for code, name in context['LANGUAGES']:
            codes.append(code)

        curr_langcode = curr_url[1:3]
        if lang_code not in codes or curr_langcode not in codes:
            return curr_url

    changed_url = '/' + lang_code + curr_url[3:]
    return changed_url


@register.simple_tag(takes_context=True)
def get_value_from_session_or_cookie(context, key):
    request = context['request']

    try:
        # First check for key in session
        # If no session is available this throws an AttributeError, if the key is not available in an existing session
        # this throws a KeyError
        return request.session[key]
    except (AttributeError, KeyError):
        try:
            # Second check for key in cookies
            return request.COOKIES[key]
        except KeyError:
            # Third fallback to settings or return default value
            return getattr(settings, key, '')
