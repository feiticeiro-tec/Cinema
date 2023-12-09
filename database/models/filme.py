from .. import db
from database.adapters.type import UUID
from database.adapters.functions import datetime_local

class Filme(db.Model):
    __tablename__ = "Filme"
    id = db.Column(UUID, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(255), nullable=True)
    is_ativo = db.Column(db.Boolean, nullable=False, default=True)
    dt_criado = db.Column(db.Datetime, nullable=False, default=datetime_local)
