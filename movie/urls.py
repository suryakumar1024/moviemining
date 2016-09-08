from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^user/', views.user, name='user'),
    url(r'^admin/', views.admin, name='admin'),
    url(r'^registry', views.movie_registry, name='registry'),
    url(r'^details/(?P<movie_id>[0-9]+)$', views.movie_details, name='details'),
    url(r'^remove/(?P<movie_id>[0-9]+)$', views.remove_movie, name='remove_movie'),
]