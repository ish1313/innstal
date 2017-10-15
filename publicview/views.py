# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def index(request):
    # return HttpResponse('Hello from Python!')

    # products = Product()

    # products = Product.objects.all()

    return render(request, 'index.html', {})

def SignUp(request):
    # if request.method == 'POST':
    #     form = UserRegistrationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         username = form.cleaned_data.get('username')
    #         raw_password = form.cleaned_data.get('password1')
    #         user = authenticate(username=username, password=raw_password)
    #         login(request, user)
    #         return redirect('/')
    # else:
    #     form = UserRegistrationForm()
    return render(request, 'login.html', {})


def login(request):
	return render(request, 'login.html')

def register_warrantly(request):
	return render(request, 'register_warrantly.html')

def pricing(request):
	return render(request, 'pricing.html')

def about(request):
	return render(request, 'about.html')

def service(request):
	return render(request, 'service.html')

def contact(request):
    return render(request, 'contact.html')


def search_result(request):
    # products = Product()

    # products = Product.objects.all()

    return render(request, 'search_result.html', {})

