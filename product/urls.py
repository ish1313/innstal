from django.conf.urls import url
from django.contrib.auth import views as auth_views
# from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    url('search-manual/$', search_product_manual, name='search_product_manual'),
    url('category/$', product_category, name='product_category'),
    url('category/(?P<category_id>\d+)/$', category_products, name='category_products'),
    url('(?P<product_id>\d+)/details/$', product_details, name='product_details'),
    url('(?P<register_id>\d+)/claim-warranty/$', create_claim_warranty, name='create_claim_warranty'),
    url('register-warranty/$', product_register_warranty, name='product_register_warranty'),
    # url('warranty-claimed/$', product_warranty_claimed, name='product_warranty_claimed'),
]
