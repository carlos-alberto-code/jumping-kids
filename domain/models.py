from dataclasses import dataclass
import datetime


@dataclass
class Categoria:
    id: int
    nombre: str


@dataclass
class Rutina:
    id: int
    nombre: str
    descripcion: str
    categoria: Categoria


@dataclass
class Ejercicio:
    id: int
    nombre: str
    descripcion: str


@dataclass
class RutinaEjercicio:
    rutina: Rutina
    ejercicio: Ejercicio


@dataclass
class Tutor:
    id: int
    nombre_completo: str


@dataclass
class Nino:
    id: int
    nombre_completo: str
    edad: int
    tutor: Tutor


@dataclass
class NivelRutina:
    id: int
    nivel: int
    tiempo: int
    valor_medalla: int


@dataclass
class Asignacion:
    nino: Nino
    rutina: Rutina
    nivel_rutina: NivelRutina
    fecha: datetime.date
    hecho: bool
