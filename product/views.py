# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import *
# Create your views here.

def search_product_manual(request):
    qstring = request.POST.get('search')
    if qstring:
        products = Product.objects.filter(product_search_string__icontains=qstring)
    else:
        products = []
    return render(request, 'product-manual-search.html', {"products": products})

def product_category(request):
    categories = ProductCategory.objects.all()
    return render(request, 'product-categories.html', {'categories': categories})
