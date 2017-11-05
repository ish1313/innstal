# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _

from django.db import models
from product.models import Product
from usms.models import InnstalUser

# Create your models here.
WARRANTY_STATUS = (
    ('EX', 'EXPIRED'),
    ('VL', 'VALID'),
    ('AC', 'ACCEPTED'),
    ('RJ', 'REJECTED'),
    ('SB', 'SUBMITTED'),
)

def warranty_card_directory_path(instance, filename):
    ut = instance.user_type
    # import pdb; pdb.set_trace()
    filepath = str(instance.id) + filename[-4:]

    filepath = 'warranty/' + filepath

    return filepath


class RegisterWarrenty(models.Model):
    buyer = models.ForeignKey(InnstalUser)
    product = models.ForeignKey(Product)
    product_serial = models.CharField(_('Product Serial'), max_length=100, db_index=True)
    shop_name = models.CharField(_('Shop Name'), max_length=50, db_index=True)
    shop_address = models.TextField(max_length=500, blank=True, null=True)
    purchase_date = models.DateField(_('Purchase Date'))
    warranty_expire_date = models.DateTimeField(_('Expire Date'), editable=False)
    warranty_status = models.CharField(_('Warranty Status'), choices=WARRANTY_STATUS, max_length=3)
    warranty_card_image = models.ImageField(upload_to=warranty_card_directory_path, null=True, blank=True)
