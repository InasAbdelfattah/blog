# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-01 09:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoApp', '0004_auto_20160401_0900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 1, 9, 2, 45, 874898)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 1, 9, 2, 45, 875924)),
        ),
    ]
