from __future__ import unicode_literals
from django.shortcuts import render, redirect
from ..login_app.models import User
from django.contrib import messages

def home(request):
    if 'alias' not in request.session:
        return redirect('/')
    if len(User.objects.get(id=request.session['id']).friends.all()) == 0:
        messages.error(request, "You don't have any friends yet :(")
    context={
        'users':User.objects.exclude(id=request.session['id']),
        'you':User.objects.get(id=request.session['id']),
    }
    return render(request, 'home_app/home.html', context)

def addFriend(request, id):
    user1=User.objects.get(id=request.session['id'])
    user2=User.objects.get(id=id)
    user1.friends.add(user2)
    user2.friends.add(user1)
    return redirect('/home')

def removeFriend(request, id):
    user1=User.objects.get(id=request.session['id'])
    user2=User.objects.get(id=id)
    user1.friends.remove(user2)
    user2.friends.remove(user1)
    return redirect('/home')

def show(request, id):
    context={
        'user':User.objects.get(id=id),
    }
    return render(request, 'home_app/show.html', context)



