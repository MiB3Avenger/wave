from django.conf import settings
from django.urls import reverse


def core_processor(request):
    """
    Injects core project variables in templates
    """
    return {
        "less_compile": getattr(settings, "LESS_COMPILE_CLIENTSIDE", False),
        "app_env": getattr(settings, "APP_ENV", False),
    }


def global_variables(request):
    """
    Add global variables to be used by the front-end application
    """
    return {
        "global_variables": {
            "staticUrl": request.build_absolute_uri(settings.STATIC_URL),
            "mediaUrl": request.build_absolute_uri(settings.MEDIA_URL),
            "urls": {
                "api": request.build_absolute_uri(reverse("api.v1:default")),
            },
        }
    }
