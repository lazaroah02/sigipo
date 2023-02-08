#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import sys

# Build paths inside the project like this: BASE_DIR / 'subdir'.


def main():
    """Run administrative tasks."""
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:  # pragma: no cover
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    from dotenv import find_dotenv, load_dotenv

    load_dotenv(find_dotenv())

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
