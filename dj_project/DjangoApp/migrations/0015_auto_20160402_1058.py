# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('DjangoApp', '0014_auto_20160401_1635'),
    ]

    operations = [
        migrations.CreateModel(
            name='like',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='mark',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='reply',
            field=models.ForeignKey(default=1, to='DjangoApp.Comment'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 2, 10, 57, 54, 845963)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 2, 10, 57, 54, 846994)),
        ),
        migrations.AddField(
            model_name='mark',
            name='Article_mark_id',
            field=models.ForeignKey(to='DjangoApp.Comment'),
        ),
        migrations.AddField(
            model_name='mark',
            name='User_mark_id',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='like',
            name='Comment_like_id',
            field=models.ForeignKey(to='DjangoApp.Comment'),
        ),
        migrations.AddField(
            model_name='like',
            name='User_like_id',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
