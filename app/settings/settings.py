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
ALLOWED_HOSTS = ['*']
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': None,
    },
}
BASE_URL = 'https://gulshendikmen.az/'

# Application definition

SITE_ID = 1

INSTALLED_APPS = [
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

    # 'rosetta',

    'django.contrib.sites',
    'django.contrib.sitemaps',

    # 'cuser',
    # 'tinymce',
    'modeltranslation'
    # 'robots',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',

    # + For Multiple Language
    'django.middleware.locale.LocaleMiddleware',
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

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'myopt_dev',
        'USER': 'myopt',
        'PASSWORD': 'myopt',
        'HOST': 'db',
        'PORT': '5432'
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


LANGUAGES = [
    # ('az', '{}'.format(ugettext('az'))),
    # ('ru', '{}'.format(ugettext('ru'))),
    ('az', 'Azerbaijan'),
    ('ru', 'Russian'),
]


MODELTRANSLATION_TRANSLATION_FILES = (
    'blog.translation',
)

# LOCALE_PATHS = ( os.path.join(SITE_ROOT, 'locale'), )

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),

]

"""
LOCALE_PATHS = [
    BASE_DIR / 'locale/',
]
"""

LANGUAGE_CODE = 'az'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

USE_L10N = True


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


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.mail.ru'
EMAIL_HOST_USER = 'info@gulshendikmen.az'
EMAIL_HOST_PASSWORD = 'MbuLeQTNrCxDtbfM0qXB'
EMAIL_PORT = 2525
DEFAULT_FROM_EMAIL = "info@gulshendikmen.az"
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False


TRANSLATABLE_MODEL_MODULES = ["blog.models", ]
