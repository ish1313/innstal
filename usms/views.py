# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate, login as admin_login
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


from .models import *
# Create your views here.

def signup(request):
    if request.method == 'POST':
        import pdb; pdb.set_trace()
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        terms = request.POST.get('terms')
        password = request.POST.get('password2')
        user = InnstalUser(email=email, first_name=first_name, last_name=last_name, phone=phone)
        user.set_password(password)
        user.save()
        return HttpResponseRedirect('/login/')

    else:
        return render(request, 'signup.html', {})



def login(request):
    if request.method == 'POST':
        # import pdb; pdb.set_trace()
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        admin_login(request, user)
        return HttpResponseRedirect('/dashboard/')
    else:
        return render(request, 'login.html', {})

def dashboard(request):
    return render(request, 'dashboard.html', {})

def product_manual(request):
    return render(request, 'product-manual.html', {})
