# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
import os

DOCKER = True

from . import database

DATABASES = {
    'default': database.config()
}

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql_psycopg2',
#        'NAME': 'mail_db_main',
#        'USER': 'mail_user_main',
#        'PASSWORD': '1234',
#        'HOST': 'mail_db_main',
#        'PORT': '5432',
#    }
#}

#if DOCKER:
#	DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql_psycopg2',
#        'NAME': os.getenv('POSTGRES_DB'),
#        'USER': os.getenv('POSTGRES_USER'),
#        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
#        'HOST': os.getenv('POSTGRES_HOST'),
#        'PORT': '5432',
#    }
#}

AWS_S3_ENDPOINT_URL = 'http://hb.bizmrg.com'
AWS_ACCESS_KEY_ID = '8iPxtbPze7LaAhXQizdnCV'
AWS_SECRET_ACCESS_KEY = 'auMoTfsBUT1JGUjSqdNgyJnUrKb4FcA6wNDXMWkRHfE5'
AWS_STORAGE_BUCKET_NAME = 'abdrakhimov_track'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

SOCIAL_AUTH_VK_OAUTH2_KEY = '7233862'
SOCIAL_AUTH_VK_OAUTH2_SECRET = 'ft0aqlPo0JIcp6Ymq64G'
SOCIAL_AUTH_VK_OAUTH2_SCOPE = ['email']
