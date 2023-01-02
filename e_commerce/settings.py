from pathlib import Path
import os 
from e_commerce.base.base import *

BASE_DIR = Path(__file__).resolve().parent.parent
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ecommerce'
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
TEMPLATES_DIR = os.path.join(BASE_DIR,'templates')
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],

            'libraries':{
            'filtertags': 'ecommerce.templatetags.filtertags',
            'is_selected':'ecommerce.templatetags.is_selected',
            'product_price':'ecommerce.templatetags.product_price',
            
            }
        },
    },
]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
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

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

AUTH_USER_MODEL = 'ecommerce.User'


STRIPE_SECRET_KEY='sk_test_51MHLavSHaSaa8XAPYywgCwZgqQfPKT9LCte7pvqYEaAe8vyUS62l52RoXtm95pwBtnFz7R5ncvyTTkTM4ahj1AdG00HaoCMClI'

STRIPE_PUBLISH_KEY='pk_test_51MHLavSHaSaa8XAPZpjWLVj6v3JtHCUCslsQ8rDmOcEv437SrMZ0jmKcm8QgeiqcwcnkQSWLnTtETdVj3m2caWGD00xn0vB6Bi'

LOGIN_REDIRECT_URL = '/homepage/'