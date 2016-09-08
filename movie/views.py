from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from models import Movie, Rating
from form import MovieDetails, UserRating
# Create your views here.


def index(request):
    return render(request, 'movie/index.html')


def user(request):
    if request.method == 'GET':
        return render(request,'movie/movie_list.html', {'requester': True,'movie_list' : Movie.objects.all(), 'rating': Rating})


def admin(request):
    if request.method == 'GET':
        return render(request, 'movie/movie_list.html', {'requester': False, 'movie_list' : Movie.objects.all(), 'rating': Rating})


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
    return render(request, 'movie/movie_registry.html', {'form': form})


def movie_details(request, movie_id):
    movie_instance = get_object_or_404(Movie, pk=movie_id)
    rating_instance = get_object_or_404(Rating, pk=movie_id)
    movie = Movie.objects.get(pk=movie_id)
    ratings = Rating.objects.get(pk=movie_id)
    # total = Rating.total_vote(movie_instance)
    return render(request, 'movie/movie_details.html', {'movie': movie, 'rating': ratings, 'total': 5})


def remove_movie(request, movie_id):
    get_object_or_404(Movie, pk=movie_id)
    movie = Movie.objects.filter(pk=movie_id).delete()
    return render(request, 'movie/movie_list.html', {'requester': False, 'movie_list' : Movie.objects.all()})