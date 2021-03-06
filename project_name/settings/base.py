"""
Django settings for {{ project_name }} project.

Generated by 'django-admin startproject' using Django {{ django_version }}.

For more information on this file, see
https://docs.djangoproject.com/en/{{ django_version }}/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/{{ django_version }}/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from genericpath import exists
import os
# Use 12factor inspired environment variables or from a file
import environ

env = environ.Env()
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Static files directories
STATICFILES_DIRS = [
    # os.path.join(BASE_DIR, 'static'),
    # os.path.join(BASE_DIR, 'components'),
]
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'



# Ideally move env file should be outside the git repo
# i.e. BASE_DIR.parent.parent
# env_file = join(BASE_DIR, 'local.env')
env_file = os.path.join(os.path.dirname(__file__), 'local.env')

if exists(env_file):
    environ.Env.read_env(str(env_file))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = env('SECRET_KEY')
SECRET_KEY = '14a+yc0k*6v-e0fu0+sqnqo9jm86tpqv3g49s7ya2p9qvvt8df'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

ALLOWED_HOSTS = []


# Application definition
INSTALLED_APPS = (
    # django admin bootstrapped
    'django_admin_bootstrapped',
    # Native apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    # ThirdParty apps
    'authtools',
    'pipeline',
    'djangobower',
    'rest_framework'
    # Custom apps
)

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

ROOT_URLCONF = '{{ project_name }}.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            # insert more TEMPLATE_DIRS here
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.core.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = '{{ project_name }}.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    # Raises ImproperlyConfigured exception if DATABASE_URL not in
    # os.environ
    'default': env.db()
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'components')

# django-authtools Configurations
AUTH_USER_MODEL = 'authtools.User'

# Django Admin bootstrapped Configuration
# DAB_FIELD_RENDERER = 'django_admin_bootstrapped.renderers.BootstrapFieldRenderer'

# Static files and Pipeline finders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
    'djangobower.finders.BowerFinder',

)
# Pipeline storage
STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage'


# Pipeline Configuration
# CSS Files.
PIPELINE_CSS = {
    # Project libraries.
    'styles': {
        'source_filenames': (
            'bootstrap/dist/css/bootstrap.min.css',
            'animate.css/animate.css',
            'font-awesome/css/font-awesome.min.css',
        ),
        # Compress passed libraries and have
        # the output in`css/libs.min.css`.
        'output_filename': 'css/styles.min.css',
    }
}
# JavaScript files.
PIPELINE_JS = {
    # Project JavaScript libraries.
    'scripts': {
        'source_filenames': (
            'jquery/dist/jquery.js',
            'bootstrap/dist/js/bootstrap.js',
            'bootstrap/js/carousel.js',
        ),
        'output_filename': 'js/scripts.min.js',
    }

}
# Bower components Configurations
BOWER_COMPONENTS_ROOT = os.path.join(BASE_DIR, '')

# Bower Installed apps
BOWER_INSTALLED_APPS = (
    'jquery',
    'underscore'
)
