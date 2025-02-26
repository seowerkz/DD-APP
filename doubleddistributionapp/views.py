from django.shortcuts import render, redirect
from django.template import RequestContext
from django.contrib.auth import logout
from django.contrib.auth.decorators import user_passes_test
from doubleddistributionapp.helpers import is_member

@user_passes_test(lambda u:u.is_staff, login_url='/accounts/login/')
def home(request):
    if is_member(request.user, 'office'):
        return redirect('dispatch')
    if is_member(request.user, 'driver'):
        return redirect('service_request_create')
    if is_member(request.user, 'shop'):
        return redirect('services')
    return render(request, 'index.html',
                               {})

def logout_user(request):
    logout(request)
    return redirect('home')
