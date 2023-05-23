import dj_database_url
from decouple import config

from .settings import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = ['huzzy.up.railway.app',
                 'huzzy.cleverapps.io', '.vercel.app', '10.2.216.67']

CSRF_TRUSTED_ORIGINS = ['https://' + host for host in ALLOWED_HOSTS]

DATABASES = {
    'default': dj_database_url.config(
        conn_max_age=600,
        conn_health_checks=True,
    ),
}

STORAGES = {
    "default": {
        "BACKEND": 'cloudinary_storage.storage.MediaCloudinaryStorage'
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': config('CLOUD_NAME'),
    'API_KEY': config('CLOUD_API_KEY'),
    'API_SECRET': config('CLOUD_API_SECRET'),
}
