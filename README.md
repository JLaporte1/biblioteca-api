# Biblioteca API

Este es mi proyecto para practicar Django REST Framework. Permite guardar libros y reseñas. Cada reseña pertenece a un libro y, cuando consulto un libro, también puedo ver sus reseñas.

## Qué tiene

- Modelo `Libro` y modelo `Resena`, relacionados con una clave foránea.
- Serializers para los dos modelos. El de libros muestra las reseñas anidadas.
- ViewSets para crear, consultar, editar y borrar libros y reseñas.
- Un catálogo de solo lectura hecho con `ReadOnlyModelViewSet`.
- Permisos: cualquiera puede consultar; para crear, editar o borrar hay que iniciar sesión con JWT.
- Una página simple para ver y administrar los libros.

## Requisitos

- Python 3.10 o superior
- [uv](https://docs.astral.sh/uv/)

## Cómo ejecutar el proyecto

Abrí una terminal en la carpeta del proyecto y ejecutá:

```bash
uv sync
uv run python manage.py migrate
uv run python manage.py createsuperuser
uv run python manage.py runserver
```

Cuando crees el usuario, anotá el nombre y la contraseña: los vas a necesitar para iniciar sesión y pedir un token. La primera vez que se ejecuta Django se crea el archivo `.django_secret`. Ese archivo es privado y no se sube a GitHub.

- Página de la biblioteca: <http://127.0.0.1:8000/>
- API de libros: <http://127.0.0.1:8000/api/libros/>
- Catálogo de solo lectura: <http://127.0.0.1:8000/api/catalogo/>

## Rutas de la API

| Método | Ruta | Para qué sirve |
| --- | --- | --- |
| GET, POST | `/api/libros/` | Ver los libros o crear uno |
| GET, PUT, PATCH, DELETE | `/api/libros/<id>/` | Consultar, editar o borrar un libro |
| GET, POST | `/api/resenas/` | Ver las reseñas o crear una |
| GET, PUT, PATCH, DELETE | `/api/resenas/<id>/` | Consultar, editar o borrar una reseña |
| GET | `/api/resenas/?libro=<id>` | Ver las reseñas de un libro |
| GET | `/api/catalogo/` y `/api/catalogo/<id>/` | Consultar el catálogo, sin modificarlo |
| POST | `/api/token/` | Obtener los tokens JWT |
| POST | `/api/token/refresh/` | Renovar el token de acceso |

Las rutas de libros y reseñas usan `ModelViewSet`. El catálogo usa `ReadOnlyModelViewSet`. El router que conecta las rutas con los ViewSets está en `libros/routers.py`.

## Probar con Postman

Primero hay que pedir un token. En Postman, hacé un `POST` a:

```text
http://127.0.0.1:8000/api/token/
```

En **Body → raw → JSON**, mandá tu usuario y contraseña:

```json
{
  "username": "tu_usuario",
  "password": "tu_contraseña"
}
```

La respuesta trae `access` y `refresh`. Para crear, editar o borrar, usá el valor de `access` en **Authorization → Bearer Token**. No hace falta iniciar sesión para hacer consultas `GET`.

Por ejemplo, para crear una reseña, hacé un `POST` a `/api/resenas/` con el token y este JSON. El número de `libro` tiene que ser el ID de un libro existente:

```json
{
  "libro": 1,
  "lector": "Ana",
  "comentario": "Una historia que me encantó.",
  "puntuacion": 5
}
```

La puntuación va de 1 a 5. Después podés hacer un `GET` a `/api/libros/1/` para ver el libro y sus reseñas.

## Subir cambios a GitHub

Desde la carpeta del proyecto, ejecutá:

```bash
git add .
git commit -m "Actualizar README"
git push
```
