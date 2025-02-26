# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('drivers', '0009_auto_20150115_1900'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicerequest',
            name='completed_at',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='servicerequest',
            name='completed_by',
            field=models.ForeignKey(related_name='service_request_completed_by', blank=True, to=settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='created_by',
            field=models.ForeignKey(related_name='service_request_created_by', to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE),
            preserve_default=True,
        ),
    ]
