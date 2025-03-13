from dataclasses import dataclass
from domain.model.categoria import Categoria


@dataclass
class Rutina:
    id: int
    nombre: str
    descripcion: str
    categoria: Categoria