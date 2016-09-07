from django import forms


class MovieDetails(forms.Form):
    name_of_movie = forms.CharField(max_length=100)
    movie_director = forms.CharField(max_length=100)
    movie_producer = forms.CharField(max_length=100)
    movie_cast_actor = forms.CharField(max_length=100)
    movie_cinematography = forms.CharField(max_length=100)


class UserRating(forms.Form):
    up_vote_count = forms.IntegerField()
    down_vote_count = forms.IntegerField()