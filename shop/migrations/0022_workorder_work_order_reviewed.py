# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0021_auto_20160315_2211'),
    ]

    operations = [
        migrations.AddField(
            model_name='workorder',
            name='work_order_reviewed',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
