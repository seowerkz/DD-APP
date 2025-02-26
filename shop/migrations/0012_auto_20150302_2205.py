# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_auto_20150302_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workorder',
            name='mechanics',
            field=models.ManyToManyField(related_name='work_order_mechanic', null=True, to=settings.AUTH_USER_MODEL, blank=True),
            preserve_default=True,
        ),
    ]
