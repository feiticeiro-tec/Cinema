from database.repositorys.sala import SalaRepository, Sala
from database.repositorys.cinema import CinemaRepository
from database import db
import pytest


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


def test_get_by_id_not_found(app):
    with app.app_context():
        with pytest.raises(SalaRepository.NotFoundSalaException):
            SalaRepository.get_by_id("123")


def test_use_by_id(app):
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
        repo = SalaRepository.use_by_id(sala_id)
        assert repo.sala.nome == "sala"
        assert repo.sala.descricao == "descricao"
        assert repo.sala.cinema_id == cinema_id


def test_use_by_id_not_found(app):
    with app.app_context():
        with pytest.raises(SalaRepository.NotFoundSalaException):
            SalaRepository.use_by_id("123")


def test_new(app):
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

    with app.app_context():
        repo = SalaRepository.new(
            nome="sala",
            descricao="descricao",
            cinema_id=cinema_id,
        )
        repo.add()
        repo.commit()
        sala_id = repo.sala.id

    with app.app_context():
        sala = Sala.query.filter(Sala.id == sala_id).first()
        assert sala.nome == "sala"
        assert sala.descricao == "descricao"
        assert sala.cinema_id == cinema_id
