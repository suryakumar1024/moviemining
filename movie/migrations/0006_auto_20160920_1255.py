# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0005_auto_20160920_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='name_of_movie',
            field=models.CharField(unique=True, max_length=100),
        ),
    ]
