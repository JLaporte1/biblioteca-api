from django.db import models


class Libro(models.Model):
    titulo = models.CharField(max_length=150)
    autor = models.CharField(max_length=120)
    anio_publicacion = models.PositiveSmallIntegerField()
    disponible = models.BooleanField(default=True)

    class Meta:
        ordering = ["titulo"]

    def __str__(self):
        return f"{self.titulo} — {self.autor}"


class Resena(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name="resenas")
    lector = models.CharField(max_length=100)
    comentario = models.TextField(max_length=500)
    puntuacion = models.PositiveSmallIntegerField()
    fecha = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["-fecha", "id"]

    def __str__(self):
        return f"Reseña de {self.lector} para {self.libro.titulo}"
