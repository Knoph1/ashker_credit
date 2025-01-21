#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myapp.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # Handle the case where the package is not installed
        raise
    execute_from_command_line(sys.argv)
