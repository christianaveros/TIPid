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
            model_name='history',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 26, 9, 44, 17, 511388, tzinfo=utc), blank=True),
        ),
    ]
