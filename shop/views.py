from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.conf import settings
from django.template import RequestContext
from django.contrib.auth.decorators import user_passes_test
from drivers.models import ServiceRequest, ServiceRequestProblem
from django.utils import timezone
from django.contrib import messages
from doubleddistributionapp.helpers import render_to_pdf
from shop.models import WorkOrder, Part
from shop.forms import WorkOrderForm, PartFormSet, MechanicFormSet, WorkPerformedFormSet
from messaging.models import Message, MessageRead
from drivers.forms import ServiceRequestForm, NoExtraProblemFormSet, ProblemFormSet, ServiceRequestImage, ServiceRequestImageFormSet
from itertools import chain
import pytz

@user_passes_test(lambda u:u.is_staff, login_url='/accounts/login/')
def services(request):
    in_the_yard = ServiceRequest.objects.get_in_the_yard()
    on_the_road = ServiceRequest.objects.get_on_the_road()
    completed_services = sorted(chain(ServiceRequest.objects.get_completed(), WorkOrder.objects.get_completed()), key=lambda instance: instance.work_order.completed_at if 'work_order' in dir(instance) else instance.completed_at)
    entered_services = sorted(chain(ServiceRequest.objects.get_entered(), WorkOrder.objects.get_entered()), key=lambda instance: instance.work_order.completed_at if 'work_order' in dir(instance) else instance.completed_at)
    work_orders = WorkOrder.objects.get_new()
    completed_work_orders = WorkOrder.objects.get_completed()
    return render(request, 'shop/services.html',
                              {'in_the_yard': in_the_yard, 'on_the_road': on_the_road,
                               'work_orders': work_orders, 'completed_work_orders': completed_work_orders,
                               'entered_services': entered_services, 'completed_services': completed_services})

@user_passes_test(lambda u:u.is_staff, login_url='/accounts/login/')
def work_order_create(request):
    if request.method == 'POST':
        if request.POST.get("serviceForm"):
            service_request = get_object_or_404(ServiceRequest.objects, id=request.GET['service_request_id'])
            service_form = ServiceRequestForm(request.POST, request.FILES, instance=service_request)
            problem_formset = NoExtraProblemFormSet(request.POST, instance=service_request)
            if service_form.is_valid() and problem_formset.is_valid():
                service_request = service_form.save(commit=False)
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
        else:
            form = WorkOrderForm(request.POST)
            mechanic_formset = MechanicFormSet(request.POST)
            part_formset = PartFormSet(request.POST)
            work_performed_formset = WorkPerformedFormSet(request.POST)
            service_request = None
            problems = None
            work_order = None
            if request.POST.get('service_request'):
                service_request = ServiceRequest.objects.get(id=request.POST['service_request'])
                problems = ServiceRequestProblem.objects.filter(service_request = service_request)
            if form.is_valid() and part_formset.is_valid():
                work_order = form.save(commit=False)
                work_order.created_by = request.user
                work_order.updated_by = request.user
                work_order.save()
                if service_request:
                    service_request.work_order = work_order
                    service_request.save()
                for mechanic_form in mechanic_formset:
                    if mechanic_form.is_valid() and 'mechanic' in mechanic_form.cleaned_data:
                        mechanic = mechanic_form.save(commit=False)
                        mechanic.work_order = work_order
                        mechanic.save()
                for part_form in part_formset:
                    if part_form.is_valid() and part_form.has_changed():
                        part = part_form.save(commit=False)
                        part.work_order = work_order
                        if part_form.cleaned_data['new_part']:
                            try:
                                part.part = Part.objects.get(name__iexact=part_form.cleaned_data['new_part'])
                            except:
                                part.part = Part.objects.create(name=part_form.cleaned_data['new_part'])
                        part.save()
                        # Delete part if one is not entered
                        if not part.part or not part.quantity:
                            part.delete()
                        else:
                            part.save()
                for work_performed_form in work_performed_formset:
                    if work_performed_form.is_valid():
                        work_performed = work_performed_form.save(commit=False)
                        if work_performed.work_performed:
                            work_performed.work_order = work_order
                            work_performed.save()
                        # Delete work performed if removed
                        elif work_performed.id:
                            work_performed.delete()
                if request.POST['save_or_complete'] == 'complete':
                    work_order.completed_by = request.user
                    work_order.completed_at = timezone.now()
                    work_order.save()
                    if service_request:
                        # Send message to driver
                        subject = 'Work Order Completed - %s' % service_request.equipment
                        tz = pytz.timezone(settings.TIME_ZONE)
                        message_text = 'Attached is a copy of the work order completed by <b>%s</b> at <b>%s</b>.<br/><br/>' % (request.user, timezone.now().astimezone(tz).strftime('%d %B %Y - %H:%M'))
                        message_text += render_to_string('shop/work_order_copy.html',
                                          {'form': form, 'service_request': service_request, 'part_formset': part_formset, 'mechanic_formset': mechanic_formset, 'work_order': work_order, 'work_performed_formset': work_performed_formset})
                        message = Message.objects.create(message_from=request.user, subject=subject, message=message_text)
                        message.save()
                        message_read = MessageRead(message=message, to=service_request.created_by)
                        message_read.save()
                messages.success(request, 'Work Order created successfully.')
                return redirect('services')
    service_request = None
    form = WorkOrderForm()
    mechanic_formset = MechanicFormSet()
    part_formset = PartFormSet()
    work_performed_formset = WorkPerformedFormSet()
    work_order = None
    problems = None
    service_form = None
    problem_formset = None
    if request.GET.get('service_request_id'):
        service_request = get_object_or_404(ServiceRequest.objects, id=request.GET['service_request_id'])
        unit_number = service_request.equipment[:255]  # Limit TextField to CharField length of 255
        problems = ServiceRequestProblem.objects.filter(service_request=service_request).exclude(problem='').exclude(problem__isnull=True).order_by('id')
        form = WorkOrderForm(initial={'service_request': service_request, 'unit_number': unit_number})
        if request.user.is_superuser:
            service_form = ServiceRequestForm(instance=service_request)
            problem_formset = NoExtraProblemFormSet(instance=service_request)
    return render(request, 'shop/work_order_form.html',
                              {'form': form,
                               'service_request': service_request,
                               'problems': problems,
                               'part_formset': part_formset,
                               'work_performed_formset': work_performed_formset,
                               'mechanic_formset': mechanic_formset,
                               'work_order': work_order,
                               'service_form': service_form,
                               'problem_formset': problem_formset})

