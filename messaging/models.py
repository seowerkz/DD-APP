from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    message_from = models.ForeignKey(User, related_name='message_from', on_delete=models.CASCADE)
    message_to = models.ManyToManyField(User, through='MessageRead', related_name='message_to')
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class MessageRead(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    to = models.ForeignKey(User, on_delete=models.CASCADE)
    read = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
