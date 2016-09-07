# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_of_movie', models.CharField(max_length=100)),
                ('movie_director', models.CharField(max_length=100)),
                ('movie_producer', models.CharField(max_length=100)),
                ('movie_cast_actor', models.CharField(max_length=100)),
                ('movie_cinematography', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('up_vote_count', models.IntegerField(default=0)),
                ('down_vote_count', models.IntegerField(default=0)),
                ('movie', models.OneToOneField(to='movie.Movie')),
            ],
        ),
    ]
