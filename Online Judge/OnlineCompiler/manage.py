#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os  # Import the os module to interact with the operating system
import sys  # Import the sys module to access command-line arguments

def main():
    """Run administrative tasks."""
    # Set the default value for the DJANGO_SETTINGS_MODULE environment variable
    # This tells Django which settings module to use for the project
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'OnlineCompiler.settings')
    
    try:
        # Try to import the execute_from_command_line function from django.core.management
        # This function is used to execute the command-line utility
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # If the import fails, raise an ImportError with a helpful error message
        # This usually happens if Django is not installed or the virtual environment is not activated
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    # Call the execute_from_command_line function with the command-line arguments
    # This will execute the appropriate Django management command based on the arguments provided
    execute_from_command_line(sys.argv)

# If this script is executed as the main program, call the main function
if __name__ == '__main__':
    main()