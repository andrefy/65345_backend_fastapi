# BACKEND usando FastAPI

## Persistencia de datos con FastAPI y SQLModel

## Objetivo

Implementar una API básica utilizando FastAPI y SQLModel, incorporando una base de datos que permita almacenar, consultar y administrar información mediante endpoints.

## Instrucciones

Desarrollar una API para gestionar un registro de estudiantes.

### 1. Modelo de datos

Crear un modelo `Estudiante` utilizando SQLModel con los siguientes atributos:

- `id`: identificador autogenerado.
- `nombre`: nombre del estudiante.
- `apellido`: apellido del estudiante.
- `correo`: correo electrónico.
- `edad`: edad del estudiante.

### 2. Conexión con la base de datos

- Configurar una base de datos SQLite local.
- Crear la conexión utilizando SQLModel.
- Generar automáticamente la tabla correspondiente.
- Configurar la inicialización de la base de datos al iniciar FastAPI.

### 3. Desarrollo de endpoints

Implementar los siguientes endpoints:

| Método | Endpoint            | Funcionalidad                    |
| ------ | ------------------- | -------------------------------- |
| POST   | `/estudiantes/`     | Registrar un estudiante.         |
| GET    | `/estudiantes/`     | Consultar todos los estudiantes. |
| GET    | `/estudiantes/{id}` | Consultar un estudiante por ID.  |
| DELETE | `/estudiantes/{id}` | Eliminar un estudiante.          |

## Guia Instalación

Instalación:

```bash
python3 -m venv .venv
```

Activar ambiente

```bash
source .venv/bin/activate
```

Instalar dependencias
```bash
python3 -m pip install -r requirements.txt
```

Iniciar FastAPI

```bash
uvicorn main:app --reload
```



