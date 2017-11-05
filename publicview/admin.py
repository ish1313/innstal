# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import *
# Register your models here.

class HomeBlogAdmin(SummernoteModelAdmin):
    pass

admin.site.register(HomeBlog, HomeBlogAdmin)
