from django.contrib.auth.models import User
from django.db import models

class Group(models.Model):
    created = models.DateTimeField(auto_now_add=True)

class Chore(models.Model):
    group = models.ForeignKey(Group)
    text = models.CharField(max_length=20)
    desc = models.CharField(max_length=200, default='')

class ChoresUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, blank=True, null=True)
