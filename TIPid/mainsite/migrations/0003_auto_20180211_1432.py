# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0002_auto_20180211_0207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 11, 14, 32, 2, 867690, tzinfo=utc), blank=True),
        ),
    ]
