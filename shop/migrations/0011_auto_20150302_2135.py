# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0010_auto_20150302_2127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workorder',
            name='mechanic',
        ),
        migrations.AddField(
            model_name='workorder',
            name='mechanics',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, null=True, blank=True),
            preserve_default=True,
        ),
    ]
