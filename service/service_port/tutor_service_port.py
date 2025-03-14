from abc import ABC, abstractmethod

from domain.model.tutor import Tutor


# Los puertos de servicio en el dominio declaran 
class TutorServicePort(ABC):
    
    @abstractmethod
    def crear_tutor(self, tutor: Tutor) -> Tutor:
        """Crea un nuevo tutor en la base de datos."""
        pass

    @abstractmethod
    def obtener_tutor(self, tutor_id: str) -> Tutor:
        """Obtiene un tutor por su ID."""
        pass