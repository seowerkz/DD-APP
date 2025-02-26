from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models import Q
from datetime import datetime, timedelta, date
from shop.models import WorkOrder


class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True, on_delete=models.CASCADE)
    phone = models.CharField(max_length=16)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'


class Truck(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Trailer(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class AsphaltTrailerMeasurement(models.Model):
    gross_weight = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return '%s lbs Gross Weight' % self.gross_weight

    class Meta:
        verbose_name = 'Asphalt Trailer Measurement'
        verbose_name_plural = 'Asphalt Trailer Measurements'


class AsphaltTrailerOutage(models.Model):
    measurement = models.ForeignKey(AsphaltTrailerMeasurement, on_delete=models.CASCADE)
    trailer = models.ForeignKey(Trailer, on_delete=models.CASCADE)
    outage = models.CharField(max_length=255)

    def __str__(self):
        return '%s: %s - %s' % (self.measurement, self.trailer, self.outage)

    class Meta:
        verbose_name = 'Asphalt Trailer Outage'
        verbose_name_plural = 'Asphalt Trailer Outages'


class CrudeTrailerLevel(models.Model):
    trailer = models.ForeignKey(Trailer, on_delete=models.CASCADE)
    gravity = models.CharField(max_length=255)
    gauge_measurement = models.CharField(max_length=255)

    def __str__(self):
        return '%s: %s - %s' % (self.trailer, self.gravity, self.gauge_measurement)

    class Meta:
        verbose_name = 'Crude Trailer Level'
        verbose_name_plural = 'Crude Trailer Levels'


class Shipper(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class DemurrageReason(models.Model):
    reason = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.reason


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class BolManager(models.Manager):
    def get_new(self):
        return self.filter(completed_at__isnull=True).order_by('-created_at')

    def get_completed(self):
        current_time = timezone.now()
        last_month = current_time - timedelta(days=30)
        return self.filter(completed_at__isnull=False, completed_at__gte=last_month).order_by('-completed_at')


class Bol(models.Model):
    created_by = models.ForeignKey(User, related_name='bol_created_by', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_by = models.ForeignKey(User, null=True, blank=True, related_name='bol_completed_by', on_delete=models.CASCADE)
    completed_at = models.DateTimeField(null=True, blank=True)
    order_number = models.CharField(max_length=255, null=True, blank=True)
    truck = models.ForeignKey(Truck, null=True, blank=True, on_delete=models.CASCADE)
    trailer_1 = models.ForeignKey(Trailer, null=True, blank=True, related_name='bol_trailer_1', on_delete=models.CASCADE)
    trailer_2 = models.ForeignKey(Trailer, null=True, blank=True, related_name='bol_trailer_2', on_delete=models.CASCADE)
    shipper = models.ForeignKey(Shipper, null=True, blank=True, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.CASCADE)
    demurrage_reason = models.ForeignKey(DemurrageReason, null=True, blank=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE)
    arrive_at = models.DateTimeField(null=True, blank=True)
    depart_at = models.DateTimeField(null=True, blank=True)
    weight = models.CharField(max_length=255)
    bol_number = models.CharField(max_length=255)
    comments = models.TextField(null=True, blank=True)
    objects = BolManager()

    def __str__(self):
        return self.bol_number

    class Meta:
        verbose_name = 'BOL'
        verbose_name_plural = 'BOL'


class ServiceRequestManager(models.Manager):
    def get_new(self):
        return self.filter(work_order__completed_at__isnull=True).order_by('created_at')

    def get_in_the_yard(self):
        return self.filter(Q(expected_date_of_arrival__isnull=True) | Q(expected_date_of_arrival__lte=date.today()), work_order__completed_at__isnull=True).order_by('created_at')

    def get_on_the_road(self):
        return self.filter(work_order__completed_at__isnull=True, expected_date_of_arrival__gt=date.today()).order_by('created_at')

    def get_completed(self):
        current_time = timezone.now()
        last_month = current_time - timedelta(days=30)
        return self.filter(work_order__completed_at__isnull=False, work_order__finished_at__isnull=True, work_order__completed_at__gte=last_month).order_by('-work_order__completed_at')

    def get_entered(self):
        current_time = timezone.now()
        last_month = current_time - timedelta(days=30)
        return self.filter(work_order__finished_at__isnull=False, work_order__printed_at__isnull=True, work_order__finished_at__gte=last_month).order_by('-work_order__completed_at')


class ServiceRequest(models.Model):
    created_by = models.ForeignKey(User, related_name='service_request_created_by', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    expected_date_of_arrival = models.DateField(null=True, blank=True)
    equipment = models.TextField()
    priority = models.IntegerField(default=0)
    work_order = models.OneToOneField(WorkOrder, null=True, blank=True, on_delete=models.CASCADE)
    objects = ServiceRequestManager()

    def is_complete(self):
        return self.work_order.completed_by

    def __str__(self):
        return '%s %s' % (self.id, self.equipment)

    class Meta:
        verbose_name = 'Service Request'
        verbose_name_plural = 'Service Requests'


class ServiceRequestProblem(models.Model):
    service_request = models.ForeignKey(ServiceRequest, on_delete=models.CASCADE)
    problem = models.TextField(null=True, blank=True)


class ServiceRequestImage(models.Model):
    service_request = models.ForeignKey(ServiceRequest, on_delete=models.CASCADE)
    image = models.ImageField()


class MileageReport(models.Model):
    created_by = models.ForeignKey(User, related_name='mileage_report_created_by', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    truck = models.ForeignKey(Truck, on_delete=models.CASCADE)
    mileage = models.IntegerField()
    dismissed_at = models.DateTimeField(null=True, blank=True)
    dismissed_by = models.ForeignKey(User, null=True, blank=True, related_name='mileage_report_dismissed_by', on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.truck, self.mileage)

    class Meta:
        verbose_name = 'Mileage Report'
        verbose_name_plural = 'Mileage Reports'


def check_profile(sender, instance, signal, *args, **kwargs):
    profile, created = UserProfile.objects.get_or_create(user=instance)
    if created:
        profile.save()

post_save.connect(check_profile, sender=User)
