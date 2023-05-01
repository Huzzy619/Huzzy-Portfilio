from .settings import *
import os
import dj_database_url


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['huzzy.up.railway.app']

CSRF_TRUSTED_ORIGINS = ['https://huzzy.up.railway.app']

DATABASES = {
    'default': dj_database_url.parse(
        'postgres://nhryipuu:Qykbmz4M7zJFvgdW5R3dS6_oGpZ4f2Da@kashin.db.elephantsql.com/nhryipuu',
        conn_max_age=600,
        conn_health_checks=True, 
    )
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.environ['CLOUD_NAME'],
    'API_KEY': os.environ['CLOUD_API_KEY'],
    'API_SECRET': os.environ['CLOUD_API_SECRET'], 
}