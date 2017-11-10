# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import *
# Create your views here.

def search_product_manual(request):
    # import pdb; pdb.set_trace()
    qstring = request.GET.get('search')
    if qstring:
        products = Product.objects.filter(product_search_string__icontains=qstring)
    else:
        products = []

    if request.user.is_authenticated():
        return render(request, 'dashboard/product-manual-search.html',
                {"products": products, 'qstring': qstring})
    else:
        return render(request, 'product-manual-search.html', {"products": products, 'qstring': qstring})

def product_category(request):
    categories = ProductCategory.objects.all()
    return render(request, 'product-categories.html', {'categories': categories})


def product_register_warranty(request):
    current_user = request.user
    if not current_user.is_authenticated():
        return HttpResponseRedirect('/login')

    if request.method == 'GET':
        products = Product.objects.all()
        return render(request, 'product-register-warranty.html', {'products': products})
    else:
        buyer = request.POST.get('buyer')
        product = request.POST.get('product')
        product_serial = request.POST.get('product_serial')
        shop_name = request.POST.get('shop_name')
        shop_address = request.POST.get('shop_address')
        purchase_date = request.POST.get('purchase_date')

        warranty = RegisterWarrenty(buyer=buyer, product=product, product_serial=product_serial,
                                    shop_name=shop_name, shop_address=shop_address, purchase_date=purchase_date)
        warranty.warranty_status = 'SB'
