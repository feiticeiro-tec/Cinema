from .. import db
from database.adapters.type import UUID, generate_uuid
from sqlalchemy.orm import relationship


class Sala(db.Model):
    __tablename__ = "Sala"
    id = db.Column(UUID, primary_key=True, default=generate_uuid)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(255), nullable=True)
    is_ativo = db.Column(db.Boolean, nullable=False, default=True)

    cinema_id = db.Column(UUID, db.ForeignKey("Cinema.id"), nullable=False)
    cinema = relationship("Cinema", backref="salas")
