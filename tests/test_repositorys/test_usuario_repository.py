from database.models import Usuario
from database.repositorys.usuario import Usuario, UsuarioRepository
from database import db
import pytest


def test_get_by_id(app):
    with app.app_context():
        usuario = Usuario(
            nome="teste",
            email="email@email.com",
            senha="senha",
        )
        db.session.add(usuario)
        db.session.commit()
        usuario_id = usuario.id

    with app.app_context():
        usuario = UsuarioRepository.get_by_id(usuario_id)
        assert usuario.nome == "teste"
        assert usuario.email == usuario.email
        assert usuario.senha == usuario.senha


def test_get_by_id_not_found(app):
    with app.app_context():
        with pytest.raises(Exception) as e:
            UsuarioRepository.get_by_id("123")


def test_use_by_id(app):
    with app.app_context():
        usuario = Usuario(
            nome="teste",
            email="email@email.com",
            senha="senha",
        )
        db.session.add(usuario)
        db.session.commit()
        usuario_id = usuario.id

    with app.app_context():
        repo = UsuarioRepository.use_by_id(usuario_id)
        assert repo.usuario.nome == "teste"
        assert repo.usuario.email == "email@email.com"
        assert repo.usuario.senha == "senha"


def test_use_by_id_not_found(app):
    with app.app_context():
        with pytest.raises(Exception):
            UsuarioRepository.use_by_id("123")


def test_set_credencial(app):
    with app.app_context():
        usuario = Usuario(nome="teste")
        repo = UsuarioRepository(usuario)
        repo.set_credencial("email", "senha")
        repo.add()
        repo.commit()
        usuario_id = repo.usuario.id

    with app.app_context():
        usuario = Usuario.query.filter(Usuario.id == usuario_id).first()
        assert usuario
        assert usuario.email == "email"
        assert usuario.senha == "senha"
