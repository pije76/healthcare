from django.contrib.auth.decorators import user_passes_test
from functools import wraps
from django.contrib import messages
from django.contrib.auth.views import redirect_to_login
from django.contrib.auth import REDIRECT_FIELD_NAME


def patient_required(function=None):
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_patient
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def admin_required(function=None):
    # def admin_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='/login', message=default_message):
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_superuser
        #        login_url=login_url,
        #        redirect_field_name=redirect_field_name,
        #        message=message
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def staff_required(function=None):
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_staff
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
