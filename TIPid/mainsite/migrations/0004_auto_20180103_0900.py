# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0003_auto_20180103_0557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 3, 9, 0, 56, 565740, tzinfo=utc), blank=True),
        ),
    ]
