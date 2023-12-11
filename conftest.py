from flask import Flask
import database
import pytest
import api


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
