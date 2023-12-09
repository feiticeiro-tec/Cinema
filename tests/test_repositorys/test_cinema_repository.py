from database.models import Cinema
from database.repositorys.cinema import CinemaRepository
import pytest


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

def test_use_by_id_not_found(app):
    with app.app_context():
        with pytest.raises(CinemaRepository.NotFoundCinemaException):
            CinemaRepository.use_by_id('123')

def test_set_endereco(app):
    with app.app_context():
        cinema = Cinema(
            nome="Cinema 1",
            descricao="Cinema 1",
        )
        enderco = CinemaRepository.Endereco(
            cep="00000000",
            uf="Estado 1",
            cidade="Cidade 1",
            bairro="Bairro 1",
            rua="Rua 1",
            numero=1,
            complemento="Complemento 1",
        )
        repo = CinemaRepository(cinema)
        repo.set_endereco(enderco)
        repo.add()
        repo.commit()
        cinema_id = repo.cinema.id

    with app.app_context():
        cinema = Cinema.query.filter(Cinema.id == cinema_id).first()
        assert cinema
        assert cinema.cep == enderco.cep
        assert cinema.uf == enderco.uf
        assert cinema.cidade == enderco.cidade
        assert cinema.bairro == enderco.bairro
        assert cinema.rua == enderco.rua
        assert cinema.numero == enderco.numero
        assert cinema.complemento == enderco.complemento
        assert cinema.referencia == enderco.referencia


def test_set_info(app):
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
        repo = CinemaRepository(cinema)
        repo.set_infos("Cinema 2", "Cinema 2")
        repo.add()
        repo.commit()
        cinema_id = repo.cinema.id

    with app.app_context():
        cinema = Cinema.query.filter(Cinema.id == cinema_id).first()
        assert cinema
        assert cinema.nome == "Cinema 2"
        assert cinema.descricao == "Cinema 2"


def test_get_by_id(app):
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
        cinema = CinemaRepository.get_by_id(cinema_id)
        assert cinema
        assert cinema.id == cinema_id
        assert isinstance(cinema, Cinema)


def test_get_by_id_not_found(app):
    with app.app_context():
        with pytest.raises(CinemaRepository.NotFoundCinemaException):
            CinemaRepository.get_by_id("123")

def test_new(app):
    with app.app_context():
        endereco = CinemaRepository.Endereco(
            cep="00000000",
            uf="Estado 1",
            cidade="Cidade 1",
            bairro="Bairro 1",
            rua="Rua 1",
            numero=1,
            complemento="Complemento 1",
        )
        repo = CinemaRepository.new("Cinema 1", "Cinema 1", endereco)
        repo.add()
        repo.commit()
        cinema_id = repo.cinema.id
    
    with app.app_context():
        cinema = Cinema.query.filter(Cinema.id == cinema_id).first()
        assert cinema
        assert cinema.nome == "Cinema 1"
        assert cinema.descricao == "Cinema 1"
        assert cinema.cep == endereco.cep
        assert cinema.uf == endereco.uf
        assert cinema.cidade == endereco.cidade
        assert cinema.bairro == endereco.bairro
        assert cinema.rua == endereco.rua
        assert cinema.numero == endereco.numero
        assert cinema.complemento == endereco.complemento
        assert cinema.referencia == endereco.referencia