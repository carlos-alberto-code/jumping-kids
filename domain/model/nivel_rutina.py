from dataclasses import dataclass


@dataclass
class NivelRutina:
    id: int
    nivel: int
    tiempo: int
    valor_medalla: int