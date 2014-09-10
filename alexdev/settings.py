"""
Django settings for alexdev project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PRODUCTION_DIR = "/home/http/alexandre.deverteuil.net/alexdev"


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'c8$2^a5+(-p^p&=v(sm0n9kl6-w9achks%ine^1jy1za))dn+c'

if BASE_DIR == PRODUCTION_DIR:
    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = TEMPLATE_DEBUG = False
    ALLOWED_HOSTS = [
        "alexandre.deverteuil.net",
        "localhost",
        "198.58.102.179",
        ]
    ADMINS = (('Alexandre de Verteuil', 'alexandre@deverteuil.net'),)
    MANAGERS = ADMINS
    SERVER_EMAIL = "http@baryon"
    EMAIL_HOST = "alexdev.chickenkiller.net"
    DATABASES = {
        'default': {
            'ENGINE': "django.db.backends.postgresql_psycopg2",
            'NAME': "alexdev",
            'USER': "alexandre.deverteuil.net",
            'PASSWORD': "87a6sdf6g5xcvb67786",
        }
    }
else:
    # Options for the development server.
    DEBUG = True
    TEMPLATE_DEBUG = True
    ALLOWED_HOSTS = []

    # Database
    # https://docs.djangoproject.com/en/1.6/ref/settings/#databases

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.redirects',
    'django.contrib.flatpages',
    'blog',
    'pages',
    'dry_urls',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
)

ROOT_URLCONF = 'alexdev.urls'

WSGI_APPLICATION = 'alexdev.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Montreal'

USE_I18N = True

USE_L10N = True

USE_TZ = False

DATE_FORMAT = "Y-m-d"
DATETIME_FORMAT = "Y-m-d H:i"
TIME_FORMAT = "H:i"


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, "static_root")
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "alexdev/static"),
    )


# Media files
# https://docs.djangoproject.com/en/1.6/topics/files/
# https://docs.djangoproject.com/en/1.6/howto/static-files/#serving-uploaded-files-in-development

MEDIA_ROOT = os.path.join(BASE_DIR, "media_root")
MEDIA_URL = "/media/"


# Sites framework

SITE_ID = 1


# Template directories
# https://docs.djangoproject.com/en/1.6/ref/templates/api/#the-template-dirs-setting

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "alexdev", "templates"),
    )

TEMPLATE_CONTEXT_PROCESSORS = (
    # Defaults:
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    # Non-default:
    "django.core.context_processors.request",
    )
