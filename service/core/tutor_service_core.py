from domain.model.tutor import Tutor
from domain.service.service_port.tutor_service_port import TutorServicePort
from domain.service.port.tutor_repository_port import TutorRepositoryPort

# Los servicios core usan los puertos de repositorio para interactuar con la base de datos.
# El servicio core es el que implementa la lógica de negocio.
class TutorServiceCore(TutorServicePort):

    def __init__(self, tutor_repository_port: TutorRepositoryPort) -> None:
        super().__init__()
        self._tutor_repository_port = tutor_repository_port
    
    def crear_tutor(self, tutor: Tutor) -> Tutor:
        return self._tutor_repository_port.save(tutor=tutor)

    def obtener_tutor(self, tutor_id: int) -> Tutor | None:
        return self._tutor_repository_port.get_by_id(id=tutor_id)