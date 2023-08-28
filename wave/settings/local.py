import os
from .base import *

DEBUG = True
DJANGO_VITE_DEV_MODE = DEBUG

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=["*"])

ROOT_URLCONF = "wave.urls.local"

# We want full debugging in development
LOGGING["root"]["level"] = "DEBUG"
# Normal formatting for local development
LOGGING["handlers"]["console"]['formatter'] = "verbose"

# Remove cached loader for local development
del TEMPLATES[0]['OPTIONS']['loaders']
TEMPLATES[0]['APP_DIRS'] = True
TEMPLATES[0]['OPTIONS']['debug'] = True

# For local development we don't want to bother with interactive debugger PIN
os.environ['WERKZEUG_DEBUG_PIN'] = 'off'

DEBUG_TOOLBAR_PATCH_SETTINGS = True

AUTH_PASSWORD_VALIDATORS = []

# This is feature branch so we check for local settings first
user_settings = BASE_DIR / "config" / "settings.py"
if user_settings.exists():
    with open(user_settings) as f:
        exec(f.read())

SERVE_MEDIA_FILES = True
SERVE_STATIC_FILES = True