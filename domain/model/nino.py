from dataclasses import dataclass

from domain.model.tutor import Tutor


@dataclass
class Nino:
    id: int
    nombre_completo: str
    edad: int
    tutor: Tutor