# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-01 10:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoApp', '0006_auto_20160401_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 1, 10, 18, 43, 681954)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 1, 10, 18, 43, 682906)),
        ),
    ]
