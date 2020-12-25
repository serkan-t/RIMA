"""
Django settings for interest_miner_api project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 's%@4^(t8&xdlj(nzd3(wnk1czjbf@^jhz24_od8&^)o!6jic_f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True if os.environ.get("DOCKER_ENV") else True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_celery_beat',
    'django_celery_results',
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    'common',
    'accounts',
    'interests',
    'drf_yasg',
]


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        
    ],
    #This line needs to be commented only for conference Insights and doesn't work with docker at the moment
    #'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAuthenticated',),
}

CORS_ORIGIN_ALLOW_ALL = True

AUTH_USER_MODEL = "accounts.User"


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'interest_miner_api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ]
        },
    }
]

WSGI_APPLICATION = 'interest_miner_api.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DOCKER = bool(os.environ.get("DOCKER_ENV", False))

if DOCKER:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'interest_miner_db',
            'USER': 'interest_miner',
            'PASSWORD': 'interest_miner',
            'HOST': 'db',
            'PORT': 5432,
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'
    },
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


TWITTER_FETCH_DAYS = int(
    os.environ.get("TWITTER_FETCH_DAYS", 180)
)  # No of days for which the tweets needs to be imported

# Celery settings
REDIS_HOST = os.environ.get("REDIS_HOST", "localhost")
CELERY_BROKER_URL = 'redis://{}:6379'.format(REDIS_HOST)
CELERY_RESULT_BACKEND = 'redis://{}:6379'.format(REDIS_HOST)
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = TIME_ZONE
CELERYD_TASK_SOFT_TIME_LIMIT = 60 * 60  # 1 hour timeout

# preload data models
# if bool(os.environ.get("PRELOAD_GLOVE_MODEL", False)) and os.environ.get("BACKGROUND_ENV") == "web":
#     from interests.Semantic_Similarity.Word_Embedding.data_models import glove_model

SWAGGER_SETTINGS = {
    "USE_SESSION_AUTH": False,
}
