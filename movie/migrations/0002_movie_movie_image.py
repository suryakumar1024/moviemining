# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='movie_image',
            field=models.ImageField(default=b'movie/None/no-img.jpg', upload_to=b'movie/'),
        ),
    ]
