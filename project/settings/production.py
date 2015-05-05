# SECURITY WARNING: keep these keys secret! Use env variables in Heroku.
from django.conf import settings
import os

DEBUG = False

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')  
TWITTER_CONSUMER_KEY = os.environ.get('TWITTER_CONSUMER_KEY')  
TWITTER_CONSUMER_SECRET = os.environ.get('TWITTER_CONSUMER_SECRET')  
TWITTER_ACCESS_TOKEN = os.environ.get('TWITTER_ACCESS_TOKEN')  
TWITTER_ACCESS_TOKEN_SECRET = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')  

import dj_database_url
DATABASES = settings.DATABASES
DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']