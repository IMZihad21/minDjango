from decouple import config
from django.core.management.utils import get_random_secret_key
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_DIR = BASE_DIR.joinpath("static")

SECRET_KEY = config("SECRET_KEY", default=get_random_secret_key())
ON_PRODUCTION = config("ON_PRODUCTION", default=False, cast=bool)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG", default=True, cast=bool)

ALLOWED_HOSTS = ["*"]

# Django built-in apps
DJANGO_APPS = [
    "django.contrib.staticfiles",
]

# Third Party apps
THIRD_PARTY_APPS = []

# User defined apps
USER_APPS = []

# Django built-in middleware
DJANGO_MIDDLEWARE = []

# Third Party middleware
THIRD_PARTY_MIDDLEWARE = []

# Application definition
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + USER_APPS

# Middleware definition
MIDDLEWARE = DJANGO_MIDDLEWARE + THIRD_PARTY_MIDDLEWARE

# Module definition
WSGI_APPLICATION = "core.wsgi.application"
ROOT_URLCONF = "core.urls"

# Static files (CSS, JavaScript, Images)
STATIC_URL = "static/"

if ON_PRODUCTION:
    STATIC_ROOT = STATIC_DIR
else:
    STATICFILES_DIRS = [STATIC_DIR]
