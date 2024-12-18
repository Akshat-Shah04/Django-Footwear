import os
import sys
from django.core.wsgi import get_wsgi_application

sys.path.append(os.path.join(os.path.dirname(__file__), "myproject2"))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject2.settings")

application = get_wsgi_application()
