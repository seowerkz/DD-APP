# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0022_auto_20150204_1955'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceRequestProblem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('problem', models.TextField(null=True, blank=True)),
                ('service_request', models.ForeignKey(to='drivers.ServiceRequest', on_delete=models.CASCADE)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='servicerequest',
            name='problem1',
        ),
        migrations.RemoveField(
            model_name='servicerequest',
            name='problem2',
        ),
        migrations.RemoveField(
            model_name='servicerequest',
            name='problem3',
        ),
        migrations.RemoveField(
            model_name='servicerequest',
            name='problem4',
        ),
        migrations.RemoveField(
            model_name='servicerequest',
            name='problem5',
        ),
        migrations.RemoveField(
            model_name='servicerequest',
            name='problem6',
        ),
    ]
