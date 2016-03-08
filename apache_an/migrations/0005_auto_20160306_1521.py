# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apache_an', '0004_auto_20160306_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apachelogline',
            name='date_time',
            field=models.DateTimeField(),
        ),
    ]
