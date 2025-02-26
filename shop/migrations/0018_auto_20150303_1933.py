# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_auto_20150303_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workordermechanics',
            name='hours',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
