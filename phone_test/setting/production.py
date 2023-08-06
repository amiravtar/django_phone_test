from .base import *

from .config import SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "host.example.com"]

# INSTALLED_APPS.append("debug_toolbar")
# MIDDLEWARE.append("debug_toolbar.middleware.DebugToolbarMiddleware")
ZARINPAL_CONFIG = {
    "request_pay": "https://api.zarinpal.com/pg/v4/payment/request.json",
    "start_pay": "https://www.zarinpal.com/pg/StartPay/",
    "verify_pay": "https://api.zarinpal.com/pg/v4/payment/verify.json",
}
