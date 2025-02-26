# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('unit_number', models.CharField(max_length=255)),
                ('odometer', models.CharField(max_length=255)),
                ('hours', models.CharField(max_length=255)),
                ('changed_oil', models.BooleanField(default=False)),
                ('fuel_filters', models.BooleanField(default=False)),
                ('oil_filter', models.BooleanField(default=False)),
                ('greased', models.BooleanField(default=False)),
                ('changed_brakes', models.BooleanField(default=False)),
                ('changed_wheel_seals', models.BooleanField(default=False)),
                ('work_performed', models.TextField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('completed_at', models.DateTimeField(null=True, blank=True)),
                ('completed_by', models.ForeignKey(related_name='work_order_completed_by', blank=True, to=settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)),
                ('created_by', models.ForeignKey(related_name='work_order_created_by', to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)),
                ('mechanic', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)),
                ('updated_by', models.ForeignKey(related_name='work_order_updated_by', to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)),
            ],
            options={
                'verbose_name': 'Work Order',
                'verbose_name_plural': 'Work Orders',
            },
            bases=(models.Model,),
        ),
    ]
