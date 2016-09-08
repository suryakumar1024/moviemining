from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<requester>[\w\-]+)/$', views.check_requester, name='requester'),
    url(r'^(?P<requester>[\w\-]+)/registry/$', views.movie_registry, name='registry'),
    url(r'^details/(?P<movie_id>[0-9]+)/(?P<requester>[\w\-]+)/$', views.movie_details, name='details'),
    url(r'^remove/(?P<movie_id>[0-9]+)$', views.remove_movie, name='remove_movie'),
    url(r'^like/(?P<movie_id>[0-9]+)$', views.like_movie, name='like_movie'),
    url(r'^unlike/(?P<movie_id>[0-9]+)$', views.unlike_movie, name='unlike_movie'),

    # url(r'^(?P<requester>[\w\-]+)/$', views.remove_movie, name='requester_page'),

]