from datetime import datetime

from sqlalchemy.sql import func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Boolean, Integer, String, ForeignKey, DateTime, Column, Table, CheckConstraint


class Base(DeclarativeBase):
    pass


class Categoria(Base):
    """
    Representa un categoría de rutina. Ejemplos de categorías de rutinas con Yoga, Spinning, Crossfit, Fuerza, Resistencia, etc. Cada categoría puede tener varias rutinas asociadas.
    """
    __tablename__ = "categorias"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)

    def __repr__(self):
        return f"Categoria(id={self.id}, nombre={self.nombre})"


class Rutina(Base):
    """
    Representa una rutina de ejercicios. Cada rutina puede tener un nombre, una descripción y una categoría asociada. Las rutinas pueden estar asociadas a varios ejercicios."
    """
    __tablename__ = "rutinas"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    descripcion: Mapped[str] = mapped_column(String(255), nullable=False)
    categoria_id: Mapped[int] = mapped_column(Integer, ForeignKey("categorias.id"), nullable=False)

    def __repr__(self):
        return f"Rutina(id={self.id}, nombre={self.nombre})"


class Ejercicio(Base):
    """
    Representa un ejercicio individual. Cada ejercicio puede tener un nombre y una descripción. Los ejercicios pueden estar asociados a varias rutinas.
    """
    __tablename__ = "ejercicios"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(50), nullable=False)
    descripcion: Mapped[str] = mapped_column(String(255), nullable=False)

    def __repr__(self):
        return f"Ejercicio(id={self.id}, nombre={self.nombre})"


rutina_ejercicio = Table(
    "rutinas_ejercicios",
    Base.metadata,
    Column("rutina_id", Integer, ForeignKey("rutinas.id"), primary_key=True),
    Column("ejercicio_id", Integer, ForeignKey("ejercicios.id"), primary_key=True),
)


class Tutor(Base):
    """
    Representa un tutor o cuidador de un niño. Cada tutor puede tener un nombre completo y puede estar asociado a varios niños.
    """
    __tablename__ = "tutores"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nombre_completo: Mapped[str] = mapped_column(String(100), nullable=False)

    def __repr__(self):
        return f"Tutor(id={self.id}, nombre={self.nombre_completo})"
    

class Nino(Base):
    """
    Representa un niño que realiza las rutinas. Cada niño puede tener un nombre completo, una edad y un tutor asociado. Los niños pueden estar asociados a varias rutinas a través de la tabla de asignaciones.
    """
    __tablename__ = "ninos"
    __table_args__ = (
        CheckConstraint("edad >= 10", name="check_edad_minima"),
        CheckConstraint("edad <= 15", name="check_edad_maxima"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nombre_completo: Mapped[str] = mapped_column(String(100), nullable=False)
    edad: Mapped[int] = mapped_column(Integer, nullable=False)
    tutor_id: Mapped[int] = mapped_column(Integer, ForeignKey("tutores.id"), nullable=False)

    def __repr__(self):
        return f"Nino(id={self.id}, nombre={self.nombre_completo}, edad={self.edad})"
    

class NivelRutina(Base):
    """
    Representa un nivel de dificultad para una rutina. Cada nivel puede tener un número, un tiempo asociado y un valor de medalla. Los niveles pueden estar asociados a varias rutinas a través de la tabla de asignaciones.
    """
    __tablename__ = "niveles_rutinas"
    __table_args__ = (
        CheckConstraint("valor_medalla IN (1, 2, 3)", name="check_valor_medalla"),
        CheckConstraint("((nivel = 1 AND tiempo BETWEEN 10 AND 15) OR (nivel = 2 AND tiempo BETWEEN 15 AND 20) OR (nivel = 3 AND tiempo BETWEEN 20 AND 30))", name="check_tiempo"),
        CheckConstraint("((nivel = 1 AND valor_medalla = 1) OR (nivel = 2 AND valor_medalla = 2) OR (nivel = 3 AND valor_medalla = 3))", name="check_nivel_valor_medalla"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nivel: Mapped[int] = mapped_column(Integer, nullable=False, unique=True)
    tiempo: Mapped[int] = mapped_column(Integer, nullable=False, unique=True)
    valor_medalla: Mapped[int] = mapped_column(Integer, nullable=False, unique=True)


class Asignacion(Base):
    __tablename__ = "asignaciones"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nino_id: Mapped[int] = mapped_column(Integer, ForeignKey("ninos.id"), nullable=False)
    rutina_id: Mapped[int] = mapped_column(Integer, ForeignKey("rutinas.id"), nullable=False)
    nivel_rutina_id: Mapped[int] = mapped_column(Integer, ForeignKey("niveles_rutinas.id"), nullable=False)
    fecha: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    hecho: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    fecha_completado: Mapped[datetime] = mapped_column(DateTime, nullable=True)