# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-01 16:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoApp', '0011_auto_20160401_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 1, 16, 32, 20, 319467)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 1, 16, 32, 20, 320798)),
        ),
    ]
