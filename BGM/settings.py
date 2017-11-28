"""
Django settings for BGM project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import psycopg2
import dj_database_url

if os.path.isfile(os.path.dirname(os.path.realpath(__file__)) + '/secret_settings.py'):
    from secret_settings import *
elif 'SECRET_KEY' in os.environ:
    SECRET_KEY = os.getenv('SECRET_KEY')

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'upeqe3&yvyg6ff8x3v8h*+s6i^wc@i)yb_6v!8!7cgi=bkw5zc'

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = True

#TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']

# Once logged in redirect to the home page
LOGIN_REDIRECT_URL = '/'

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
)

ROOT_URLCONF = 'BGM.urls'

WSGI_APPLICATION = 'BGM.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = { } 
if 'DATABASE_URL' in os.environ:
    DATABASES['default'] = dj_database_url.config(default=os.getenv('DATABASE_URL'))
else:
    DATABASES['default'] = dj_database_url.config(default=DATABASE_URL)

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
#STATIC_URL = '/static/'
#STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")];

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

##### BEGIN ORIG ###
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
#STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
#STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
#STATICFILES_DIRS = (
##    os.path.join(PROJECT_ROOT, 'static'),
#    os.path.join(PROJECT_ROOT, 'staticfiles'),
#)

##### END ORIG ###


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
#STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'staticfiles'),
)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'




#Template location

#TEMPLATE_DIRS = (
#    os.path.join(PROJECT_ROOT, 'templates'),
#                  )


TEMPLATES = [
{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [os.path.join(BASE_DIR, 'BGM', 'templates')],
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',

        ],
    },
},] 
