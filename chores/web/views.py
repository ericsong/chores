from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout

def home(request):
    context = {}
    template = 'home.html'
    return render(request, template, context)

def creategroup(request):
    context = {}
    template = 'creategroup.html'
    return render(request, template, context)

def addmembers(request):
    context = {}
    template = 'addmembers.html'
    return render(request, template, context)

def main(request):
    context = {}
    template = 'main.html'
    return render(request, template, context)

def logout(request):
    auth_logout(request)
    return redirect('/')
