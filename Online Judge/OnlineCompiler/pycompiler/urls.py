# Import the path and include functions from the django.urls module.
# These functions are used to define URL patterns for the Django application.
from django.urls import path, include

# Import the views module from the current package.
# This module contains the view functions that will handle the requests for the defined URLs.
from . import views

# Define the URL patterns for the application.
# Each entry in the urlpatterns list is a call to the path function, which maps a URL pattern to a view function.
urlpatterns = [
    # Map the root URL ('') to the index view function.
    # The name parameter assigns a name to this URL pattern, which can be used to refer to it in templates and other parts of the code.
    path('', views.index, name="indexpage"),
    
    # Map the 'runcode' URL to the runcode view function.
    # Similarly, the name parameter assigns a name to this URL pattern.
    path('runcode', views.runcode, name="runcode"),
]