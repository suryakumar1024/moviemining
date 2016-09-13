from django import forms
from django.forms import ModelForm
from movie.models import Movie, Rating


class MovieDetails(ModelForm):
    class Meta:
        model = Movie
        fields = ['name_of_movie', 'movie_director', 'movie_producer', 'movie_cast_actor', 'movie_cinematography']
    # name_of_movie = forms.CharField(max_length=100)
    # movie_director = forms.CharField(max_length=100)
    # movie_producer = forms.CharField(max_length=100)
    # movie_cast_actor = forms.CharField(max_length=100)
    # movie_cinematography = forms.CharFie`ld(max_length=100)


class UserRating(ModelForm):
    class Meta:
        model = Rating
        fields = ['up_vote_count', 'down_vote_count']
    # up_vote_count = forms.IntegerField()
    # down_vote_count = forms.IntegerField()