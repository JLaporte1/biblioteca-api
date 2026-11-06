from django.contrib import admin
from .models import Libro


@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "anio_publicacion", "disponible")
    search_fields = ("titulo", "autor")
    list_filter = ("disponible", "anio_publicacion")
