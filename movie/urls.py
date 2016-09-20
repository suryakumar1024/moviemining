from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from moviemining import settings


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<requester>[\w\-]+)/$', views.check_requester, name='requester'),
    url(r'^(?P<requester>[\w\-]+)/registry/$', views.movie_registry, name='registry'),
    url(r'^(?P<requester>[\w\-]+)/details/(?P<movie_id>[0-9]+)/$', views.movie_details, name='details'),
    url(r'^remove/(?P<movie_id>[0-9]+)$', views.remove_movie, name='remove_movie'),
    url(r'^update/(?P<movie_id>[0-9]+)$', views.update_movie, name='update'),

    url(r'^like/(?P<requester>[\w\-]+)/(?P<movie_id>[0-9]+)$', views.like_movie, name='like_movie'),
    url(r'^unlike/(?P<requester>[\w\-]+)/(?P<movie_id>[0-9]+)$', views.unlike_movie, name='unlike_movie'),

    # url(r'^(?P<requester>[\w\-]+)/$', views.remove_movie, name='requester_page'),

]