import logging
import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# E-mail config
if DEBUG:
	EMAIL_PORT = 1025
	
if DEBUG == True:
	CACHE_BACKEND = 'dummy:///'

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))

# Location of project directory.
SITE_ROOT = os.path.realpath(os.path.dirname(__file__))

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(SITE_ROOT, 'assets')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/assets/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Primary templates directory.
TEMPLATE_DIRS = (os.path.join(SITE_ROOT, 'templates'),)

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
		'NAME': 'site.db',						# Or path to database file if using sqlite3.
		'USER': '',						 # Not used with sqlite3.
		'PASSWORD': '',					 # Not used with sqlite3.
		'HOST': '',						 # Set to empty string for localhost. Not used with sqlite3.
		'PORT': '',						 # Set to empty string for default. Not used with sqlite3.
	}
}

# Logging Configuration
logging.basicConfig(
	level = logging.DEBUG,
	format = '%(asctime)s %(levelname)s %(message)s',
	filename = os.path.join(SITE_ROOT, 'site.log'),
	filemode = 'a',
)

# djanog-compress settings.
# Insert link or script tags for compressed JS/CSS files - must run ./manage.py synccompress
# If false, this inserts the uncompressed version. Use this in development.
COMPRESS = False

# Add version strings to compressed files
COMPRESS_VERSION = True

# Automatically generate new compressed JS and CSS files without running synccompress - only use this in DEV
COMPRESS_AUTO = DEBUG

# Uncomment to add a debug toolbar if in DEBUG mode - requires debug_toolbar
# Add the debug toolbar if in debug mode
#if DEBUG == True:
#	MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES+('debug_toolbar.middleware.DebugToolbarMiddleware',)
#	INTERNAL_IPS = ('127.0.0.1',)
#	INSTALLED_APPS = INSTALLED_APPS + ('debug_toolbar',)