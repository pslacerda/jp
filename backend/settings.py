import dj_database_url

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'jp',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'postgres',
        'PORT': '5432',
    }
}
INSTALLED_APPS = (
    'jp.models',
    'django.contrib.postgres',
)
SECRET_KEY = 'REPLACE_ME'
DEBUG = True
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
