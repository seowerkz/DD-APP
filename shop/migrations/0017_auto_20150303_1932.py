# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_auto_20150303_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workordermechanics',
            name='hours',
            field=models.FloatField(),
            preserve_default=True,
        ),
    ]
