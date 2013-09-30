# Django settings for cloudywatch project.
import sys
import os

def rel(*x):
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)

sys.path.insert(0, rel('..','lib'))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Error', 'error@code-on.be'),
)

MANAGERS = ADMINS


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': rel('database.sqlite')
    }
}

TIME_ZONE = 'America/Chicago'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1
USE_I18N = False
USE_L10N = True

MEDIA_ROOT = rel('..', 'files', 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = rel('..', 'files', 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    rel('static'),
)

SECRET_KEY = '1xrw3xlzdyu_s$qxdr84a6aen&lr$lai59txZx$#&b4v5&1*lf'


MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'cloudywatch.urls'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth', 
    'django.core.context_processors.debug', 
    'django.core.context_processors.i18n', 
    'django.core.context_processors.media', 
    'django.core.context_processors.static', 
    'django.core.context_processors.request', 
    'django.core.context_processors.tz', 
    'django.contrib.messages.context_processors.messages',
)

TEMPLATE_DIRS = (
    rel('templates'),
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    #'sorl.thumbnail',
    'staging',
    
    'apps',
    'pingdom',
)


FIXTURE_DIRS = (
    rel('fixtures'),
)

PINGDOM_API_KEY = 'xce4pti219pxnf2zehzfb4luidpuqizf'
PINGDOM_EMAIL = 'gregdingle@yahoo.com'
PINGDOM_PASSWORD = 'cloudywatch'

try:
    from settings_local import *
except ImportError:
    pass
