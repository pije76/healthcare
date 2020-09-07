from django import forms
from django.utils.translation import ugettext_lazy as _

from ..models import *
from ..forms import *
from ..lookups import *
#from .custom_layout import *
from accounts.models import *

from bootstrap_modal_forms.forms import *
from django_summernote.widgets import SummernoteWidget

class PhysioProgressNoteBack_ModelForm(BSModalModelForm):

    class Meta:
        model = PhysioProgressNoteBack
        fields = '__all__'
        widgets = {
            'patient': forms.HiddenInput(),
        }

    date_time = forms.DateTimeField(required=False, label="", initial=timezone.now, input_formats=settings.DATETIME_INPUT_FORMATS, widget=DateTimePickerInput(format="%d/%m/%Y %H:%M", attrs={'class': "form-control"}))
    report = forms.CharField(required=False, label="", widget=SummernoteWidget(attrs={'class': "form-control", 'summernote': {'width': '100%', 'height': '400px'}}))
