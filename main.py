from infrastructure.model.models import CategoriaEntity
from infrastructure.repository.repository import Repository
from infrastructure.database.connection import get_session


with get_session() as session:
    repo = Repository[CategoriaEntity](model=CategoriaEntity, session=session)
    repo.add(CategoriaEntity(id=1, nombre="Categoria 1"))
    repo.delete(CategoriaEntity(id=1, nombre="Categoria 1"))
    repo.update(CategoriaEntity(id=1, nombre="Categoria 2"))
    repo.get_by_id(id=1)


CategoriaEntity.id
CategoriaEntity.nombre