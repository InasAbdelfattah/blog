# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-09 16:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoApp', '0042_auto_20160409_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 9, 16, 17, 14, 681127)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 9, 16, 17, 14, 683635)),
        ),
    ]
