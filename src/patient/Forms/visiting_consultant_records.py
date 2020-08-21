from django import forms
from django.utils.translation import ugettext_lazy as _

from ..models import *
from ..forms import *
from ..lookups import *
#from .custom_layout import *
from accounts.models import *

from bootstrap_modal_forms.forms import *


class VisitingConsultantForm(BSModalModelForm):

    class Meta:
        model = VisitingConsultant
        fields = '__all__'
        widgets = {
            'patient': forms.HiddenInput(),
        }

    date_time = forms.DateTimeField(required=False, label="", initial=timezone.now, input_formats=settings.DATETIME_INPUT_FORMATS, widget=DateTimePickerInput(format="%d/%m/%Y %H:%M", attrs={'class': "form-control"}))
    complaints = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control"}))
    treatment_orders = forms.CharField(required=False, label="", widget=forms.Textarea(attrs={'class': "form-control"}))
    consultant = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': "form-control"}))


VisitingConsultant_FormSet_Factory = formset_factory(
    VisitingConsultantForm,
    #   formset = MedicationAdministrationRecord_BaseFormSetFactory,
    extra=0,
    max_num=0,
    #   can_delete=True,
)
