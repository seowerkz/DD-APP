from doubleddistributionapp.settings.common import *

SECRET_KEY = 'f)qnj6y$2yuwv#q)o7*7phcrv=co7mp+1gyzwwk$(26#g@6zro'
DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'doubled',
        'USER': 'doubledadmin',
        'PASSWORD': 'DXSxD81V',
        'HOST': 'db',
        'PORT': '',
    }
}

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'static')

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
