import os
from datetime import timedelta
from pathlib import Path

from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv()
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'drf_spectacular',
    'phonenumber_field',
    'rest_framework',
    'djoser',
    "rest_framework_simplejwt",

    # my app
    'users',
    'companies',
]

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
        'DIRS': [],
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
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.flex',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = "Europe/Moscow"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "/django_static/"
STATIC_ROOT = os.path.join(BASE_DIR, "django_static")

MEDIA_URL = "/django_media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "django_media")

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = "users.User"

# Settings Djoser
DJOSER = {
    'PERMISSIONS': {
        'user_create': ['rest_framework.permissions.AllowAny']
    },
    # URL-адрес страницы сброса пароля
    'PASSWORD_RESET_CONFIRM_URL': 'api/reset_password_confirm/{uid}/{token}',
    # Изменение пароля авторизованного пользователя
    'SET_PASSWORD_RETYPE': True,
    'LOGOUT_ON_PASSWORD_CHANGE': True,

    # URL-адрес страницы сброса имени пользователя
    # (в данном случае - электронной почты, как имени пользователя для авторизации)
    'USERNAME_RESET_CONFIRM_URL': 'api/auth/users/reset_email_confirm/{uid}/{token}',
    # Изменение имени (в данном случае - электронной почты) авторизованного пользователя
    'SET_USERNAME_RETYPE': True,

    # URL-адрес страницы активации
    'ACTIVATION_URL': 'api/activate/{uid}/{token}',
    # Активация по ссылке, присланной по электронной почте
    'SEND_ACTIVATION_EMAIL': True,
    'TOKEN_MODEL': None,  # We use only JWT

    # Проверка равенства паролей
    'USER_CREATE_PASSWORD_RETYPE': True,

    # сериализаторы
    'SERIALIZERS': {
        'user': 'users.serializers.UserSerializer',
        'user_create': 'users.serializers.UserRegistrationSerializer',
        'current_user': 'users.serializers.CurrentUserSerializer',
        'user_create_password_retype': 'users.serializers.CustomUserCreatePasswordRetypeSerializer',
        'activation': 'djoser.serializers.ActivationSerializer',
        'password_reset': 'djoser.serializers.SendEmailResetSerializer',
    },
    # настройка почты
    "EMAIL": {
        "confirmation": "users.email.UserConfirmationEmail",
        "password_reset": "users.email.UserPasswordResetEmail",
        "password_changed_confirmation": "users.email.UserPasswordChangedConfirmationEmail",
        "username_changed_confirmation": "users.email.UserUsernameChangedConfirmationEmail",
    },
    # Имя поля в модели пользователя, которое будет использоваться в качестве поля входа.
    'LOGIN_FIELD': 'email'
}

# REST_FRAMEWORK OPTIONS
REST_FRAMEWORK = {
    # "DEFAULT_FILTER_BACKENDS": ("django_filters.rest_framework.DjangoFilterBackend",),
    "DEFAULT_AUTHENTICATION_CLASSES": ("rest_framework_simplejwt.authentication.JWTAuthentication",),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.AllowAny",),
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

# Настройки срока действия токенов
SIMPLE_JWT = {
    # 'AUTH_HEADER_TYPES': ('Bearer',),
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=20),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
}

# DRF SPECTACULAR OPTIONS
SPECTACULAR_SETTINGS = {
    "TITLE": "Flex",
    "DESCRIPTION": "Backend сервер 'тестовое задание Flex'",
    "VERSION": "1.0.1",
    "SERVE_INCLUDE_SCHEMA": False,
}

# Настройки почты, для отправки яндекс
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = 465
EMAIL_USE_SSL = True
DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL")