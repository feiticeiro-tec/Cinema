from .. import db
from core.adapters.type import UUID, generate_uuid
from core.adapters.functions import datetime_local


class Filme(db.Model):
    __tablename__ = "Filme"
    id = db.Column(UUID, primary_key=True, default=generate_uuid)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(255), nullable=True)
    is_ativo = db.Column(db.Boolean, nullable=False, default=True)
    dt_criado = db.Column(db.DateTime, nullable=False, default=datetime_local)
