from flask import Flask
import core
import pytest
import api


@pytest.fixture(scope="session")
def _app():
    app = Flask(__name__)
    app.secret_key = "secret"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    core.init_app(app)
    api.init_app(app)
    return app


@pytest.fixture(scope="function")
def app(_app):
    with _app.app_context():
        core.db.create_all()
        yield _app
        core.db.session.remove()
        core.db.drop_all()
