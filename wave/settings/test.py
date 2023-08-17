from .base import *


LOGGING["root"]["level"] = "DEBUG"

SHOW_DJDT = env.bool("SHOW_DJDT", default=False)
DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda *_: SHOW_DJDT,
}
