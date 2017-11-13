# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
import datetime as dt
from django.db import models
from product.models import Product
from usms.models import InnstalUser

# Create your models here.
WARRANTY_STATUS = (
    ('0', 'SUBMITTED'),
    ('1', 'ACCEPTED'),
    ('2', 'REJECTED'),
    ('3', 'WARRANTY EXPIRED'),
    ('4', 'WARRANTY CLAIMED'),
    ('5', 'CLAIM REVIEWING'),
    ('6', 'CLAIM REJECTED'),
    ('7', 'CLAIM RESOLVED'),
)

CLAIM_STATUS = (
    ('4', 'CLAIMED'),
    ('5', 'REVIEWING'),
    ('6', 'REJECTED'),
    ('7', 'RESOLVED'),

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
    product_serial = models.CharField(_('Product Serial'), max_length=100, unique=True, db_index=True)
    shop_name = models.CharField(_('Shop Name'), max_length=50, db_index=True)
    shop_address = models.TextField(max_length=500, blank=True, null=True)
    purchase_date = models.DateField(_('Purchase Date'), editable=False)
    warranty_expire_date = models.DateField(_('Expire Date'), editable=False)
    warranty_status = models.CharField(_('Warranty Status'), choices=WARRANTY_STATUS, max_length=1)
    warranty_card_image = models.ImageField(upload_to=warranty_card_directory_path, null=True, blank=True)

    def __unicode__(self):
        return self.product_serial

    def save(self, *args, **kwargs):
        # import pdb; pdb.set_trace();
        if isinstance(self.purchase_date, dt.date):
            pdate = self.purchase_date
        else:
            pdate = dt.datetime.strptime(self.purchase_date, "%d %B, %Y")
            pdate = dt.datetime.strptime(pdate.strftime('%Y-%m-%d'), "%Y-%m-%d")
        duration = dt.timedelta(days=int(self.product.warranty_duration))
        self.warranty_expire_date = pdate + duration
        self.purchase_date = pdate
        super(RegisterWarrenty, self).save(*args, **kwargs)

class ClaimProductWarranty(models.Model):
    warranty_claim_subject = models.CharField(max_length=200, blank=False, null=False)
    product = models.OneToOneField(RegisterWarrenty)
    claim_date = models.DateField(_('Claim Date'), auto_now_add=True, editable=False)
    resolve_date = models.DateField(_('Resolve Date'), editable=False, null=True, blank=True)
    warranty_details = models.TextField(blank=True, null=True)
    claim_status = models.CharField(_('Claim Status'), choices=CLAIM_STATUS, max_length=1)

    def __unicode__(self):
        return self.warranty_claim_subject


    def save(self, *args, **kwargs):
        # import pdb; pdb.set_trace();
        if self.pk is None:
            self.product.warranty_status = '4'
            self.product.save()
            self.claim_status = '4'
        super(ClaimProductWarranty, self).save(*args, **kwargs)
