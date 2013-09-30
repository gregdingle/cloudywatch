#WSGI
import sys
sys.path.insert(0, '/srv/cloudywatch')
sys.path.insert(0, '/srv/cloudywatch/cloudywatch')

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
