from django.contrib import admin
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^movie/', include('movie.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
