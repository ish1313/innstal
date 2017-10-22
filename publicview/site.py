from django.contrib.admin import AdminSite
from django.conf.urls import url

from .views import *


class PublicViewSite(AdminSite):

	def get_urls(self):
		urls = super(PublicViewSite, self).get_urls()

		urls += [
			url(r'/$', index, name='index'),
		    url(r'login/$', login, name='login'),
		    url(r'register_warrantly/$', 'publicview.views.register_warrantly', name='register_warrantly'),
		    url(r'pricing/$', 'publicview.views.pricing', name='pricing'),
		    url(r'service/$', 'publicview.views.service', name='service'),
		    url(r'about/$', 'publicview.views.about', name='about'),
		    url(r'contact/$', 'publicview.views.contact', name='contact'),
		    url(r'search_result/$', 'publicview.views.search_result', name='search_result'),
		    url(r'signup/$', 'publicview.views.SignUp', name='signup'),
		]

		return urls
