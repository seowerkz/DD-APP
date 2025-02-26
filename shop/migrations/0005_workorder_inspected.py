# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20150117_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='workorder',
            name='inspected',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
