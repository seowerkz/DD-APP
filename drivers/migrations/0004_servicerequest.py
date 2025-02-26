# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('drivers', '0003_bol_created_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('equipment', models.TextField()),
                ('problem1', models.TextField(null=True, blank=True)),
                ('problem2', models.TextField(null=True, blank=True)),
                ('problem3', models.TextField(null=True, blank=True)),
                ('problem4', models.TextField(null=True, blank=True)),
                ('problem5', models.TextField(null=True, blank=True)),
                ('problem6', models.TextField(null=True, blank=True)),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
