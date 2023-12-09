from database.repositorys.colaborador import ColaboradorRepository, Colaborador
from database.repositorys.usuario import UsuarioRepository
from database.repositorys.cinema import CinemaRepository
from database import db
import pytest


def test_get_by_id(app):
    with app.app_context():
        usuario = UsuarioRepository.new(
            nome="teste",
            email="email",
            senha="senha",
        )
        usuario.add()
        db.session.flush()
        usuario_id = usuario.usuario.id
        cinema = CinemaRepository.new(
            nome="cinema",
            descricao="descricao",
            endereco=CinemaRepository.Endereco(
                cep="cep",
                uf="uf",
                cidade="cidade",
                bairro="bairro",
                rua="rua",
                numero=1,
                complemento="complemento",
                referencia="referencia",
            ),
        )
        cinema.add()
        db.session.flush()
        cinema_id = cinema.cinema.id
        colaborador = Colaborador(
            usuario_id=usuario_id,
            cinema_id=cinema_id,
        )
        db.session.add(colaborador)
        db.session.commit()
        colaborador_id = colaborador.id

    with app.app_context():
        repo = ColaboradorRepository.get_by_id(colaborador_id)
        assert repo.usuario_id == usuario_id
        assert repo.cinema_id == cinema_id


def test_get_by_id_not_found(app):
    with app.app_context():
        with pytest.raises(ColaboradorRepository.NotFoundColaboradorException):
            ColaboradorRepository.get_by_id("123")


def test_use_by_id(app):
    with app.app_context():
        usuario = UsuarioRepository.new(
            nome="teste",
            email="email",
            senha="senha",
        )
        usuario.add()
        db.session.flush()
        usuario_id = usuario.usuario.id
        cinema = CinemaRepository.new(
            nome="cinema",
            descricao="descricao",
            endereco=CinemaRepository.Endereco(
                cep="cep",
                uf="uf",
                cidade="cidade",
                bairro="bairro",
                rua="rua",
                numero=1,
                complemento="complemento",
                referencia="referencia",
            ),
        )
        cinema.add()
        db.session.flush()
        cinema_id = cinema.cinema.id
        colaborador = Colaborador(
            usuario_id=usuario_id,
            cinema_id=cinema_id,
        )
        db.session.add(colaborador)
        db.session.commit()
        colaborador_id = colaborador.id

    with app.app_context():
        repo = ColaboradorRepository.use_by_id(colaborador_id)
        assert repo.colaborador.usuario_id == usuario_id
        assert repo.colaborador.cinema_id == cinema_id


def test_use_by_id_not_found(app):
    with app.app_context():
        with pytest.raises(ColaboradorRepository.NotFoundColaboradorException):
            ColaboradorRepository.use_by_id("123")


def test_get_by_usuario_id(app):
    with app.app_context():
        usuario = UsuarioRepository.new(
            nome="teste",
            email="email",
            senha="senha",
        )
        usuario.add()
        db.session.flush()
        usuario_id = usuario.usuario.id
        cinema = CinemaRepository.new(
            nome="cinema",
            descricao="descricao",
            endereco=CinemaRepository.Endereco(
                cep="cep",
                uf="uf",
                cidade="cidade",
                bairro="bairro",
                rua="rua",
                numero=1,
                complemento="complemento",
                referencia="referencia",
            ),
        )
        cinema.add()
        db.session.flush()
        cinema_id = cinema.cinema.id
        colaborador = Colaborador(
            usuario_id=usuario_id,
            cinema_id=cinema_id,
        )
        db.session.add(colaborador)
        db.session.commit()

    with app.app_context():
        colaborador = ColaboradorRepository.get_by_usuario_id(usuario_id)
        assert colaborador.usuario_id == usuario_id
        assert colaborador.cinema_id == cinema_id


def test_get_by_usuario_id_not_found(app):
    with app.app_context():
        with pytest.raises(ColaboradorRepository.NotFoundColaboradorException):
            ColaboradorRepository.get_by_usuario_id("123")


def test_use_by_usuario_id(app):
    with app.app_context():
        usuario = UsuarioRepository.new(
            nome="teste",
            email="email",
            senha="senha",
        )
        usuario.add()
        db.session.flush()
        usuario_id = usuario.usuario.id
        cinema = CinemaRepository.new(
            nome="cinema",
            descricao="descricao",
            endereco=CinemaRepository.Endereco(
                cep="cep",
                uf="uf",
                cidade="cidade",
                bairro="bairro",
                rua="rua",
                numero=1,
                complemento="complemento",
                referencia="referencia",
            ),
        )
        cinema.add()
        db.session.flush()
        cinema_id = cinema.cinema.id
        colaborador = Colaborador(
            usuario_id=usuario_id,
            cinema_id=cinema_id,
        )
        db.session.add(colaborador)
        db.session.commit()

    with app.app_context():
        repo = ColaboradorRepository.use_by_usuario_id(usuario_id)
        assert repo.colaborador.usuario_id == usuario_id
        assert repo.colaborador.cinema_id == cinema_id


def test_use_by_usuario_id_not_found(app):
    with app.app_context():
        with pytest.raises(ColaboradorRepository.NotFoundColaboradorException):
            ColaboradorRepository.use_by_usuario_id("123")


def test_usuario_is_admin(app):
    with app.app_context():
        usuario = UsuarioRepository.new(
            nome="teste",
            email="email",
            senha="senha",
        )
        usuario.add()
        db.session.flush()
        usuario_id = usuario.usuario.id
        cinema = CinemaRepository.new(
            nome="cinema",
            descricao="descricao",
            endereco=CinemaRepository.Endereco(
                cep="cep",
                uf="uf",
                cidade="cidade",
                bairro="bairro",
                rua="rua",
                numero=1,
                complemento="complemento",
                referencia="referencia",
            ),
        )
        cinema.add()
        db.session.flush()
        cinema_id = cinema.cinema.id
        colaborador = Colaborador(
            usuario_id=usuario_id,
            cinema_id=cinema_id,
        )
        db.session.add(colaborador)
        db.session.commit()

    with app.app_context():
        assert ColaboradorRepository.usuario_is_admin(usuario_id) == False
        colaborador = ColaboradorRepository.get_by_usuario_id(usuario_id)
        colaborador.is_admin = True
        db.session.commit()
    with app.app_context():
        assert ColaboradorRepository.usuario_is_admin(usuario_id) == True


def test_new(app):
    with app.app_context():
        usuario = UsuarioRepository.new(
            nome="teste",
            email="email",
            senha="senha",
        )
        usuario.add()
        db.session.flush()
        usuario_id = usuario.usuario.id
        cinema = CinemaRepository.new(
            nome="cinema",
            descricao="descricao",
            endereco=CinemaRepository.Endereco(
                cep="cep",
                uf="uf",
                cidade="cidade",
                bairro="bairro",
                rua="rua",
                numero=1,
                complemento="complemento",
                referencia="referencia",
            ),
        )
        cinema.add()
        db.session.flush()
        cinema_id = cinema.cinema.id
        repo = ColaboradorRepository.new(usuario_id, cinema_id)
        repo.add()
        repo.commit()
        colaborador_id = repo.colaborador.id

    with app.app_context():
        colaborador = Colaborador.query.filter(Colaborador.id == colaborador_id).first()
        assert colaborador
        assert colaborador.usuario_id == usuario_id
        assert colaborador.cinema_id == cinema_id
        assert colaborador.is_admin == False
