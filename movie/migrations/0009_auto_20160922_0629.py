# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0008_movie_times_of_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='data_delete',
            field=models.BooleanField(default=False),
        ),
    ]
