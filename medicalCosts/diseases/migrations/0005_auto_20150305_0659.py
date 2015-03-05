# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('diseases', '0004_auto_20141223_0529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operation',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 5, 6, 59, 53, 698912, tzinfo=utc), blank=True),
            preserve_default=True,
        ),
    ]
