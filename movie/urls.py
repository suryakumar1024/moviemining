from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^user/', views.user, name='user'),
    url(r'^admin/', views.admin, name='admin'),
    url(r'^registry', views.movie_registry, name='registry'),
]