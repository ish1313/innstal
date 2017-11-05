# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class HomeBlog(models.Model):
    looking_for_instruction = models.TextField(max_length=500, blank=True, null=True)
    want_to_register_your_warranty_car = models.TextField(max_length=500, blank=True, null=True)
    find_user_manual = models.TextField(max_length=500, blank=True, null=True)
    read_installation_instruction = models.TextField(max_length=500, blank=True, null=True)
    claim_your_warranty_in_future = models.TextField(max_length=500, blank=True, null=True)
    how_it_works = models.TextField(max_length=500, blank=True, null=True)
