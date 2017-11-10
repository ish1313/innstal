from django.conf.urls import url
from django.contrib.auth import views as auth_views
# from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    url(r'search-manual/$', search_product_manual, name='search_product_manual'),
    url(r'category/$', product_category, name='product_category'),
    url(r'register-warranty/$', product_register_warranty, name='product_register_warranty'),
]
