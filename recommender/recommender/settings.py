from pathlib import Path

from .local_conf import DATABASE, KEY, EMAIL, HOST_PASS, GIT_HUB_CLIENT_ID, GIT_HUB_SECRET, GOOGLE_CLINT_ID, GOOGLE_SECRET, GOOGLE_KEY


BASE_DIR = Path(__file__).resolve().parent.parent
import os

SECRET_KEY = KEY

DEBUG = False

ALLOWED_HOSTS = ['*']



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Movies.apps.MoviesConfig',
    
    'django.contrib.sites',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.google',

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

ROOT_URLCONF = 'recommender.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = 'recommender.wsgi.application'


SITE_ID = 1



AUTHENTICATION_BACKENDS = [

    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]


SOCIALACCOUNT_PROVIDERS = {
    'github': {

        'APP': {
            'client_id': GIT_HUB_CLIENT_ID,
            'secret': GIT_HUB_SECRET,
            'key': ''
        }
    },
    'google': {

        'APP': {
            'client_id': GOOGLE_CLINT_ID,
            'secret': GOOGLE_SECRET,
            'key': GOOGLE_KEY
        }
    }
}


ACCOUNT_EMAIL_REQUIRED = True 
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_MAX_EMAIL_ADDRESSES = 1
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = True
LOGIN_REDIRECT_URL = '/movies/list-movie/'
LOGOUT_REDIRECT_URL = '/movies/list-movie/'
ACCOUNT_SIGNUP_REDIRECT_URL = '/movies/list-movie/'
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = '/movies/list-movie/'


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' 
EMAIL_HOST = 'smtp.gmail.com' 
EMAIL_PORT = 587 
EMAIL_HOST_USER = EMAIL
EMAIL_HOST_PASSWORD = HOST_PASS
EMAIL_USE_TLS = True 
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'



DATABASES = DATABASE


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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
