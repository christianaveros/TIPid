# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0005_auto_20171226_0956'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=512)),
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
                ('original_price', models.IntegerField()),
                ('rating', models.DecimalField(max_digits=10, decimal_places=2)),
                ('reviews', models.IntegerField()),
                ('bayes_est', models.DecimalField(max_digits=10, decimal_places=2)),
            ],
        ),
        migrations.DeleteModel(
            name='History',
        ),
        migrations.RemoveField(
            model_name='item',
            name='information',
        ),
        migrations.AddField(
            model_name='item',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 28, 6, 52, 28, 728868, tzinfo=utc), blank=True),
        ),
        migrations.AddField(
            model_name='scrapedproduct',
            name='item',
            field=models.ForeignKey(to='mainsite.Item'),
        ),
        migrations.AddField(
            model_name='sample',
            name='item',
            field=models.ForeignKey(to='mainsite.Item'),
        ),
    ]
