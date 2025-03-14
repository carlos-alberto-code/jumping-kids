import os
from dotenv import load_dotenv

from sqlalchemy import create_engine

from infrastructure.model.models import Base


load_dotenv() # Cargar variables de entorno desde el archivo .env
DATABASE_URL_PRE = os.getenv("DATABASE_URL_PRE", "sqlite:///:memory:") # Asigna una base de datos en memoria si no se encuentra la variable de entorno

engine = create_engine(DATABASE_URL_PRE, echo=True)

Base.metadata.create_all(bind=engine) # Crear todas las tablas en la base de datos
