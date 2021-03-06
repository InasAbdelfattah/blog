"""
Django settings for DjangoProject project.

Generated by 'django-admin startproject' using Django 1.9.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
from django.conf import settings
from django.conf.urls.static import static
from django.utils.module_loading import import_module

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'a@mwd78j1qjg9-u9nn$$hwyh5myjavd@@ytlot08(cty81!zdb'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
#SITE_ID = 1

AUTHENTICATION_BACKENDS = (
# Needed to login by username in Django admin, regardless of `allauth`
'django.contrib.auth.backends.ModelBackend',
# `allauth` specific authentication methods, such as login by e-mail
'allauth.account.auth_backends.AuthenticationBackend',

)
ALLOWED_HOSTS = []

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS= True
EMAIL_PORT = 587
EMAIL_HOST_USER='DjangoITI@gmail.com'
EMAIL_HOST_PASSWORD='iti123456'



# Application definition

INSTALLED_APPS = [
    'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_counter_field',
    'DjangoApp',
    'password_reset',
    'captcha',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',

]

# AUTH_USER_MODEL = 'accounts.UserProfile'

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'DjangoProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['template'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'DjangoProject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Blogd',
        'USER':"root",
        'PASSWORD':'iti',
        'HOST':'localhost'
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

AUTH_PROFILE_MODULE = 'DjangoApp.UserProfile'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
# SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_AGE = 360*12
DEFAULT_FROM_EMAIL = 'Your Name '
##Captcha

RECAPTCHA_PUBLIC_KEY = '6Lfs_RwTAAAAALhskMK5bmlhLF_kVi6UzqVbi3aF'
RECAPTCHA_PRIVATE_KEY = '6Lfs_RwTAAAAAB5_uZIyJBxsUNiBmNtMGUO4FX7B'
RECAPTCHA_USE_SSL = True
# NOCAPTCHA = True
#RECAPTCHA_PROXY = 'http://127.0.0.1:8000'

TEMPLATE_CONTEXT_PROCESSORS = [
    'django.core.context_processors.request',
]
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
LOGIN_URL='/login/'
LOGOUT_URL='/logout/'
LOGIN_REDIRECT_URL = '/'
# LOGOUT_REDIRECT_URL ='/'


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    os.path.join(BASE_DIR, "static/css"),
]
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_cdn")
MEDIA_URL = '/images/user/'
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "/media/")
CRISPY_TEMPLATE_PACK = 'bootstrap3'


SOCIAL_AUTH_FACEBOOK_KEY = '191280037921935'
SOCIAL_AUTH_FACEBOOK_SECRET = 'ea423033cb2f86de768aa3db5175a6d1'

SOCIALACCOUNT_PROVIDERS = {
 'facebook': {
            'SCOPE': ['email', 'user_friends','public_profile'],
            'AUTH_PARAMS': { 'auth_type': 'reauthenticate' },
            'METHOD': 'oauth2'  # instead of 'oauth2'
 }
}

SITE_ID = 2

LOGIN_REDIRECT_URL = '/'
