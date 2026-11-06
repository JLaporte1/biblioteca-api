from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render

from .models import Libro
from .serializers import LibroSerializer


def inicio(request):
    """Sirve la interfaz visual de la biblioteca."""
    return render(request, "libros/index.html")


@api_view(["GET", "POST"])
def lista_libros(request):
    """Lista libros o crea uno nuevo."""
    if request.method == "GET":
        libros = Libro.objects.all()
        return Response(LibroSerializer(libros, many=True).data)

    serializer = LibroSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "PATCH", "DELETE"])
def detalle_libro(request, libro_id):
    """Consulta, actualiza o elimina un libro por su identificador."""
    libro = get_object_or_404(Libro, pk=libro_id)

    if request.method == "GET":
        return Response(LibroSerializer(libro).data)
    if request.method in ["PUT", "PATCH"]:
        serializer = LibroSerializer(
            libro, data=request.data, partial=(request.method == "PATCH")
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    libro.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
