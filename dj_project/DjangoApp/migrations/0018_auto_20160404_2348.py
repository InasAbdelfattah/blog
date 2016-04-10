# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
import django_counter_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoApp', '0017_auto_20160404_1953'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='comment_count',
            field=django_counter_field.fields.CounterField(default=0),
        ),
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 4, 23, 48, 10, 677507)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 4, 23, 48, 10, 678832)),
        ),
    ]
