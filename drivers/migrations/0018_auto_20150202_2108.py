# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('drivers', '0017_auto_20150202_1906'),
    ]

    operations = [
        migrations.AddField(
            model_name='mileagereport',
            name='dismissed_at',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mileagereport',
            name='dismissed_by',
            field=models.ForeignKey(related_name='mileage_report_dismissed_by', blank=True, to=settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mileagereport',
            name='created_by',
            field=models.ForeignKey(related_name='mileage_report_created_by', to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE),
            preserve_default=True,
        ),
    ]
