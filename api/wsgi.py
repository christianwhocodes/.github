"""WSGI configuration.

For more information on this file, see
https://docs.djangoproject.com/en/stable/howto/deployment/wsgi/
"""

from os import environ

from django.core.wsgi import get_wsgi_application
from tawala import Package

environ.setdefault("DJANGO_SETTINGS_MODULE", Package.SETTINGS_MODULE)

app = get_wsgi_application()
