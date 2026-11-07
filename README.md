# Biblioteca API

Proyecto Django REST Framework para administrar libros de una biblioteca y sus reseñas. La API incluye CRUD con ViewSets, serializers anidados, permisos y autenticación JWT.

## Requisitos

- Python 3.10 o superior
- [uv](https://docs.astral.sh/uv/)

## Preparar y ejecutar

Desde esta carpeta, en una terminal:

```bash
uv sync
uv run python manage.py migrate
uv run python manage.py createsuperuser
uv run python manage.py runserver
```

En el primer inicio, Django genera una clave secreta local en `.django_secret`; el archivo está excluido de Git.

La interfaz visual queda en `http://127.0.0.1:8000/` y la API en `http://127.0.0.1:8000/api/`.

Desde la portada podés buscar, agregar, editar y borrar libros. La pantalla se conecta a los mismos endpoints de la API.

## Endpoints

| Método | Ruta | Acción |
| --- | --- | --- |
| GET | `/api/libros/` | Listar libros con sus reseñas anidadas |
| POST | `/api/libros/` | Crear un libro (JWT requerido) |
| GET | `/api/libros/<id>/` | Ver un libro y sus reseñas |
| PUT / PATCH / DELETE | `/api/libros/<id>/` | Actualizar o eliminar un libro (JWT requerido) |
| GET | `/api/resenas/` | Listar todas las reseñas |
| GET | `/api/resenas/?libro=<id>` | Filtrar reseñas por libro |
| POST | `/api/resenas/` | Crear una reseña (JWT requerido) |
| GET / PUT / PATCH / DELETE | `/api/resenas/<id>/` | Consultar, actualizar o eliminar (JWT requerido para cambios) |
| GET | `/api/catalogo/` y `/api/catalogo/<id>/` | Catálogo de solo lectura |
| POST | `/api/token/` | Obtener tokens de acceso y refresco |
| POST | `/api/token/refresh/` | Renovar el token de acceso |

El router está definido en `libros/routers.py`. `LibroViewSet` y `ResenaViewSet` heredan de `ModelViewSet`; `LibroCatalogoViewSet` hereda de `ReadOnlyModelViewSet`. Las lecturas son públicas; crear, editar y borrar requieren un token JWT. También está habilitada SessionAuthentication para la interfaz navegable de DRF.

## Probar autenticación y permisos

1. Creá un usuario con `uv run python manage.py createsuperuser` y seguí las preguntas de la terminal.
2. En Postman, Bruno o Thunder Client, enviá un `POST` a `http://127.0.0.1:8000/api/token/` con `Content-Type: application/json` y el usuario y contraseña:

   ```json
   {"username": "tu_usuario", "password": "tu_contraseña"}
   ```

3. Copiá el valor de `access` de la respuesta. En las operaciones que modifican datos, agregá el encabezado `Authorization: Bearer TU_ACCESS_TOKEN`.
4. Probá crear una reseña en `POST /api/resenas/`, usando un ID de libro que exista:

   ```json
   {"libro": 1, "lector": "Ana", "comentario": "Una historia que me encantó.", "puntuacion": 5}
   ```

5. Consultá `GET /api/libros/1/` para ver la reseña anidada. Probá también `PATCH` y `DELETE` sobre `/api/resenas/ID/` con el mismo encabezado.
6. Como comprobación del permiso, intentá un `POST` sin token: debe responder `401 Unauthorized`.

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
git commit -m "Agregar ViewSets, permisos y autenticacion JWT"
git push
```
