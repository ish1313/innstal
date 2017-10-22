from django.conf.urls import url, include
from django.contrib import admin

# from publicview.site import PublicViewSite
# publicview_site = PublicViewSite()

urlpatterns = [
	url(r'^', include('publicview.urls')),
    url(r'^admin/', admin.site.urls),
]
