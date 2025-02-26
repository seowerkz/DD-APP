# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def create_work_performed(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    WorkOrder = apps.get_model("shop", "WorkOrder")
    WorkPerformed = apps.get_model("shop", "WorkPerformed")
    for work_order in WorkOrder.objects.all():
        if work_order.work_performed:
            WorkPerformed.objects.create(work_order=work_order, work_performed=work_order.work_performed)

class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0020_workperformed'),
    ]

    operations = [
        migrations.RunPython(create_work_performed),
    ]
