# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django_summernote.admin import SummernoteModelAdmin
from django.utils.html import format_html

from django.contrib import admin
from .models import *

# Register your models here.
class ProductAdmin(SummernoteModelAdmin):
    list_display = ['product_name', 'product_brand', 'product_model', 'product_image']
    list_filter = ['product_brand', 'product_model', 'product_category', 'product_type']

    def product_image(self, obj):
        img_tag = format_html('<img src="{}" width="100" height="100" />'.format(obj.product_image1.url))
        return img_tag


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'product_image']

    def product_image(self, obj):
        if obj.category_image:
            img_tag = format_html('<img src="{}" width="100" height="100" />'.format(obj.category_image.url))
        else:
            img_tag = format_html('<img src="/static/images/product-avatar.png" width="100" height="100" />')
        return img_tag

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(ProductType)
admin.site.register(ProductBrand)
