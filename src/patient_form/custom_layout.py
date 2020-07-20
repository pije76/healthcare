from crispy_forms.layout import LayoutObject, TEMPLATE_PACK
#from django.shortcuts import render
from django.template.loader import render_to_string


class Formset(LayoutObject):
	template = "patient_form/formset.html" % TEMPLATE_PACK

	def __init__(self, formset_context_name, helper_context_name=None, template=None, label=None):
		self.formset_context_name = formset_context_name
		self.helper_context_name = helper_context_name
		self.fields = []
		if template:
			self.template = template

	def render(self, form, form_style, context, template_pack=TEMPLATE_PACK):
		formset = context[self.formset_name_in_context]
		helper = context.get(self.helper_context_name)
		if helper:
			helper.form_tag = False
		context.update({'formset': formset, 'helper': helper})
#		return render_to_string(self.template, {'formset': formset})
#		return render_to_string(self.template, context({'wrapper': self, 'formset': formset}))
		return render_to_string(self.template, context.flatten())
