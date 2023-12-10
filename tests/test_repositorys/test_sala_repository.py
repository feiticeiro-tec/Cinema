from database.repositorys.sala import SalaRepository, Sala
from database.repositorys.cinema import CinemaRepository
from database import db


def test_get_by_id(app):
    with app.app_context():
        cinema = CinemaRepository.new(
            nome="cinema",
            descricao="descricao",
            endereco=CinemaRepository.Endereco(
                cep="00000000",
                uf="uf",
                cidade="cidade",
                bairro="bairro",
                rua="rua",
                numero=2,
                complemento="complemento",
                referencia="referencia",
            ),
        )
        cinema.add()
        db.session.flush()
        cinema_id = cinema.cinema.id
        sala = Sala(
            nome="sala",
            descricao="descricao",
            cinema_id=cinema_id,
        )
        db.session.add(sala)
        db.session.commit()
        sala_id = sala.id

    with app.app_context():
        sala = SalaRepository.get_by_id(sala_id)
        assert sala.nome == "sala"
        assert sala.descricao == "descricao"
        assert sala.cinema_id == cinema_id
