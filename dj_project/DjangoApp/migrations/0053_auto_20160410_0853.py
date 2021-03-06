# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-10 08:53
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoApp', '0052_auto_20160409_2001'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='is_like',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='mark',
            name='is_mark',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 10, 8, 53, 31, 735877)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 10, 8, 53, 31, 738237)),
        ),
    ]
