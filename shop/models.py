from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime, timedelta
from django.conf import settings


class Part(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = 'Part'
        verbose_name_plural = 'Parts'
        ordering = ['name']


class WorkOrderManager(models.Manager):
    def get_new(self):
        return self.filter(servicerequest__isnull=True, completed_at__isnull=True).order_by('-created_at')

    def get_completed(self):
        current_time = timezone.now()
        ninty_days_ago = current_time - timedelta(days=90)
        return self.filter(servicerequest__isnull=True, completed_at__isnull=False, completed_at__gte=ninty_days_ago, finished_at__isnull=True).order_by('-completed_at')

    def get_entered(self):
        current_time = timezone.now()
        ninty_days_ago = current_time - timedelta(days=90)
        return self.filter(servicerequest__isnull=True, completed_at__isnull=False, finished_at__isnull=False, printed_at__isnull=True, finished_at__gte=ninty_days_ago).order_by('-completed_at')


class WorkOrder(models.Model):
    created_by = models.ForeignKey(User, related_name='work_order_created_by', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    unit_number = models.CharField(max_length=255)
    odometer = models.CharField(max_length=255, null=True, blank=True)
    mechanics = models.ManyToManyField(User, null=True, blank=True, through='WorkOrderMechanics')
    full_service = models.BooleanField(default=False)
    greased = models.BooleanField(default=False)
    inspected = models.BooleanField(default=False)
    work_performed = models.TextField(null=True, blank=True)  # This is deprecated, use WorkPerformed
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, related_name='work_order_updated_by', on_delete=models.CASCADE)
    completed_at = models.DateTimeField(null=True, blank=True)
    completed_by = models.ForeignKey(User, null=True, blank=True, related_name='work_order_completed_by', on_delete=models.CASCADE)
    work_order_reviewed = models.BooleanField(default=False, blank=True)
    axon_number = models.CharField(max_length=255, null=True, blank=True)
    finished_at = models.DateTimeField(null=True, blank=True)
    finished_by = models.ForeignKey(User, null=True, blank=True, related_name='work_order_finished_by', on_delete=models.CASCADE)
    printed_at = models.DateTimeField(null=True, blank=True)
    printed_by = models.ForeignKey(User, null=True, blank=True, related_name='work_order_printed_by', on_delete=models.CASCADE)
    parts = models.ManyToManyField(Part, through='PartsUsed')
    objects = WorkOrderManager()

    def __str__(self):
        return '%s' % self.unit_number

    class Meta:
        verbose_name = 'Work Order'
        verbose_name_plural = 'Work Orders'

class WorkOrderMechanics(models.Model):
    work_order = models.ForeignKey(WorkOrder, on_delete=models.CASCADE)
    mechanic = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    hours = models.FloatField(null=True, blank=True)

class WorkPerformed(models.Model):
    work_order = models.ForeignKey(WorkOrder, on_delete=models.CASCADE)
    work_performed = models.TextField(null=True, blank=True)

class PartsUsed(models.Model):
    work_order = models.ForeignKey(WorkOrder, on_delete=models.CASCADE)
    part = models.ForeignKey(Part, null=True, blank=True, on_delete=models.CASCADE)
    quantity = models.FloatField()
