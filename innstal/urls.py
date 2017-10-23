from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
	url(r'^', include('publicview.urls')),
    url(r'^', include('usms.urls')),
	url(r'^admin/', admin.site.urls),
]
