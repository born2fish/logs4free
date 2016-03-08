# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apache_an', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apachelogline',
            name='user_agent',
            field=models.CharField(max_length=2000),
        ),
    ]
