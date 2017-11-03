from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
	url(r'^', include('publicview.urls')),
    url(r'^', include('usms.urls')),
	url(r'^product/', include('product.urls')),
	url(r'^admin/', admin.site.urls),
	url(r'^summernote/', include('django_summernote.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
