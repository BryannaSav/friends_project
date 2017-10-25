# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import User
from django.contrib import messages
from django.shortcuts import render, redirect
import datetime

def index(request):
    context={
        'date':datetime.datetime.now().strftime ("%Y-%m-%d")
    }
    return render(request, 'login_app/index.html', context)

def register(request):
    errors = User.objects.registerVal(request.POST)
    if len(errors) != 0:
        for error in errors.itervalues():
            messages.error(request, error)
    else:
        User.objects.createUser(request.POST)
        messages.success(request, "User created")
    return redirect('/')

def login(request):
    results = User.objects.loginUser(request.POST)
    if type(results) == dict:
        for error in results.itervalues():
            messages.error(request, error)
        return redirect('/')
    else:
        request.session['name']=results.name
        request.session['alias']=results.alias
        request.session['email']=results.email
        request.session['id']=results.id
        return redirect('/home')

def logout(request):
    request.session.flush()
    return redirect('/')

# Type localhost:8000/clear to reset Userdata

def clear(request):
    User.objects.all().delete()
    return redirect('/')
        

