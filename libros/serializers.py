from rest_framework import serializers
from .models import Libro, Resena


class ResenaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resena
        fields = ["id", "libro", "lector", "comentario", "puntuacion", "fecha"]
        read_only_fields = ["id", "fecha"]

    def validate_puntuacion(self, value):
        if not 1 <= value <= 5:
            raise serializers.ValidationError("La puntuación debe estar entre 1 y 5.")
        return value


class LibroSerializer(serializers.ModelSerializer):
    resenas = ResenaSerializer(many=True, read_only=True)

    class Meta:
        model = Libro
        fields = ["id", "titulo", "autor", "anio_publicacion", "disponible", "resenas"]
        read_only_fields = ["id"]
