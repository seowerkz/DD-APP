from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.contrib import messages
from django.template import RequestContext
from django.http import HttpResponse
from django.utils import timezone
from reminders.models import Reminder, ReminderRead
from reminders.forms import ReminderForm
import json

@user_passes_test(lambda u:u.is_staff, login_url='/accounts/login/')
def reminder_list(request):
    upcoming_reminders = Reminder.objects.filter(time__gte=timezone.now())
    past_reminders = Reminder.objects.filter(time__lt=timezone.now())
    return render(request, 'reminders/reminders.html',
                              {'upcoming_reminders': upcoming_reminders, 'past_reminders': past_reminders})

@user_passes_test(lambda u:u.is_staff, login_url='/accounts/login/')
def reminder_new(request):
    if request.method == 'POST':
        form = ReminderForm(request.POST)
        if form.is_valid():
            reminder = form.save(commit=False)
            reminder.created_by = request.user
            reminder.save()
            users = User.objects.filter(groups__name='shop')
            for user in users:
                rr = ReminderRead(reminder=reminder, user=user)
                rr.save()
            messages.success(request, 'Message sent successfully.')
            return redirect('reminder_list')
    else:
        form = ReminderForm()
    return render(request, 'reminders/reminder_form.html',
                              {'form': form})

@user_passes_test(lambda u:u.is_staff, login_url='/accounts/login/')
def reminder_edit(request, id):
    reminder = Reminder.objects.get(id=id)
    if request.method == 'POST':
        form = ReminderForm(request.POST, instance=reminder)
        if form.is_valid():
            reminder = form.save(commit=False)
            reminder.created_by = request.user
            reminder.save()
            users = User.objects.filter(groups__name='shop')
            for user in users:
                rr = ReminderRead(reminder=reminder, user=user)
                rr.save()
            messages.success(request, 'Message sent successfully.')
            return redirect('reminder_list')
    else:
        form = ReminderForm(instance=reminder)
    return render(request, 'reminders/reminder_form.html',
                              {'form': form})

@user_passes_test(lambda u:u.is_staff, login_url='/accounts/login/')
def reminder_read(request):
    if request.is_ajax() and request.method == 'POST':
        reminder = ReminderRead.objects.get(id=request.POST['id'])
        reminder.read = timezone.now()
        reminder.save()
        return HttpResponse(json.dumps('success'), content_type = "application/json")
