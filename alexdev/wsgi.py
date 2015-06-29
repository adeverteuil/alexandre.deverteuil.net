"""
WSGI config for alexdev project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
import sys

activate_this = "/home/http/alexandre.deverteuil.net/virtualenv/bin/activate_this.py"
exec(open(activate_this).read(), dict(__file__=activate_this))
sys.path.append("/home/http/alexandre.deverteuil.net")
sys.path.append("/home/http/alexandre.deverteuil.net/alexdev")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "alexdev.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
