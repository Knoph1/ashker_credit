STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# settings.py

# Static files (CSS, JavaScript, images)
STATIC_URL = '/static/'

# The path where static files will be stored during development
STATICFILES_DIRS = [
    BASE_DIR / "static",  # Add a "static" folder at the root of your project
]

# Folder to collect static files during `python manage.py collectstatic`
STATIC_ROOT = BASE_DIR / "staticfiles"

# settings.py

# Production static file storage using S3
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_ACCESS_KEY_ID = 'your-access-key'
AWS_SECRET_ACCESS_KEY = 'your-secret-key'
AWS_STORAGE_BUCKET_NAME = 'your-bucket-name'
AWS_S3_REGION_NAME = 'your-region'
AWS_DEFAULT_ACL = None  # Optional: Ensure public access is restricted

# settings.py

# For serving files in production:
STATIC_URL = '/static/'

# Path to the directory where static files will be stored
STATIC_ROOT = BASE_DIR / 'staticfiles'

# AWS S3 config if needed
AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"

python manage.py collectstatic
