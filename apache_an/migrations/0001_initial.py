# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApacheLogLine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('from_ip', models.CharField(max_length=200)),
                ('date_time', models.DateTimeField(verbose_name=b'req date')),
                ('req_type', models.CharField(max_length=7)),
                ('req_uri', models.CharField(max_length=2000)),
                ('req_protocol', models.CharField(max_length=10)),
                ('req_status', models.IntegerField(default=None)),
                ('from_url', models.CharField(max_length=500)),
                ('user_agent', models.CharField(max_length=500)),
            ],
        ),
    ]
