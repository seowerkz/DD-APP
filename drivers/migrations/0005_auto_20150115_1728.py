# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0004_servicerequest'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='servicerequest',
            options={'verbose_name': 'Service Request', 'verbose_name_plural': 'Service Requests'},
        ),
        migrations.AddField(
            model_name='servicerequest',
            name='image',
            field=models.ImageField(null=True, upload_to=b''),
            preserve_default=True,
        ),
    ]
