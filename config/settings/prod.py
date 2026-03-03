from .base import *

DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com']
import os

DEBUG = False

ALLOWED_HOSTS = ['*']  # temporaire pour test

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')