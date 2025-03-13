from domain.service.port.tutor_service_port import TutorServicePort
from domain.service.repo.tutor_repository_port import TutorRepositoryPort


class TutorServiceCore(TutorServicePort):

    tutor_repository_port: TutorRepositoryPort