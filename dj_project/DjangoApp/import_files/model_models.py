from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from pytz import timezone
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django_counter_field import CounterField
from django_counter_field import CounterMixin, connect_counter
from django.conf import settings
from django.contrib import admin
from django.template.defaultfilters import slugify