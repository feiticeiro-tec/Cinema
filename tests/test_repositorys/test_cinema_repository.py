from database.models import Cinema
from database.repositorys.cinema import CinemaRepository


def test_use_by_id(app):
    with app.app_context():
        cinema = Cinema(
            nome="Cinema 1",
            descricao="Cinema 1",
            cep="00000000",
            uf="Estado 1",
            cidade="Cidade 1",
            bairro="Bairro 1",
            rua="Rua 1",
            numero=1,
            complemento="Complemento 1",
        )
        app.db.session.add(cinema)
        app.db.session.commit()
        cinema_id = cinema.id

    with app.app_context():
        repo = CinemaRepository.use_by_id(cinema_id)
        assert repo
        assert repo.cinema.id == cinema_id
        assert isinstance(repo, CinemaRepository)
        assert isinstance(repo.cinema, Cinema)
