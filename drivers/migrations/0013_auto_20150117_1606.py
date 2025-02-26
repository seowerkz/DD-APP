# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0012_servicerequest_work_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicerequest',
            name='completed_at',
        ),
        migrations.RemoveField(
            model_name='servicerequest',
            name='completed_by',
        ),
    ]
