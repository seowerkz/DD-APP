from django.conf.urls import url

from drivers import views

urlpatterns = [
    url(r'bol/add/$', views.bol_create, name='bol_create'),
    url(r'bol/edit/(?P<id>\d+)/$', views.bol_edit, name='bol_edit'),
    url(r'request/add/$', views.service_request_create, name='service_request_create'),
    url(r'request/edit/(?P<id>\d+)/$', views.service_request_edit, name='service_request_edit'),
    url(r'mileage/add/$', views.mileage_report_create, name='mileage_report_create'),
    url(r'mileage/edit/(?P<id>\d+)/$', views.mileage_report_edit, name='mileage_report_edit'),
    url(r'contact/$', views.contact_list, name='contact_list'),
    url(r'accident/$', views.accident_report, name='accident_report'),
    url(r'trailer_loading_levels/$', views.trailer_loading_levels, name='trailer_loading_levels'),
    url(r'move_to_road/(?P<id>\d+)/$', views.move_to_road, name='move_to_road'),
    url(r'fuel-pricing/$', views.fuel_pricing, name='fuel_pricing')
]
