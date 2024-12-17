"""
WSGI config for classmanager project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
import sys

# Add the project directory to the Python path
sys.path.append('/home/SharuHinge/classroom_connect')

# Specify the Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'classmanager.settings'

# Add the virtual environment's site-packages directory to the path
sys.path.append('/home/ShraddhaHinge/.virtualenvs/my_virtualenv/lib/python3.10/site-packages')

# Load the WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
