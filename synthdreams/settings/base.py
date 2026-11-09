"""
SYNTH DREAMS SETTINGS
"""

import os

from django.core.exceptions import ImproperlyConfigured

# Project root (where manage.py lives); build paths with BASE_DIR.child(...)
from unipath import Path
BASE_DIR = Path(__file__).ancestor(3)


# Config read from environment variables (locally they come from .env via Docker Compose)

def get_env(name, default=None):
    value = os.environ.get(name, default)
    if value is None:
        raise ImproperlyConfigured("Environment variable %s is not set" % name)
    return value


def get_env_list(name, default=''):
    return [item.strip() for item in get_env(name, default).split(',') if item.strip()]


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_env('DJANGO_SECRET_KEY')

DEBUG = get_env('DJANGO_DEBUG', '0') == '1'

ALLOWED_HOSTS = get_env_list('DJANGO_ALLOWED_HOSTS')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': get_env('POSTGRES_DB'),
        'USER': get_env('POSTGRES_USER'),
        'PASSWORD': get_env('POSTGRES_PASSWORD'),
        'HOST': get_env('POSTGRES_HOST', 'db'),
        'PORT': get_env('POSTGRES_PORT', '5432'),
    }
}



# Application definition

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)
LOCAL_APPS = (
    'apps.pages',
    'apps.galleries',
)
THIRD_PARTY_APPS = (
    'modeltranslation',
    'webpack_loader',
    'ckeditor',
    'adminsortable',
    'autoslug',
    'solo',
    'model_clone',
    'cookielaw',
)

INSTALLED_APPS = THIRD_PARTY_APPS + DJANGO_APPS + LOCAL_APPS 

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'synthdreams.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        'DIRS': [BASE_DIR.child('templates')],

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

WSGI_APPLICATION = 'synthdreams.wsgi.application'





# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'es'

LANGUAGES = (
    ('es', 'Spanish'),
    ('en', 'English'),
)

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True



# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



# Static files (CSS, JavaScript, images) and media
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]
STATIC_ROOT = BASE_DIR.child('staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')



# Webpack loader

WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'bundles/',
        'STATS_FILE': BASE_DIR.child('webpack-stats.json'),
    }
}



# CKEditor config

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Format'],
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Table'],
            ['Link', 'Unlink'],
            ['RemoveFormat', 'Source'],
        ],
        'format_tags': 'p;h2;h3;pre'
    },
    'simple_edit': {
        'toolbar': 'Custom2',
        'toolbar_Custom2': [
            ['Bold', 'Italic', 'Underline'],
            ['Link', 'Unlink'],
            ['RemoveFormat', 'Source'],
        ],
        'height': 120,
        'autoParagraph': False
    },
    'simplest': {
        'toolbar': 'Basic',
        'height': 90,
        'autoParagraph': False
    },
}