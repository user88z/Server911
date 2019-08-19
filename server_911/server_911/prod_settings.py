import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ALLOWED_HOSTS = [
    '94.19.137.180',
    'localhost',
    '127.0.0.1',
    '192.168.245.16'
]

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'x62@4pffyp07!#k(ab^dgf&fpix^c864dh_ae!&**(9*w)rjh3'

DEBUG = False

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')