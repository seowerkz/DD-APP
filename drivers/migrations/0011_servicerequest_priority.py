# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0010_auto_20150116_1755'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicerequest',
            name='priority',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
