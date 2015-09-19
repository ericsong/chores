from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout

def home(request):
    context = {}
    template = 'home.html'
    return render(request, template, context)

def members(request):
    context = {}
    template = 'members.html'
    return render(request, template, context)

def logout(request):
    auth_logout(request)
    return redirect('/')
