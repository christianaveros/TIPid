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
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 3, 5, 57, 32, 492937, tzinfo=utc), blank=True),
        ),
        migrations.AlterField(
            model_name='scrapedproduct',
            name='bayes_est',
            field=models.DecimalField(max_digits=10, decimal_places=9),
        ),
        migrations.AlterField(
            model_name='scrapedproduct',
            name='price',
            field=models.DecimalField(max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='scrapedproduct',
            name='rating',
            field=models.DecimalField(max_digits=10, decimal_places=10),
        ),
    ]
