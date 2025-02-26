# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_auto_20150302_2226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workorder',
            name='hours',
        ),
        migrations.AddField(
            model_name='workordermechanics',
            name='hours',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
