# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _

from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

from django.db import models
from usms.models import *
# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    company_phone = models.CharField(_('Company Phone Number'), max_length=15, blank=True, null=True)
    address = models.TextField(max_length=200, blank=True, null=True)

    def __unicode__(self):
        return self.name


class ProductCategory(models.Model):
    name = models.CharField(_('Product Category'), max_length=50, db_index=True)

    def __unicode__(self):
        return self.name

class ProductType(models.Model):
    type_name = models.CharField(_('Type Name'), max_length=50, db_index=True)
    category = models.ForeignKey(ProductCategory, blank=True, null=True)

    def __unicode__(self):
        return self.type_name

class ProductModel(models.Model):
    model_no = models.CharField(_('Model No'), max_length=50, db_index=True)
    Company = models.ForeignKey(Company, blank=True, null=True)

    def __unicode__(self):
        return self.model_no

class ProductBrand(models.Model):
    brand_name = models.CharField(_('Brand Name'), max_length=50, db_index=True)
    Company = models.ForeignKey(Company, blank=True, null=True)

    def __unicode__(self):
        return self.brand_name

def product_directory_path(instance, filename):
    name = instance.product_name
    company = instance.company
    model = instance.product_model
    brand = instance.product_brand

    filepath = 'product/'
    if company:
        filepath =  filepath + company.name + '/'

    if brand:
        filepath = filepath + brand.brand_name + '/'

    if model:
        filepath = filepath + model.model_no + '/'

    filepath = filepath + name + filename[-4:]

    return filepath


class Product(models.Model):
    product_name = models.CharField(_('Product Name'), max_length=50, db_index=True)
    company = models.ForeignKey(Company, blank=True, null=True)
    product_category = models.ForeignKey(ProductCategory, blank=True, null=True)
    product_type = models.ForeignKey(ProductType, blank=True, null=True)
    product_brand = models.ForeignKey(ProductBrand, blank=True, null=True)
    product_model = models.ForeignKey(ProductModel, blank=True, null=True)
    warranty_duration = models.DurationField(default=2000, blank=True, null=True)
    installation_instruction = models.TextField(max_length=500, blank=True, null=True)
    product_image1 = models.ImageField(upload_to=product_directory_path)
    product_image2 = models.ImageField(upload_to=product_directory_path, blank=True, null=True)
    product_manual = models.FileField(upload_to=product_directory_path, blank=True, null=True)

    def __unicode__(self):
        return self.product_name
