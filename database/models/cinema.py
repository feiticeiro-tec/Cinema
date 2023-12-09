from .. import db
from database.adapters.type import UUID
from database.adapters.models import EnderecoModel


class Cinema(EnderecoModel, db.Model):
    __tablename__ = "Cinema"
    id = db.Column(UUID, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(255), nullable=True)
    is_ativo = db.Column(db.Boolean, nullable=False, default=True)
