# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrapers', '0002_auto_20171119_1239'),
    ]

    operations = [
        migrations.RenameField(
            model_name='amazonproductresponses',
            old_name='note',
            new_name='response',
        ),
    ]
