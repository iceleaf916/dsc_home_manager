#-*- coding:utf-8 -*-

import os
import sys
 
os.environ['DJANGO_SETTINGS_MODULE'] = 'dsc_home_manager.settings'
 
path = os.path.dirname(os.path.abspath(__file__))
if path not in sys.path:
    sys.path.insert(1, path)

path = os.path.dirname(os.path.abspath(__file__)) + '/dsc_home_manager'
if path not in sys.path:
    sys.path.insert(1, path)
 
from django.core.handlers.wsgi import WSGIHandler
from bae.core.wsgi import WSGIApplication
 
application = WSGIApplication(WSGIHandler())
