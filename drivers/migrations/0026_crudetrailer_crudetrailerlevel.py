# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0025_auto_20150702_2116'),
    ]

    operations = [
        migrations.CreateModel(
            name='CrudeTrailer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
            ],
            options={
                'verbose_name': 'Crude Trailer',
                'verbose_name_plural': 'Crude Trailers',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CrudeTrailerLevel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gravity', models.CharField(max_length=255)),
                ('gauge_measurement', models.CharField(max_length=255)),
                ('trailer', models.ForeignKey(to='drivers.CrudeTrailer', on_delete=models.CASCADE)),
            ],
            options={
                'verbose_name': 'Crude Trailer Level',
                'verbose_name_plural': 'Crude Trailer Levels',
            },
            bases=(models.Model,),
        ),
    ]
