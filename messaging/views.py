from django.shortcuts import render, redirect
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.decorators import user_passes_test
from messaging.models import Message, MessageRead
import datetime

@user_passes_test(lambda u:u.is_staff, login_url='/accounts/login/')
def inbox(request):
    all_messages = MessageRead.objects.filter(to=request.user, deleted_at__isnull=True, message__created_at__gte=timezone.now()-datetime.timedelta(days=30)).order_by('-message__created_at')
    return render(request, 'messaging/inbox.html',
                              {'all_messages': all_messages})

@user_passes_test(lambda u:u.is_staff, login_url='/accounts/login/')
def message_create(request):
    message_to = []
    message = ''
    users_to = None
    subject = None
    if request.method == 'POST':
        if 'message_to' in request.POST:
            user_from = request.user
            message = request.POST['message']
            users_to = request.POST.getlist('message_to')
            subject = request.POST['subject']
            if '-1' in users_to:
                users_send = User.objects.filter(groups__name='driver').exclude(id=request.user.id)
            else:
                users_send = User.objects.filter(id__in=request.POST['message_to']).exclude(id=request.user.id)
            if users_send and message:
                message = Message.objects.create(message_from=user_from, subject=subject, message=message)
                message.save()
                for user in users_send:
                    message_read = MessageRead(message=message, to=user)
                    message_read.save()
                users_to = None
                message = None
                subject = None
                messages.success(request, 'Message sent successfully.')
            elif not users_send:
                messages.error(request, 'Missing a recipient.')
            elif not message:
                messages.error(request, 'Missing a message.')
            else:
                messages.error(request, 'Missing a recipient or a message.')
        else:
            messages.error(request, 'Missing a recipient.')
    return render(request, 'messaging/message_form.html',
                              {'users': User.objects.all(), 'message_to': message_to, 'message': message, 'users_to': users_to, 'subject': subject, 'edit': True})

@user_passes_test(lambda u:u.is_staff, login_url='/accounts/login/')
def message_view(request, id):
    message = MessageRead.objects.get(message__id=id, to=request.user)
    if message.to != request.user:
        messages.error(request, 'You do not have permission to view that message.')
        return redirect('inbox')
    if not message.read:
        message.read = timezone.now()
        message.save()
    return render(request, 'messaging/message_form.html',
                              {'message': message, 'edit': False})

@user_passes_test(lambda u:u.is_staff, login_url='/accounts/login/')
def message_delete(request, id):
    message = MessageRead.objects.get(message__id=id, to=request.user)
    if message.to != request.user:
        messages.error(request, 'You do not have permission to delete that message.')
        return redirect('inbox')
    if not message.deleted_at:
        message.deleted_at = timezone.now()
        message.save()
    messages.success(request, 'Message moved to trash.')
    return redirect('inbox')
