from typing import Generator
from contextlib import contextmanager



from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from infrastructure.database.models import Base

DATABASE_URL = "sqlite:///jumping_kids_pre.db"

engine = create_engine(DATABASE_URL, echo=True)

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