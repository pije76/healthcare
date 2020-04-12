from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import loader
from django.dispatch import receiver

from allauth.account.signals import user_signed_up, user_logged_in

from patient.models import *


def account(request):
    context = {
        'navbar': 'account',
    }
    return render(request, 'account.html', context)
