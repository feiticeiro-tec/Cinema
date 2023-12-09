from flask_sqlalchemy import SQLAlchemy
from flask_alembic import Alembic
from importlib import import_module

db = SQLAlchemy()
alembic = Alembic()


def init_app(app):
    db.init_app(app)
    alembic.init_app(app)
    import_module('database.models')


def upgrade():
    alembic.upgrade()
