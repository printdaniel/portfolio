from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('home.urls')),
    path("", include('about.urls')),
    path("", include('projects.urls')),
    path("", include('contact.urls')),
]
