# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('diseases', '0003_operation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operation',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 23, 5, 29, 16, 614539, tzinfo=utc), blank=True),
            preserve_default=True,
        ),
    ]
