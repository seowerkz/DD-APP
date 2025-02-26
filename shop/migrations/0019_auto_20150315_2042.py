# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0018_auto_20150303_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partsused',
            name='part',
            field=models.ForeignKey(blank=True, to='shop.Part', null=True, on_delete=models.CASCADE),
            preserve_default=True,
        ),
    ]
