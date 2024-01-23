from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

ALLOWED_HOSTS = ['msnessim.pythonanywhere.com']

STATIC_ROOT = '/home/msnessim/minanessim_site/static'
STATIC_URL = '/home/msnessim/minanessim_site/static'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static/')
]