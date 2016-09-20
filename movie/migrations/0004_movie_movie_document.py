# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_auto_20160919_1222'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='movie_document',
            field=models.FileField(default=b'movie/nodoc.doc', upload_to=b'movie/'),
        ),
    ]
