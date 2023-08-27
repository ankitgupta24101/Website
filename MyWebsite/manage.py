#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import subprocess


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MyWebsite.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


def install_packages_from_requirements(requirements_file):
    try:
        subprocess.check_call(["pip", "install", "-r", requirements_file])
        print("Packages installed successfully.")
    except subprocess.CalledProcessError as e:
        print("An error occurred while installing packages:", e)


if __name__ == "__main__":
    install_packages_from_requirements("requirements.txt")
    main()
