from django.conf.urls import url
from django.contrib.auth import views as auth_views
# from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    url(r'signup/$', signup, name='signup'),
    url(r'login/$', login, name='login'),
    url(r'logout/$', auth_views.logout, name='logout'),
    url(r'dashboard/$', dashboard, name='dashboard'),
    url(r'product-manual/$', product_manual, name='product-manual'),
]
