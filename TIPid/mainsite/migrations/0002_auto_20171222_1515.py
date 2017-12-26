# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('history', models.CharField(max_length=200)),
                ('create_at', models.DateTimeField(default=datetime.datetime(2017, 12, 22, 15, 15, 19, 396511, tzinfo=utc), blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('information', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Search_bar',
        ),
    ]