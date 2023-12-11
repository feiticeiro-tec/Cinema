from .. import db
from ..adapters.type import UUID, generate_uuid
from ..adapters.functions import datetime_local


class Usuario(db.Model):
    __tablename__ = "Usuario"
    id = db.Column(UUID, primary_key=True, default=generate_uuid)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    senha = db.Column(db.String(255), nullable=False)
    is_ativo = db.Column(db.Boolean, nullable=False, default=True)
    dt_criado = db.Column(db.DateTime, nullable=False, default=datetime_local)
