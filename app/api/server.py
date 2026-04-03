from os import environ

from tawala import Package
from tawala.api.backends import server_application

environ.setdefault("DJANGO_SETTINGS_MODULE", Package.SETTINGS_MODULE)

app = server_application
