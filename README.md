# Biblioteca API

Proyecto Django REST Framework para administrar libros de una biblioteca. Incluye un modelo, un serializer y endpoints CRUD implementados con `@api_view`.

## Requisitos

- Python 3.10 o superior
- [uv](https://docs.astral.sh/uv/)

## Preparar y ejecutar

Desde esta carpeta, en una terminal:

```bash
uv sync
uv run python manage.py makemigrations libros
uv run python manage.py migrate
uv run python manage.py runserver
```

La interfaz visual queda en `http://127.0.0.1:8000/` y la API en `http://127.0.0.1:8000/api/`.

Desde la portada podés buscar, agregar, editar y borrar libros. La pantalla se conecta a los mismos endpoints de la API.

## Endpoints

| Método | Ruta | Acción |
| --- | --- | --- |
| GET | `/api/libros/` | Listar libros |
| POST | `/api/libros/` | Crear un libro |
| GET | `/api/libros/<id>/` | Ver un libro |
| PUT | `/api/libros/<id>/` | Reemplazar todos sus datos |
| PATCH | `/api/libros/<id>/` | Actualizar algunos datos |
| DELETE | `/api/libros/<id>/` | Eliminar un libro |

Ejemplo de JSON para crear un libro:

```json
{
  "titulo": "El túnel",
  "autor": "Ernesto Sabato",
  "anio_publicacion": 1948,
  "disponible": true
}
```

`disponible` puede omitirse al crear; su valor predeterminado es `true`. Django REST Framework ofrece una interfaz navegable para probar los endpoints desde el navegador. También se pueden usar Postman, Bruno o Thunder Client, enviando `Content-Type: application/json` en las solicitudes con cuerpo.

## Subir el proyecto a GitHub

Creá un repositorio vacío en GitHub y, desde esta carpeta, ejecutá:

```bash
git init
git add .
git commit -m "Crear API de biblioteca con Django REST Framework"
git branch -M main
git remote add origin URL_DEL_REPOSITORIO
git push -u origin main
```
