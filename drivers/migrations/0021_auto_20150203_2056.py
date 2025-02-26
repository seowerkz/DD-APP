# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.contrib.auth.models import User

def create_profiles(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    UserProfile = apps.get_model("drivers", "UserProfile")
    for user in User.objects.all():
        profile, created = UserProfile.objects.get_or_create(user_id=user.id)
        if created:
            profile.save()

class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0020_userprofile'),
    ]

    operations = [
        migrations.RunPython(create_profiles),
    ]
