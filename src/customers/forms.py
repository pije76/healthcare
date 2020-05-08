from django import forms

from crispy_forms.bootstrap import Field, InlineRadios, TabHolder, Tab
from crispy_forms.helper import FormHelper

from crispy_forms.layout import Submit, Layout, Div, Fieldset

from patient_form.models import *


class AdmissionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AdmissionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-3'
        self.helper.field_class = 'col-lg-7'

    class Meta:
        model = Admission
        fields = '__all__'

    def as_p(self):
        return self._html_output(
            normal_row='<br />%(html_class_attr)s%(label)s %(field)s',
            error_row='%s',
            row_ender='</p>',
            help_text_html=' <span class="helptext">%s</span>',
            errors_on_separate_row=False)
