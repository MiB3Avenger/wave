"""
Django settings for My project.
"""
import os
import sys
import environ
from pathlib import Path

from django.utils.translation import gettext_lazy as _

env = environ.Env()

# Get base dir using environ
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Cast project dirs as string for future manipulation
PROJECT_ROOT = BASE_DIR / "wave"

# This is WSGI sccript prefix, used to resolve urls
APP_PREFIX = env.str("APP_PREFIX", default="/")
APP_ENV = env.str("APP_ENV", default="local")

ROOT_URLCONF = "wave.urls.prod"

sys.path.insert(1, str(PROJECT_ROOT / "apps"))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str(
    "SECRET_KEY",
    default="z()@=u8hjeg1w864d$g*1pm$#7l0m5txos!qppg4x+p=lnwzx3"
)

# SECURITY WARNING: don"t run with debug turned on in production!
DEBUG = env.bool("DJANGO_DEBUG", default=False)

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["*"])
INTERNAL_IPS = env.list("INTERNAL_IPS", default=[
    "127.0.0.1",
])

# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOGIN_URL = "admin:login"

# Application definition
INSTALLED_APPS = (
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django_vite",
    "django.contrib.staticfiles",
    "django.contrib.sites",

    "debug_toolbar",
    "django_extensions",
    "corsheaders",
    "rest_framework",
    "rest_framework.authtoken",
    "drf_yasg",

    "core",
    "api.v1",
    "modules.wave",
    "modules.account",
)

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",

    "django.middleware.cache.UpdateCacheMiddleware",

    # Custom app middleware
    "core.middleware.AppIdMiddleware",
]

WSGI_APPLICATION = "wave.wsgi.application"


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            PROJECT_ROOT / "templates",
        ],
        # "APP_DIRS": True,  # must not be set when loaders is defined
        "OPTIONS": {
            "loaders": [
                ("django.template.loaders.cached.Loader", [
                    "django.template.loaders.filesystem.Loader",
                    "django.template.loaders.app_directories.Loader",
                ]),
            ],
            "context_processors": [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven"t customized them:

                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.request",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
                "core.context_processors.core_processor",
                "core.context_processors.global_variables",
            ],
            "debug": DEBUG,
        },
    },
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = "en"

LANGUAGES = (
    ("en", _("English")),
    ("nb", _("Norwegian")),
)

TIME_ZONE = "Europe/Oslo"
USE_I18N = True
USE_L10N = False
USE_TZ = True

DECIMAL_SEPARATOR = ","

# Static files (CSS, JavaScript, Images)
STATICFILES_DIRS = [
    PROJECT_ROOT / "global_staticfiles",
]
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "django.contrib.staticfiles.finders.FileSystemFinder",
)
STATIC_URL = env.str("STATIC_URL", default="/static/")
STATIC_ROOT = env.str("STATIC_ROOT", default=PROJECT_ROOT / "site_media" / "static")
STATICFILES_STORAGE = env.str(
    "STATICFILES_STORAGE",
    default="django.contrib.staticfiles.storage.StaticFilesStorage"
)

MEDIA_URL = env.str("MEDIA_URL", default="/media/")
MEDIA_ROOT = env.str("MEDIA_ROOT", default=PROJECT_ROOT / "site_media" / "media")
DEFAULT_FILE_STORAGE = env.str(
    "DEFAULT_FILE_STORAGE",
    default="django.core.files.storage.FileSystemStorage"
)

SERVE_MEDIA_FILES = env.bool("SERVE_MEDIA", default=False)
SERVE_STATIC_FILES = env.bool("SERVE_STATIC", default=False)

# Where ViteJS assets are built.
DJANGO_VITE_ASSETS_PATH = BASE_DIR / "frontend" / "dist"

# If use HMR or not.
DJANGO_VITE_DEV_MODE = DEBUG
DJANGO_VITE_STATIC_URL_PREFIX = "/"

# Include DJANGO_VITE_ASSETS_PATH into STATICFILES_DIRS to be copied inside
# when run command python manage.py collectstatic
STATICFILES_DIRS += [DJANGO_VITE_ASSETS_PATH]

LOGGING_FORMATTER = env.str("LOGGING_FORMATTER", default="verbose")
# Logging setup
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug": {
            "()": "django.utils.log.RequireDebugTrue",
        },
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse",
        },
        "skippped_logs": {
            "()": "core.logging_filters.DisabledLogFilter"
        },
    },
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s "
                      "%(process)d %(thread)d %(message)s"
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": LOGGING_FORMATTER,
            "filters": ["skippped_logs"],
        }
    },
    "root": {"level": "INFO", "handlers": ["console"]},
}

DEFAULT_EXCEPTION_REPORTER_FILTER = "core.logging_filters.CustomExceptionFilter"

# Application settings #

DATE_FORMAT = "d.m.Y"
SHORT_DATE_FORMAT = "d.m.y"
DATE_INPUT_FORMATS = (
    "%d.%m.%Y",
    "%d.%m.%Y.",
    "%Y-%m-%d",
)

# Caching settings
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.dummy.DummyCache",
        "KEY_PREFIX": "wave",
    },
}

# Add prefix for cookies so that there isn"t mixup of cookies
SESSION_COOKIE_PATH = APP_PREFIX
CSRF_COOKIE_PATH = APP_PREFIX

SESSION_SERIALIZER = "django.contrib.sessions.serializers.JSONSerializer"
# Expire session after 3 days to avoid long session storages
SESSION_COOKIE_AGE = 259200

SITE_ID = 1

EMAIL_PORT = 1025

# Disable patching of the settings files as it breaks when used with WSGI
DEBUG_TOOLBAR_PATCH_SETTINGS = env.bool("DT_PATCH_SETTINGS", default=False)

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        # "rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly",
    ],
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
    ],
    "DEFAULT_PAGINATION_CLASS":
        "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 25,
}
