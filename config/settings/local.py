from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str('DJANGO_SECRET_KEY', default='jkl685u9^4t60k0&$-u!78$e&itm7=g8so1j2@$n58k+fy4l^&rw7i')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DJANGO_DEBUG', default=True)

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
]
