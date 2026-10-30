from fastapi import FastAPI, HTTPException, status
from sqlmodel import SQLModel, Field, create_engine, Session, select


# Modelo de la tabla de estudiantes
class Estudiante(SQLModel, table=True):
    """
    Datos del estudiante guardados en la base de datos
    """
    id: int | None = Field(default=None, primary_key=True)
    nombre: str
    apellido: str
    correo: str
    edad: int
    
# Datos para registrar un estudiante
class EstudianteCreate(SQLModel):
    """
    Datos necesarios para crear un estudiante
    """
    nombre: str
    apellido: str
    correo: str
    edad: int

class EstudianteRead(EstudianteCreate):
    """
    Datos del estudiante que devuelve la API, incluyendo su id
    """
    id: int

# Ruta de la base de datos SQLite
sqlite_url = "sqlite:///estudiantes.db"

# Crear la conexión con la base de datos
engine = create_engine(
    sqlite_url, 
    echo=True,
    connect_args={"check_same_thread": False},
)

app = FastAPI(title="API de estudiantes")


@app.on_event("startup")
def crear_tablas():
    """
    Crear las tablas al iniciar la API si todavía no existen
    """
    SQLModel.metadata.create_all(engine)

@app.get("/")
def read_root():
    """
    Mostrar el mensaje de inicio y la ruta de la documentación
    """
    return {"mensaje": "API de estudiantes", "documentacion": "/docs"}


@app.post("/estudiantes/", status_code=status.HTTP_201_CREATED, response_model=EstudianteRead)
def crear_estudiante(datos: EstudianteCreate):
    """
    Registrar un estudiante en la base de datos
    """
    estudiante = Estudiante(
        nombre=datos.nombre,
        apellido=datos.apellido,
        correo=datos.correo,
        edad=datos.edad,
    )
    with Session(engine) as session:
        session.add(estudiante)
        session.commit()
        session.refresh(estudiante)
        return estudiante


@app.get("/estudiantes/", response_model=list[EstudianteRead])
def obtener_estudiantes():
    """
    Obtener todos los estudiantes ordenados por id
    """
    with Session(engine) as session:
        return session.exec(select(Estudiante).order_by(Estudiante.id)).all()


@app.get("/estudiantes/{id}", response_model=EstudianteRead)
def obtener_estudiante(id: int):
    """
    Obtener estudiante por id
    """
    with Session(engine) as session:
        estudiante = session.get(Estudiante, id)
        if estudiante is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Estudiante no encontrado")
        return estudiante


@app.delete("/estudiantes/{id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_estudiante(id: int):
    """
    Eliminar un estudiante por id
    """
    with Session(engine) as session:
        estudiante = session.get(Estudiante, id)
        if estudiante is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Estudiante no encontrado")
        session.delete(estudiante)
        session.commit()
    raise HTTPException(status_code=status.HTTP_204_NO_CONTENT)
