from django.db import models

# Create your models here.


class Movie(models.Model):
    name_of_movie = models.CharField(max_length=100)
    movie_director = models.CharField(max_length=100)
    movie_producer = models.CharField(max_length=100)
    movie_cast_actor = models.CharField(max_length=100)
    movie_cinematography = models.CharField(max_length=100)
    movie_image = models.ImageField(upload_to='movie/', default = 'movie/google.jpg')

    def __str__(self):
        return self.name_of_movie


class Rating(models.Model):
    movie = models.OneToOneField(Movie)
    up_vote_count = models.IntegerField(default=0)
    down_vote_count = models.IntegerField(default=0)

    def total_vote(self):
        return self.up_vote_count + self.down_vote_count
