from django.shortcuts import render, redirect
from django.template import RequestContext
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.models import User
from doubleddistributionapp.helpers import is_member
from drivers.models import *
from drivers.forms import BolForm, ServiceRequestForm, MileageReportForm, ProblemFormSet
import json
import pytz
import datetime

def _create_bol_objects(form):
    if form.data.get('new_truck'):
        try:
            new_truck = Truck.objects.get(name__iexact=form.data['new_truck'])
        except:
            new_truck = Truck.objects.create(name=form.data['new_truck'])
            new_truck.save()
        form.data['truck'] = new_truck.id
        form.data['new_truck'] = ''
    if form.data.get('new_trailer_1'):
        try:
            new_trailer_1 = Trailer.objects.get(name__iexact=form.data['new_trailer_1'])
        except:
            new_trailer_1 = Trailer.objects.create(name=form.data['new_trailer_1'])
            new_trailer_1.save()
        form.data['trailer_1'] = new_trailer_1.id
        form.data['new_trailer_1'] = ''
    if form.data.get('new_trailer_2'):
        try:
            new_trailer_2 = Trailer.objects.get(name__iexact=form.data['new_trailer_2'])
        except:
            new_trailer_2 = Trailer.objects.create(name=form.data['new_trailer_2'])
            new_trailer_2.save()
        form.data['trailer_2'] = new_trailer_2.id
        form.data['new_trailer_2'] = ''
    if form.data.get('new_shipper'):
        try:
            new_shipper = Shipper.objects.get(name__iexact=form.data['new_shipper'])
        except:
            new_shipper = Shipper.objects.create(name=form.data['new_shipper'])
            new_shipper.save()
        form.data['shipper'] = new_shipper.id
        form.data['new_shipper'] = ''
    if form.data.get('new_customer'):
        try:
            new_customer = Customer.objects.get(name__iexact=form.data['new_customer'])
        except:
            new_customer = Customer.objects.create(name=form.data['new_customer'])
            new_customer.save()
        form.data['customer'] = new_customer.id
        form.data['new_customer'] = ''
    if form.data.get('new_demurrage_reason'):
        try:
            new_demurrage_reason = DemurrageReason.objects.get(reason__iexact=form.data['new_demurrage_reason'])
        except:
            new_demurrage_reason = DemurrageReason.objects.create(reason=form.data['new_demurrage_reason'])
            new_demurrage_reason.save()
        form.data['demurrage_reason'] = new_demurrage_reason.id
        form.data['new_demurrage_reason'] = ''
    if form.data.get('new_product'):
        try:
            new_product = Product.objects.get(name__iexact=form.data['new_product'])
        except:
            new_product = Product.objects.create(name=form.data['new_product'])
            new_product.save()
        form.data['product'] = new_product.id
        form.data['new_product'] = ''
    return form

@user_passes_test(lambda u:u.is_staff, login_url='/accounts/login/')
def bol_create(request):
    if request.method == 'POST':
        form = BolForm(request.POST.copy())
        # Create custom objects if any were given
        form = _create_bol_objects(form)
        if form.is_valid():
            bol = form.save(commit=False)
            bol.created_by = request.user
            bol.save()
            form = BolForm()
            messages.success(request, 'BOL created successfully.')
    else:
        form = BolForm()

    return render(request, 'drivers/bol_form.html',
                               {'form': form, 'edit': False})

@user_passes_test(lambda u:u.is_staff, login_url='/accounts/login/')
def bol_edit(request, id):
    bol = Bol.objects.get(id=id)
    if bol.created_by != request.user and not (is_member(request.user, 'office') or is_member(request.user, 'shop')):
        messages.error(request, 'You do not have permission to access that BOL.')
        return redirect('bol_create')
    if request.method == 'POST':
        form = BolForm(request.POST.copy(), instance=bol)
        # Create custom objects if any were given
        form = _create_bol_objects(form)
        if form.is_valid():
            bol = form.save(commit=False)
            bol.completed_by = request.user
            bol.completed_at = timezone.now()
            bol.save()
            messages.success(request, 'BOL confirmed successfully.')
            return redirect('dispatch')
    else:
        form = BolForm(instance=bol)

    return render(request, 'drivers/bol_form.html',
                               {'form': form, 'edit': True})

@user_passes_test(lambda u:u.is_staff, login_url='/accounts/login/')
def service_request_create(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)
        problem_formset = ProblemFormSet(request.POST)
        if form.is_valid() and problem_formset.is_valid():
            service_request = form.save(commit=False)
            service_request.created_by = request.user
            service_request.save()
            for image in request.FILES.getlist('image[]'):
                service_image = ServiceRequestImage(service_request=service_request, image=image)
                service_image.save()
            for problem_form in problem_formset:
                if problem_form.is_valid():
                    problem = problem_form.save(commit=False)
                    if problem.problem:
                        problem.service_request = service_request
                        problem.save()
            messages.success(request, 'Service Record created successfully.')
    form = ServiceRequestForm()
    problem_formset = ProblemFormSet()

    return render(request, 'drivers/service_request_form.html',
                               {'form': form, 'problem_formset': problem_formset, 'edit': False})

