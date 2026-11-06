from django.shortcuts import render
from rest_framework import generics

from .models import Libro, Resena
from .serializers import LibroSerializer, ResenaSerializer


def inicio(request):
    """Sirve la interfaz visual de la biblioteca."""
    return render(request, "libros/index.html")


class LibroListCreateView(generics.ListCreateAPIView):
    """Lista libros y permite crear uno (GET, POST)."""
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer


class LibroDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Consulta, actualiza o elimina un libro (GET, PUT, PATCH, DELETE)."""
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    lookup_url_kwarg = "libro_id"


class ResenaListCreateView(generics.ListCreateAPIView):
    """Lista reseñas o crea una vinculada a un libro."""
    serializer_class = ResenaSerializer

    def get_queryset(self):
        queryset = Resena.objects.select_related("libro").all()
        libro_id = self.request.query_params.get("libro")
        if libro_id:
            queryset = queryset.filter(libro_id=libro_id)
        return queryset


class ResenaDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Consulta, actualiza o elimina una reseña."""
    queryset = Resena.objects.select_related("libro").all()
    serializer_class = ResenaSerializer
