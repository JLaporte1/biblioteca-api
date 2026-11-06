from rest_framework import serializers
from .models import Libro


class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = ["id", "titulo", "autor", "anio_publicacion", "disponible"]
        read_only_fields = ["id"]
