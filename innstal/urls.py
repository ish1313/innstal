from django.conf.urls import url
from django.contrib import admin

import publicview.views

urlpatterns = [
	url(r'^$', publicview.views.index, name='index'),
    url(r'^login', publicview.views.login, name='login'),
    url(r'^register_warrantly', publicview.views.register_warrantly, name='login'),
    url(r'^pricing', publicview.views.pricing, name='pricing'),
    url(r'^service', publicview.views.service, name='service'),
    url(r'^about', publicview.views.about, name='about'),
    url(r'^contact', publicview.views.contact, name='contact'),
    url(r'^search_result', publicview.views.search_result, name='search_result'),
    url(r'^signup', publicview.views.SignUp),

    url(r'^admin/', admin.site.urls),
]
