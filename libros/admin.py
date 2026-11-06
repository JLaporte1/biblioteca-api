from django.contrib import admin
from .models import Libro, Resena


@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "anio_publicacion", "disponible")
    search_fields = ("titulo", "autor")
    list_filter = ("disponible", "anio_publicacion")


@admin.register(Resena)
class ResenaAdmin(admin.ModelAdmin):
    list_display = ("libro", "lector", "puntuacion", "fecha")
    list_filter = ("puntuacion", "fecha")
    search_fields = ("libro__titulo", "lector", "comentario")
