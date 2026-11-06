from django.urls import path
from . import views

urlpatterns = [
    path("libros/", views.LibroListCreateView.as_view(), name="lista-libros"),
    path("libros/<int:libro_id>/", views.LibroDetailView.as_view(), name="detalle-libro"),
    path("resenas/", views.ResenaListCreateView.as_view(), name="lista-resenas"),
    path("resenas/<int:pk>/", views.ResenaDetailView.as_view(), name="detalle-resena"),
]
