# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bol',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=255)),
                ('arrive_at', models.DateTimeField()),
                ('depart_at', models.DateTimeField()),
                ('weight', models.CharField(max_length=255)),
                ('bol_number', models.CharField(max_length=255)),
                ('comments', models.TextField(null=True, blank=True)),
            ],
            options={
                'verbose_name': 'BOL',
                'verbose_name_plural': 'BOL',
            },
            bases=(models.Model,),
        ),
    ]
