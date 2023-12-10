from flask_sqlalchemy import SQLAlchemy
from flask_alembic import Alembic
from importlib import import_module

db = SQLAlchemy()
alembic = Alembic()


def init_app(app):
    db.init_app(app)
    app.db = db
    app.extensions['sqlalchemy'].db = db
    alembic.init_app(app)
    db.alembic = alembic
    import_module('core.models')
    return db


def upgrade():
    alembic.upgrade()
