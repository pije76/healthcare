from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


messageserror = _('IC Number format needs to be yymmdd-xx-zzzz.')

ic_number_validator = RegexValidator(regex='\d{6}\-\d{2}\-\d{4}', message=messageserror, code="invalid")


def validate_round_hour(value):
	if not value.minute == value.second == value.microsecond == 0:
		raise ValidationError(
			'This should be a round hour.',
			params={'value': value},
		)
