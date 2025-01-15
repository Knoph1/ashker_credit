INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'api',
]

MIDDLEWARE = [
    ...
    'corsheaders.middleware.CorsMiddleware',
]

CORS_ALLOW_ALL_ORIGINS = True  # Customize for production

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Change to PostgreSQL if needed
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_ROOT = BASE_DIR / 'static'
STATIC_URL = '/static/'

from decouple import config

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
DATABASES = {
    'default': dj_database_url.config(default=config('DATABASE_URL'))
}

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    ...
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

INSTALLED_APPS += ['corsheaders']

MIDDLEWARE.insert(0, 'corsheaders.middleware.CorsMiddleware')

CORS_ALLOW_ALL_ORIGINS = True  # Restrict to frontend domain in production

# Add REST Framework JWT settings
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

MIDDLEWARE += [
    'api.middleware.RequestLoggingMiddleware',
]
