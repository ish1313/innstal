from django.conf.urls import url
from django.contrib.auth import views as auth_views
# from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    url(r'signup/$', signup, name='signup'),
    url(r'login/$', login, name='login'),
    url(r'subscription/$', subscription, name='subscription'),
    url(r'logout/$', auth_views.logout, name='logout'),
    url(r'dashboard/$', dashboard, name='dashboard'),
    url(r'dashboard/product-manual/$', ds_product_manual, name='ds_product_manual'),
    url(r'dashboard/warranties/$', ds_warranties, name='ds_warranties'),
    url(r'dashboard/account-details/$', account_details, name='account-details'),
]
