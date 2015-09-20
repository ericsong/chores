# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChoresUser',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
            ],
        ),
        migrations.AlterField(
            model_name='chore',
            name='desc',
            field=models.CharField(max_length=200, default=''),
        ),
        migrations.AlterField(
            model_name='group',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AddField(
            model_name='choresuser',
            name='group',
            field=models.ForeignKey(to='web.Group'),
        ),
        migrations.AddField(
            model_name='choresuser',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
