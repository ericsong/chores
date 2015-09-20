# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20150920_0435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choresuser',
            name='group',
            field=models.ForeignKey(blank=True, null=True, to='web.Group'),
        ),
    ]