@user_passes_test(lambda u:u.is_staff, login_url='/accounts/login/')
def work_order_edit(request, id):
    work_order = WorkOrder.objects.get(id=id)
    if request.method == 'POST':
        if request.POST.get("serviceForm"):
            service_request = ServiceRequest.objects.get(id=request.POST.get('service_request'))
            work_order.servicerequest = service_request
            work_order.save()
            service_form = ServiceRequestForm(request.POST, request.FILES, instance=service_request)
            problem_formset = NoExtraProblemFormSet(request.POST, instance=service_request)
            if service_form.is_valid() and problem_formset.is_valid():
                service_request = service_form.save(commit=False)
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
            service_request.work_order = work_order
            service_request.save()
        else:
            form = WorkOrderForm(request.POST, instance=work_order)
            mechanic_formset = MechanicFormSet(request.POST, instance=work_order)
            part_formset = PartFormSet(request.POST, instance=work_order)
            work_performed_formset = WorkPerformedFormSet(request.POST, instance=work_order)
            service_request = None
            problems = None
            if request.POST.get('service_request'):
                service_request = ServiceRequest.objects.get(id=request.POST['service_request'])
                problems = ServiceRequestProblem.objects.filter(service_request=service_request).exclude(problem='').exclude(problem__isnull=True).order_by('id')
            if form.is_valid() and mechanic_formset.is_valid() and part_formset.is_valid():
                work_order = form.save(commit=False)
                work_order.updated_by = request.user
                if request.POST['save_or_complete'] == 'complete':
                    work_order.completed_by = request.user
                    work_order.completed_at = timezone.now()
                elif request.POST['save_or_complete'] == 'finish':
                    work_order.finished_by = request.user
                    work_order.finished_at = timezone.now()
                work_order.save()
                if service_request:
                    service_request.work_order = work_order
                    service_request.save()
                for mechanic_form in mechanic_formset:
                    if mechanic_form.is_valid() and 'mechanic' in mechanic_form.cleaned_data:
                        mechanic = mechanic_form.save(commit=False)
                        mechanic.work_order = work_order
                        mechanic.save()
                for part_form in part_formset:
                    if part_form.is_valid() and part_form.has_changed():
                        part = part_form.save(commit=False)
                        part.work_order = work_order
                        if part_form.cleaned_data['new_part']:
                            try:
                                part.part = Part.objects.get(name__iexact=part_form.cleaned_data['new_part'])
                            except:
                                part.part = Part.objects.create(name=part_form.cleaned_data['new_part'])
                        # Delete part if one is not entered
                        if not part.part or not part.quantity:
                            part.delete()
                        else:
                            part.save()
                for work_performed_form in work_performed_formset:
                    if work_performed_form.is_valid():
                        work_performed = work_performed_form.save(commit=False)
                        if work_performed.work_performed:
                            work_performed.work_order = work_order
                            work_performed.save()
                        # Delete work performed if removed
                        elif work_performed.id:
                            work_performed.delete()
                if request.POST['save_or_complete'] == 'complete':
                    if service_request:
                        # Send message to driver
                        tz = pytz.timezone(settings.TIME_ZONE)
                        subject = 'Work Order Completed - %s' % service_request.equipment
                        message_text = 'Attached is a copy of the work order completed by <b>%s</b> at <b>%s</b>.<br/><br/>' % (request.user, timezone.now().astimezone(tz).strftime('%d %B %Y - %H:%M'))
                        message_text += render_to_string('shop/work_order_copy.html',
                                          {'form': form, 'service_request': service_request, 'part_formset': part_formset, 'mechanic_formset': mechanic_formset, 'work_order': work_order, 'work_performed_formset': work_performed_formset})
                        message = Message.objects.create(message_from=request.user, subject=subject, message=message_text)
                        message.save()
                        message_read = MessageRead(message=message, to=service_request.created_by)
                        message_read.save()
                    messages.success(request, 'Work Order completed successfully. <a href="shop/workorder/print/%s/" target="_blank"><b>Print Work Order</b></a>' % work_order.id, extra_tags='safe')
                else:
                    messages.success(request, 'Work Order saved successfully.')
                return redirect('services')
    form = WorkOrderForm(instance=work_order)
    mechanic_formset = MechanicFormSet(instance=work_order)
    part_formset = PartFormSet(instance=work_order)
    work_performed_formset = WorkPerformedFormSet(instance=work_order)
    service_form = None
    problem_formset = None
    try:
        service_request = work_order.servicerequest
        problems = ServiceRequestProblem.objects.filter(service_request=service_request).exclude(problem='').exclude(problem__isnull=True).order_by('id')
    except:
        service_request = None
        problems = None
    if request.user.is_superuser and service_request:
        service_form = ServiceRequestForm(instance=service_request)
        problem_formset = NoExtraProblemFormSet(instance=service_request)

    return render(request, 'shop/work_order_form.html',
                              {'form': form, 'service_request': service_request,
                               'part_formset': part_formset,
                               'work_performed_formset': work_performed_formset,
                               'mechanic_formset': mechanic_formset,
                               'problems': problems,
                               'work_order': work_order,
                               'service_form': service_form,
                               'problem_formset': problem_formset}
                             )

