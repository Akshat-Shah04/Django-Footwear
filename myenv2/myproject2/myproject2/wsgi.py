import os
from django.core.wsgi import get_wsgi_application

# Default settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject2.settings")

application = get_wsgi_application()
