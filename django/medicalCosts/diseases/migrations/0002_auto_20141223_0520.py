# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diseases', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='procedure',
            name='cost',
        ),
        migrations.AddField(
            model_name='operation',
            name='cost',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
    ]
