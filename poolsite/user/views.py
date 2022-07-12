from gc import get_objects
from django.shortcuts import render , get_object_or_404 , redirect
from django.contrib.auth.decorators import   login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404
# Create your views here.
from django.views.generic  import *
from django.http import JsonResponse,HttpResponseRedirect
from django.core import serializers
from django.urls import reverse
from json import dumps
from pathlib import Path
import os
from .forms import *
from .models import *





"""
    USER VEIWS
"""
def user_view(request):

    if request.method == "POST":
        form = PoolForm(request.POST)
        if form.is_valid():
            source = form.cleaned_data.get("Source").strip()
            destination = form.cleaned_data.get("Destination").strip() 

            drivers_obj = Driver.objects.filter(source = source, destination=destination)
            form = PoolForm()
            template_name = 'userview.html'
            context = {"form" : form, "driver_list" : drivers_obj }
            return render(request,template_name,context)
    else:
        form = PoolForm()
        template_name = 'userview.html'
        context = {"form" : form }
        return render(request,template_name,context)


def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():

            # user = form.save(commit=False)
            # user.save()
            return redirect('/user/user_view')
    else:
        form = UserLoginForm()
        context = {"form" : form }
        template_name = "user/login.html"
        return render(request,template_name, context)

def user_register(request):
    print(" \n\n\n user view called for registeration", request)
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            print("\n\n\n\n\nuser -- ", user.source)
            user.save()
            return redirect('/user/user_view')
            # new_user = form.save(commit=False)
            # profile = Profile(username=new_user.username, user_email=new_user.email)
            # profile.save()
            # new_user.save()
            # user = authenticate(request,username=form.cleaned_data["username"] ,password=form.cleaned_data["password1"])            
            # login(request,user)
            # return redirect("/")
    else:
        form = UserRegistrationForm()
        context = {"form" : form }
        template_name = "user/register.html"
        return render(request,template_name, context)




"""
    DRIVER's VIEWS
"""
def driver_view(request):
    template_name = 'driverview.html'
    drivers = Driver.objects.all()
    context = {'object_list': drivers}
    return render(request,template_name,context)





def driver_login(request):
    template_name = 'userview.html'
    userabc = Userprof.objects.all()
    context = {'object_list': userabc}
    return render(request,template_name,context)

def driver_register(request):
    template_name = 'userview.html'
    userabc = Userprof.objects.all()
    context = {'object_list': userabc}
    return render(request,template_name,context)