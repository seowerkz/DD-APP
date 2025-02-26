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
            name='Reminder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('time', models.DateTimeField()),
                ('equipment_number', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('created_by', models.ForeignKey(related_name='created_by', to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ReminderRead',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('read', models.DateTimeField(null=True, blank=True)),
                ('reminder', models.ForeignKey(to='reminders.Reminder', on_delete=models.CASCADE)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='reminder',
            name='users',
            field=models.ManyToManyField(related_name='read_by', through='reminders.ReminderRead', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
