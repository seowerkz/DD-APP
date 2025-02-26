# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def remove_empty_problems(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    ServiceRequestProblem = apps.get_model("drivers", "ServiceRequestProblem")
    ServiceRequestProblem.objects.filter(problem="").delete()
    ServiceRequestProblem.objects.filter(problem=None).delete()

class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0029_auto_20150704_1202'),
    ]

    operations = [
        migrations.RunPython(remove_empty_problems),
    ]
