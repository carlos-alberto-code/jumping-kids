from domain.service.port.tutor_service_port import TutorServicePort
from infrastructure.repository.adapter.tutor_repository_adapter import TutorRepositoryAdapter


class TutorRepositoryImpl(TutorServicePort):

    def __init__(self) -> None:
        super().__init__()
        self._tutor_repository: TutorRepositoryAdapter
