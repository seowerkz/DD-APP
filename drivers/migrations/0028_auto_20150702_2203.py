# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0027_auto_20150702_2202'),
    ]

    operations = [
        migrations.AddField(
            model_name='asphalttraileroutage',
            name='trailer',
            field=models.ForeignKey(default=1, to='drivers.Trailer', on_delete=models.CASCADE),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='crudetrailerlevel',
            name='trailer',
            field=models.ForeignKey(default=1, to='drivers.Trailer', on_delete=models.CASCADE),
            preserve_default=False,
        ),
    ]
