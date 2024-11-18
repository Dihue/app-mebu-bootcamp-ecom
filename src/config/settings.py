import environ
import os

from django.urls import reverse_lazy
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Configuración con variables de entorno
env = environ.Env()
env_file = os.path.join(os.path.dirname(BASE_DIR), 'env/.env')

env.read_env(env_file=env_file, overwrite=True)


SECRET_KEY_DEFAULT = 'django-insecure-p@kh0k@q)y7b&^r2&$ox-3nxic!xhs@h-1zy7rvz2orw6@7!21'
SECRET_KEY = env('SECRET_KEY', default=SECRET_KEY_DEFAULT)


DEBUG = env.bool('DJANGO_DEBUG', default=True)


ENVIRONMENT_RUN = env('ENVIRONMENT_RUN', default='local')


ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default=['*'])


# Application definition
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

LOCAL_APPS = []

THIRD_APPS = []

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_APPS


# Modelo para el manejo de Usuarios
# AUTH_USER_MODEL = ''
#TODO usuarios.Usuario

# Redirección al iniciar sesión
LOGIN_REDIRECT_URL = reverse_lazy('#')
#TODO 'inicio'

# Redirección al cerrar sesión
LOGIN_URL = reverse_lazy('#')
#TODO 'login'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'config.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'config.wsgi.application'


# Database
DEFAULT_DB_NAME = env("POSTGRES_DB")
DEFAULT_DB_USER = env("POSTGRES_USER")
DEFAULT_DB_HOST = env("POSTGRES_HOTS")
DEFAULT_DB_PORT = env("POSTGRES_PORT")

DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': DEFAULT_DB_NAME,
            'USER': DEFAULT_DB_USER,
            'PASSWORD': env("POSTGRES_PASSWORD"),
            'HOST': DEFAULT_DB_HOST,
            'POST': DEFAULT_DB_PORT,
    }
}


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
LANGUAGE_CODE = 'es-Ar'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Contenido Media
RUTA_CARPETA_MEDIA = os.path.join(BASE_DIR, 'media')

MEDIA_URL = 'media/'

MEDIA_ROOT = RUTA_CARPETA_MEDIA


# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'