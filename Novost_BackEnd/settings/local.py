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

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = "senanovost@gmail.com"
EMAIL_HOST_PASSWORD = "jdywyuhalcojshvu"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/


# Configure Django App for Heroku.
import django_heroku
django_heroku.settings(locals())