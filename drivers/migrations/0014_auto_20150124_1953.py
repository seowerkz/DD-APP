# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.contrib.auth.models import Group

def create_groups(apps, schema_editor):
    driver_group = Group(name='driver')
    driver_group.save()
    shop_group = Group(name='shop')
    shop_group.save()
    office_group = Group(name='office')
    office_group.save()


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0013_auto_20150117_1606'),
    ]

    operations = [
        migrations.RunPython(create_groups),
    ]
