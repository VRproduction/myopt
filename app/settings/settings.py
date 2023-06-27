from pathlib import Path
import os
from django.utils.translation import gettext_lazy as _


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-^%*=oc7$g77yio7=w-=vb+od%sp@22m5de^+-c=uacbz=)$lmh'

DEBUG = True
# DEBUG = False

ALLOWED_HOSTS = ["*"]


# Application definition

SITE_ID = 1

INSTALLED_APPS = [
    # 'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'blog',
    'settings',
    'crispy_forms',
    'crispy_bootstrap5',
    'ckeditor',
    'corsheaders',
    # 'modeltranslation',
    'rosetta',

    'django.contrib.sites',
    'django.contrib.sitemaps',

    # 'robots',
]



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    'django.middleware.locale.LocaleMiddleware',

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'settings.urls'

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
                'blog.context_processors.extras',
            ],
        },
    },
]

WSGI_APPLICATION = 'settings.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/


LANGUAGE_CODE = 'az'

LANGUAGES = (
    ("az", _("Azerbaijani")),
    ("ru", _("Russian")),
)

LOCALE_PATHS = [
    BASE_DIR / 'locale/',
]

"""
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)
"""

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

USE_L10N = True

MODELTRANSLATION_DEFAULT_LANGUAGE = 'az'

MODELTRANSLATION_LANGUAGES = ('az', 'ru')


STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static/'


STATICFILES_DIRS = [
    BASE_DIR / 'apps-static',
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media/'


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

CSRF_TRUSTED_ORIGINS = ['https://gulshendikmen.az']


"""
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.mail.ru'
EMAIL_HOST_USER = 'info@gulshendikmen.az'
EMAIL_HOST_PASSWORD = 'gulsendikmen123'
EMAIL_PORT = 2525
DEFAULT_FROM_EMAIL = "info@gulshendikmen.az"
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
# EMAIL_PORT = 465
"""


# EMAIL_BACKEND = 'django.core.mail.console.smtp.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'ilkine2191@gmail.com'
# EMAIL_HOST_PASSWORD = 'ankarailkinodessa'
EMAIL_HOST_PASSWORD = 'hcpkljyfxsmehfcl'
