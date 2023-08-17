"""
WSGI config for My project

It exposes the WSGI callable as a module-level variable named ``application``.
"""
import os
from django.core.wsgi import get_wsgi_application


sys_env = os.environ.get("APP_ENV", "local")
default_settings = f"my_project.settings.{sys_env}"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", default_settings)

application = get_wsgi_application()
