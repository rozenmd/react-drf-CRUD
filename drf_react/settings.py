import os

PROJECT_APP_PATH = os.path.dirname(os.path.abspath(__file__))
PROJECT_APP = os.path.basename(PROJECT_APP_PATH)
PROJECT_ROOT = BASE_DIR = os.path.dirname(PROJECT_APP_PATH)

SECRET_KEY = '123'  # os.environ.get('DJANGO_SECRET_KEY')
DEBUG = False

ALLOWED_HOSTS = []

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # third party apps
    'rest_framework',
    'rest_framework.authtoken',
    'allauth',
    'allauth.account',

    'rest_auth',
    'rest_auth.registration',

    'webpack_loader',
    # local apps
    'api',
)
SITE_ID = 1


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'drf_react.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'drf_react.wsgi.application'

####
# DATABASE
####

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

####
# INTERNATIONALIZATION
####

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

####
# STATIC FILES
####

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'assets'),
)

####
# WEBPACK
####

WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'bundles/',
        'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.json'),
    }
}

f = os.path.join(PROJECT_APP_PATH, "local_settings.py")
if os.path.exists(f):
    import sys
    import imp

    module_name = "%s.local_settings" % PROJECT_APP
    module = imp.new_module(module_name)
    module.__file__ = f
    sys.modules[module_name] = module
    exec (open(f, "rb").read())
