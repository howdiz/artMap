import os
import sys

sys.path = ['/home/echoability/webapps/django', '/home/echoability/webapps/django/lib/python2.5'] + sys.path
from django.core.handlers.wsgi import WSGIHandler

os.environ['DJANGO_SETTINGS_MODULE'] = 'artmaps.settings'
application = WSGIHandler()
