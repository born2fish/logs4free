# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('apache_an', '0003_auto_20160306_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apachelogline',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 6, 13, 21, 14, 247422, tzinfo=utc)),
        ),
    ]
