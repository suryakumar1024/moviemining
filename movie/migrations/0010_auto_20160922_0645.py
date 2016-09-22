# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0009_auto_20160922_0629'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='new_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='movie',
            name='old_field',
            field=models.IntegerField(default=0),
        ),
    ]
