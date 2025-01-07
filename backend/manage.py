#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ashker_credit.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and available on your PYTHONPATH?"
            )
        raise
    execute_from_command_line(sys.argv)



# settings.py

import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from the .env file

# Retrieve the environment variables
SECRET_KEY = os.getenv('SECRET_KEY', 'default-secret-key')  # Use default if not found
DEBUG = os.getenv('DEBUG', 'False') == 'True'  # Convert 'True'/'False' string to boolean

# Database configuration
DATABASE_URL = os.getenv('DATABASE_URL')

# You can use `DATABASE_URL` directly to configure your database connection,
# for example, using `dj-database-url` for PostgreSQL:

import dj_database_url

DATABASES = {
    'default': dj_database_url.config(default=DATABASE_URL)
}

