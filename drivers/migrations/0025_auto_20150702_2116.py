# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0024_auto_20150701_2131'),
    ]

    operations = [
        migrations.CreateModel(
            name='AsphaltTrailer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('trailer', models.CharField(max_length=255)),
                ('outage', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Asphalt Trailer',
                'verbose_name_plural': 'Asphalt Trailers',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AsphaltTrailerMeasurement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gross_weight', models.CharField(unique=True, max_length=255)),
            ],
            options={
                'verbose_name': 'Asphalt Trailer Measurement',
                'verbose_name_plural': 'Asphalt Trailer Measurements',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='asphalttrailer',
            name='measurement',
            field=models.ForeignKey(to='drivers.AsphaltTrailerMeasurement', on_delete=models.CASCADE),
            preserve_default=True,
        ),
    ]
