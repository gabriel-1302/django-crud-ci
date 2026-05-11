# django-crud-ci

API REST de gestión de tareas construida con Django REST Framework.
Incluye un pipeline de CI completo con GitHub Actions.

![CI](https://github.com/gabriel-1302/django-crud-ci/actions/workflows/ci.yml/badge.svg)

## Endpoints

| Método | URL                    | Descripción             |
|--------|------------------------|-------------------------|
| GET    | /api/tareas/           | Listar todas las tareas |
| POST   | /api/tareas/           | Crear una tarea         |
| GET    | /api/tareas/{id}/      | Obtener una tarea       |
| PUT    | /api/tareas/{id}/      | Actualizar una tarea    |
| PATCH  | /api/tareas/{id}/      | Actualizar parcialmente |
| DELETE | /api/tareas/{id}/      | Eliminar una tarea      |
| GET    | /api/health/           | Health check            |

## Setup local

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Ejecutar pruebas

```bash
pytest --cov=api --cov-report=term-missing
```

## Documentación del Laboratorio

Puedes encontrar el informe completo con capturas de pantalla y evidencias en:

- [Ver informe del laboratorio](./INFORME.md)
