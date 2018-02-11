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
        migrations.AlterField(
            model_name='item',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 11, 2, 7, 17, 549182, tzinfo=utc), blank=True),
        ),
        migrations.AlterField(
            model_name='scrapedproduct',
            name='ranking',
            field=models.IntegerField(null=True),
        ),
    ]
