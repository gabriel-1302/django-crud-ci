# Informe — Laboratorio 5.1: CI con GitHub Actions y Django

## Descripción del proyecto

API REST de gestión de tareas construida con **Django 5** y **Django REST Framework**.
Expone endpoints CRUD completos para el modelo `Tarea` y un endpoint de health check.

### Stack tecnológico

- Python 3.12
- Django 5.x
- Django REST Framework
- pytest + pytest-django + pytest-cov
- flake8 (linting)
- GitHub Actions (CI)

## Pipeline de CI configurado

El workflow `.github/workflows/ci.yml` ejecuta los siguientes pasos en cada push y PR a `main`:

1. **Checkout** — descarga el código del repositorio
2. **Setup Python 3.12** — configura el entorno de ejecución
3. **Instalar dependencias** — `pip install -r requirements.txt`
4. **Linting con flake8** — análisis estático de código
5. **Migraciones** — aplica migraciones de base de datos para el entorno de test
6. **Pruebas con cobertura** — ejecuta pytest con reporte de cobertura
7. **Subir artefacto** — guarda `coverage.xml` como artefacto descargable

## Capturas de evidencia

### Historial de ejecuciones en Actions

<!-- Insertar captura de la pestaña Actions con múltiples ejecuciones -->

### Workflow exitoso con cobertura

<!-- Insertar captura de un workflow completo con todos los pasos en verde y el reporte de cobertura -->

### Workflow fallido por linting

<!-- Insertar captura del workflow fallando en el paso de flake8 con el mensaje de error -->

### Merge bloqueado por CI pendiente

<!-- Insertar captura del PR con el mensaje "Some checks haven't completed yet" y el botón de merge desactivado -->

### Configuración de Branch Protection Rule

<!-- Insertar captura de Settings > Branches mostrando la regla configurada sobre main -->

## Resultados de cobertura

| Módulo             | Statements | Missed | Cover |
|--------------------|-----------|--------|-------|
| api/models.py      | 7         | 0      | 100%  |
| api/serializers.py | 6         | 0      | 100%  |
| api/views.py       | 8         | 0      | 100%  |
| api/urls.py        | 5         | 0      | 100%  |
| **TOTAL**          | **26**    | **0**  | **100%** |

## Conclusiones

La integración de GitHub Actions en este proyecto demostró que la automatización del pipeline de CI aporta valor concreto en varios niveles:

**Detección temprana de errores:** El linting con flake8 detectó variables no utilizadas y problemas de estilo antes de que el código llegara a revisión. Esto reduce el tiempo que los revisores dedican a señalar problemas superficiales.

**Confianza en los merges:** La branch protection rule garantiza que ningún código con pruebas fallidas pueda integrarse a `main`. El equipo puede hacer merge con confianza sabiendo que la suite de pruebas pasó en un entorno limpio e independiente.

**Reproducibilidad:** Al usar `pip install -r requirements.txt` con versiones fijadas, cada ejecución del CI instala exactamente las mismas dependencias. Esto elimina la clase de bugs "funciona en mi máquina".

**Visibilidad de cobertura:** El reporte de cobertura subido como artefacto permite rastrear qué código está siendo ejercido por las pruebas. Mantener la cobertura en 100% para los módulos core obliga a escribir pruebas junto con el código de producción.
