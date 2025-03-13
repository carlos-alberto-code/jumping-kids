from infrastructure import Repository, get_session, Categoria


with get_session() as session:
    categoria_repo = Repository[Categoria](Categoria, session)
    print(categoria_repo.get_by_id(1))