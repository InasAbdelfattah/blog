# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-09 20:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoApp', '0051_auto_20160409_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 9, 20, 0, 59, 856048)),
        ),
        migrations.AlterField(
            model_name='banwords',
            name='word',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 9, 20, 0, 59, 858479)),
        ),
    ]
