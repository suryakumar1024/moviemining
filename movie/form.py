from django import forms
from django.forms import ModelForm, CharField
from movie.models import Movie, Rating
from django.utils.translation import ugettext_lazy as _


class MovieDetails(ModelForm):
    # slug = CharField(validators=[validate_slug])
    class Meta:
        model = Movie
        fields = ['name_of_movie', 'movie_director', 'movie_producer', 'movie_cast_actor', 'movie_cinematography',
                  'movie_image']
        help_texts = {
            'name_of_movie': _('some useful text'),
        }
        error_messages = {
            'name_of_movie': {'max_length': _("some useful text"),},
        }

    # name_of_movie = forms.CharField(max_length=100)
    # movie_director = forms.CharField(max_length=100)
    # movie_producer = forms.CharField(max_length=100)
    # movie_cast_actor = forms.CharField(max_length=100)
    # movie_cinematography = forms.CharField(max_length=100)


class UserRating(ModelForm):
    class Meta:
        model = Rating
        fields = ['up_vote_count', 'down_vote_count']
    # up_vote_count = forms.IntegerField()
    # down_vote_count = forms.IntegerField()