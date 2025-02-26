# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20150228_1015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workorder',
            name='changed_brakes',
        ),
        migrations.RemoveField(
            model_name='workorder',
            name='changed_oil',
        ),
        migrations.RemoveField(
            model_name='workorder',
            name='changed_wheel_seals',
        ),
        migrations.RemoveField(
            model_name='workorder',
            name='fuel_filters',
        ),
        migrations.RemoveField(
            model_name='workorder',
            name='oil_filter',
        ),
        migrations.AddField(
            model_name='workorder',
            name='full_service',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
