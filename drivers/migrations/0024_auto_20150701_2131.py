# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def transfer_images(apps, schema_editor):
    ServiceRequest = apps.get_model("drivers", "ServiceRequest")
    ServiceRequestImage = apps.get_model("drivers", "ServiceRequestImage")
    service_requests = ServiceRequest.objects.all()
    for service_request in service_requests:
        service_image = ServiceRequestImage(service_request=service_request, image=service_request.image)
        service_image.save()


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0023_auto_20150302_2240'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceRequestImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'')),
                ('service_request', models.ForeignKey(to='drivers.ServiceRequest', on_delete=models.CASCADE)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RunPython(transfer_images),
        migrations.RemoveField(
            model_name='servicerequest',
            name='image',
        ),
    ]
