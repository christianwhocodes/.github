"""ASGI configuration.

For more information on this file, see
https://docs.djangoproject.com/en/stable/howto/deployment/asgi/
"""

from os import environ

from django.core.asgi import get_asgi_application
from tawala import Package

environ.setdefault("DJANGO_SETTINGS_MODULE", Package.SETTINGS_MODULE)

app = get_asgi_application()
