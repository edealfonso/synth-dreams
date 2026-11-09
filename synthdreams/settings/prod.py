
from .base import *

import mimetypes

mimetypes.add_type("text/css", ".css", True)


# DEBUG, ALLOWED_HOSTS and DATABASES come from environment variables (see base.py).
# DJANGO_DEBUG must not be 1 in production.

CSRF_TRUSTED_ORIGINS = get_env_list('DJANGO_CSRF_TRUSTED_ORIGINS')

