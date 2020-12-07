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
TEMPLATES[0]['OPTIONS']['context_processors'].append("administration.context_processors.contact_email")


MEDIA_ROOT = BASE_DIR + '/media/'

WSGI_APPLICATION = 'hoohacks.wsgi.application'
STATIC_URL = '/static/'

if DEBUG:
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static'),
    ]
else:
    STATIC_ROOT = '/app/static'

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
VOLUNTEER_PASSWORD = os.environ.get('VOLUNTEER_PASSWORD', secret.VOLUNTEER_PASSWORD)
JUDGING_PASSWORD = os.environ.get('JUDGING_PASSWORD', secret.JUDGING_PASSWORD)
DROPBOX_ACCESS_TOKEN = os.environ.get('DROPBOX_ACCESS_TOKEN', secret.DROPBOX_ACCESS_TOKEN)

SLACK_ENABLED = os.environ.get('SLACK_ENABLED', secret.SLACK_ENABLED) 
if SLACK_ENABLED == "True":
    SLACK_ENABLED = True
if SLACK_ENABLED != True:
    SLACK_ENABLED = False
SLACK_API_TOKEN = os.environ.get('SLACK_API_TOKEN', secret.SLACK_API_TOKEN)
SLACK_MENTOR_TICKET_CHANNEL = ""
if SLACK_ENABLED:
    SLACK_MENTOR_TICKET_CHANNEL = "G010LQSEU75"
    SLACK_NOTIFICATIONS_CHANNEL = "CSQKP19EC"

TWITTER_ENABLED = os.environ.get('TWITTER_ENABLED', secret.TWITTER_ENABLED) 
if TWITTER_ENABLED == "True":
    TWITTER_ENABLED = True
if TWITTER_ENABLED != True:
    TWITTER_ENABLED = False
TWITTER_CONSUMER_KEY = os.environ.get('TWITTER_CONSUMER_KEY', secret.TWITTER_CONSUMER_KEY)
TWITTER_CONSUMER_SECRET = os.environ.get('TWITTER_CONSUMER_SECRET', secret.TWITTER_CONSUMER_SECRET)
TWITTER_ACCESS_TOKEN = os.environ.get('TWITTER_ACCESS_TOKEN', secret.TWITTER_ACCESS_TOKEN)
TWITTER_ACCESS_TOKEN_SECRET = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET', secret.TWITTER_ACCESS_TOKEN_SECRET)

MAX_NUMBER_TICKETS = 2
EVENT_NAME = os.environ.get('EVENT_NAME', 'HooHacks')

TZ = timezone('US/Eastern')
APPLICATION_SUBMISSION_DEADLINE = TZ.localize(datetime.datetime(2019, 11, 20, 23, 59, 59, 0))
APPLICATION_SUBMISSION_DEADLINE_FMT = APPLICATION_SUBMISSION_DEADLINE.strftime("%B %d, %Y %I:%M:%S %Z")

APPLICATION_CONFIRMATION_DEADLINE = TZ.localize(datetime.datetime(2019, 11, 21, 23, 59, 59, 0))
APPLICATION_CONFIRMATION_DEADLINE_FMT = APPLICATION_CONFIRMATION_DEADLINE.strftime("%B %d, %Y %I:%M:%S %Z")

SCHOOLS = []
GRADUATION_YEARS = [2021, 2022, 2023, 2024, 2025, 2026]
GRADUATION_YEARS_TITLES = {
    "2021": "Senior",
    "2022": "Junior",
    "2023": "Sophomore",
    "2024": "Freshman",
    "2025": "High School Senior",
    "2026": "High School Junior"
}
RACES = ["African American", "American Indian", "Asian",
    "Hispanic", "Native Hawaiian", "White", "Other"]
GENDERS = ["Female", "Male", "Non-binary", "Transgender", "Other", "Prefer not to say"]
TRAVEL_METHODS = ["Car", "Bus", "Train", "Airplane", "Other"]
TSHIRT_SIZES = ["XS", "S", "M", "L", "XL"]
DIETARY_RESTRICTIONS = ["None", "Vegetarian", "Vegan", "Nut Allergy", "Halal", "Gluten Free", "Other"]
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

CONTACT_EMAIL = "travel@hoohacks.io"

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

CARRIER_EMAIL_LOOKUP = {
    'Alltel': '@message.alltel.com',
    'AT&T': '@txt.att.net',
    'Nextel': '@messaging.nextel.com',
    'Sprint': '@messaging.sprintpcs.com',
    'T-Mobile': '@tmomail.net',
    'US Cellular': '@mms.uscc.net',
    'Verizon Wireless': '@vtext.com',
    'Virgin Mobile': '@vmobl.com',
    'Other': ''
}

SENDGRID_HOST = 'smtp.sendgrid.net'
SENDGRID_PORT = 587
SENDGRID_HOST_USER = 'apikey'
SENDGRID_HOST_PASSWORD = os.environ.get('SENDGRID_HOST_PASSWORD', secret.SENDGRID_HOST_PASSWORD)

TEXTING_ENABLED = True

TEXTING_FROM_EMAIL = os.environ.get('TEXTING_FROM_EMAIL', secret.TEXTING_FROM_EMAIL)

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
    if ON_HEROKU:
        try:
            del DATABASES['default']['OPTIONS']['sslmode']
        except:
            pass
        import sentry_sdk
        from sentry_sdk.integrations.django import DjangoIntegration

        sentry_sdk.init(
            dsn=os.environ['SENTRY_DSN'],
            integrations=[DjangoIntegration()]
        )
        SECURE_SSL_REDIRECT = True
        SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
except ImportError:
    found = False

ALLOWED_HOSTS = [
    PROD_URL,
    '*'
]
