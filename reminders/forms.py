from django import forms
from django.forms.models import inlineformset_factory
from django.conf import settings
from django.contrib.auth.models import User
from reminders.models import Reminder
from datetime import datetime
import pytz

class ReminderForm(forms.ModelForm):
    time = forms.CharField()

    def clean_time(self):
        local = pytz.timezone(settings.TIME_ZONE)
        time = datetime.strptime(self.cleaned_data['time'], '%d %B %Y - %H:%M')
        return local.localize(time)

    class Meta:
        model = Reminder
        exclude = ['created_by', 'completed_by', 'users']
