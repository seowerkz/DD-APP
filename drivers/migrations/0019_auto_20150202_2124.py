# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0018_auto_20150202_2108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mileagereport',
            name='truck_number',
        ),
        migrations.AddField(
            model_name='mileagereport',
            name='truck',
            field=models.ForeignKey(default=1, to='drivers.Truck', on_delete=models.CASCADE),
            preserve_default=False,
        ),
    ]
