from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^user/', views.user, name='user'),
    url(r'^admin/', views.admin, name='admin'),
    url(r'^admin/movie_registry', views.movie_registry, name='movie_registry'),
]