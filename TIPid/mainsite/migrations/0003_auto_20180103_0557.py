# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0002_auto_20180103_0557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 3, 5, 57, 58, 462524, tzinfo=utc), blank=True),
        ),
        migrations.AlterField(
            model_name='scrapedproduct',
            name='bayes_est',
            field=models.DecimalField(max_digits=10, decimal_places=8),
        ),
        migrations.AlterField(
            model_name='scrapedproduct',
            name='rating',
            field=models.DecimalField(max_digits=10, decimal_places=8),
        ),
    ]
