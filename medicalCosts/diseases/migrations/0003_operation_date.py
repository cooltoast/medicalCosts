# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('diseases', '0002_auto_20141223_0520'),
    ]

    operations = [
        migrations.AddField(
            model_name='operation',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 23, 5, 27, 43, 771501, tzinfo=utc), blank=True),
            preserve_default=True,
        ),
    ]
