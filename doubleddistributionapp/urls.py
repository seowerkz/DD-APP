from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as django_auth_views
from doubleddistributionapp import views as doubledviews

urlpatterns = [
    url(r'^$', doubledviews.home, name='home'),
    url(r'^accounts/login/', django_auth_views.LoginView.as_view(), name='login'),
    url(r'^accounts/logout/', django_auth_views.logout_then_login, name='logout'),
    url(r'^drivers/', include('drivers.urls')),
    url(r'^office/', include('office.urls')),
    url(r'^shop/', include('shop.urls')),
    url(r'^messaging/', include('messaging.urls')),
    url(r'^reminders/', include('reminders.urls')),
    url(r'^admin/', admin.site.urls),
]
