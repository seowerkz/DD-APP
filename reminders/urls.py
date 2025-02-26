from django.conf.urls import url
from reminders import views

urlpatterns = [
    url(r'list/$', views.reminder_list, name='reminder_list'),
    url(r'new/$', views.reminder_new, name='reminder_new'),
    url(r'edit/(?P<id>\d+)/$', views.reminder_edit, name='reminder_edit'),
    url(r'read/$', views.reminder_read, name='reminder_read'),
]
