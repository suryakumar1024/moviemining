# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0007_movie_data_delete'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='times_of_updated',
            field=models.IntegerField(default=0),
        ),
    ]
