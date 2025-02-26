# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20150117_1617'),
    ]

    operations = [
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Part',
                'verbose_name_plural': 'Parts',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PartsUsed',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField()),
                ('part', models.ForeignKey(to='shop.Part', on_delete=models.CASCADE)),
                ('work_order', models.ForeignKey(to='shop.WorkOrder', on_delete=models.CASCADE)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='workorder',
            name='parts',
            field=models.ManyToManyField(to='shop.Part', through='shop.PartsUsed'),
            preserve_default=True,
        ),
    ]
