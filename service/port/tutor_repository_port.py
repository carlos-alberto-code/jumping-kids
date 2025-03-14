# Los puertos en el dominio son interfaces que definen lo que el dominio necesita del exterior.
from abc import ABC, abstractmethod

from domain.model.tutor import Tutor


class TutorRepositoryPort(ABC):

    @abstractmethod
    def get_by_id(self, id: int) -> Tutor | None:
        pass

    @abstractmethod
    def save(self, tutor: Tutor) -> Tutor:
        """Guarda el tutor y lo devuelve cuando se ha guardado en base de datos, permitiendo retornar el id generado."""
        pass