# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-01 12:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoApp', '0009_auto_20160401_1124'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'permissions': ('is_publish', 'is_publish')},
        ),
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 1, 12, 22, 33, 918244)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 1, 12, 22, 33, 919276)),
        ),
    ]
