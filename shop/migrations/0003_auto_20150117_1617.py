# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20150117_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workorder',
            name='work_performed',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
