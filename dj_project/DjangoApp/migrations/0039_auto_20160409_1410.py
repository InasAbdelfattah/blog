# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-09 14:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoApp', '0038_auto_20160409_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 9, 14, 10, 38, 559150)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 9, 14, 10, 38, 561558)),
        ),
    ]
