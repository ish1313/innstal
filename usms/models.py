# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager
# Create your models here.
USER_TYPE = (
    ('0', 'Admin'),
    ('1', 'Customer'),
    ('2', 'BUSINESS')
)

def avatar_directory_path(instance, filename):
    ut = instance.user_type
    # import pdb; pdb.set_trace()
    filepath = str(instance.id) + filename[-4:]
    if ut == '1':
        filepath = 'customer/' + filepath
    elif ut == '2':
        filepath =  'business/' + filepath

    filepath = 'avatar/' + filepath

    return filepath


class InnstalUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True, db_index=True)
    phone = models.CharField(_('mobile number'), max_length=15, blank=True, null=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True, null=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True, null=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True, editable=False)
    last_login = models.DateTimeField(_('last login'), auto_now=True, editable=False)
    user_type = models.CharField(choices=USER_TYPE, max_length=1, default=1)
    # terms = models.BooleanField(_('Terms & Condition'), default=False)
    is_active = models.BooleanField(_('active'), default=False)
    is_active_subscription = models.BooleanField(_('active subscription'), default=False, editable=False)
    is_staff = models.BooleanField(_('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin site.'))
    is_superuser = models.BooleanField(_('staff status'), default=False,
        help_text=_('Designates whether the user is admin.'))
    avatar = models.ImageField(upload_to=avatar_directory_path, null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('innstaluser')
        verbose_name_plural = _('innstalusers')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name



class Package(models.Model):
    name = models.CharField(_('Package Name'), max_length=50, unique=True)
    title = models.CharField(_('Package Title'), max_length=50, blank=True, null=True)
    price = models.CharField(_('Package Cost'), max_length=50)
    duration = models.DurationField(default=2000, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(_('Service Name'), max_length=100)
    package = models.ManyToManyField(Package, related_name="package_service")
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name


class Subscription(models.Model):
    package = models.ForeignKey(Package)
    user = models.ForeignKey(InnstalUser)
    subscription_date = models.DateTimeField(auto_now_add=True)
    subscription_expire_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.package.name
