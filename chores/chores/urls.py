"""chores URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin

urlpatterns = patterns('',
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'web.views.home', name='home'),
    url(r'^main/', 'web.views.main', name='main'),
    url(r'^newuser/', 'web.views.newuser', name='newuser'),
    url(r'^create/group/', 'web.views.creategroup', name='creategroup'),
    url(r'^add/members/', 'web.views.addmembers', name='addmembers'),
    url(r'^logout/$', 'web.views.logout', name='logout'),
)
