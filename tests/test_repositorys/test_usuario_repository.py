from database.models import Usuario
from database.repositorys.usuario import UsuarioRepository
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
        with pytest.raises(Exception):
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


def test_set_nome(app):
    with app.app_context():
        usuario = Usuario(email="email", senha="senha")
        repo = UsuarioRepository(usuario)
        repo.set_nome("teste2")
        repo.add()
        repo.commit()
        usuario_id = repo.usuario.id

    with app.app_context():
        usuario = Usuario.query.filter(Usuario.id == usuario_id).first()
        assert usuario
        assert usuario.nome == "teste2"


def test_set_is_ativo(app):
    with app.app_context():
        usuario = Usuario(email="email", senha="senha", nome="teste")
        repo = UsuarioRepository(usuario)
        repo.set_is_ativo(False)
        repo.add()
        repo.commit()
        usuario_id = repo.usuario.id

    with app.app_context():
        usuario = Usuario.query.filter(
            Usuario.id == usuario_id,
        ).first()
        assert usuario
        assert usuario.is_ativo is False


def test_get_all(app):
    with app.app_context():
        for i in range(10):
            usuario = Usuario(
                email=f"email{i}",
                senha=f"senha{i}",
                nome=f"teste{i}",
            )
            db.session.add(usuario)
        db.session.commit()

    with app.app_context():
        usuarios = UsuarioRepository.get_all(0, 10)
        assert len(usuarios) == 10
        for i in range(10):
            assert usuarios[i].nome == f"teste{i}"
            assert usuarios[i].email == f"email{i}"
            assert usuarios[i].senha == f"senha{i}"


def test_get_by_email(app):
    with app.app_context():
        usuario = Usuario(email="email", senha="senha", nome="teste")
        db.session.add(usuario)
        db.session.commit()

    with app.app_context():
        usuario = UsuarioRepository.get_by_email("email")
        assert usuario.nome == "teste"
        assert usuario.email == "email"
        assert usuario.senha == "senha"


def test_get_by_email_not_found(app):
    with app.app_context():
        with pytest.raises(UsuarioRepository.NotFoundUsuarioException):
            UsuarioRepository.get_by_email("email")


def test_use_by_email(app):
    with app.app_context():
        usuario = Usuario(email="email", senha="senha", nome="teste")
        db.session.add(usuario)
        db.session.commit()

    with app.app_context():
        repo = UsuarioRepository.use_by_email("email")
        assert repo.usuario.nome == "teste"
        assert repo.usuario.email == "email"
        assert repo.usuario.senha == "senha"


def test_use_by_email_not_found(app):
    with app.app_context():
        with pytest.raises(UsuarioRepository.NotFoundUsuarioException):
            UsuarioRepository.use_by_email("email")


def test_new(app):
    with app.app_context():
        repo = UsuarioRepository.new("teste", "email", "senha")
        repo.add()
        repo.commit()
        usuario_id = repo.usuario.id

    with app.app_context():
        usuario = Usuario.query.filter(Usuario.id == usuario_id).first()
        assert usuario
        assert usuario.nome == "teste"
        assert usuario.email == "email"
        assert usuario.senha == "senha"


def test_update(app):
    with app.app_context():
        usuario = Usuario(nome="teste", email="email", senha="senha")
        repo = UsuarioRepository(usuario)
        repo.update("teste2", "email2", "senha2")
        repo.add()
        repo.commit()
        usuario_id = repo.usuario.id

    with app.app_context():
        usuario = Usuario.query.filter(Usuario.id == usuario_id).first()
        assert usuario
        assert usuario.nome == "teste2"
        assert usuario.email == "email2"
        assert usuario.senha == "senha2"

def test_exists_email(app):
    with app.app_context():
        usuario = Usuario(nome="teste", email="email", senha="senha")
        db.session.add(usuario)
        db.session.commit()
        usuario_id = usuario.id

    with app.app_context():
        assert UsuarioRepository.exists_email("email") is True
        assert UsuarioRepository.exists_email("email", ["123"]) is True
        assert UsuarioRepository.exists_email("email", [usuario_id]) is False
        assert UsuarioRepository.exists_email("email2") is False
        assert UsuarioRepository.exists_email("email2", ["123"]) is False