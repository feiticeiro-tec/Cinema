from flask import Flask
import database
import pytest
import api
from core.cases import UsuarioCase
from flask_jwt_extended import create_access_token


@pytest.fixture(scope="session")
def _app():
    app = Flask(__name__)
    app.secret_key = "secret"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    database.init_app(app)
    api.init_app(app)
    return app


@pytest.fixture(scope="function")
def app(_app):
    with _app.app_context():
        database.db.create_all()
        yield _app
        database.db.session.remove()
        database.db.drop_all()


@pytest.fixture(scope="function")
def usuario_login(app) -> Flask:
    with app.app_context():
        case = UsuarioCase.create(
            UsuarioCase.Contratos.CreateContrato(
                nome="teste",
                email="teste@gmail.com",
                senha="123456",
            )
        )
        case.commit()
        case.repository.set_is_ativo(True)
        case.commit()
        access_token = create_access_token(identity=case.repository.usuario.id)
        access_token = f"Bearer {access_token}"
        app.access_token = access_token
        app.usuario_id = str(case.repository.usuario.id)
    return app