@user_passes_test(lambda u:u.is_staff, login_url='/accounts/login/')
def service_request_print(request, id):
    service_request = ServiceRequest.objects.get(id=id)
    form = ServiceRequestForm(instance=service_request)
    image_formset = ServiceRequestImageFormSet(instance=service_request)
    problem_formset = NoExtraProblemFormSet(instance=service_request)
    uri = request.build_absolute_uri('/')[:-1]
    return render_to_pdf(
            'shop/service_request_print.html',
            {
                'pagesize':'Letter',
                'form': form,
                'image_formset': image_formset,
                'problem_formset': problem_formset,
                'service_request': service_request
            }
        )

@user_passes_test(lambda u:u.is_staff, login_url='/accounts/login/')
def work_order_print(request, id):
    work_order = WorkOrder.objects.get(id=id)
    work_order.printed_by = request.user
    work_order.printed_at = timezone.now()
    work_order.save()
    form = WorkOrderForm(instance=work_order)
    mechanic_formset = MechanicFormSet(instance=work_order)
    part_formset = PartFormSet(instance=work_order)
    work_performed_formset = WorkPerformedFormSet(instance=work_order)
    return render_to_pdf(
            'shop/work_order_print.html',
            {
                'pagesize':'Letter',
                'form': form,
                'work_order': work_order,
                'mechanic_formset': mechanic_formset,
                'part_formset': part_formset,
                'work_performed_formset': work_performed_formset
            }
        )

@user_passes_test(lambda u:u.is_staff, login_url='/accounts/login/')
def work_order_print_batch(request, axon):
    forms = []
    unit_number, axon_number = axon.split('-')
    work_orders = WorkOrder.objects.filter(unit_number=unit_number, axon_number=axon_number)
    if not work_orders:
        messages.error(request, 'No records found with that Unit Number and Axon Work Order Number.')
        return redirect('services')
    for work_order in work_orders:
        work_order.printed_by = request.user
        work_order.printed_at = timezone.now()
        work_order.save()
        form = WorkOrderForm(instance=work_order)
        mechanic_formset = MechanicFormSet(instance=work_order)
        part_formset = PartFormSet(instance=work_order)
        work_performed_formset = WorkPerformedFormSet(instance=work_order)
        forms.append({'work_order': work_order, 'form': form, 'mechanic_formset': mechanic_formset, 'part_formset': part_formset, 'work_performed_formset': work_performed_formset})
    return render_to_pdf(
            'shop/work_order_print_batch.html',
            {
                'pagesize':'Letter',
                'forms': forms
            }
        )
