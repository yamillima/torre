# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='search',
            name='jobsid',
            field=models.TextField(default=0),
        ),
        migrations.AlterField(
            model_name='search',
            name='text',
            field=models.CharField(max_length=500),
        ),
    ]
