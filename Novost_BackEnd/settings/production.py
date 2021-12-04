from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'CLIENT': {
            "host" : "mongodb+srv://Novost:SistemaNovost123@cluster0.vjiyz.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
            , "name" : "Database_Novost",
            "authMechanism" : "SCRAM-SHA-1" # Para la conexion a MongodbAtlas
        },
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/


STATIC_URL = '/static/'



# Configure Django App for Heroku.
import django_heroku
django_heroku.settings(locals())