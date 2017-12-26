# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrapers', '0003_auto_20171119_1253'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AmazonProductResponses',
        ),
    ]
