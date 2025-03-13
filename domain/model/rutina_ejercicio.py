from dataclasses import dataclass

from domain.model.rutina import Rutina
from domain.model.ejercicio import Ejercicio


@dataclass
class RutinaEjercicio:
    rutina: Rutina
    ejercicio: Ejercicio