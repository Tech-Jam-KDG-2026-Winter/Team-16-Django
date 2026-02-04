from .base import *  # noqa

DEBUG = True

# U-006 パスワード再設定用
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
DEFAULT_FROM_EMAIL = "noreply@example.com"