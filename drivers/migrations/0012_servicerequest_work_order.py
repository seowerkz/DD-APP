# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
        ('drivers', '0011_servicerequest_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicerequest',
            name='work_order',
            field=models.OneToOneField(null=True, blank=True, to='shop.WorkOrder', on_delete=models.CASCADE),
            preserve_default=True,
        ),
    ]
