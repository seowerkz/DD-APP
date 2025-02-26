from messaging.models import MessageRead
from reminders.models import ReminderRead

def messages_processor(request):
    user_messages = None
    if request.user and request.user.is_authenticated:
        user_messages = MessageRead.objects.filter(to=request.user, read__isnull=True)
    return {'user_messages': user_messages}

def reminders_processor(request):
    user_reminders = None
    if request.user and request.user.is_authenticated:
        user_reminders = ReminderRead.objects.filter(user=request.user, read__isnull=True)
    return {'user_reminders': user_reminders}
