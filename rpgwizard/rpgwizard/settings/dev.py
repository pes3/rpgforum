# -*- coding: utf-8 -*-

# THIS IS FOR DEVELOPMENT ENVIRONMENT
# DO NOT USE IT IN PRODUCTION

# Create your own dev_local.py
# import * this module there and use it like this:
# python manage.py runserver --settings=rpgwizard.settings.dev_local

from __future__ import unicode_literals

from .base import *
import dj_database_url

DEBUG = True

TEMPLATES[0]['OPTIONS']['debug'] = True
# TEMPLATES[0]['OPTIONS']['string_if_invalid'] = '\{\{%s\}\}'  # Some Django templates relies on this being the default

ADMINS = (('John', 'john@example.com'), )  # Log email to console when DEBUG = False

ALLOWED_HOSTS = ['*', ]

# INSTALLED_APPS.extend([
#    'debug_toolbar',
# ])

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    #'sqlite': {
     #   'ENGINE': 'django.db.backends.sqlite3',
     #   'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
   # }
    
    'default': dj_database_url.config()
}

DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql_psycopg2'

CACHES.update({
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
    'st_rate_limit': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'spirit_rl_cache',
        'TIMEOUT': None
    }
})

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
