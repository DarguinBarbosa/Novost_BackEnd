importar os
desde pathlib import path

# Construye rutas dentro del proyecto de esta manera: BASE_DIR / 'subdir'.
BASE_DIR = Ruta(__file__). resolver(). padre. padre

MEDIA_URL = '/solicitudes/'
MEDIA_ROOT = os. ruta. join(BASE_DIR, '.. /solicitudes')

# Configuración de desarrollo de inicio rápido: no es adecuada para la producción
# Ver https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/
X_FRAME_OPTIONS='permitir-desde*'
# ADVERTENCIA DE SEGURIDAD: ¡mantenga en secreto la clave secreta utilizada en la producción!
SECRET_KEY = 'django-insecure-a%x(lw#5km*v@jv78yx_h&5%h1rbubekuo_db@cb=7(ibn+jyq'

# ADVERTENCIA DE SEGURIDAD: ¡no se ejecute con la depuración activada en producción!
DEPURAR = Falso

ALLOWED_HOSTS = ['*']


# Definición de la aplicación

BASE_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

CORS_ORIGIN_ALLOW_ALL = Verdadero

LOCAL_APPS = [
    'apps.users',
    'apps.base',
    'apps.novedades',
]

THIRD_APPS = [
    'rest_framework',
    'simple_history',
    'import_export',
    'rest_framework.authtoken',
    'corsheaders',
]

INSTALLED_APPS  = BASE_APPS + LOCAL_APPS + THIRD_APPS

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
]

ROOT_URLCONF = 'Novost_BackEnd.urls'

PLANTILLAS = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
 «DIRS»: [],
 'APP_DIRS': Verdadero,
 'OPCIONES': {
            'context_processors': [
 'django.template.context_processors.debug',
 «django.template.context_processors.request»,
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Novost_BackEnd.wsgi.application'


# Validación de contraseña
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
 'NOMBRE': 'django.contrib.auth.password_validation. UserAttributeSimilarityValidator',
    },
    {
 'NOMBRE': 'django.contrib.auth.password_validation. MinimumLengthValidator',
    },
    {
 'NOMBRE': 'django.contrib.auth.password_validation. CommonPasswordValidator',
    },
    {
 'NOMBRE': 'django.contrib.auth.password_validation. NumericPasswordValidator',
    },
]


# Internacionalización
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'es-co'

TIME_ZONE = 'UTC'

USE_I18N = Verdadero

USE_L10N = Verdadero

USE_TZ = Verdadero

AUTH_USER_MODEL = 'usuarios. Usuario'

# Archivos estáticos (CSS, JavaScript, Imágenes)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/estático/'

# Tipo de campo de clave principal predeterminado
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = Verdadero
EMAIL_PORT = 587
EMAIL_HOST_USER = "senanovost@gmail.com"
EMAIL_HOST_PASSWORD = "SistemaNovost123"


# Configurar la aplicación Django para Heroku.
django_heroku de importación
django_heroku. configuración(locales()) 
