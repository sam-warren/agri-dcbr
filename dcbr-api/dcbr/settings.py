"""
Django settings for dcbr project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os


def parse_bool(val):
    return val and val != "0" and str(val).lower() != "false"


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# The SECRET_KEY is provided via an environment variable in OpenShift
SECRET_KEY = os.getenv(
    "DJANGO_SECRET_KEY",
    # safe value used for development when DJANGO_SECRET_KEY might not be set
    "75f46345-af2d-497d-a3ec-b6f05e5266f4",
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = parse_bool(os.getenv("DJANGO_DEBUG", "False"))

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.admindocs",
    "django.contrib.auth",
    "mozilla_django_oidc",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "health_check",
    "health_check.db",
    "rest_framework",
    "drf_yasg",
    "corsheaders",
    "post_office",
    "background_task",
    "dcbr",
    "api",
    "email_service.apps.EmailServiceConfig",
    "import_export",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "mozilla_django_oidc.middleware.SessionRefresh",
]

AUTHENTICATION_BACKENDS = [
    "dcbr.oidc_authentication.AdminOIDCAB",
    "django.contrib.auth.backends.ModelBackend",
]

CORS_URLS_REGEX = r"^/(api|email)/.*$"
CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = "dcbr.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "dcbr.wsgi.application"


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DATABASE_NAME"),
        "USER": os.getenv("DATABASE_USER"),
        "PASSWORD": os.getenv("DATABASE_PASSWORD"),
        "HOST": os.getenv("DATABASE_SERVICE_HOST"),
        "PORT": os.getenv("DATABASE_SERVICE_PORT"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = "/static/"

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Set up support for proxy headers (provide correct URL in swagger UI)
USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# API Metadata
# fmt: off
API_METADATA = {
    "title": "Dog and Cat Breeder/Operator Registry API",
    "description": 
        "The purpose of the Dog and Cat Breeder Registration System (DCBR) "
        "is to act as one of the pillars of the Dog and Cat Breeder Regulatory Framework (DCBF) "
        "to target irresponsible dog and cat breeders and sellers (operators). "
        "The DCBR will provide a system wherein a person must register in order to be in compliance with the law "
        "and legally able to undertake the regulated activity of breeding and/or selling cats and dogs and their offspring.",
    "terms": {
        "url": "https://www2.gov.bc.ca/gov/content/data/open-data"
    },
    "contact": {
        "email": "bcdevexchange@gov.bc.ca"
    },
    "license": {
        "name": "Open Government License - British Columbia",
        "url": "https://www2.gov.bc.ca/gov/content/data/open-data/api-terms-of-use-for-ogl-information",
    },
}
# fmt: on

# Django rest framework
REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 100,
    # "DEFAULT_PERMISSION_CLASSES": [
    #     "rest_framework.permissions.IsAuthenticatedOrReadOnly"
    # ],
    # "DEFAULT_AUTHENTICATION_CLASSES": [
    #     "mozilla_django_oidc.contrib.drf.OIDCAuthentication"
    # ],
}

# e-mail management
EMAIL_BACKEND = os.getenv("EMAIL_BACKEND")
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = os.getenv("EMAIL_PORT")
EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS")
POST_OFFICE = {"LOG_LEVEL": 2, "BATCH_SIZE": 50}
AGRI_EMAIL = os.getenv("AGRI_EMAIL")

# PDF printing
WEASYPRINT_HOST = os.getenv("WEASYPRINT_HOST")
WEASYPRINT_PORT = os.getenv("WEASYPRINT_PORT")

if WEASYPRINT_HOST is not None and WEASYPRINT_PORT is not None:
    WEASYPRINT_REQUEST_URL = (
        "http://" + WEASYPRINT_HOST + ":" + WEASYPRINT_PORT + "/pdf?filename="
    )

# mozilla-django-oidc
OIDC_RP_CLIENT_ID = os.getenv("OIDC_RP_CLIENT_ID")
OIDC_RP_CLIENT_SECRET = os.getenv("OIDC_RP_CLIENT_SECRET")
OIDC_OP_AUTHORIZATION_ENDPOINT = os.getenv("OIDC_OP_AUTHORIZATION_ENDPOINT")
OIDC_OP_TOKEN_ENDPOINT = os.getenv("OIDC_OP_TOKEN_ENDPOINT")
OIDC_OP_USER_ENDPOINT = os.getenv("OIDC_OP_USER_ENDPOINT")
OIDC_RP_SIGN_ALGO = os.getenv("OIDC_RP_SIGN_ALGO")
OIDC_OP_JWKS_ENDPOINT = os.getenv("OIDC_OP_JWKS_ENDPOINT")

LOGIN_URL = "/authenticate"
LOGIN_REDIRECT_URL = "/admin"
LOGIN_REDIRECT_URL_FAILURE = "/authenticate"
LOGOUT_REDIRECT_URL = os.getenv("OIDC_LOGOUT_REDIRECT_URL", "/admin/logout")

# Logging
DCBR_LOG_LEVEL = "INFO"
if DEBUG is True:
    DCBR_LOG_LEVEL = "DEBUG"

# fmt:off
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_false": {"()": "django.utils.log.RequireDebugFalse"}
    },
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s"
        },
        "simple": {"format": "%(levelname)s %(message)s"},
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "verbose",
        }
    },
    "loggers": {
        "mozilla_django_oidc": {
            "handlers": ["console"],
            "level": DCBR_LOG_LEVEL
        }
    },
    "root": {
        "handlers": ["console"],
        "level": DCBR_LOG_LEVEL,
        "propagate": False,
    },
}
# fmt:on

# Number of months after which the registration will need to be renewed.
# Set to 0 if the registration will never expire.
REGISTRATION_VALIDITY_MONTHS = os.getenv("REGISTRATION_VALIDITY_MONTHS", 12)
