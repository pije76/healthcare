from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import loader
from django.dispatch import receiver

from allauth.account.signals import user_signed_up, user_logged_in

from accounts.models import *

def account(request):
    context = {
        'navbar': 'account',
    }
    return render(request, 'account.html', context)

def etext(request):
    context = {
        'navbar': 'etext',
    }   
    return render(request, 'etext.html', context)

def practise(request):
    tables = [{"concepts":"sssss","details":"sssss"}]
    context = {
        'tables': tables,
        'navbar': 'practise',
    }   
    return render(request, 'practise.html', context)

def progress(request):
    return render(request, 'progress.html', {'navbar': 'progress'})
