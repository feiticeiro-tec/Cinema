from .. import db
from database.adapters.type import UUID
from sqlalchemy import UniqueConstraint

class Acento(db.Model):
    __tablename__ = "Acento"
    __table_args__ = (
        UniqueConstraint("acento", "sala_id", name="uq_acento_sala"),
    )
    
    id = db.Column(UUID, primary_key=True)
    acento = db.Column(db.String(50), nullable=False)
    is_ativo = db.Column(db.Boolean, nullable=False, default=True)

    sala_id = db.Column(UUID, db.ForeignKey("Sala.id"), nullable=False)
    sala = db.relationship("Sala", backref="acentos")

    