from django.db import models
from django.contrib.auth.models import User

class Reminder(models.Model):
    created_by = models.ForeignKey(User, related_name='created_by', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    time = models.DateTimeField()
    equipment_number = models.CharField(max_length=255)
    description = models.TextField()
    users = models.ManyToManyField(User, through='reminders.ReminderRead', related_name='read_by')

class ReminderRead(models.Model):
    reminder = models.ForeignKey(Reminder, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    read = models.DateTimeField(null=True, blank=True)
