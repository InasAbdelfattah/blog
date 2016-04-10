from django import forms
from django.db import models
from django.contrib import admin
from django.db.models import signals
from django.core.mail import send_mail
from django.contrib.auth.models import User , Group ,Permission
from django.contrib.admin.helpers import ActionForm
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.contrib.admin.views.main import ChangeList
from DjangoApp.models import Article  , UserProfile ,Tag , Comment , LockSystem
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.db.models import Count
from django.contrib.admin.views.main import ChangeList
# from model_utils import Choices
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import UserManager
from django.contrib.contenttypes.models import ContentType
from django.conf.urls import patterns
