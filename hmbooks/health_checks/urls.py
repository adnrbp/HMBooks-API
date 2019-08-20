"""Health Check URLs"""

# Django
from django.urls import path

# Views
from hmbooks.health_checks.views import health

urlpatterns = [
    path('health/', health, name="health"),
]