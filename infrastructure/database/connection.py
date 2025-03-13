import os
from dotenv import load_dotenv

from typing import Generator
from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from infrastructure.database.models import Base


load_dotenv() # Cargar variables de entorno desde el archivo .env
JUMPING_KIDS_PRE = os.getenv("JUMPING_KIDS_PRE", "sqlite:///:memory:") # Asigna una base de datos en memoria si no se encuentra la variable de entorno

engine = create_engine(JUMPING_KIDS_PRE, echo=True)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Función para inicializar la base de datos
def init_db():
    Base.metadata.create_all(bind=engine)

@contextmanager
def get_session() -> Generator[Session, None, None]:
    """Generador de sesión para la base de datos."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()