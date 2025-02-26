# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0019_auto_20150315_2042'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkPerformed',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('work_performed', models.TextField(null=True, blank=True)),
                ('work_order', models.ForeignKey(to='shop.WorkOrder', on_delete=models.CASCADE)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
