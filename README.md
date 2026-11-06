# Biblioteca API

Proyecto Django REST Framework para administrar libros de una biblioteca y sus reseñas. Incluye CRUD con `@api_view` y vistas genéricas basadas en clases.

## Requisitos

- Python 3.10 o superior
- [uv](https://docs.astral.sh/uv/)

## Preparar y ejecutar

Desde esta carpeta, en una terminal:

```bash
uv sync
uv run python manage.py migrate
uv run python manage.py runserver
```

La interfaz visual queda en `http://127.0.0.1:8000/` y la API en `http://127.0.0.1:8000/api/`.

Desde la portada podés buscar, agregar, editar y borrar libros. La pantalla se conecta a los mismos endpoints de la API.

## Endpoints

| Método | Ruta | Acción |
| --- | --- | --- |
| GET | `/api/libros/` | Listar libros con sus reseñas anidadas |
| POST | `/api/libros/` | Crear un libro |
| GET | `/api/libros/<id>/` | Ver un libro y sus reseñas |
| PUT / PATCH / DELETE | `/api/libros/<id>/` | Actualizar o eliminar un libro |
| GET | `/api/resenas/` | Listar todas las reseñas |
| GET | `/api/resenas/?libro=<id>` | Filtrar reseñas por libro |
| POST | `/api/resenas/` | Crear una reseña vinculada a un libro |
| GET / PUT / PATCH / DELETE | `/api/resenas/<id>/` | Consultar, actualizar o eliminar una reseña |

Las rutas de libros usan `ListCreateAPIView` y `RetrieveUpdateDestroyAPIView`. Las reseñas tienen los mismos tipos de vista genérica. El serializer de libros incluye el serializer de reseñas en el campo `resenas`.

Ejemplo de JSON para crear un libro:

```json
{
  "titulo": "El túnel",
  "autor": "Ernesto Sabato",
  "anio_publicacion": 1948,
  "disponible": true
}
```

Ejemplo de JSON para crear una reseña (el `libro` debe ser un ID existente):

```json
{
  "libro": 1,
  "lector": "Ana",
  "comentario": "Una historia que me encantó.",
  "puntuacion": 5
}
```

La puntuación permitida va de 1 a 5. Al consultar libros, cada objeto incluye su lista `resenas`.

`disponible` puede omitirse al crear; su valor predeterminado es `true`. Django REST Framework ofrece una interfaz navegable para probar los endpoints desde el navegador. También se pueden usar Postman, Bruno o Thunder Client, enviando `Content-Type: application/json` en las solicitudes con cuerpo.

## Subir el proyecto a GitHub

Para publicar cambios en el repositorio existente, desde esta carpeta ejecutá:

```bash
git add .
git commit -m "Agregar reseñas y vistas genericas"
git push
```
