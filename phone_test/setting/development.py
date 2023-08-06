from .base import *
from .config import SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]
SITE_URL = "localhost:8000"

INSTALLED_APPS += [
    # "debug_toolbar",
]
MIDDLEWARE += [
    # "debug_toolbar.middleware.DebugToolbarMiddleware",
]
