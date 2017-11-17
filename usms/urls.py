from django.conf.urls import url
from django.contrib.auth import views as auth_views
# from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    url(r'signup/$', signup, name='signup'),
    url(r'login/$', user_login, name='login'),
    url(r'logout/$', auth_views.logout, name='logout'),
    url(r'subscription/$', subscription, name='subscription'),
    url(r'dashboard/$', dashboard, name='dashboard'),
    url(r'dashboard/product-manual/$', ds_product_manual, name='ds_product_manual'),
    url(r'dashboard/warranties/$', ds_warranties, name='ds_warranties'),
    url(r'dashboard/account-details/$', account_details, name='account-details'),
    url(r'subscribe/package/(?P<package_id>\d+)/$', user_subscribe, name='user_subscribe'),
]
