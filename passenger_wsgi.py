# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/home/l/legalro8/legalro_backend/api')
sys.path.insert(1, '/home/l/legalro8/.local/lib/python3.6/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'api.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()