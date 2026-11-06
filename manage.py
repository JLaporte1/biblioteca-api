#!/usr/bin/env python
"""Utilidad de línea de comandos de Django."""
import os
import sys


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "biblioteca.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "No se encontraron las dependencias. Instala el proyecto con: uv sync"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
