"""Main URLs module."""

# Django Configurations
from django.conf import settings

from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    # Django Admin
    path(settings.ADMIN_URL, admin.site.urls),

    path('', include(('hmbooks.health_checks.urls', 'health_checks'), namespace='health')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
