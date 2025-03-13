from infrastructure import Repository, get_session, Categoria


with get_session() as session:
    categoria_repo = Repository[Categoria](Categoria, session)
    categoria_repo.add(Categoria(nombre="Yoga"))