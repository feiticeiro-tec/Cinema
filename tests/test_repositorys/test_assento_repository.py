from database.models.assento import Assento
from database.repositorys.assento import AssentoRepository
from database.repositorys.cinema import CinemaRepository
from database.repositorys.sala import SalaRepository
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
        sala = SalaRepository.new(
            nome="sala",
            descricao="descricao",
            cinema_id=cinema_id,
        )
        sala.add()
        sala.commit()
        db.session.flush()
        sala_id = sala.sala.id
        assento = Assento(
            sala_id=sala_id,
            fileira="A",
            numero=1,
        )
        db.session.add(assento)
        db.session.commit()
        assento_id = assento.id

    with app.app_context():
        assento = AssentoRepository.get_by_id(assento_id)
        assert assento.id


def test_get_by_id_not_found(app):
    with app.app_context():
        with pytest.raises(AssentoRepository.NotFoundAssentoException):
            AssentoRepository.get_by_id("123")


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
        sala = SalaRepository.new(
            nome="sala",
            descricao="descricao",
            cinema_id=cinema_id,
        )
        sala.add()
        sala.commit()
        db.session.flush()
        sala_id = sala.sala.id
        assento = Assento(
            sala_id=sala_id,
            fileira="A",
            numero=1,
        )
        db.session.add(assento)
        db.session.commit()
        assento_id = assento.id

    with app.app_context():
        repo = AssentoRepository.use_by_id(assento_id)
        assert repo.assento.id


def test_use_by_id_not_found(app):
    with app.app_context():
        with pytest.raises(AssentoRepository.NotFoundAssentoException):
            AssentoRepository.use_by_id("123")


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
        sala = SalaRepository.new(
            nome="sala",
            descricao="descricao",
            cinema_id=cinema_id,
        )
        sala.add()
        sala.commit()
        db.session.flush()
        sala_id = sala.sala.id

    with app.app_context():
        repo = AssentoRepository.new(
            fileira="A",
            numero=1,
            sala_id=sala_id,
        )
        repo.add()
        repo.commit()
        assento_id = repo.assento.id
    with app.app_context():
        assento = AssentoRepository.get_by_id(assento_id)
        assert assento.fileira == "A"
        assert assento.numero == 1
        assert assento.sala_id == sala_id
        assert assento.is_ativo


def test_new_duplicado(app):
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
        sala = SalaRepository.new(
            nome="sala",
            descricao="descricao",
            cinema_id=cinema_id,
        )
        sala.add()
        sala.commit()
        db.session.flush()
        sala_id = sala.sala.id

    with app.app_context():
        repo = AssentoRepository.new(
            fileira="A",
            numero=1,
            sala_id=sala_id,
        )
        repo.add()
        repo.commit()
    with app.app_context():
        with pytest.raises(AssentoRepository.DuplocadoAssentoException):
            repo = AssentoRepository.new(
                fileira="A",
                numero=1,
                sala_id=sala_id,
            )


def test_update(app):
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
        sala = SalaRepository.new(
            nome="sala",
            descricao="descricao",
            cinema_id=cinema_id,
        )
        sala.add()
        sala.commit()
        db.session.flush()
        sala_id = sala.sala.id

        repo = AssentoRepository.new(
            fileira="A",
            numero=1,
            sala_id=sala_id,
        )
        repo.add()
        repo.commit()
        assento_id = repo.assento.id

    with app.app_context():
        repo = AssentoRepository.use_by_id(assento_id)
        repo.update(
            fileira="B",
            numero=2,
            is_ativo=False,
        )
        repo.commit()

    with app.app_context():
        assento = AssentoRepository.get_by_id(assento_id)
        assert assento.fileira == "B"
        assert assento.numero == 2
        assert assento.is_ativo is False


def test_update_duplicado(app):
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
        sala = SalaRepository.new(
            nome="sala",
            descricao="descricao",
            cinema_id=cinema_id,
        )
        sala.add()
        sala.commit()
        db.session.flush()
        sala_id = sala.sala.id

        repo = AssentoRepository.new(
            fileira="A",
            numero=1,
            sala_id=sala_id,
        )
        repo.add()
        repo.commit()
        assento_id = repo.assento.id

        repo = AssentoRepository.new(
            fileira="B",
            numero=2,
            sala_id=sala_id,
        )
        repo.add()
        repo.commit()

    with app.app_context():
        repo = AssentoRepository.use_by_id(assento_id)
        with pytest.raises(AssentoRepository.DuplocadoAssentoException):
            repo.update(
                fileira="B",
                numero=2,
                is_ativo=False,
            )
