from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("libros.page_urls")),
    path("admin/", admin.site.urls),
    path("api/", include("libros.urls")),
]
