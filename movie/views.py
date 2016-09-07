from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from models import Movie, Rating
from form import MovieDetails, UserRating
# Create your views here.


def index(request):
    return render(request, 'movie/index.html')


def user(request):
    return render(request, 'movie/movie_list.html', {'requester': True})


def admin(request):
    return render(request, 'movie/movie_list.html', {'requester': False})


def movie_registry(request):
    if request.method == 'GET':
        form = MovieDetails()
    else:
        form = MovieDetails(request.POST)
        if form.is_valid():
            name_of_movie = form.cleaned_data['name_of_movie']
            movie_director = form.cleaned_data['movie_director']
            movie_producer = form.cleaned_data['movie_producer']
            movie_cast_actor = form.cleaned_data['movie_cast_actor']
            movie_cinematography = form.cleaned_data['movie_cinematography']
            movie_obj = Movie.objects.create(name_of_movie = name_of_movie, movie_director = movie_director, movie_producer= movie_producer, movie_cast_actor = movie_cast_actor, movie_cinematography = movie_cinematography)
            return HttpResponseRedirect(reverse('index'))
    return render(request, 'movie/movie_registry.html', {'form': form, 'requester': False})