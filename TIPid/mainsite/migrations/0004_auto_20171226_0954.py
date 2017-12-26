# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0003_auto_20171226_0951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 26, 9, 54, 35, 652289, tzinfo=utc), blank=True),
        ),
    ]
