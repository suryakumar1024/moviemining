from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from models import Movie, Rating
from form import MovieDetails


def index(request):
    return render(request, 'movie/index.html')


def check_requester(request, requester):
    if request.method == 'GET':
        return render(request, 'movie/movie_list.html', {'requester': requester, 'movie_list': Movie.objects.all(),
                                                         'rating': Rating})


def movie_registry(request, requester):
    if request.method == 'GET':
        form = MovieDetails()
    else:
        form = MovieDetails(request.POST)
        if form.is_valid():
            movie_obj = form.save()
            Rating.objects.create(movie=movie_obj, up_vote_count=0, down_vote_count=0)
            return HttpResponseRedirect(reverse('index'))

    return render(request, 'movie/movie_registry.html', {'form': form, 'requester': requester})


def movie_details(request, movie_id, requester):
    movie_instance = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movie/movie_details.html', {'movie': movie_instance, 'requester': requester})


def remove_movie(request, movie_id):
    get_object_or_404(Movie, pk=movie_id).delete()
    return render(request, 'movie/movie_list.html', {'requester': False, 'movie_list': Movie.objects.all()})


def like_movie(request, requester, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    rating_instance = movie.rating
    rating_instance.up_vote_count += 1
    rating_instance.save()
    return HttpResponseRedirect(reverse('details', kwargs={'movie_id': movie_id, 'requester': requester}))


def unlike_movie(request, requester, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    rating_instance = movie.rating
    rating_instance.down_vote_count += 1
    rating_instance.save()
    return HttpResponseRedirect(reverse('details', kwargs={'movie_id': movie_id, 'requester': requester}))


def update_movie(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.method == 'GET':
        form = MovieDetails(instance=movie)
    else:
        form = MovieDetails(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('details', kwargs={'movie_id': movie_id, 'requester': 'admin'}))
    return render(request, 'movie/update_movie.html', {'movie_id': movie_id, 'form': form})