#
# Production WSGI Settings
#

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "doubleddistributionapp.settings.prod")

from doubleddistributionapp.wsgi.common import *
