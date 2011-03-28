import logging
import os

SECRET_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Mr. Admin', 'info@domain.tld'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'site.sqlite',
    },
}

SITE_NAME='Site'
SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
TIME_ZONE = 'UTC'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = False
USE_L10N = False

MEDIA_ROOT = os.path.join(SITE_ROOT, 'assets')
MEDIA_URL = '/assets/'

STATIC_ROOT = os.path.join(SITE_ROOT, 'assets/contrib')
STATIC_URL = '/assets/contrib/'
ADMIN_MEDIA_PREFIX = '/assets/contrib/admin/'
STATICFILES_DIRS = ()
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATE_DIRS = (os.path.join(SITE_ROOT, 'templates'),)
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
TEMPLATE_CONTEXT_PROCESSORS =(
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
    "context_processors.default"
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = 'urls'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.staticfiles',
    'django_extensions',
    'south',
    'compress',
    'gunicorn',
)

EMAIL_SUBJECT_PREFIX = '[%s] ' % (SITE_NAME,)
DEFAULT_FROM_EMAIL = 'info@domain.tld'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

COMPRESS_CSS = {
    'main': {
        'source_filenames': (
            #'css/reset.css',
            'css/site.css',
        ),
        'output_filename': 'css/site.r?.css',
    },
}
COMPRESS_JS = {
    'main': {
        'source_filenames': (
            'js/csrf.js',
            'js/googleAnalytics.js',
            'js/form.js',
            'js/site.js'
        ),
        'output_filename': 'js/site.r?.js',
    },
}
COMPRESS = True
COMPRESS_VERSION = True
COMPRESS_AUTO = DEBUG

LOGIN_URL = '/login/'
LOGOUT_URL = '/logout/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

try:
    from local_settings import *
except ImportError:
    pass