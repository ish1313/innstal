from django.conf.urls import url

from .views import *

urlpatterns = [
	url(r'', index, name='index'),
	url(r'how-it-works/$', how_it_works, name='how_it_works'),
	url(r'business/$', business_page, name='business_page'),
    # url(r'register_warrantly/$', register_warrantly, name='register_warrantly'),
    # url(r'pricing/$', pricing, name='pricing'),
    # url(r'service/$', service, name='service'),
    # url(r'about/$', about, name='about'),
    # url(r'contact/$', contact, name='contact'),
    # url(r'search_result/$', search_result, name='search_result'),
]
