# todoApp/settings.py

import os
from pathlib import Path  # Modern way to handle file paths

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
# For production, it's better to load this from an environment variable.
SECRET_KEY = '8)810zj@#^2xp=1=2rkozbv8#)gub6m1a^9qf&)d-9&x9*c2a_'

# SECURITY WARNING: don't run with debug turned on in production!
# Set this to False when you deploy your application permanently.
DEBUG = True

# --- ADDED: This is required for your app to run on a server ---
# Add the IP address or domain name of your server here.
ALLOWED_HOSTS = ['3.144.80.170']


# Application definition
INSTALLED_APPS = [
    'todos.apps.TodosConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'todoApp.urls'

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

WSGI_APPLICATION = 'todoApp.wsgi.application'


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',  # Modern way using pathlib
    }
}


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True
# --- UPDATED: USE_L10N is deprecated in newer Django versions ---
USE_FORMATTING = True


# Static files (CSS, JavaScript, Images)
# The URL to access static files in the browser.
STATIC_URL = '/static/'

# The single directory where 'collectstatic' will gather all static files for production.
STATIC_ROOT = BASE_DIR / 'static'

# --- ADDED: The directory where you place your project's own static files ---
STATICFILES_DIRS = [
    BASE_DIR / "staticfiles",
]

# Media files (User-uploaded content)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# --- ADDED: Fixes the primary key warning you saw earlier ---
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
