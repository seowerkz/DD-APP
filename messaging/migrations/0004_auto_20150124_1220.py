# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0003_auto_20150122_2014'),
    ]

    operations = [
        migrations.AddField(
            model_name='messageread',
            name='deleted_at',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=False,
        ),
    ]
