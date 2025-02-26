#
# Development WSGI Settings
#

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "doubleddistributionapp.settings")

from doubleddistributionapp.wsgi.common import *
