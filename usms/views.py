# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate, login as admin_login
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


from .models import *
# Create your views here.

def signup(request):
    if request.method == 'POST':
        # import pdb; pdb.set_trace()
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        terms = request.POST.get('terms')
        user_type = request.POST.get('user_type')
        password = request.POST.get('password2')
        user = InnstalUser(email=email, first_name=first_name,
                                        last_name=last_name, phone=phone, user_type=user_type)
        user.set_password(password)
        user.save()
        if user.user_type == '1':
            user.is_active = True
            user.is_staff = True
            user.is_superuser == False
            user.save()
            admin_login(request, user)
            return HttpResponseRedirect('/dashboard/account-details/')
        elif user.user_type == '2':
            user.is_active = True
            user.is_staff = True
            user.save()
            return HttpResponseRedirect('/')


    else:
        return render(request, 'signup.html', {})

def login(request):
    if request.method == 'POST':
        # import pdb; pdb.set_trace()
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)

        try:
            admin_login(request, user)
            if user.is_superuser == True:
                return HttpResponseRedirect('/admin/')
            if user.is_active == True and user.is_staff == True:
                return HttpResponseRedirect('/dashboard/')

        except Exception as e:
            return HttpResponseRedirect('/login')
    else:
        return render(request, 'login.html', {})

def dashboard(request):
    # import pdb; pdb.set_trace()
    user = request.user
    if user.user_type == '2' and user.is_active_subscription == False:
        return HttpResponseRedirect('/subscription/')
    else:
        return render(request, 'dashboard.html', {})

def subscription(request):
    return render(request, 'subscription.html', {})


def account_details(request):
    return render (request, 'dashboard/account_details.html', {})

def product_manual(request):
    return render(request, 'product-manual.html', {})
