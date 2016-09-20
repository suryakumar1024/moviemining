# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_movie_movie_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='movie_document',
            field=models.FileField(default=b'movie/nodoc.doc', upload_to=b'movie/documents'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='movie_image',
            field=models.ImageField(default=b'movie/google.jpg', upload_to=b'movie/images'),
        ),
    ]
