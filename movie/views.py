from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from models import Movie, Rating
from form import MovieDetails, UserRating


def index(request):
    return render(request, 'movie/index.html')


def check_requester(request,requester):
    if request.method == 'GET':
        return render(request,'movie/movie_list.html', {'requester': requester,'movie_list' : Movie.objects.all(),
                                                        'rating': Rating})


def movie_registry(request, requester):
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
            movie_obj = Movie.objects.create(name_of_movie = name_of_movie, movie_director = movie_director,
                                             movie_producer= movie_producer, movie_cast_actor = movie_cast_actor,
                                             movie_cinematography = movie_cinematography)
            Rating.objects.create(movie=movie_obj,up_vote_count=0,down_vote_count=0)

            return HttpResponseRedirect(reverse('index'))
    return render(request, 'movie/movie_registry.html', {'form': form, 'requester':requester})


def movie_details(request, movie_id, requester):
    # import ipdb;ipdb.set_trace()
    movie_instance = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movie/movie_details.html', {'movie': movie_instance, 'requester': requester})


def remove_movie(request, movie_id):
    get_object_or_404(Movie, pk=movie_id).delete()
    # Movie.objects.filter(pk=movie_id).delete()
    return render(request, 'movie/movie_list.html', {'requester': False, 'movie_list' : Movie.objects.all()})


def like_movie(request, movie_id):
    import ipdb;ipdb.set_trace()
    movie = get_object_or_404(Movie,pk=movie_id)
    rating_inst=movie.rating.up_vote_count+1
    return  reverse('details', kwargs={'movie_id': movie_id, 'requester': 'AnonymousUser'})


def unlike_movie(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    rating_inst = movie.rating.up_vote_count + 1
    return render(request, 'movie/movie_details.html', {'movie': movie_id, 'requester': 'AnonymousUser'})


def update_movie(request, movie_id):
    if request.method == 'GET':
        movie = get_object_or_404(Movie, pk=movie_id)
        data = {'name_of_movie': movie.name_of_movie, 'movie_director': movie.movie_director,
                'movie_producer': movie.movie_producer, 'movie_cast_actor': movie.movie_cast_actor,
                'movie_cinematography': movie.movie_cinematography}
        form = MovieDetails(data)
        return render(request, 'movie/movie_registry.html', {'form': form, 'requester': 'AnonymousUser'})