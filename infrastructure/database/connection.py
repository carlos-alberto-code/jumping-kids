import os
from dotenv import load_dotenv

from typing import Generator
from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from infrastructure.model.models import Base


load_dotenv() # Cargar variables de entorno desde el archivo .env
DATABASE_URL_PRE = os.getenv("DATABASE_URL_PRE", "sqlite:///:memory:") # Asigna una base de datos en memoria si no se encuentra la variable de entorno

engine = create_engine(DATABASE_URL_PRE, echo=True)

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