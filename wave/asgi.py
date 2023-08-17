"""
ASGI config for My project

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""
import os
from django.core.asgi import get_asgi_application

sys_env = os.environ.get("APP_ENV", "local")
default_settings = f"my_project.settings.{sys_env}"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", default_settings)

application = get_asgi_application()
