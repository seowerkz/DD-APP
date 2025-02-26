from django.conf.urls import url

from messaging import views

urlpatterns = [
    url(r'inbox/$', views.inbox, name='inbox'),
    url(r'new/$', views.message_create, name='message_create'),
    url(r'delete/(?P<id>\d+)/$', views.message_delete, name='message_delete'),
    url(r'(?P<id>\d+)/$', views.message_view, name='message_view'),
]
