# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-06 11:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoApp', '0028_auto_20160406_0721'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='Article_comment_id',
        ),
        migrations.RemoveField(
            model_name='article',
            name='comment_count',
        ),
        migrations.RemoveField(
            model_name='emotion',
            name='Comment_emotion_id',
        ),
        migrations.RemoveField(
            model_name='like',
            name='Comment_like_id',
        ),
        migrations.RemoveField(
            model_name='mark',
            name='Article_mark_id',
        ),
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 6, 11, 15, 17, 751783)),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
