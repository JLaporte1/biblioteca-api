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
