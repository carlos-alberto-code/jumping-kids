from domain.model.tutor import Tutor
from domain.service.port.tutor_repository_port import TutorRepositoryPort


class TutorRepositoryAdpater(TutorRepositoryPort):
    
    def get_by_id(self, id: int) -> Tutor | None:
        return super().get_by_id(id)
    
    def save(self, tutor: Tutor) -> Tutor:
        return super().save(tutor)