from django import template
from django.urls import reverse, resolve, translate_url
from django.utils import translation
from django.template.defaultfilters import register
from django.utils.translation import activate, get_language

register = template.Library()

class TranslatedURL(template.Node):
	def __init__(self, language):
		self.language = language

	def render(self, context):
		view = resolve(context['request'].path)
		request_language = translation.get_language()
		translation.activate(self.language)
		url = reverse(view.url_name, args=view.args, kwargs=view.kwargs)
		translation.activate(request_language)
		return url

@register.simple_tag(name='translate_url')
def do_translate_url(parser, token):
	language = token.split_contents()[1]
	return TranslatedURL(language)

@register.simple_tag(takes_context=True, name="change_lang")
def change_lang(context, lang=None, *args, **kwargs):
	url = context['request'].path
	cur_language = get_language()
	try:
		url_parts = resolve(url)
		activate(lang)
		url = reverse(url_parts.view_name, kwargs=url_parts.kwargs)
	except:
		url = reverse("index") #or whatever page you want to link to
		# or just pass if you want to return same url
	finally:
		activate(cur_language)
	return "%s" % url

@register.simple_tag(takes_context=True)
def change_lang(context, lang=None, *args, **kwargs):
	path = context['request'].path
	url_parts = resolve( path )
	url = path
	cur_language = get_language()

	try:
		activate(lang)
		url = reverse( url_parts.view_name, kwargs=url_parts.kwargs )
	finally:
		activate(cur_language)

	return "%s" % url

@register.simple_tag(takes_context=True)
def change_lang(context, lang=None, *args, **kwargs):
	path = context['request'].path
	return translate_url(path, lang)


@register.simple_tag
def get_url_with_kwargs(request):
	url_name = ''.join([request.resolver_match.app_name, ':', request.resolver_match.url_name,])
	url_kwargs = request.resolver_match.kwargs
	return reverse(url_name, None, None, url_kwargs)