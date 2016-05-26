"""
Django settings for DjangoWebProject project.
"""

from os import path
from shared_files.dishi_config import *
PROJECT_ROOT = path.dirname(path.abspath(path.dirname(__file__)))

DEBUG = True
# TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['dishi-dev.azurewebsites.net', 'localhost']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dishihub',
        'USER': 'postgres',
        'PASSWORD': POSTGRESQL_PASSWORD,
        'HOST': 'localhost',
        'PORT': '',
    }
}
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Africa/Nairobi'


# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = path.join(PROJECT_ROOT, 'static').replace('\\', '/')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    path.join(PROJECT_ROOT, 'assets'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '_k)$lq4hr!56^m%cn@6a+!hzdr^3!*+ww2_rwsg*!*m#ca3ir0'

# # List of callables that know how to import templates from various sources.
# TEMPLATE_LOADERS = (
#     'django.template.loaders.filesystem.Loader',
#     'django.template.loaders.app_directories.Loader',
# )

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.models.Session',
)

ROOT_URLCONF = 'Dishi_Web.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'Dishi_Web.wsgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [path.join(PROJECT_ROOT, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `all auth`
    'django.contrib.auth.backends.ModelBackend',
    # `all auth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend'
)


INSTALLED_APPS = (
 'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'dishi_chef',
    'dishi_auth',
    'dishi_kitchen',
    'dishi_user',
    # third party apps
    'djrill',
    'crispy_forms',
    'crispy_forms_foundation',
    'django_summernote',
    'storages',
    'allauth',
    # allauth accounts'
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.twitter',
    # django activity stream
    'actstream',
    # django postman
    'postman',
)

CRISPY_ALLOWED_TEMPLATE_PACKS = "foundation-5"
CRISPY_TEMPLATE_PACK = 'foundation-5'

# djrill email settings
MANDRILL_API_KEY = MANDRILL_API_KEY
EMAIL_BACKEND = "djrill.mail.backends.djrill.DjrillBackend"
DEFAULT_FROM_EMAIL = DEFAULT_FROM_EMAIL


# django summernote settings
SUMMERNOTE_CONFIG = {
    'width': '100%',
    'height': '250px',
}


SOCIALACCOUNT_PROVIDERS = \
    {
        'facebook': {
            'SCOPE': ['email'],
            'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
            'METHOD': 'oauth2',
            'LOCALE_FUNC': 'path.to.callable'
        }
    }

SITE_ID = 4

SOCIALACCOUNT_QUERY_EMAIL = True
ACCOUNT_ACTIVATION_DAYS = 7
ACCOUNT_EMAIL_VERIFICATION = "none"
ACCOUNT_AUTHENTICATION_METHOD = "username_email"
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3
ACCOUNT_SIGNUP_PASSWORD_VERIFICATION = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = True
EMAIL_CONFIRMATION_SIGNUP = True
ACCOUNT_EMAIL_REQUIRED = True
LOGIN_REDIRECT_URL = '/'
LOGOUT_URL = '/'

ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_LOGOUT_REDIRECT_URL = '/'
SOCIALACCOUNT_AUTO_SIGNUP = True
SOCIALACCOUNT_AVATAR_SUPPORT = ('avatar' in INSTALLED_APPS)


# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
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

# Specify the default test runner.
TEST_RUNNER = 'django.test.runner.DiscoverRunner'

# django activity stream settings
ACTSTREAM_SETTINGS = {
    'MANAGER': 'actstream.managers.ActionManager',
    'FETCH_RELATIONS': True,
}
