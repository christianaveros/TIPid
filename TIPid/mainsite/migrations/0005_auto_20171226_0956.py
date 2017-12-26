# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0004_auto_20171226_0954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 26, 9, 56, 23, 812468, tzinfo=utc), blank=True),
        ),
    ]
