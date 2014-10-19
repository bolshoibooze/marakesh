from __future__ import absolute_import

import os.path

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
     ('Arthur Mwai', 'mwaigaryan@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'tours',
        # The following settings are not used with sqlite3:
        'USER': 'siteadmin',
        'PASSWORD': 'siteadmin_53$',
        'HOST': 'localhost',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}


# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['*']

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Africa/Nairobi'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'static/media/')


#MEDIA_ROOT = '/root/marakesh/marakesh/static/media/'


MEDIA_URL = '/static/media/'


#STATIC_ROOT = '/root/marakesh/marakesh/static/'
STATIC_ROOT = os.path.join(os.path.dirname(__file__),'static/')

STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    #os.path.join(os.path.dirname(__file__), 'static'),
)


# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

#Cache Settings
CACHE_BACKEND = 'memcached://127.0.0.1:11211/'

CACHE_MIDDLEWARE_SECONDS = 3600



#default plus additional caches
CACHES = {
  'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'TIMEOUT':60,
    }
}

USE_ETAGS = True
DATE_INPUT_FORMATS = '%d-%m-%Y'


# Make this unique, and don't share it with anybody.
SECRET_KEY = 'nvs9p3!9gysocf@mio&5s#mfe4g7os$ewfkrzc6efo-)w$7!gy'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
)

MIDDLEWARE_CLASSES = (
    #cache
    'django.middleware.cache.UpdateCacheMiddleware',
    #'htmlmin.middleware.HtmlMinifyMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    #'htmlmin.middleware.MarkRequestMiddleware',
    
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    #'django.core.context_processors.csrf',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.RemoteUserMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'yawdadmin.middleware.PopupMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',

)


ROOT_URLCONF = 'marakesh.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'marakesh.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    #'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'yawdadmin',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.sitemaps',
    
    'photos',
    'places',
    'accounts',
    'bookings',
    'packages',
    'yawdadmin',
    'ua_detector',
    
)

AUTH_USER_MODEL = 'accounts.CustomUser'

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

TYPES = (
   ('Peak','Peak'),
   ('High','High'),
   ('Medium','Medium'),
   ('Low','Low')
)

CATEGORIES = (
   ('Full Board','Full Board'),
   ('Half Board','Half Board'),
   ('Bed & Breakfast','Bed & Breakfast')
)

CATEGORY = (
   ('Villa','Villa'),
   ('Hotel','Hotel')
)

GENDER = (
   ('Female','Female'),
   ('Male','Male')
)


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
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
