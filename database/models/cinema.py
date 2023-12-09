from .. import db
from database.adapters.type import UUID, generate_uuid
from database.adapters.models import EnderecoModel


class Cinema(EnderecoModel, db.Model):
    __tablename__ = "Cinema"
    id = db.Column(UUID, primary_key=True, default=generate_uuid)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(255), nullable=True)
    is_ativo = db.Column(db.Boolean, nullable=False, default=True)
