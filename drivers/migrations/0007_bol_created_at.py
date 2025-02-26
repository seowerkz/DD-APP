# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0006_auto_20150115_1732'),
    ]

    operations = [
        migrations.AddField(
            model_name='bol',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 16, 1, 48, 47, 699660, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
