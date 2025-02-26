# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0028_auto_20150702_2203'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='asphalttraileroutage',
            options={'verbose_name': 'Asphalt Trailer Outage', 'verbose_name_plural': 'Asphalt Trailer Outages'},
        ),
        migrations.AddField(
            model_name='servicerequest',
            name='expected_date_of_arrival',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
