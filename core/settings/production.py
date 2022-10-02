from .base import *

DEBUG = False

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*']

try:
    from .local import *
except ImportError:
    pass
