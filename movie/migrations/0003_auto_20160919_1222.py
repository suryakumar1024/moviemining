# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_movie_movie_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='movie_image',
            field=models.ImageField(default=b'movie/google.jpg', upload_to=b'movie/'),
        ),
    ]