@user_passes_test(lambda u:u.is_staff, login_url='/accounts/login/')
def service_request_edit(request, id):
    if request.is_ajax() and request.method == 'POST':
        service_request = ServiceRequest.objects.get(id=id)
        if 'stars' in request.POST:
            service_request.priority = request.POST['stars']
        if 'expected_date' in request.POST:
            if request.POST['expected_date']:
                service_request.expected_date_of_arrival = datetime.datetime.strptime(request.POST['expected_date'], '%Y-%m-%d')
        service_request.save()
        in_the_yard = ServiceRequest.objects.get_in_the_yard()
        json_list = []
        for service in in_the_yard:
            work_order_id = None
            if service.work_order:
                work_order_id = service.work_order.id
            formatted_time = service.created_at.astimezone(pytz.timezone(settings.TIME_ZONE)).strftime('%B %-d, %Y, %-I:%M %p').replace('AM', 'a.m.').replace('PM', 'p.m.')
            json_list.append({'created_by': service.created_by.username, 'equipment': service.equipment, 'created_at': formatted_time, 'priority': service.priority, 'work_order': service.work_order_id, 'id': service.id})

        return HttpResponse(json.dumps(json_list), content_type = "application/json")
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        problem_formset = ProblemFormSet(request.POST)
        if form.is_valid() and problem_formset.is_valid():
            service_request = form.save(commit=False)
            service_request.created_by = request.user
            service_request.save()
            for problem_form in problem_formset:
                if problem_form.is_valid():
                    problem = problem_form.save(commit=False)
                    if problem.problem != "":
                        problem.service_request = service_request
                        problem.save()
                    else:
                        problem.delete()
            form = ServiceRequestForm()
            messages.success(request, 'Service Record created successfully.')
    else:
        form = ServiceRequestForm()
        problem_formset = ProblemFormSet()

    return render(request, 'drivers/service_request_form.html',
                               {'form': form, 'problem_formset': problem_formset, 'edit': True})

@user_passes_test(lambda u:u.is_staff, login_url='/accounts/login/')
def mileage_report_create(request):
    if request.method == 'POST':
        form = MileageReportForm(request.POST.copy())
        form = _create_bol_objects(form)
        if form.is_valid():
            mileage_report = form.save(commit=False)
            mileage_report.created_by = request.user
            mileage_report.save()
            form = MileageReportForm()
            messages.success(request, 'Mileage Report created successfully.')
    else:
        form = MileageReportForm()

    return render(request, 'drivers/mileage_report_form.html',
                               {'form': form})

@user_passes_test(lambda u:u.is_staff, login_url='/accounts/login/')
def mileage_report_edit(request, id):
    if request.is_ajax() and request.method == 'POST':
        mileage_report = MileageReport.objects.get(id=id)
        if 'dismiss' in request.POST:
            mileage_report.dismissed_at = timezone.now()
            mileage_report.dismissed_by = request.user
            mileage_report.save()
            return JsonResponse({'status': 'success'})

@user_passes_test(lambda u:u.is_staff, login_url='/accounts/login/')
def contact_list(request):
    users = UserProfile.objects.order_by('user__last_name')
    return render(request, 'drivers/contact_list.html',
                               {'users': users})

@user_passes_test(lambda u:u.is_staff, login_url='/accounts/login/')
def accident_report(request):
    return render(request, 'drivers/accident_report.html',
                               {})

@user_passes_test(lambda u:u.is_staff, login_url='/accounts/login/')
def fuel_pricing(request):
    return render(request, 'drivers/fuel_pricing.html',
                               {})

@user_passes_test(lambda u:u.is_staff, login_url='/accounts/login/')
def trailer_loading_levels(request):
    asphalt_measurements = AsphaltTrailerMeasurement.objects.all().order_by('gross_weight')
    trailers = Trailer.objects.all().order_by('name')
    return render(request, 'drivers/trailer_loading_levels.html',
                              {'asphalt_measurements': asphalt_measurements, 'trailers': trailers})

@user_passes_test(lambda u:u.is_staff, login_url='/accounts/login/')
def move_to_road(request, id):
    service_request = ServiceRequest.objects.get(id=id)
    today = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    future_time = datetime.timedelta(days=7)  # Currently one week out
    service_request.expected_date_of_arrival = today + future_time
    service_request.save()
    return redirect('/shop/services/')
