# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from warrenty.models import RegisterWarrenty, ClaimProductWarranty
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


def category_products(request, category_id):
    category = ProductCategory.objects.get(id=category_id)
    products = Product.objects.filter(product_category=category)
    if request.user.is_authenticated():
        return render(request, 'dashboard/category-products.html', {"products": products, 'category': category})
    else:
        return render(request, 'category-products.html', {"products": products, 'category': category})

def product_details(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'dashboard/product-details.html', {'product': product})


def product_register_warranty(request):
    current_user = request.user
    if not current_user.is_authenticated():
        return HttpResponseRedirect('/login')

    if request.method == 'GET':
        products = Product.objects.all()
        return render(request, 'dashboard/product-register-warranty.html', {'products': products})
    else:
        # import pdb; pdb.set_trace()
        buyer_id = request.POST.get('buyer')
        buyer = InnstalUser.objects.get(email=buyer_id)
        product_id = request.POST.get('product')
        product = Product.objects.get(id=product_id)
        product_serial = request.POST.get('product_serial')
        shop_name = request.POST.get('shop_name')
        shop_address = request.POST.get('shop_address')
        purchase_date = request.POST.get('purchase_date')
        warranty_card_image = request.POST.get('warranty_card_image')

        warranty = RegisterWarrenty(buyer=buyer, product=product, product_serial=product_serial,
                                    shop_name=shop_name, shop_address=shop_address,
                                    purchase_date=purchase_date, warranty_card_image=warranty_card_image)
        warranty.warranty_status = '0'
        warranty.save()
        return HttpResponseRedirect("/dashboard")



def create_claim_warranty(request, register_id):
    registered_warranty = RegisterWarrenty.objects.get(id=register_id)
    if request.method == 'GET':
        return render(request, 'dashboard/claim-warranty.html', {'registered_warranty':registered_warranty})
    else:
        # import pdb; pdb.set_trace()
        # cpw = ClaimProductWarranty.objects.get(id=register_id)
        sub = request.POST.get('warranty_claim_subject')
        details = request.POST.get('warranty_details')
        cpw = ClaimProductWarranty(warranty_claim_subject=sub, warranty_details=details, product=registered_warranty)
        cpw.save()
        return HttpResponseRedirect('/dashboard/warranties')


def product_warranty_claimed(request):
    claimed_products = ClaimProductWarranty.objects.all()
    return render(request, 'dashboard/warranty-claimed-products.html',
                {'claimed_products': claimed_products})
