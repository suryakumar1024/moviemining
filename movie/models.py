from django.db import models

# Create your models here.


class Movie(models.Model):
    name_of_movie = models.CharField(max_length=100)
    movie_director = models.CharField(max_length=100)
    movie_producer = models.CharField(max_length=100)
    movie_cast_actor = models.CharField(max_length=100)
    movie_cinematography = models.CharField(max_length=100)


class Rating(models.Model):
    movie = models.OneToOneField(Movie)
    up_vote_count = models.IntegerField(default=0)
    down_vote_count = models.IntegerField(default=0)
