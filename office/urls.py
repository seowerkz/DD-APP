from django.conf.urls import url

from office import views

urlpatterns = [
    url(r'dispatch/$', views.dispatch, name='dispatch'),
    url(r'mileage/$', views.mileage, name='mileage'),
]
