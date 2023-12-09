from .. import db
from database.adapters.type import UUID
from database.adapters.functions import datetime_local


class Usuario(db.Model):
    __tablename__ = "Usuario"
    id = db.Column(UUID, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    senha = db.Column(db.String(255), nullable=False)
    is_ativo = db.Column(db.Boolean, nullable=False, default=True)
    dt_criado = db.Column(db.Datetime, nullable=False, default=datetime_local)