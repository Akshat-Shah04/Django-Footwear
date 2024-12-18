"""
WSGI config for myproject2 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject2.settings')

# assuming your django settings file is at '/home/AkshatShah/mysite/mysite/settings.py'
# and your manage.py is is at '/home/AkshatShah/mysite/manage.py'
path = '/C:/Users/pathi/Desktop/Program/Tops/BackEnd/Django/myenv2/myproject2'
if path not in sys.path:

   sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'myproject.settings'

# then:
application = get_wsgi_application()


