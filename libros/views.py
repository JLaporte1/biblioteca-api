from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Libro, Resena
from .serializers import LibroSerializer, ResenaSerializer


def inicio(request):
    """Sirve la interfaz visual de la biblioteca."""
    return render(request, "libros/index.html")


class LibroViewSet(viewsets.ModelViewSet):
    """CRUD completo de libros; las escrituras requieren autenticación."""
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class LibroCatalogoViewSet(viewsets.ReadOnlyModelViewSet):
    """Endpoint de solo lectura para demostrar ReadOnlyModelViewSet."""
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ResenaViewSet(viewsets.ModelViewSet):
    """CRUD completo de reseñas, con filtro opcional por libro."""
    serializer_class = ResenaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Resena.objects.select_related("libro").all()
        libro_id = self.request.query_params.get("libro")
        if libro_id:
            queryset = queryset.filter(libro_id=libro_id)
        return queryset
