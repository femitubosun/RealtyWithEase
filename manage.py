#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from validator import validate
from dotenv import load_dotenv

from Env import EnvironmentVariablesSchema

load_dotenv()


def main():
    """Run administrative tasks."""

    # Validate environment variables
    environment_variables = dict(os.environ)

    is_valid, _, errors = validate(
        environment_variables, EnvironmentVariablesSchema, return_info=True
    )

    if not is_valid:
        raise Exception(
            f"Invalid environment variables: {errors}.\nPlease Update your .env file"
        )

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
