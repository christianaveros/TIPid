# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('create_at', models.DateTimeField(default=datetime.datetime(2018, 1, 2, 6, 24, 46, 83531, tzinfo=utc), blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=512)),
                ('item', models.ForeignKey(to='mainsite.Item')),
            ],
        ),
        migrations.CreateModel(
            name='ScrapedProduct',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=512)),
                ('website', models.CharField(max_length=32, choices=[(b'amazon', b'Amazon.com'), (b'lazada', b'Lazada.com.ph'), (b'shopee', b'Shopee.ph')])),
                ('url', models.URLField()),
                ('price', models.IntegerField()),
                ('rating', models.DecimalField(max_digits=10, decimal_places=2)),
                ('reviews', models.IntegerField()),
                ('bayes_est', models.DecimalField(max_digits=10, decimal_places=10)),
                ('item', models.ForeignKey(to='mainsite.Item')),
            ],
        ),
    ]