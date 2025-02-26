# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20150204_2046'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='part',
            options={'ordering': ['name'], 'verbose_name': 'Part', 'verbose_name_plural': 'Parts'},
        ),
        migrations.AlterField(
            model_name='partsused',
            name='quantity',
            field=models.FloatField(),
            preserve_default=True,
        ),
    ]
