# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0015_auto_20150201_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bol',
            name='arrive_at',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bol',
            name='depart_at',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
