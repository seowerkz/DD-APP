from doubleddistributionapp.settings.common import *

ADMINS = (
    ('Trey Richards', 'trey@embrk.com'),
    ('Eric Saupe', 'eric@embrk.com'),
)

SECRET_KEY = os.environ["SECRET_KEY"]
DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = [
    '.doubleddistribution.com', # Allow domain and subdomains
    '.doubleddistribution.com.', # Also allow FQDN and subdomains
    'doubled-env.eba-ayic7sfr.us-east-1.elasticbeanstalk.com',
    os.environ["SITE_DOMAIN"],
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ["DB_NAME"],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ["DB_PASSWORD"],
        'HOST': os.environ["DB_HOST"],
        'PORT': os.environ["DB_PORT"],
    }
}

HOST = "%s://%s" % (os.environ["SITE_PROTOCOL"], os.environ["SITE_DOMAIN"])

S3_URL = "https://s3.amazonaws.com/%s/" % (
    os.environ['S3_BUCKET_NAME']
)
AWS_S3_ADDRESSING_STYLE = 'path'
AWS_DEFAULT_ACL = 'public-read'
AWS_ACCESS_KEY_ID = os.environ["AWS_ACCESS_KEY_ID"]
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_KEY']
AWS_STORAGE_BUCKET_NAME = os.environ['S3_BUCKET_NAME']
AWS_QUERYSTRING_AUTH = False
AWS_HEADERS = {
  'Cache-Control': 'max-age=86400',
}

STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = 'doubleddistributionapp.custom_storages.StaticStorage'
STATIC_URL = "%s/%s/" % (S3_URL, STATICFILES_LOCATION)

MEDIAFILES_LOCATION = 'media'
MEDIA_URL = "%s/%s/" % (S3_URL, MEDIAFILES_LOCATION)
DEFAULT_FILE_STORAGE = 'doubleddistributionapp.custom_storages.MediaStorage'


SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = os.environ["SITE_PROTOCOL"] == 'https'
SECURE_SSL_HOST = os.environ["SITE_DOMAIN"]

########## LOGGING CONFIGURATION
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'null': {
            'class': 'logging.NullHandler',
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.security.DisallowedHost': {
            'handlers': ['null'],
            'propagate': False,
        },
    }
}
########## END LOGGING CONFIGURATION

########## EMAIL CONFIGURATION
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = os.environ["EMAIL_HOST"]
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ["EMAIL_HOST_USER"]
EMAIL_HOST_PASSWORD = os.environ["EMAIL_HOST_PASSWORD"]
SERVER_EMAIL = os.environ["DEFAULT_FROM_EMAIL"]
DEFAULT_FROM_EMAIL = os.environ["DEFAULT_FROM_EMAIL"]
########## END EMAIL CONFIGURATION
