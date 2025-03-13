from datetime import date
from dataclasses import dataclass

from domain.model.nino import Nino
from domain.model.rutina import Rutina
from domain.model.nivel_rutina import NivelRutina


@dataclass
class Asignacion:
    nino: Nino
    rutina: Rutina
    nivel_rutina: NivelRutina
    fecha: date
    hecho: bool