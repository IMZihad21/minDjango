from decouple import config
from datetime import timedelta
from django.core.management.utils import get_random_secret_key
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_DIR = BASE_DIR.joinpath("static")
TEMPLATE_DIR = BASE_DIR.joinpath("templates")

# Environment configurations
SECRET_KEY = config("SECRET_KEY", default=get_random_secret_key())
ON_PRODUCTION = config("ON_PRODUCTION", default=False, cast=bool)

# Database configurations
DB_ENGINE = config("DB_ENGINE", default="postgresql")
DB_NAME = config("DB_NAME", default="dbname")
DB_USER = config("DB_USER", default="dbuser")
DB_PASSWORD = config("DB_PASSWORD", default="dbpassword")
DB_HOST = config("DB_HOST", default="localhost")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG", default=True, cast=bool)

ALLOWED_HOSTS = ["*"]

# Django built-in apps
DJANGO_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.staticfiles",
]

# Third Party apps
THIRD_PARTY_APPS = ["graphene_django"]

# User defined apps
USER_APPS = []

# Django built-in middleware
DJANGO_MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
]

# Third Party middleware
THIRD_PARTY_MIDDLEWARE = []

# Application definition
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + USER_APPS

# Middleware definition
MIDDLEWARE = DJANGO_MIDDLEWARE + THIRD_PARTY_MIDDLEWARE

# Module definition
WSGI_APPLICATION = "core.wsgi.application"
ROOT_URLCONF = "core.urls"

# Template Definition
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [TEMPLATE_DIR],
        "APP_DIRS": True,
    },
]

# Authentication Definition
AUTHENTICATION_BACKENDS = [
    "graphql_jwt.backends.JSONWebTokenBackend",
    "django.contrib.auth.backends.ModelBackend",
]

# Graphene Definitions
GRAPHENE = {
    "SCHEMA": "core.schema.schema",
    "MIDDLEWARE": [
        "graphql_jwt.middleware.JSONWebTokenMiddleware",
    ],
}

# GRAPHQL_JWT definition
GRAPHQL_JWT = {
    "JWT_VERIFY_EXPIRATION": True,
    "JWT_EXPIRATION_DELTA": timedelta(hours=1),
    "JWT_REFRESH_EXPIRATION_DELTA": timedelta(days=7),
    # Cookie authentication
    "JWT_HIDE_TOKEN_FIELDS": True,
    "JWT_COOKIE_SECURE": True,
    "JWT_COOKIE_SAMESITE": "None",
    "JWT_COOKIE_NAME": "__jwt",
    "JWT_CSRF_ROTATION": True,
}

# Database Definitions
if ON_PRODUCTION:
    DATABASES = {
        "default": {
            "ENGINE": f"django.db.backends.{DB_ENGINE}",
            "NAME": DB_NAME,
            "USER": DB_USER,
            "PASSWORD": DB_PASSWORD,
            "HOST": DB_HOST,
        }
    }

else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

# Static files (CSS, JavaScript, Images)
STATIC_URL = "static/"

if ON_PRODUCTION:
    STATIC_ROOT = STATIC_DIR
else:
    STATICFILES_DIRS = [STATIC_DIR]
