# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0026_crudetrailer_crudetrailerlevel'),
    ]

    operations = [
        migrations.CreateModel(
            name='AsphaltTrailerOutage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('outage', models.CharField(max_length=255)),
                ('measurement', models.ForeignKey(to='drivers.AsphaltTrailerMeasurement', on_delete=models.CASCADE)),
            ],
            options={
                'verbose_name': 'Asphalt Trailer',
                'verbose_name_plural': 'Asphalt Trailers',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='asphalttrailer',
            name='measurement',
        ),
        migrations.DeleteModel(
            name='AsphaltTrailer',
        ),
        migrations.RemoveField(
            model_name='crudetrailerlevel',
            name='trailer',
        ),
        migrations.DeleteModel(
            name='CrudeTrailer',
        ),
    ]
