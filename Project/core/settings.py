"""
# twilio code -6GZQNP5VE19GM98LS9KS7EVS
Django settings for core project.

Generated by 'django-admin startproject' using Django 3.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from datetime import timedelta
import os
from pathlib import Path

import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = 'ld6vy!t6f19^gk1h4&i=in^we$0mz@frefxic33l_($e*!kd*j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# export DATABASE_URL="postgres://postgres1:hl8wO7HxW9QLWXOZxa3BNZh5mcW7Ri7r@dpg-cmnpm7ocmk4c738mpnmg-a.singapore-postgres.render.com/kapdb"

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'quiz',
    'django.contrib.postgres',
    'graphene_django',
    'django_ratelimit',
    'rest_framework',
    'gunicorn',
    'rest_framework.authtoken',
    'corsheaders',
    'storages',
    'celery',
    'django_redis',
    'drf_yasg',
    "sslserver",
    "django_prometheus",
    
]
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_PRIVATE_NETWORK = True
CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:3000",  # Replace with the actual origin of your frontend
    "http://localhost:3000",
    # 'http://*'  # Replace with the actual origin of your frontend
]
CORS_ALLOWED_ORIGIN_REGEXES = [
    
]
CORS_ALLOW_HEADERS = [
    ""
    "x-password",
    "X-Requested-With",
      "x-username",
      "accept",
    "Authorization",
    "content-type",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
    "access-control-allow-origin",
        # Add any other custom headers you need to allow
]
SESSIONS_ENGINE='django.contrib.sessions.backends.cache'
# CORS_ALLOW_METHODS  = ("DELETE","GET","OPTIONS","PATCH","POST","PUT")
CSRF_USE_SESSIONS = True
AUTH_USER_MODEL = "quiz.Userkap"
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    # Add other authentication backends as needed
]
SWAGGER_SETTINGS = {
    'DEFAULT_AUTO_SCHEMA_CLASS': 'drf_yasg.inspectors.SwaggerAutoSchema',
}
MIDDLEWARE = [
    "django_prometheus.middleware.PrometheusBeforeMiddleware",
    # 'django_zipkin.middleware.ZipkinMiddleware',
    
    'django.middleware.security.SecurityMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    'django_ratelimit.middleware.RatelimitMiddleware',
    
    'django_referrer_policy.middleware.ReferrerPolicyMiddleware',
    
    "django_prometheus.middleware.PrometheusAfterMiddleware",
    # 
    # 'quiz.middleware.LogEntryMiddleware',
]
ZIPKIN_SERVICE_NAME = 'awesome-service'
CSRF_TRUSTED_ORIGINS = [
    'http://127.0.0.1:3000',  # Replace with the actual origin of your frontend
    'http://localhost:3000',
    'https://kap-test-backend.onrender.com',
    'http://*.127.0.0.1'
    # 'http://*'  # Replace with the actual origin of your frontend
]


REFERRER_POLICY = 'no-referrer'

ROOT_URLCONF = 'core.urls'
CSRF_COOKIE_SECURE = False
CSRF_COOKIE_HTTPONLY = False

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# Amazon S3 settings.
AWS_ACCESS_KEY_ID = 'your-access-key-id'
AWS_SECRET_ACCESS_KEY = 'your-secret-access-key'
AWS_STORAGE_BUCKET_NAME = 'your-s3-bucket-name'
AWS_S3_REGION_NAME = 'your-region' # e.g., us-east-1

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
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'
SECURE_REFERRER_POLICY = "same-origin"

# Database
# # https://docs.djangoproject.com/en/3.1/ref/settings/#databases


DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL')
    )
}

CELERY_BEAT_SCHEDULE = {
    'update-cache-every-30-minutes': {
        'task': 'quiz.tasks.update_top_search_results',
        'schedule': timedelta(minutes=30),
    },
}
REST_FRAMEWORK = {
    "NON_FIELD_ERRORS_KEY": "errors",
    "DEFAULT_AUTHENTICATION_CLASSES": (
        'rest_framework.authentication.BasicAuthentication',
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        
    ),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated"),
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
    'DEFAULT_THROTTLE_RATES': {
        'user': '1000/minute',
          'graphql': '1/minute',  # Adjust the rate as needed
    },
    
}

CACHES = {
    # "default": {
    #     "BACKEND": "django_redis.cache.RedisCache",
    #     "LOCATION": "redis://kappcluster.e55wko.ng.0001.aps1.cache.amazonaws.com:6379",
    #     "OPTIONS": {
    #         "CLIENT_CLASS": "django_redis.client.DefaultClient"
    #     }
    # }
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'kappbackend-cache',
        'TIMEOUT': 60,
    },
    'cachefor': {
        "BACKEND": "django.core.cache.backends.memcached.PyMemcacheCache",
        "LOCATION": "127.0.0.1:11211",
        'TIMEOUT': 60,
    }
}
CACHE_TTL = 60 * 60 * 3
RATELIMIT_USE_CACHE = 'cachefor'

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# SECURE_SSL_REDIRECT = True

# Properly handle proxy headers for HTTPS
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

GRAPHENE = {
    'SCHEMA': 'quiz.schema.schema',
    'DJANGO_OPTIMIZER': {
        'ENABLED': True,
        'MAX_DEPTH': 3,  # Define your maximum allowed depth
    },
}



# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True



REDIRECT_DOMAIN = 'http://127.0.0.1:8000'



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATIC_ROOT = '/static/'
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
