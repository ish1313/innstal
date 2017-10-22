from django.conf.urls import url

from .views import *

urlpatterns = [
	url(r'^$', index, name='index'),
    url(r'^login/$', login, name='login'),
    # url(r'register_warrantly/$', register_warrantly, name='register_warrantly'),
    # url(r'pricing/$', pricing, name='pricing'),
    # url(r'service/$', service, name='service'),
    # url(r'about/$', about, name='about'),
    # url(r'contact/$', contact, name='contact'),
    # url(r'search_result/$', search_result, name='search_result'),
    url(r'^signup/$', SignUp, name='signup'),
]

