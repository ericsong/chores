from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from web.models import Group, Chore, ChoresUser

def home(request):
    context = {}
    template = 'home.html'
    return render(request, template, context)

def newuser(request):
    print(request.user)
    print(request.user.id)
    if not ChoresUser.objects.filter(user=request.user).exists():
        newChoresUser = ChoresUser(user=request.user)
        newChoresUser.save()
        return render(request, 'creategroup.html', {})
    else:
        return render(request, 'main.html', {})

def creategroup(request):
    context = {}
    template = 'creategroup.html'
    return render(request, template, context)

def creategroup_submit(request):
    newGroup = Group()
    newGroup.save()

    #update user with newly created group
    current_user = ChoresUser.objects.get(user=request.user);
    current_user.group_id = newGroup.id;
    current_user.save();

    for chore in request.POST.getlist('chores'):
        newChore = Chore(group=newGroup, text=chore)
        newChore.save()

    return render(request, 'addmembers.html', {})

def addmembers(request):
    print(request.POST)
    context = {}
    template = 'main.html'
    return render(request, template, context)

def main(request):
    print(request.POST)
    context = {}
    template = 'main.html'
    return render(request, template, context)

def logout(request):
    auth_logout(request)
    return redirect('/')
