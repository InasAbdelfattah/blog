# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-08 14:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoApp', '0032_auto_20160406_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 8, 14, 27, 23, 814230)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 8, 14, 27, 23, 815417)),
        ),
    ]
