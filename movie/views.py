from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from models import Movie, Rating
from form import MovieDetails

# movie_objects = Movie.objects.filter(data_delete=1)


def index(request):
    return render(request, 'movie/index.html')


def check_requester(request, requester):
    if request.method == 'GET':
        return render(request, 'movie/movie_list.html', {'requester': requester,
                                                         'movie_list': Movie.objects.filter(data_delete=False),
                                                         'rating': Rating})


def movie_registry(request, requester):
    if request.method == 'GET':
        form = MovieDetails()
    else:
        form = MovieDetails(request.POST, request.FILES)
        if form.is_valid():
            movie_obj = form.save()
            Rating.objects.create(movie=movie_obj, up_vote_count=0, down_vote_count=0)
            return HttpResponseRedirect(reverse('index'))

    return render(request, 'movie/movie_registry.html', {'form': form, 'requester': requester})


def movie_details(request, movie_id, requester):
    movie_instance = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movie/movie_details.html', {'movie': movie_instance, 'requester': requester})


def remove_movie(request, movie_id):
    delete_instance = get_object_or_404(Movie, pk=movie_id)
    delete_instance.data_delete = True
    delete_instance.save()
    return render(request, 'movie/movie_list.html', {'requester': 'admin',
                                                     'movie_list': Movie.objects.filter(data_delete=False)})


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
        form = MovieDetails(request.POST, request.FILES)
        if form.is_valid():
            import ipdb; ipdb.set_trace()
            new_data = form.save()
            movie.data_delete = True
            movie.new_field = new_data.id
            movie.times_of_updated += 1
            movie.save()
            new_data.old_field = movie_id
            new_data.save()
            Rating.objects.create(movie=new_data, up_vote_count= movie.rating.up_vote_count,
                                  down_vote_count=movie.rating.down_vote_count)
            return HttpResponseRedirect(reverse('details', kwargs={'movie_id': new_data.id, 'requester': 'admin'}))
        # form = MovieDetails(request.POST, instance=movie)
        # if form.is_valid():
        #     form.save()
        #     movie.times_of_updated += 1
        #     movie.save()
        #     return HttpResponseRedirect(reverse('details', kwargs={'movie_id': movie_id, 'requester': 'admin'}))
    return render(request, 'movie/update_movie.html', {'movie_id': movie_id, 'form': form})