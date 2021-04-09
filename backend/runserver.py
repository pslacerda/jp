#!/bin/env/python3
import os, waitress
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from jp.app import app
waitress.serve(app, listen='*:8000', url_prefix='/api')
