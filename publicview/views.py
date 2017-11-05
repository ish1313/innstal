# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from product.models import ProductCategory
from .models import *
# Create your views here.

def index(request):
    categories = ProductCategory.objects.all()[:8]
    blog = HomeBlog.objects.all()[0]
    context = {
        'site_title': 'Innstal',
        'page_title': 'Home',
        'categories': categories,
        'blog': blog
    }

    return render(request, 'index.html', context)

def SignUp(request):
    context = {
        'site_title': 'Innstal',
        'page_title': 'SignUp'
    }
    return render(request, 'signup.html', context)


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
