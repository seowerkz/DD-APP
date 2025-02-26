from django.shortcuts import render
from django.template import RequestContext
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.utils import timezone
from drivers.models import Bol, MileageReport
from drivers.forms import BolForm

@user_passes_test(lambda u:u.is_staff, login_url='/accounts/login/')
def dispatch(request):
    new_loads = Bol.objects.get_new()
    completed_loads = Bol.objects.get_completed()
    return render(request, 'office/dispatch.html',
                               {'new_loads': new_loads, 'completed_loads': completed_loads})

@user_passes_test(lambda u:u.is_staff, login_url='/accounts/login/')
def mileage(request):
    mileage_reports = MileageReport.objects.filter(dismissed_at__isnull=True)
    return render(request, 'office/mileage.html',
                               {'mileage_reports': mileage_reports})
