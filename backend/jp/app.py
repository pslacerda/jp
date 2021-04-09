'''
Run the following commands (bc. gists don't allow directories)
pip install flask django dj-database-url psycopg2
mkdir -p app/migrations
touch app/__init__.py app/migrations/__init__.py
mv models.py app/
python manage.py makemigrations
python manage.py migrate
DJANGO_SETTINGS_MODULE=settings python app.py
visit http://localhost:5000
See https://docs.djangoproject.com/en/1.11/topics/settings/#either-configure-or-django-settings-module-is-required for documentation
'''

from flask import Flask
from django.apps import apps
from django.conf import settings
import django.dispatch


apps.populate(settings.INSTALLED_APPS)
app = Flask(__name__)

customer_updated = django.dispatch.Signal()

from jp.views import *
from jp.models.models import *
from jp.signals import *

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='8000')
