# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-05 18:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoApp', '0023_auto_20160405_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 5, 18, 57, 34, 514980)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 5, 18, 57, 34, 516302)),
        ),
    ]
