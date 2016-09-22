from django.db import models

# Create your models here.


class Movie(models.Model):
    name_of_movie = models.CharField(max_length=100)
    movie_director = models.CharField(max_length=100)
    movie_producer = models.CharField(max_length=100)
    movie_cast_actor = models.CharField(max_length=100)
    movie_cinematography = models.CharField(max_length=100)
    movie_image = models.ImageField(upload_to='movie/images', default = 'movie/google.jpg')
    movie_document = models.FileField(upload_to='movie/documents', default='movie/nodoc.doc')
    # data_delete = models.IntegerField(default=1)
    data_delete = models.BooleanField(default=False)
    times_of_updated = models.IntegerField(default=0)
    old_field = models.IntegerField(default=0)
    new_field = models.IntegerField(default=0)

    def __str__(self):
        return self.name_of_movie


class Rating(models.Model):
    movie = models.OneToOneField(Movie)
    up_vote_count = models.IntegerField(default=0)
    down_vote_count = models.IntegerField(default=0)

    def total_vote(self):
        return self.up_vote_count + self.down_vote_count
