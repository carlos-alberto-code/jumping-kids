from datetime import date
from dataclasses import dataclass

from domain.model.nino import Nino
from domain.model.nivel_rutina import NivelRutina
from domain.model.rutina import Rutina


@dataclass
class Asignacion:
    nino: Nino
    rutina: Rutina
    nivel_rutina: NivelRutina
    fecha: date
    hecho: bool