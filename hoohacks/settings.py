"""
Django settings for hoohacks project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
try:
    from . import secret
except ImportError:
    from . import secret_example as secret
import datetime 
from pytz import timezone

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=)ek5=w3u09$!%g2mbn$ppbpjot1jq2o^f577gxpq&w^yh9txm'

# SECURITY WARNING: don't run with debug turned on in production

ON_HEROKU = 'ON_HEROKU' in os.environ

DEBUG = False if ON_HEROKU else True

# Application definition

INSTALLED_APPS = [
    'channels',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'administration',
    'applications',
    'mentors',
    'users',
    'judging',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hoohacks.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

TEMPLATES[0]['OPTIONS']['context_processors'].append("administration.context_processors.event_name")


MEDIA_ROOT = BASE_DIR + '/media/'

WSGI_APPLICATION = 'hoohacks.wsgi.application'
STATIC_URL = '/static/'
STATIC_ROOT = 'static'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'CONN_MAX_AGE': 500
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

AUTH_USER_MODEL = 'users.User'
LOGIN_URL = '/users/login'
LOGIN_REDIRECT_URL = '/dashboard'

ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD', secret.ADMIN_PASSWORD)
MENTOR_PASSWORD = os.environ.get('MENTOR_PASSWORD', secret.MENTOR_PASSWORD)
JUDGING_PASSWORD = os.environ.get('JUDGING_PASSWORD', secret.JUDGING_PASSWORD)
DROPBOX_ACCESS_TOKEN = os.environ.get('DROPBOX_ACCESS_TOKEN', secret.DROPBOX_ACCESS_TOKEN)
REMIND_URL = os.environ.get('REMIND_URL', secret.REMIND_URL)

MAX_NUMBER_TICKETS = 2
EVENT_NAME = "HooHacks"

TZ = timezone('US/Eastern')
APPLICATION_SUBMISSION_DEADLINE = TZ.localize(datetime.datetime(2019, 11, 20, 23, 59, 59, 0))
APPLICATION_SUBMISSION_DEADLINE_FMT = APPLICATION_SUBMISSION_DEADLINE.strftime("%B %d, %Y %I:%M:%S %Z")

APPLICATION_CONFIRMATION_DEADLINE = TZ.localize(datetime.datetime(2019, 11, 21, 23, 59, 59, 0))
APPLICATION_CONFIRMATION_DEADLINE_FMT = APPLICATION_CONFIRMATION_DEADLINE.strftime("%B %d, %Y %I:%M:%S %Z")

SCHOOLS = []
GRADUATION_YEARS = [2020, 2021, 2022, 2023, 2024, 2025]
RACES = ["African American", "American Indian", "Asian",
    "Hispanic", "Native Hawaiian", "White", "Other"]
GENDERS = ["Male", "Female", "Other", "Prefer not to say"]
TRAVEL_METHODS = ["Car", "Bus", "Train", "Airplane", "Other"]
TSHIRT_SIZES = ["XS", "S", "M", "L", "XL"]
DIETARY_RESTRICTIONS = ["None", "Vegetarian", "Vegan", "Nut Allergy", "Halal", "Other"]
CITIES = ["Pittsburgh", "Washington, DC", "Richmond", "NYC", "Charlottesville"] # Test Cities

f = open(BASE_DIR + "/hoohacks/data/schools.csv", "r")
for school in f:
    SCHOOLS.append(school.strip())
f.close()

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ.get('GMAIL_USERNAME', secret.GMAIL_USERNAME)
EMAIL_HOST_PASSWORD = os.environ.get('GMAIL_PASSWORD', secret.GMAIL_PASSWORD)

f = open(BASE_DIR + "/hoohacks/emails/verify_email.html", "r")
VERIFY_EMAIL = f.read()
f.close()

f = open(BASE_DIR + "/hoohacks/emails/password_reset.html", "r")
PASSWORD_RESET_EMAIL = f.read()
f.close()

f = open(BASE_DIR + "/hoohacks/emails/accepted.html", "r")
ACCEPTED_EMAIL = f.read()
f.close()

f = open(BASE_DIR + "/hoohacks/emails/waitlisted.html", "r")
WAITLISTED_EMAIL = f.read()
f.close()

f = open(BASE_DIR + "/hoohacks/emails/rejected.html", "r")
REJECTED_EMAIL = f.read()
f.close()

f = open(BASE_DIR + "/hoohacks/emails/confirmed.html", "r")
CONFIRMED_EMAIL = f.read()
f.close()

ASGI_APPLICATION = 'hoohacks.routing.application'

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [os.environ.get('REDIS_URL', 'redis://localhost:6379')],
        },
    },
}

PROD_URL = os.environ.get('PROD_URL', 'http://localhost:8000/')

try:
    # Configure Django App for Heroku.
    import django_heroku
    django_heroku.settings(locals())
except ImportError:
    found = False

ALLOWED_HOSTS = [
    PROD_URL,
    "hoohacks-d.herokuapp.com",
    '*'
]
