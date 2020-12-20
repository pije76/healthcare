from django.contrib.auth.decorators import user_passes_test


def patient_required(function=None):
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_patient
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def admin_required(function=None):
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_superuser
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
