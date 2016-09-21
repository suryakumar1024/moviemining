from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm, CharField
from movie.models import Movie, Rating
from django.utils.translation import ugettext_lazy as _


class MovieDetails(ModelForm):
    # slug = CharField(validators=[validate_slug])
    class Meta:
        model = Movie
        fields = ['name_of_movie', 'movie_director', 'movie_producer', 'movie_cast_actor', 'movie_cinematography',
                  'movie_image', 'movie_document']
        help_texts = {
            'name_of_movie': _('some useful text'),
        }
        error_messages = {
            'name_of_movie': {'max_length': _("Enter max of 100 characters"),},
        }

    # name_of_movie = forms.CharField(max_length=100)
    # movie_director = forms.CharField(max_length=100)
    # movie_producer = forms.CharField(max_length=100)
    # movie_cast_actor = forms.CharField(max_length=100)
    # movie_cinematography = forms.CharField(max_length=100)

    def clean_name_of_movie(self):
        name = self.cleaned_data.get('name_of_movie', '')
        try:
            import re
            reg = re.compile('^\w+$')
            if not reg.match(name):
                raise forms.ValidationError('Only Alphabets are allowed to be a movie name')
            return name
            # Movie.objects.get(name_of_movie=name)
            # raise forms.ValidationError("Movie exist.")
        except:
            print 'Error'


class UserRating(ModelForm):
    class Meta:
        model = Rating
        fields = ['up_vote_count', 'down_vote_count']
    # up_vote_count = forms.IntegerField()
    # down_vote_count = forms.IntegerField()


