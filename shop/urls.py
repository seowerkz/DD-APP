from django.conf.urls import url

from shop import views

urlpatterns = [
    url(r'services/$', views.services, name='services'),
    url(r'services/print/(?P<id>\d+)/$', views.service_request_print, name='service_request_print'),
    url(r'workorder/add/$', views.work_order_create, name='work_order_create'),
    url(r'workorder/edit/(?P<id>\d+)/$', views.work_order_edit, name='work_order_edit'),
    url(r'workorder/print_batch/(?P<axon>\w+(?:-\w+)+)/$', views.work_order_print_batch, name='work_order_print_batch'),
    url(r'workorder/print/(?P<id>\d+)/$', views.work_order_print, name='work_order_print'),
]
