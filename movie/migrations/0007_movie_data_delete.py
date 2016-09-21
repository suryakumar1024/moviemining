# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0006_auto_20160920_1255'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='data_delete',
            field=models.IntegerField(default=1),
        ),
    ]
