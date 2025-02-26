# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('drivers', '0007_bol_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='MileageReport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('truck_number', models.CharField(max_length=255)),
                ('mileage', models.IntegerField()),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)),
            ],
            options={
                'verbose_name': 'Mileage Report',
                'verbose_name_plural': 'Mileage Reports',
            },
            bases=(models.Model,),
        ),
    ]
